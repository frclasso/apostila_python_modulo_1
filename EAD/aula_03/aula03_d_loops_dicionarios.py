
germany_companies = {'name':None,
                     'industry':None,
                     'sector':None,
                     'headquarters':None,
                     'foudend':None,
                     'notes':None}

aareal_bank = {
    'name':'Aareal Bank',
    'industry':'Financials',
    'sector': 'Banks',
    'headquarters':'Wiesbaden',
    'foudend':1922,
    'notes':'Banking and financial services'
}


adidas = {
    'name':'Adidas',
    'industry':'Consumer goods',
    'sector':'Footwear',
    'headquarters':'Herzogenaurach',
    'foudend':1924,
    'notes':'Shoes, apparel and accessories'
}

for k in aareal_bank:
    print(k)

print()
for k in aareal_bank.values():
    print(k)

print()
for k,v in aareal_bank.items():
    print(k,':', v)