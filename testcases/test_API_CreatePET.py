from testcases.PET_CRUD_Operations import Pet_CRUD_Operations


def test_CretePet():
    createPetResponseInJson = Pet_CRUD_Operations.createPet()
    print('Created PET id is: ', createPetResponseInJson['id'])
    assert createPetResponseInJson['name'] == 'TestPET'




