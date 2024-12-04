import pytest

from pages.BaseClass import BaseClass
from testcases.PET_CRUD_Operations import Pet_CRUD_Operations
from utilities.Ui_Assessment_Utility import Utility_Class

updateRequestBody = Utility_Class.loadPayLoad('../testdata/payload.json')
configuration_Details = Utility_Class.read_Config_Details()

logger=BaseClass.get_Log_Details()
dataFromJsonFile = Utility_Class.read_Json_File()


@pytest.mark.usefixtures("createPet")
class Test_e2e_PET_CRUD_Operations:

    def test_validate_Created_Pet_Details(self,createPet):

        logger.info("validating created PET details")
        fixtureResponse= self.CreatePetResponse
        petID=fixtureResponse['id']
        logger.info("created PET ID is: "+str(petID))
        assert fixtureResponse['name'] == 'TestPET'

    def test_retrieve_Pet_Details(self,createPet):
        fixtureResponse = self.CreatePetResponse

        logger.info("validating retrieved PET details")
        petID = fixtureResponse['id']
        getPetResponseJson = Pet_CRUD_Operations.getPetByID(str(petID))
        #print('Retrieve PET json response is: ', getPetResponseJson)
        logger.info("Retrieved PET id is: "+str( getPetResponseJson['id']))
        assert getPetResponseJson['id'] == petID

    def test_update_Pet_Details(self,createPet):
        fixtureResponse = self.CreatePetResponse

        logger.info("validating updated PET details")
        petID = fixtureResponse['id']
        updateRequestBody['id'] = str(petID)
        updateRequestBody['name'] = 'Pet_Name_Updated'
        updateResponseJson = Pet_CRUD_Operations.updatePETDetails(updateRequestBody)
        logger.info("Updated PET id is: " + str(updateResponseJson['id']))
        assert updateResponseJson['id'] == petID
        assert updateResponseJson['name'] == 'Pet_Name_Updated'

    def test_Delete_Pet_Details(self,createPet):

        logger.info("validating deleted PET details")
        fixtureResponse = self.CreatePetResponse
        petID = fixtureResponse['id']
        deleteResponseJson = Pet_CRUD_Operations.deletePETById(str(petID))
        logger.info("Deleted PET id is: " + str(deleteResponseJson['message']))
        assert deleteResponseJson['message'] == str(petID)

