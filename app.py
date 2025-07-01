from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash
    )

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.secret_key = "cualquiercosa"
app.config['SQLALCHEMY_DATABASE_URI'] = (
    "mysql+pymysql://root:@localhost/miniblog"
)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/')
def miniblog():
    return render_template('index.html')

@app.route('/user')
def userconf():
    return render_template('userconfig.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')


if __name__ == '__main__':
    app.run(debug=True)