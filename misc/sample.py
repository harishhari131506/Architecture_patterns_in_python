from duckduckgo_search import DDGS

with DDGS() as ddgs:
    results = ddgs.text("King")
    for r in results:
        print(r["href"] + " - " + r["body"])


# import requests

# params = dict(q='King' , format='json')
# parsed = requests.get('https://api.duckduckgo.com' , params=params).json()

# results = parsed['RelatedTopics']

# for r in results:
#     if 'Text' in r:
#         print(f"{r['FirstURL']} - {r['Text']}")


# import json
# from urllib.request import urlopen
# from urllib.parse import urlencode

# params = dict(q='king',format="json")
# handle = urlopen('https://api.duckduckgo.com' + '?' + urlencode(params))

# raw_text = handle.read().decode('utf-8')
# parsed = json.loads(raw_text)

# results = parsed['RelatedTopics']

# for r in results:
#     if isinstance(r, dict) and "Text" in r:
#         print(f"{r['FirstURL']} - {r['Text']}")
#         print("------")
