from enum import Enum
from ps5Crawler import CreateFirefoxDriver
from selenium import webdriver




class ps5StoreSite:
    """
    Representation of a website that can be checked for ps5 availability
    """

    availabilityCheckType : int
    storeSiteLink : str
    targetElementCssSelector : str

    lastSearchResultCountForSite : int

    driver : webdriver.FirefoxProfile

    def __init__(self, availablityCheckType, storeSiteLink, targetElementCssSelector):
        """
        Initializing 'ps5StoreSite' object

        :param self: 
        :param availabilityCheckType: (AvailabilityCheckType) specifies the way availablity is checked 
        :param storeSiteLink: (str) link to the store site where availability is checked
        :param targetElementCssSelector: (str) css selector for the element which is used when checking availability
        """

        self.availabilityCheckType = availablityCheckType
        self.storeSiteLink = storeSiteLink
        self.targetElementCssSelector = targetElementCssSelector

        self.driver = CreateFirefoxDriver(True)
        self.driver.get(storeSiteLink)

        if availablityCheckType == AvailabilityCheckType.SEARCH_RESULT_COUNT_CHECK:
            self.lastSearchResultCountForSite = self.__GetPs5SearchResultCountForSite(self.driver, self.targetElementCssSelector)


    def IsPs5Available(self):
        """
        Checking if ps5 is available on site

        :param self:
        :return: (bool) availibility status
        """

        isAvailable : bool = False

        if self.availabilityCheckType == AvailabilityCheckType.ELEMENT_EXIST_CHECK:
            isAvailable = self.__IsElementOnSite(self.driver, self.targetElementCssSelector)

        elif self.availabilityCheckType == AvailabilityCheckType.ELEMENT_NOT_EXIST_CHECK:
            isAvailable = not self.__IsElementOnSite(self.driver, self.targetElementCssSelector)

        elif self.availabilityCheckType == AvailabilityCheckType.SEARCH_RESULT_COUNT_CHECK:
            isAvailable = self.__IsPs5SearchResultCountChangedForSite(self.driver, self.targetElementCssSelector)

        self.driver.quit()
        return isAvailable

    
    def __IsElementOnSite(self, driver, targetElementCssSelector) -> bool:
        """
        Checks if element specified in 'targetElementCssSelector' is on site

        :param self:
        :param driver: selenium webdriver set up for target site
        :param targetElementCssSelector: (str) css selector for element, which existence is beeing checked
        :return: (bool)
        """

        elementsFittingCssSelector : list = driver.find_elements_by_css_selector(targetElementCssSelector)
        if len(elementsFittingCssSelector) == 0:
            return False

        return True

        

    def __IsPs5SearchResultCountChangedForSite(self, driver, targetElementCssSelector):
        """
        Checks if the search result count for the site for keyword 'ps5' has changed

        :param self:
        :param driver: selenium webdriver set up for target site
        :param targetElementCssSelector: (str) css selector for element holding the search result count value
        :return: (bool)
        """

        searchResultCount : int = self.__GetPs5SearchResultCountForSite(driver, targetElementCssSelector)
        
        if searchResultCount != self.lastSearchResultCountForSite:
            self.lastSearchResultCountForSite = searchResultCount
            return True

        return False

    
    def __GetPs5SearchResultCountForSite(self, driver, targetElementCssSelector):
        """
        return search result count for keyword 'ps5' for site

        :param self:
        :param driver: selenium webdriver set up for target site
        :param targetElementCssSelector: (str) css selector for element holding search result count value
        :return: (int) amount of search results for keyword 'ps5' on site
        """

        searchResultCount : int = int(driver.find_element_by_css_selector(targetElementCssSelector).text)
        return searchResultCount


    def CreateFirefoxDriver(isHeadless : bool = False):
        """
        Creating a firefox seleniunm webdriver

        :param isHeadless: (bool) enables headless mode of driver (default false)
        :return: (webdriver.FirefoxProfile) created selenium firefox webdriver
        """        

        options = webdriver.firefox.options.Options()
        options.headless = isHeadless;

        driver = webdriver.Firefox(options=options)

        return driver



class AvailabilityCheckType(Enum):
    """
    Used to specify which method to use for 'ps5StoreSite' when checking availability
    """

    ELEMENT_EXIST_CHECK = 0
    ELEMENT_NOT_EXIST_CHECK = 1
    SEARCH_RESULT_COUNT_CHECK = 2