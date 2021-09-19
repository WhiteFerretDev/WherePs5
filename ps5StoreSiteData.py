from ps5StoreSite import ps5StoreSite
from ps5StoreSite import AvailabilityCheckType

class ps5StoreSiteData:
    """
    holding the data for all Sites checked as a 'ps5StoreSite' Array
    """


    ps5StoreSites : list = [
        # Alphatecc store site data
        ps5StoreSite(
            AvailabilityCheckType.SEARCH_RESULT_COUNT_CHECK,
            "https://www.alphatecc.de/search?sSearch=ps5",
            ".headline--product-count"
        ),
        # Alternate store site data
        ps5StoreSite(
            AvailabilityCheckType.ELEMENT_NOT_EXIST_CHECK,
            "https://www.alternate.de/Sony-Interactive-Entertainment/PlayStation-5-Spielkonsole/html/product/1651220",
            "meta[content=OutOfStock]"
        ),
        # Amaton store site data
        ps5StoreSite(
            AvailabilityCheckType.ELEMENT_NOT_EXIST_CHECK,
            "https://www.amazon.de/Sony-Interactive-Entertainment-PlayStation-5/dp/B08H93ZRK9/ref=sr_1_3?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=ps5&qid=1631543211&sr=8-3",
            "#outOfStock"
        ),
        # Conrad store site data
        ps5StoreSite(
            AvailabilityCheckType.SEARCH_RESULT_COUNT_CHECK,
            "https://www.conrad.de/de/search.html?search=ps5&tfr_price=450~~~700",
            "#totalResultCount"
            #FIXME not finding #totalResultCount
        ),
        # Cyperport store site data
        ps5StoreSite(
            AvailabilityCheckType.SEARCH_RESULT_COUNT_CHECK,
            "https://www.cyberport.de/tools/search-results.html?productsPerPage=24&sort=popularity&q=ps5&productPrice=450-700&page=1",
            ".resultCount"
        ),
        # Euronics store site data
        ps5StoreSite(
            AvailabilityCheckType.ELEMENT_NOT_EXIST_CHECK,
            "https://www.euronics.de/spiele-und-konsolen-film-und-musik/spiele-und-konsolen/playstation-5/spielekonsole/playstation-5-konsole-4061856837826",
            ".product--buybox .alert"
        ),
        # TODO Expert site data
        # Meadia Markt site data
        ps5StoreSite(
            AvailabilityCheckType.ELEMENT_NOT_EXIST_CHECK,
            "https://www.mediamarkt.de/de/product/_sony-playstation%C2%AE5-2661938.html?utm_source=easymarketing&utm_medium=aff-content&utm_term=50050&utm_campaign=Deeplinkgenerator-AO&emid=61466d8e6a87fc393059fb9e",
            "[data-test=pdp-product-not-available]"
        ),

        # Saturn side data
        ps5StoreSite(
            AvailabilityCheckType.ELEMENT_NOT_EXIST_CHECK,
            "https://www.saturn.de/de/product/_sony-playstation%C2%AE5-2661938.html?utm_source=easymarketing&utm_medium=aff-content&utm_term=50051&utm_campaign=Deeplinkgenerator-AO&emid=61466e152506a2397c3ba428",
            "[data-test=pdp-product-not-available]"
        )

    ]
    """
    array holding all the sites that are checked as 'ps5StoreSites'
    """