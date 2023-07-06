from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm
from flask_behind_proxy import FlaskBehindProxy
app = Flask(__name__)
proxied = FlaskBehindProxy(app)
app.config['SECRET_KEY'] = '53dd1201743b12e4e75c3104b14d26ef'

@app.route("/")
@app.route("/home")
def home():
    return render_template('weather.html', subtitle='Home Page', text='This is the home page')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit(): # checks if entries are valid
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home')) # if so - send to home page
    return render_template('register.html', title='Register', form=form)


{% with messages = get_flashed_messages(with_categories=true) %}
  {% if messages %}
    {% for category, message in messages %}
       <div class="alert alert-{{ category }}">
         {{ message }}
      </div>
    {% endfor %}
  {% endif %}
{% endwith %}