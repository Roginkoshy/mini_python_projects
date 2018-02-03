import os
import cgi
import jinja2
import webapp2

template_dir = os.path.join(os.path.dirname(__file__),'webpage')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),autoescape=True)


class Handler(webapp2.RequestHandler):
	def write(self,*a,**kw):
		self.response.out.write(*a,**kw)

	def render_str(self,template,**params):
		t=jinja_env.get_template(template)
		return t.render(params)

	def render(self,template,**kw):
		self.write(self.render_str(template,**kw))



class MainPage(Handler):
	def write_form(self,t):
		self.response.out.write(form%t)

	def get(self):
		self.render("rot13.html")


	def post(self):
		a=self.request.get('rot13v')
		if a:
			w=a
			r=len(w)
			x=''
			for i in range(r):
				c=ord(w[i])
				if c>=65 and c<=90:
					if c+13<91:
						x=x+(chr((ord(w[i])+13)%91))
					else:
						x=x+(chr((ord(w[i])+13)%91+65))
				elif c>=97 and c<=122:
					if c+13<123:
						x=x+(chr((ord(w[i])+13)%123))
					else:
						x=x+(chr((ord(w[i])+13)%123+97))
				else:
					x=x+w[i]
			self.render("rot13.html",rot13a=x)
#		def get(self):
#			self.response.out.write(form)

		

#self.request.get('rot13v');

app=webapp2.WSGIApplication([('/',MainPage),],debug=True)



