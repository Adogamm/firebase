import auth
import web
import firebase_token as token

render = web.template.render("views/")

class List:
    def GET(self):
        query = auth.Login
        lista = query.list_all()
        return render.list(lista)

