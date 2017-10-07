import os
import pprint
import requests

class FbData(object):
    """
    Class is used to download Fb data from facebook servers and analyse the
    dataset
    """
    def __init__(self):
        """
        Constructor for FbData class
        """
        FBACCESSTOKEN=""
        # self.accessToken =os.environ['FBACCESSTOKEN']
        self.accessToken = FBACCESSTOKEN
        print (self.accessToken)

    def reqData(self, req):
        """
        Method requests data from fb Graph API explorer.
        :return:
        """
        response = requests.get("https://graph.facebook.com/v2.10/" + req,
                     {'access_token':self.accessToken})
        print (response)
        print (response.json())

def main():
    """
    Main function of the program. Creates 'FbData' class object and
    calls its download method
    :return: None
    """
    # requestion total comments and likes per post from SarcasmLOL FB page
    reqString = "sarcasmLOL?fields=posts{comments.limit(0).summary(true),likes.limit(0).summary(true)}"
    reqString2 = "me?fields=birthday,about,education"

    fb = FbData()
    fb.reqData(reqString)

if __name__ == "__main__":
    main()
