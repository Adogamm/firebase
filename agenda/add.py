import auth
import web
import firebase_token as token

render = web.template.render("views/")

class Add:
    def GET(self):
        return render.add()
    
    def POST(self):
        form = web.input()
        name = form.name
        email = form.email
        inicio = auth.Login()
        inicio.insert(name,email)
        return web.seeother('/list')
        