import os
import requests
import pickle

class FbData(object):
    """
    Class is used to download Fb data from facebook servers and analyse the
    dataset
    """
    def __init__(self):
        """
        Constructor for FbData class
        """
        self.accessToken =os.environ['FBACCESSTOKEN']

    def reqData(self, req):
        """
        Method requests data from fb Graph API explorer.
        :return: data fetched from Graph API
        """
        response = requests.get("https://graph.facebook.com/v2.10/" + req,
                     {'access_token':self.accessToken})
        print (response)
        return response.json()["id"], response.json()

    def CollectData(self, queryFilename):
        """
        Method is used to get data from facebook
        Query used in this method is saved in query.txt file in ../config
        folder

        Function extracts 18 different features for a particular user and
        thier friends and their freinds as well

        Wooh! Thats 2 level nesting

        Function writes the data fetched from Graph API into file with
        filename = userID

        :return: None
        """
        with open(queryFilename,"r") as f:
            query = f.readline()
            userId, data = self.reqData(query)
            self.writeData(data, userId)

    def writeData(self, data, filename):
        """
        Function writes the JSON formatted data to file with filename =
        filename
        :param data: JSON formatted data from Facebook
        :param filename: filename to be written on the system
        :return: None
        """
        filename = "../output/{0}".format(filename)
        with open(filename, "wb") as fileHandler:
            pickle.dump(data, fileHandler, protocol=pickle.HIGHEST_PROTOCOL)

    def readData(self, filename):
        """
        Method reads the facebook Graph API dump data already stored on the
        disk in pickle format. The data is in JSON format
        :param filename : filename for the data stored on the i=disk
        :return : None
        """
        with open(filename, "rb") as fileHandler:
            data = pickle.load(fileHandler)



def main():
    """
    Main function of the program. Creates 'FbData' class object and
    calls its download method
    :return: None
    """
    queryFilename = "../config/query.txt"

    fb = FbData()
    fb.CollectData(queryFilename)

if __name__ == "__main__":
    main()
