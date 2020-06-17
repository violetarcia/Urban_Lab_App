from app.dash.app import app as application
from config import config


def main():
    app.run_server(debug=config.debug, host=config.host, port=config.port)


if __name__ == "__main__":
    main()