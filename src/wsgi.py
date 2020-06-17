from app import dash
from config import config

application = dash.app

def main():
    application.run_server(debug=config.debug, host=config.host, port=config.port)


if __name__ == "__main__":
    main()