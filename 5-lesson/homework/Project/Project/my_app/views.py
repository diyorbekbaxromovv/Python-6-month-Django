# from django.shortcuts import render

# # Create your views here.
# def index(request):    
    
    
#     product_range = [1,2,3]
#     title = ("Diyorbek in style")
#     item_names = ["Fancy Product", "Special Item", "Sale Item", "Popular Item"]
#     price = ["$40.00 - $80.00", "$18.00","$25.00", "$40.00"]
#     img = ["https://dummyimage.com/450x300/dee2e6/6c757d.jpg","https://dummyimage.com/450x300/dee2e6/6c757d.jpg","https://dummyimage.com/450x300/dee2e6/6c757d.jpg","https://dummyimage.com/450x300/dee2e6/6c757d.jpg"]
#     data = {"item_names": item_names,
#             "price":price, 
#             "title":title,
#             "img":img, 
#             "product_range":product_range,
#             "product_range":range(len(item_names))}
#     return render(request, 'index.html' , context=data)

from django.shortcuts import render

posts = {
        "post1": {
            "for_sale": False,
            "img_url": "https://dummyimage.com/450x300/dee2e6/6c757d.jpg", 
            "product_name": "Fancy Product",
            "special_or_popular": False,
            "old_price": "",
            "new_price": "$40.00 - $80.00",
            "product_action": "View options"
        },
        "post2": {
            "for_sale": True,
            "img_url": "https://dummyimage.com/450x300/dee2e6/6c757d.jpg", 
            "product_name": "Special Item",
            "special_or_popular": True,
            "old_price": "$20.00",
            "new_price": "$18.00",
            "product_action": "Add to card"
        },
        "post3": {
            "for_sale": True,
            "img_url": "https://dummyimage.com/450x300/dee2e6/6c757d.jpg", 
            "product_name": "Sale Item",
            "special_or_popular": False,
            "old_price": "$50.00",
            "new_price": "$25.00",
            "product_action": "Add to card"
        },
        "post4": {
            "for_sale": False,
            "img_url": "https://dummyimage.com/450x300/dee2e6/6c757d.jpg", 
            "product_name": "Popular Item",
            "special_or_popular": True,
            "old_price": "",
            "new_price": "$40.00",
            "product_action": "Add to card"
        },
        "post5": {
            "for_sale": True,
            "img_url": "https://dummyimage.com/450x300/dee2e6/6c757d.jpg", 
            "product_name": "Sale Item",
            "special_or_popular": False,
            "old_price": "$50.00",
            "new_price": "$25.00",
            "product_action": "Add to card"
        },
        "post6": {
            "for_sale": False,
            "img_url": "https://dummyimage.com/450x300/dee2e6/6c757d.jpg", 
            "product_name": "Fancy Product",
            "special_or_popular": False,
            "old_price": "",
            "new_price": "$120.00 - $280.00",
            "product_action": "View options"
        },
        "post7": {
            "for_sale": True,
            "img_url": "https://dummyimage.com/450x300/dee2e6/6c757d.jpg", 
            "product_name": "Special Item",
            "special_or_popular": True,
            "old_price": "$20.00",
            "new_price": "$18.00",
            "product_action": "Add to card"
        },
        "post8": {
            "for_sale": False,
            "img_url": "https://dummyimage.com/450x300/dee2e6/6c757d.jpg", 
            "product_name": "Popular Item",
            "special_or_popular": True,
            "old_price": "",
            "new_price": "$40.00",
            "product_action": "Add to card"
        },
    }

def index(request):
    title = ("Diyorbek in style")
    return render(request, 'index.html', context={"posts": posts, "title": title} )