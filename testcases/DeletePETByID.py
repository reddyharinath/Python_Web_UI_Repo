import requests

from testcases.UpdatePETDetails import UpdatePetDetailsById

updateResponseJson = UpdatePetDetailsById.updatePETDetails()
petIDToDelete = str(updateResponseJson['id'])


class DeletePetByID:

    @staticmethod
    def deletePETById():
        deletePetResponse =requests.delete('https://petstore.swagger.io/v2/pet/'+petIDToDelete,headers={"accept":"application/json"})
        print('delete pet response...',deletePetResponse.text)
        deletePetResponseJson = deletePetResponse.json()
        return deletePetResponseJson

responseInJson = DeletePetByID.deletePETById()
print('delete pet response in json: ', responseInJson)

assert  responseInJson['message'] == petIDToDelete