import connexion


def create_app(config=None):
    app = connexion.FlaskApp(__name__, specification_dir='openapi/')
    app.add_api('api_spec.yaml')

    return app