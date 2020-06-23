import os

def env(variable,default):
    try: 
        ENV = os.environ[variable] 
        return ENV
    except KeyError:
        ENV  = default
        return ENV

## App settings
name = "Urban Lab: Datos de ZMG"
# Method 2 

URL = env('URL','http://localhost:5000')

host ='0.0.0.0'

port = int(os.environ.get("PORT", 5000))

debug = True

contacts = "https://www.linkedin.com/in/fernando-palafox-612301109/"

code = "https://github.com/IFFranciscoME/Urban_Lab/"

fontawesome = 'https://use.fontawesome.com/releases/v5.10.1/css/all.css'

## File system
root = os.path.dirname(os.path.dirname(__file__))

##port= 5001

