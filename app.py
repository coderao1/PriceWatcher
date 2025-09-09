from flask import Flask, render_template, request
from scraper import get_prices

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = None
    if request.method == 'POST':
        item_name = request.form.get('item_name')
        ean = request.form.get('ean')
        country = request.form.get('country')
        region = request.form.get('region')
        results = get_prices(item_name, ean, country, region)
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
