from config import config, desarollo
from flask_script import Manager, Server
#inportat funcion 
from src import ini_app


configuracion = config['desarollo']
app = ini_app()


# configuracio del server
Manager = Manager(app)
Manager.add_command('runserver', Server(host='127.0.0.1', port=9200))

if __name__ == '__main__':
    app.run()
