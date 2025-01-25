import reader
import requests

rss_url = "https://www.nature.com/cgt.rss"
response = requests.get(rss_url)
feed = atoma.parse_atom_bytes(response.content)
print(feed)
