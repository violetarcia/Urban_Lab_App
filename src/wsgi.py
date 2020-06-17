from app import dash as application
from config import config


def main():
    application.app.run_server(debug=config.debug, host=config.host, port=config.port)


if __name__ == "__main__":
    main()
