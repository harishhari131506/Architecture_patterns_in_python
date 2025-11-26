
from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass(frozen=True)
class OrderLine:
    orderid:str
    sku:str
    qty:int

class Batch:
    def __init__(self , ref:str, sku:str,qty:int , eta:Optional[date]):
        self.reference = ref
        self.sku = sku
        self.eta = eta
        self._purchased_quantity = qty
        self._allocations = set()

    def allocate(self,line:OrderLine):
        if self.can_allocate(line):
            self._allocations.add(line)

    def can_allocate(self,line:OrderLine) -> bool:
        return self.sku == line.sku and self.available_quantity >=line.qty

    def deallocate(self,line:OrderLine) : 
        if line in self._allocations:
            self._allocations.remove(line)

    @property
    def allocated_quantity(self) -> int:
        return sum(line.qty for line in self._allocations)
    
    @property
    def available_quantity(self) -> int:
        return self._purchased_quantity - self.allocated_quantity

    

# from duckduckgo_search import DDGS

# with DDGS() as ddgs:
#     results = ddgs.text("King")
#     for r in results:
#         print(r["href"] + " - " + r["body"])


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
