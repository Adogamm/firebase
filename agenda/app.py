import web
import auth

urls = (
    '/', 'Index',
    '/list','list.List',
    '/add','add.Add'
)
app = web.application(urls, globals())

render = web.template.render("views/")

class Index:
    def GET(self):
        return render.index()

    def POST(self):
        form = web.input()
        email = form.email
        password = form.password
        inicio = auth.Login
        credenciales = inicio.login(email,password)
        if credenciales:
            return web.seeother('/list')
        else:
            return render.index2()

if __name__ == "__main__":
    app.run()