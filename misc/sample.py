import json
from urllib.request import urlopen
from urllib.parse import urlencode

params = dict(q='king',format="json")
handle = urlopen('https://api.duckduckgo.com' + '?' + urlencode(params))

raw_text = handle.read().decode('utf-8')
parsed = json.loads(raw_text)

results = parsed['RelatedTopics']
print(results)
for r in results:
    if isinstance(r, dict) and "Text" in r:
        print(f"{r['FirstUrl']} - {r['Text']}")
