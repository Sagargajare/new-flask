from app import app

if __name__ == '__main__':
    # if app.config["APP_SETTINGS_LEVEL"] == 'production':
    #     #app.run(ssl_context='adhoc', debug=False)
    #     app.run(debug=False)
    # else:
    #     #app.run(ssl_context='adhoc', debug=True)
    app.run(host="0.0.0.0")
