import time
from selenium.webdriver.common.action_chains import ActionChains
class homepage:


    def __init__(self,driver):
        self.driver=driver
        self.location_textbox_id='search-input-location'
        self.search_button_id='search-submit'
        self.retriv_data_xpath='//li[@class="srp clearfix   "]'
        self.prop_value_xpath='//li[@id]//a[@class="listing-results-price text-price"]'
        self.property_name_xpath='//*[@class="ui-property-summary__title ui-title-subgroup"]'
        self.owner_name_xpath='//h4[@class="ui-agent__name"]'



    def Select_location(self,location):
        #self.driver.find_element_by_xpath(self.location_textbox_xpath).clear()
        self.driver.find_element_by_id(self.location_textbox_id).send_keys(location)

    def Click_On_Submit_button(self):
        self.driver.find_element_by_id(self.search_button_id).click()

    def Retrive_No_Of_Rows(self):
        val=(self.driver.find_elements_by_xpath(self.retriv_data_xpath))
        val1=len(val)

        print(val1)

    def Listout(self):
        list=self.driver.find_elements_by_xpath(self.prop_value_xpath)
        l=[]
        l1=[]
        for lists in list:
            l0=lists.text
            l2 = l0.replace(',', '')
            l3 = l2.split()
            l1.append(l3[0][1:])

        lis=[]
        print(l)
        print(l1)
        for m in l1:
            lis.append(int(m))
        print("Price Of the Property  in Descending Order:")
        ls1=sorted(lis,reverse=True)
        for m in ls1:
            print(m)
        #print('Asscending Order:',sorted(lis))
        list[6].click()
        # l1=l.sort()
        # print(l1)



    def Property_Name_Retrive(self):
        property=self.driver.find_element_by_xpath(self.property_name_xpath).text
        print(property)

    def Click_On_Seller(self):
        seller=self.driver.find_element_by_xpath(self.owner_name_xpath)
        seller_name=seller.text
        print(seller_name)
        seller.click()

    def Check_The_Product(self):
        product_name=self.driver.find_element_by_tag_name('html').text
        if property in product_name:
            print("Match Sucesfful")
        else:
            print('Match Not Sucessfull')






