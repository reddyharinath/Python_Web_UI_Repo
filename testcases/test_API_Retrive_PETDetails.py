from testcases.PET_CRUD_Operations import Pet_CRUD_Operations

CreatedPetID=Pet_CRUD_Operations.createPet()
#print(str(CreatedPetID['id']))

def test_Retrieve_Pet_Details():
    print('retrieving PET details:')
    getPetResponseJson = Pet_CRUD_Operations.getPetByID(str(CreatedPetID['id']))
    print('Retrieve PET json response is: ', getPetResponseJson)
    print('Retrieved PET id is: ', getPetResponseJson['id'])
    assert getPetResponseJson['id'] == CreatedPetID['id']

