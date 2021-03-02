from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def five_items():
    context = {
        'title': 'THE FIVE | HOME',
        'f_elements':{
            1, 'Fire',
            2, 'Earth',
            3, 'Metal', 
            4, 'Water',
            5, 'Wood'
        }
    }
    return render_template('index.html', **context)

@app.route('/five')
def the_five():
    title = "The Elements | FIVE"
    return render_template('five.html', title=title)