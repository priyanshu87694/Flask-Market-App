from market import app, render_template
from .models import Items

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = Items.query.all()
    return render_template('market.html', items=items)