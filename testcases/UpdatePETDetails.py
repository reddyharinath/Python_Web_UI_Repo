import json

import requests

from testcases.ReteievePETByID import RetrievePETByID
from utilities.Ui_Assessment_Utility import Utility_Class

getPetResponseJson = RetrievePETByID.getPetByID()

Header= {"accept":"application/json","Content-Type":"application/json"}
dataDict = Utility_Class.loadPayLoad('D:/Learn/2024/PythonRelated/RestAPIAssessment/testdata/payload.json')
dataDict['id'] = str(getPetResponseJson['id'])
dataDict['name'] = 'updateed pet'


class UpdatePetDetailsById:
    @staticmethod
    def updatePETDetails():
        print('updating the PET details..')
        updatePetResponse = requests.put('https://petstore.swagger.io/v2/pet',json=dataDict,headers=Header)
        return  updatePetResponse.json()

responseJson = UpdatePetDetailsById.updatePETDetails()
print(type(responseJson))
print(responseJson)

assert responseJson['name'] == dataDict['name']