from flask import Flask
from flask_restx import Api, Resource, Namespace

app = Flask(__name__)
api = Api(app, version='1.0', title='Learnex App', description='A comprehensive description of your API')

# Define the namespace
home_ns = Namespace('home', description='Home Page operations')

# Decorate the class with the route
@home_ns.route('/')  # This will handle requests to '/home/'
class Home(Resource):
    def get(self):
        # This method will be called for GET requests to '/home/'
        return 'This is the home page'

# Add the namespace to the API
api.add_namespace(home_ns)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
