import requests

from testcases.PET_CRUD_Operations import Pet_CRUD_Operations

Headers= {"accept":"application/json"}

createPetResponseInJson=Pet_CRUD_Operations.createPet()
petIDToRetrive = str(createPetResponseInJson['id'])


class RetrievePETByID:

    @staticmethod
    def getPetByID():
        print('retrieving pet details...')
        retrieveResponse= requests.get('https://petstore.swagger.io/v2/pet/'+petIDToRetrive,headers=Headers)
        responseJson=retrieveResponse.json()
        return  responseJson


getPetResponseJson = RetrievePETByID.getPetByID()
print('the json response is: ', getPetResponseJson)
print('the pet id is: ', getPetResponseJson['id'])