from connections import db

product_data_coll = db['product-data']


def get_product(product_id):

    all_keywords = product_id.split(" ")

    regex_exp = "(" + ")|(".join(all_keywords) + ")"

    data = product_data_coll.find({'$or': [
        {"product_name": {"$regex": regex_exp}}
    ]})

    data = list(data)

    for i in data:

        if "_id" in i:

            del i["_id"]

    return list(data)
