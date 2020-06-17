from app import dash
from config import config

app = dash.app

def main():
    app.run_server(debug=config.debug, host=config.host, port=config.port)


if __name__ == "__main__":
    main()