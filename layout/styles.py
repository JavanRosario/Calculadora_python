import qdarkstyle
from scripts.variables import PRIMARY_COLOR, DARKER_PRIMARY_COLOR, DARKEST_PRIMARY_COLOR

# QSS string defining the style for buttons with cssClass="specialButton"
qss = f"""
    QPushButton[cssClass="specialButton"] {{
        color: #fff;
        background: {PRIMARY_COLOR};
        border-radius: 5px;
    }}
    QPushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {DARKER_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {DARKEST_PRIMARY_COLOR};
    }}
"""


# function to apply the dark theme and custom button styles
def setup_theme(app):
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())
    app.setStyleSheet(app.styleSheet() + qss)
