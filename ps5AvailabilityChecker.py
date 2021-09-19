from ps5StoreSite import ps5StoreSite
from ps5StoreSiteData import ps5StoreSiteData


class ps5AvailabilityChecker:

    def GetPs5AvailabilityList():
        """
        return availability bool list for ps5 on sites listed in 'ps5StoreSiteData.ps5StoreSites'

        :return: list of boolean values for all sites listen in 'ps5StoreSiteData.ps5StoreSites'
        :rtype: bool
        """

        availabilityList : list = []

        for ps5StoreSite in ps5StoreSiteData.ps5StoreSites:
            availabilityList.append(ps5StoreSite.IsPs5Available())

        return availabilityList


