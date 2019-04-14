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
        self.driver.find_element_by_id(self.location_textbox_id).clear()
        self.driver.find_element_by_id(self.location_textbox_id).send_keys(location)

    def Click_On_Submit_button(self):
        self.driver.find_element_by_id(self.search_button_id).click()

    def Retrive_No_Of_Rows(self):
        Properties=len(self.driver.find_elements_by_xpath(self.retriv_data_xpath))
        print(Properties)


    def Listout(self):
        list=self.driver.find_elements_by_xpath(self.prop_value_xpath)
        self.l=[]
        for lists in list:
            l0=lists.text
            if l0.isalpha()==False:
                self.l.append(l0)
            else:
                print('The Price is not in Numeric')
        print('Price List As Per Displayed on the Page')
        print(self.l)


    def Sorting_List(self):
        l1=[]
        for m in self.l:
            l2 = m.replace(',', '')
            l3 = l2.split()
            l1.append(int(l3[0][1:]))

        print("Price Of the Property  in Descending Order:")
        print(sorted(l1,reverse=True))

    def Selecting_Property(self):
        list = self.driver.find_elements_by_xpath(self.prop_value_xpath)
        list[8].click()

    def Property_Name_Retrive(self):
        self.property=self.driver.find_element_by_xpath(self.property_name_xpath).text
        print(self.property)

    def Click_On_Seller(self):
        seller=self.driver.find_element_by_xpath(self.owner_name_xpath)
        seller_name=seller.text
        print(seller_name)
        seller.click()

    def Check_The_Product(self):
        product_name=self.driver.find_element_by_tag_name('html').text
        if self.property in product_name:
            print("Match Sucesfful")
        else:
            print('Match Not Sucessfull')






