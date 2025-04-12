# Star-data-logger-
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
        
