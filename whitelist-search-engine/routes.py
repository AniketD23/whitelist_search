from flask import Flask, render_template, request
import requests

app = Flask(__name__)
search_urls = []


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_search_url', methods=['POST'])
def add_search_url():
    if request.method == 'POST':
        search_urls.append(request.form['search_url'])
        return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    print(search_urls)
    if request.method == 'POST':
        search_query = request.form['query']
        API_Key = open('API-Key').read()
        Search_Engine_ID = open('Search-Engine-ID').read()
        
        url = 'https://www.googleapis.com/customsearch/v1'
        params = {
            'siteSearch': search_urls[0],
            'siteSearchFilter': "i",
            'q': search_query,
            'key': API_Key,
            'cx': Search_Engine_ID
        }
        
        responses = requests.get(url, params=params)
        results = responses.json()
        
        if 'items' in results:
            links = [item['link'] for item in results['items']]
            return render_template('results.html', links=links)
        
        # Handle case where no items are found
        return "No results found."

if __name__ == '__main__':
    app.run(debug=True)
