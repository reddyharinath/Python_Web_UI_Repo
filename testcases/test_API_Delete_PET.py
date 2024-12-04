from testcases.PET_CRUD_Operations import Pet_CRUD_Operations

CreatedPetID=Pet_CRUD_Operations.createPet()
print(str(CreatedPetID['id']))

def test_Delete_PET():
    print('deleting PET details')
    deleteResponseJson = Pet_CRUD_Operations.deletePETById(str(CreatedPetID['id']))
    assert deleteResponseJson['message'] == str(CreatedPetID['id'])