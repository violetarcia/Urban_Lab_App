from app.dash import app as application
from config import config


def main():
    application.run_server(debug=config.debug, host=config.host, port=config.port)


if __name__ == "__main__":
    main()
