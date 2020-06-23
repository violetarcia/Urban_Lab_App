import os

## App settings
name = "Urban Lab: Datos de ZMG"

host ='0.0.0.0'

port = int(os.environ.get("PORT", 5000))

debug = bool(os.environ.get("ENV", True))


fontawesome = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'
## File system
root = os.path.dirname(os.path.dirname(__file__))

#para linux
db = root +'/db/'
#para windows
#db = root +'\\db\\'

#para linux
assets  = root+'/app/assets'
#para windows
# assets  = root+'\\app\\assets\\'