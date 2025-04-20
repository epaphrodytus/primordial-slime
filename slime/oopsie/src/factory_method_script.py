from oopsie.factory_method import Application, SubApplication

if __name__ == '__main__':
    app = Application()
    app.build()
    print('-- Somebody subclasses Application and overrides factory methods build_backend() and build_frontend() --')
    subapp = SubApplication()
    subapp.build()