from ps5StoreSiteData import ps5StoreSiteData
from pywhatkit import sendwhatmsg
from datetime import timedelta
from datetime import datetime

class ps5AvailabilityMessageSender:

    phoneNumbers : list = [

    ]
    """
    phone numbers to send messages to as strings
    """

    def __init__(self, phoneNumbers):
        """
        
        :param self:
        :param phoneNumbers: phone numbers to send messages to as strings
        :type phoneNumbers: list[str]
        """

        self.phoneNumbers = phoneNumbers


    def SendMessagesForAvailabilityList(self, availabilityList):
        """
        sending whatsapp message listing sites where ps5 is or might be available

        :param self:
        :param availabilityList: list of boolean values for the sites in 'ps5SiteData' 
        :type availabilityList: list[bool]
        """

        message : str = ""

        for x in range(len(ps5StoreSiteData.ps5StoreSites)):
            if availabilityList[x]:
                message += ps5StoreSiteData.ps5StoreSites[x].GetAvailabilityMessage() + "\n"

        if message:
            self.__SendMessageToAllPhoneNumbers(message)


    def __SendMessageToAllPhoneNumbers(self, message):
        """
        sending whatsapp message to all numbers in 'phoneNumbers'

        :param self:
        :param message: message to send
        :type message: str
        """

        for phoneNumber in self.phoneNumbers:
            self.__SendMessageToPhoneNumber(message, phoneNumber)


    def __SendMessageToPhoneNumber(self, message, phoneNumber):
        """
        sending whatsapp message to phone number

        :param self:
        :param message: message to send
        :type message: str
        :param phoneNumber: phone number to send message to with country code
        :type phoneNumber: str
        """

        timeToSend = datetime.now() + timedelta(minutes = 1, seconds = 20)
        sendwhatmsg(phoneNumber, message, timeToSend.hour, timeToSend.minute, 20)