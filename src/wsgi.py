from app import dash
from config import config


def main():
    dash.app.run_server(debug=config.debug, host=config.host, port=config.port)


if __name__ == "__main__":
    main()