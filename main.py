from ps5AvailabilityChecker import ps5AvailabilityChecker
from ps5AvailabilityMessageSender import ps5AvailabilityMessageSender


def main():

    if __name__ != '__main__':
        #prevent code from being run when sphinx creates documentation
        return

    messageSender = ps5AvailabilityMessageSender(["+4915141494160"])
    availabilityList = ps5AvailabilityChecker.GetPs5AvailabilityList()
    messageSender.SendMessagesForAvailabilityList(availabilityList)

    print(availabilityList)

main()