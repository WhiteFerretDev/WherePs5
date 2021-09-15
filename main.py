from ps5StoreSite import ps5StoreSite
from ps5StoreSite import AvailabilityCheckType


def main():

    if __name__ != '__main__':
        #prevent code from being run when sphinx creates documentation
        return

    amazonPs5SiteLink : str = "https://www.amazon.de/Sony-Interactive-Entertainment-PlayStation-5/dp/B08H93ZRK9/ref=sr_1_3?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=ps5&qid=1631543211&sr=8-3"
    amazonPs5SiteTargetElementCssSelector : str = "#outOfStock"
    amazonPs5Site = ps5StoreSite(AvailabilityCheckType.ELEMENT_NOT_EXIST_CHECK, amazonPs5SiteLink, amazonPs5SiteTargetElementCssSelector)

    print(amazonPs5Site.IsPs5Available())

    alphateccPs5SiteLink : str = "https://www.alphatecc.de/search?sSearch=ps5"
    alphateccPs5SiteTargetElementCssSelector : str = ".headline--product-count"
    alphateccPs5site = ps5StoreSite(AvailabilityCheckType.SEARCH_RESULT_COUNT_CHECK, alphateccPs5SiteLink, alphateccPs5SiteTargetElementCssSelector)
    print(alphateccPs5site.IsPs5Available())

main()