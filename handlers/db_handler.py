from connections import db
from handlers.language_tools import translate_text

product_data_coll = db['product-data']


def get_product(product_id):

    all_keywords = product_id.split(" ")

    all_keywords = [translate_text(x) for x in all_keywords]

    all_keywords = [x.lower() for x in all_keywords]

    regex_exp = "(" + ")|(".join(all_keywords) + ")"

    data = product_data_coll.find({'$or': [
        {"product_name": {"$regex": regex_exp}}
    ]})

    data = list(data)

    for i in data:

        if "_id" in i:

            del i["_id"]

    return list(data)