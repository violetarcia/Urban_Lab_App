from app.dash import app
from config import config
server = app.server

def main():
    app.run_server(debug=config.debug, host=config.host, port=config.port)


if __name__ == "__main__":
    main()