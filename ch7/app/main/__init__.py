from flask import Blueprint

# __init__.py는 import를 하게 되면 호출이 된다.
# __name__: app.main
main = Blueprint('main', __name__)

# blueprint 아래에 import된 이유는 circular dependencies를 피하기 위해서임
# views에서 main blueprint를 import하기 때문에
from . import views, errors
