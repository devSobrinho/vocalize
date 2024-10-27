from app.server_setting import init_server

if __name__ == '__main__':
    app = init_server()
    app.run(debug=True, port=5000)
