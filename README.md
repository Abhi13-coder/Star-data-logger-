# Star-data-logger-
requirements.txt
git add scraper.py requirements.txt
git commit -m "Added scraper and requirements"
git push
name: Star Logger

on:
  schedule:
    - cron: '0 */6 * * *' # Runs every 6 hours
  workflow_dispatch: # Lets you run it manually too

jobs:
  run-logger:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v2

      - name: Setup Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'

      - name: Install Dependencies
        run: pip install -r requirements.txt

      - name: Run Star Scraper
        env:
          NOTION_KEY: ${{ secrets.NOTION_KEY }}
          DB_ID: ${{ secrets.NOTION_DB_ID }}
        run: python scraper.py
        
