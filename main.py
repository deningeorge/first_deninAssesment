# by Denin George
# written on MacOS system with Python 3.11
import json
import requests


class Predictor:
    test = json.loads(requests.get("https://api.genderize.io?name=peter").text)["gender"]
    if test == "male":                           # testing whether connection to api is sucessful, as peter is always male
        print("CONNECTION TO API SUCCESFUL \n")
    else:
        print("CONNECTION TO API UNSUCCESFUL")
        exit(0)

    def __init__(self, name):
        self.name = name

    def predictDetails(self):                            # the method containing body for prediction using APIs
        url = self.name
        try:
            genderreq = requests.get(
                "https://api.genderize.io?name=" + url)  # single usage url used as shown in documentation
            resultset1 = json.loads(genderreq.text)
            gender = resultset1["gender"]                # extraction of only the gender value from result set
            agereq = requests.get("https://api.agify.io?name=" + url)
            resultset2 = json.loads(agereq.text)
            age = resultset2["age"]
            print("Name:" + url + " ,predicted gender is " + gender + " and age is ", age)
            print(" ")
        except:                                          # to give exception when invalid names are given
            print("Invalid name given, please check !!")
            print(" ")


# TEST CASES by Denin

p1 = Predictor("Peter")
p1.predictDetails()
p3 = Predictor("Aisha")
p3.predictDetails()
p4 = Predictor("Sara")
p4.predictDetails()
p5 = Predictor("Denin")
p5.predictDetails()
p2 = Predictor(" ")     # invalid name given
p2.predictDetails()
p6 = Predictor("1234")  # invalid name given
p6.predictDetails()

flag = True
try:
    while flag == True:
        a = input("Press 0 (Zero) key to exit or else enter a new name to predict ")
        if a == '0':
            flag = False
            print("Exiting !! Thank You")
            exit(0)
        else:
            p7 = Predictor(a)
            p7.predictDetails()
except KeyboardInterrupt:
    exit(0)
