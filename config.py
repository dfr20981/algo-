class config:
    pass

# parametro de desarollo


class desarollo(config):
    DEBUG = True


# configuracion
config = {
    'development': desarollo,
    'default': desarollo
}
