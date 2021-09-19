from ps5AvailabilityChecker import ps5AvailabilityChecker


def main():

    if __name__ != '__main__':
        #prevent code from being run when sphinx creates documentation
        return

    print(ps5AvailabilityChecker.GetPs5AvailabilityList())

main()