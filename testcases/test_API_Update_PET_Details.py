from testcases.PET_CRUD_Operations import Pet_CRUD_Operations
from utilities.Ui_Assessment_Utility import Utility_Class

CreatedPetID=Pet_CRUD_Operations.createPet()
print(str(CreatedPetID['id']))
updateRequestBody = Utility_Class.loadPayLoad('../testdata/payload.json')
updateRequestBody['id'] =str(CreatedPetID['id'])
updateRequestBody['name'] = 'Pet_Name_Updated'

def test_Update_Pet_Details():
    print('updating PET details..')
    updateResponseJson = Pet_CRUD_Operations.updatePETDetails(updateRequestBody)
    assert updateResponseJson['id'] == CreatedPetID['id']
    assert updateResponseJson['name'] == 'Pet_Name_Updated'