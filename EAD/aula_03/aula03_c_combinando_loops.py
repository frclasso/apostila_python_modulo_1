

# CASO1  - resolvendo estruturas menos organizadas

germany_companies = [

    'A. Lange & Söhne','Consumer goods','Clothing & accessories','Glashütte',1845,'Watches',
    'Aareal Bank','Financials','Banks','Wiesbaden',1922,'Banking and financial services',
    'Adidas','Consumer goods','Footwear','Herzogenaurach',1924,'Shoes, apparel and accessories',
    'AEG','Industrials','Electronic equipment','Frankfurt',1883, 'Defunct 1996 - now part of Electrolux',
    'Air Berlin','Consumer services','Airlines','Berlin', 1979,'Airline, defunct 2017',
    'Aldi','Consumer services','Food retailers & wholesalers','Essen',1913,'Discount retail chains',
    'Allianz','Financials','Full line insurance','Munich',1890,'Insurance and asset management',
    'Alpina','Consumer goods','Automobiles','Buchloe',1965,'Automotive manufacturer',
    'Altana','Basic materials','Speciality chemicals','Wesel',1977, 'Chemicals',
    'Aral AG','Consumer services','Specialty retailers','Bochum',1898,'Part of BP',
    'Arburg','Industrials','Industrial machinery','Loßburg',1923,'Machinery and injection molding',
    'Arcandor','Consumer services','Broadline retailers','Essen',1999,'Defunct 2009',
    'Arcor','Telecommunications','Fixed line telecommunications','Eschborn',1966,'Telecom, part of Vodafone (UK)',
    'Armedangels','Consumer goods','Clothing & accessories','Cologne',2007,'Fashion',
    'Audi','Consumer goods','Automobiles','Ingolstadt',1910,'Auto manufacturer, part of Volkswagen Group',
    'August Storck','Consumer goods','Food products','Berlin',1903,'Confectionery',
    'Aurubis','Basic materials','Nonferrous metals']


# for x in range(6):
#     for l in germany_companies:
#         print(l)


# count = 0
# while count < len(germany_companies):
#     print(germany_companies[count])
#     count += 1


# Primeira linha/compania
# count = 0
# while count < 6:
#     print(germany_companies[count])
#     count += 1
# print()

# Segunda linha/compania=
# count = 6
# while count < 12:
#     print(germany_companies[count])
#     count += 1
# print()

# bizarro
# o ideal é criar uma função e reutilizar

#
# funcao, reutilizar codigo
def get_um_linha(count, max):

    while count < max:
        print(germany_companies[count])
        count +=1
    print()
print()
# get_um_linha(0, 6)
# get_um_linha(6, 12)


inicio = 0
count = 0
max = 6
while inicio < len(germany_companies):
    get_um_linha(count, max)
    inicio += 1
    count += 6
    max += 6
