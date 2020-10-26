from flask import Flask
from .settings import DEBUG, SQLALCHEMY_DATABASE_URI
from flask_sqlalchemy import SQLAlchemy
from flask import render_template_string
from flask_marshmallow import Marshmallow

# app object
app = Flask(__name__)
app.config.from_object('cancer.settings')

app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

# Data base object
db = SQLAlchemy(app)

# Initialize Marshmallow for API
ma = Marshmallow(app)

# default-index url
@app.route('/', methods=["GET"])
def index():
    return render_template_string(
        '''
            <!DOCTYPE html>
            <html>
                <head>
                    <title>Saraton</title>
                    <meta charset=utf-8>
                    <meta name=description content="">
                    <meta name=format-detection content="telephone=no">
                    <meta name=msapplication-tap-highlight content=no>
                    <meta name=viewport content="user-scalable=no,initial-scale=1,maximum-scale=1,minimum-scale=1,width=device-width">
                    <link rel=icon type=image/png sizes=128x128 href=static/icons/favicon-128x128.png>
                    <link rel=icon type=image/png sizes=96x96 href=static/icons/favicon-96x96.png>
                    <link rel=icon type=image/png sizes=32x32 href=static/icons/favicon-32x32.png>
                    <link rel=icon type=image/png sizes=16x16 href=static/icons/favicon-16x16.png>
                    <link rel=icon type=image/ico href=static/favicon.ico>
                    <link href=static/css/vendor.13c0a939.css rel=stylesheet>
                    <link href=static/css/app.0e433876.css rel=stylesheet>
                </head>
                <body>
                    <div id=q-app></div>
                    <script src=static/js/vendor.1337ab24.js>
                    </script>
                    <script src=static/js/app.d1404635.js>
                    </script>
                </body>
            </html>
        '''
    )

def create_app():
    db.create_all()
    return app