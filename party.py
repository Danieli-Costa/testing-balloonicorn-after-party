"""Flask site for Balloonicorn's Party."""

from flask import Flask, session, render_template, request, flash, redirect
from model import Game, connect_to_db

app = Flask(__name__)
app.secret_key = "SECRETSECRETSECRET"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route("/")
def homepage():
    """Show homepage."""

    return render_template("homepage.html")


@app.route("/rsvp", methods=['POST'])
def rsvp():
    """Register for the party."""

    name = request.form.get("name")
    email = request.form.get("email")

    session['RSVP'] = True
    flash("Yay!")
    return redirect("/")


@app.route("/games")
def games():
    
    if 'RSVP' in session:        
        games = Game.query.all()
        return render_template("games.html", games=games)
    else:
        # return render_template("homepage.html")
        return redirect("/")


if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')