import os
import requests
import pickle

class ParseFbData:
    """
    Class is used to convert JSON format data into adjList graph
        e.g 1 2 3 4
            2 1 10
            3 1 10 5
            4 1
            10 2 3
    """
    def __init__(self):
        pass

    def readData(self, filename):
        """
        Method reads the facebook Graph API dump data already stored on the
        disk in pickle format. The data is in JSON format
        :param filename : filename for the data stored on the disk
        :return : None
        """
        with open(filename, "rb") as fileHandler:
            data = pickle.load(fileHandler)
            print (data)


def main():
    """
    Main function of the program that create instance of ParseFbData class
    and call convert function of the same
    :return: None
    """
    fbDataFile = "../output/10207648390994439"

    parse = ParseFbData()
    parse.readData(fbDataFile)

if __name__ == "__main__":
    main()
