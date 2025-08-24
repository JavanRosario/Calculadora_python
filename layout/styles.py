import qdarkstyle
from scripts.variables import PRIMARY_COLOR, DARKER_PRIMARY_COLOR, DARKEST_PRIMARY_COLOR

# QSS string defining the style for buttons with cssClass="specialButton"
qss = f"""
    PushButton[cssClass="specialButton"] {{
        color: #fff;
        background: {PRIMARY_COLOR};
        border-radius: 5px;
    }}
    PushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {DARKER_PRIMARY_COLOR};
    }}
    PushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {DARKEST_PRIMARY_COLOR};
    }}
"""


def setup_theme(app):  # function to apply the dark theme and custom button styles
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside6()
                      )  # apply default dark theme
    app.setStyleSheet(app.styleSheet() + qss)  # append custom QSS for buttons
