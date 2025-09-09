# PriceWatcher

PriceWatcher is a Flask web app that lets you search for grocery prices by product and country, showing the store with the lowest price from an Excel file.

## Features
- Search for grocery items by name and country
- Displays the store with the lowest price
- Uses a local Excel file as the data source

## Setup
1. Clone this repository.
2. Place your Excel file (e.g., `Grocery_Price_Comp_new.xlsx`) in the `pricewatcher` folder.
3. Install dependencies:
   ```sh
   python -m pip install -r pricewatcher/requirements.txt
   ```
4. Run the app:
   ```sh
   python pricewatcher/app.py
   ```
5. Open your browser at `http://127.0.0.1:5000`

## Deployment
To make this app public, deploy to a cloud platform like Heroku, PythonAnywhere, or Azure. See below for a Heroku example:

### Heroku Quickstart
1. Install the Heroku CLI and log in.
2. Add a `Procfile` with:
   ```
   web: python pricewatcher/app.py
   ```
3. Commit and push to Heroku:
   ```sh
   git init
   git add .
   git commit -m "Initial commit"
   heroku create
   git push heroku master
   heroku open
   ```

## Notes
- Do not commit sensitive data or large Excel files to GitHub. Add them to `.gitignore`.
- Update the Excel file path in `scraper.py` if needed.

## License
MIT
