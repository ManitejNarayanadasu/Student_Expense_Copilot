import re
merchants = {
    'tesco' : {
        'category':'food',
        'subcategory':'grocery'
    },
    'sainsbury' : {
        'category':'food',
        'subcategory':'grocery'
    },
    'tfl':{
        'category':'transport',
        'subcategory':'public transport'
    },
    'spotify':{
        'category':'subscriptions',
        'subcategory':'music'
    },
    'asos':{
        'category':'shopping',
        'subcategory':'clothing'
    }
}


def categorise_transaction(description):
    lw_description = description.lower()

    for merchant in merchants:
        if re.search(rf"\b{re.escape(merchant)}\b", lw_description):
            merchant_info = merchants[merchant]
            return tuple(merchant_info.values())
    return ('other','other')
