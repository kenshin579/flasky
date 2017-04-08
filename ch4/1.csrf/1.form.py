from flask import Flask, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[Required()]) # todo: Required는 어떻게 동작을 하나?
    submit = SubmitField('Submit')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# methods가 없으면 default로 GET으로 받음
@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit(): # submit이 호출되었으며
        name = form.name.data # submit 버튼이 클릭되면, form.name정보에 데이터가 담겨져 있음
        print("name", name)
        form.name.data = '' #form.name에서 지움
    return render_template('index.html', form=form, name=name)

if __name__ == '__main__':
    # manager.run()
    app.run(debug=True)
