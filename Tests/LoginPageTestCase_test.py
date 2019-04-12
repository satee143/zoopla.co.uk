import pytest
from Pages.Homepage import homepage
from utills import utils as util
import time



@pytest.mark.usefixtures('Setup')
class TestLogin():

    def test_login(self):
        driver=self.driver
        Search=homepage(driver)
        driver.get(util.url)
        Search.Select_location(util.location)
        Search.Click_On_Submit_button()
        Search.Retrive_No_Of_Rows()
        Search.Listout()
        Search.Sorting_List()
        Search.Selecting_Property()
        Search.Property_Name_Retrive()
        Search.Click_On_Seller()
        Search.Check_The_Product()




