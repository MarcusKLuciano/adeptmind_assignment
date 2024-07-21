import json
with open('../../output/trader_joes.json','r') as f:
    data = json.load(f)
# print(data[0])

class Validation():
    
    def __init__(self,d):
        for k, v in d.items():
            setattr(self, k, v)
        assert self.sale_prices <= self.price ## Validates that sale_prices is higher or equal to price.
        assert self.title not in [None,''] ## Title is not Null or blank
        assert self.product_id not in [None,''] ## Product ID is not Null or blank
        assert self.image not in [None,''] ## Product image is not Null or blank


foo = Validation(data[0])
print(foo.product_id,foo.image)
