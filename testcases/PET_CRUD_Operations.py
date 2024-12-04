import requests

from utilities.Ui_Assessment_Utility import Utility_Class

#D:/Learn/2024/PythonRelated/RestAPIAssessment  = ../

createUserPayload = Utility_Class.loadPayLoad('../testdata/payload.json')
createUserPayload['name'] = 'TestPET'
cate= createUserPayload['category']
cate['name']='TestPETCategory'
tags=createUserPayload['tags']
print(type(tags))
tags[0]['name'] = 'TestPETags'

readConfigDetails = Utility_Class.readConfigDetails()


headers = {"accept":"application/json","Content-Type":"application/json"}
header = {"accept":"application/json"}

class Pet_CRUD_Operations:

    @staticmethod
    def createPet():
        print('creating PET')
        #print('base URL is: ',readConfigDetails['API']['baseURI'])
        createUserResponse = requests.post(readConfigDetails['API']['baseURI'],json=createUserPayload,headers=headers)
        responseJson = createUserResponse.json()
        return  responseJson

    @staticmethod
    def getPetByID(pet_id):
        print('retrieving pet details...')
        retrieveResponse = requests.get(readConfigDetails['API']['baseURI'] + pet_id, headers=header)
        responseJson = retrieveResponse.json()
        return responseJson

    @staticmethod
    def updatePETDetails(updatedRequestBody):
        print('updating the PET details..')
        updatePetResponse = requests.put(readConfigDetails['API']['baseURI'], json=updatedRequestBody, headers=headers)
        return updatePetResponse.json()

    @staticmethod
    def deletePETById(petID):
        print('deleting the PET details..')
        deletePetResponse = requests.delete(readConfigDetails['API']['baseURI'] + petID,headers=header)
        return deletePetResponse.json()





