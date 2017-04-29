from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required
from . import auth
from ..models import User
from .forms import LoginForm


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            # user session을 위해 로그인한 사용자 기록
            # login_user(##, second_인자: true이면 cookie에 저장 아니면 false: browser가 살아 있을 때까지)
            login_user(user, form.remember_me.data)

            # redirect될 수 있는 2가지 URL
            # 1. next query가 존재를 하면, 저장된 URL로 감 (flask-login이 기존 URL를 저장함)
            # 2. next query string이 없으면 home page로 감
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password.')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required  # 인증된 사용자만 route에 접근 가능함
def logout():
    logout_user()  # remote and reset the user session
    flash('You have been logged out.')
    return redirect(url_for('main.index'))
