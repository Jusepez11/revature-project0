from .file_name import file_class

def register_routes(app):
    app.register_blueprint(file_class)
