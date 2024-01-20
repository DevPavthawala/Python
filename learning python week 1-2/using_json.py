book = {}
book['dev']= {
    'name':'dev',
    'address':'1 street nyc',
    'phone':'1234567890'
}
book['neel']= {
    'name':'neel',
    'address':'15 street nyc',
    'phone':'1434167890'
}
book['manav']= {
    'name':'manav',
    'address':'258 street nyc',
    'phone':'9876567890'
}


import json

a = json.dumps(book)

with open("E://Python//custion_for_datascience//book.txt","w") as f:
    f.write(a)

for person in book:
    print(book[person])