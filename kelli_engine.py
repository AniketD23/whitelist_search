import requests

def google_search(query, api_key, cse_id, **kwargs):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'key': api_key,
        'cx': cse_id,
        'q': query
    }
    params.update(kwargs)
    response = requests.get(url, params=params)
    return response.json()

api_key = 'AIzaSyABAevYbmISCQ5VmNsD0W1YvvARH0BIY-o' # api key got from google cloud proj
cse_id = 'b3863dc4e062d46c3'

results = google_search('bunny', api_key, cse_id) # hardcoded "bunny" search

print(results)

for result in results.get('items', []):
    print(result['title'])
    print(result['link'])
    print()
