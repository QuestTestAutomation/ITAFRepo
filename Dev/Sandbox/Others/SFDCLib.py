from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.support.ui import Select
import time
import re
import CPQLib
# import Libs/CPQLib.py



# def get_webdriver_instance():
#     se2lib = BuiltIn().get_library_instance('Selenium2Library')
#     return se2lib._current_browser()

def Open_Browser_And_Launch_Application(brow,url):
    if brow ==  'ff':
        driver = webdriver.Firefox()
        driver.get(url)
    if brow ==  'gc':
        driver = webdriver.Chrome(executable_path='C:\Selenium\Selenium 3.4\Drivers\chromedriver.exe')
        #driver = webdriver.Chrome()
        # driver.get(url)
        # driver = webdriver.Remote(command_executor='http://localhost:9515/',desired_capabilities=DesiredCapabilities.CHROME)
        # driver.get(url)
    if brow == 'ie':
        driver = webdriver.Ie()
    return driver


def get_text_column_value(driver,label,Index):


    id = "-1"
    tempindex = 0
    i = 0
    tindex = 0
    lists = driver.find_elements_by_tag_name("TD")

    for list in lists:
        i = int(i) + int(1)
        # print "label : " + str(label)
        if list.get_attribute("class") == "labelCol" and list.text == label:
            # print "hurr : "  + str(list.text)
            tempindex = int(tempindex) + int(1)
            if int(tempindex) == int(Index):
                tindex = int(i) + int(1)

        if tindex == i:
            # idiv = list.find_element_by_tag_name("div")
            id = list.text
            # print "hurr hurr : " + str(list.text)
            # id = idiv.text
            # # print "hurr hurr : " + str(idiv.text)
            break

    return id

def get_Select_id(driver,title,Index,visibletext):
    id = "-1"
    tempindex = 0
    i = 0
    tindex = 0
    lists = driver.find_elements_by_tag_name("SELECT")
    for list in lists:
        if list.get_attribute("title") == title:
            tempindex = int(tempindex) + int(1)
            if int(tempindex) == int(Index):
                id = list.get_attribute("id")
                select = Select(list)
                select.select_by_visible_text(visibletext)
    return id

def Select_value_from_list(driver,title,Index,visibletext):
    id = get_Select_id(driver,title,Index,visibletext)

def set_input_column_value(driver,label,Index,fieldvalue):

    id = "-1"
    tempindex = 0
    i = 0
    tindex = 0
    lists = driver.find_elements_by_tag_name("TD")

    for list in lists:
        i = int(i) + int(1)
        # labelCol
        # requiredInput
        if list.get_attribute("class") == "labelCol" and list.text == label:

            tempindex = int(tempindex) + int(1)
            if int(tempindex) == int(Index):
                tindex = int(i) + int(1)

        if tindex == i:
            id = list.get_attribute("id")
            webele = list.find_element_by_id(list.get_attribute("id"))

            driver.execute_script("return arguments[0].scrollIntoView(true);", webele)
            webele.click()
            webele.send_keys(fieldvalue)
            print "id is " + str(id)
    return id

def click_SFDCbutton(driver,btntitle,btnindex):
    id = "-1"
    tempindex = 0
    i = 0
    tindex = 0
    lists = driver.find_elements_by_tag_name("INPUT")
    # print len(lists)
    for list in lists:
        # print " class  :"  + str(list.get_attribute("class"))
        print " Title  :"  + str(list.get_attribute("title"))
        if list.get_attribute("class") is not None and list.get_attribute("title") is not None :
            if list.get_attribute("class").upper() == ("btn").upper() and list.get_attribute("title").upper() == (btntitle).upper() :

                tempindex = int(tempindex) + int(1)
                if int(tempindex) == int(btnindex):
                 print " Title  :" + str(list.get_attribute("title"))
                 id = list.get_attribute("value")

                 driver.execute_script("return arguments[0].scrollIntoView(true);", list)
                 list.click()
                 break

    return id
def set_required_input_column_value(driver,label,Index,fieldvalue):

    id = "-1"
    tempindex = 0
    i = 0
    tindex = "-10000"
    lists = driver.find_elements_by_tag_name("TD")
    print "text " + str(len(lists))
    for list in lists:
        print str(i)
        i = int(i) + int(1)

        if tindex == i:
            inpelements = list.find_elements_by_tag_name("INPUT")


            for inpele in inpelements:
                if len(inpelements) == int(1):

                    driver.execute_script("return arguments[0].scrollIntoView(true);", inpele)
                    inpele.click()
                    inpele.send_keys(fieldvalue)

            break

        if list.get_attribute("class") == "labelCol requiredInput":
            lbllists = list.find_elements_by_tag_name("LABEL")
            # print "label : "  + str(len(lbllists))
            for lbllist in lbllists:

              if list.get_attribute("class") == "labelCol requiredInput" and int((lbllist.text).find(label)) != int('-1'):

                  tempindex = int(tempindex) + int(1)

                  if int(tempindex) == int(Index):
                    tindex = int(i) + int(1)


    return  id


def Search_Account_Country_Lookup(driver) :

    handle = []
    parent_h = driver.current_window_handle
    print "The current page title : " + driver.title

    Open_Required_Loopup_Window(driver,'Country','1')
    # driver.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr/td[2]/form/div/div[2]/div[3]/table/tbody/tr[10]/td[2]/div/span/a/img").click()
    handles = driver.window_handles  # before the pop-up window closes
    # driver.remove(parent_h)
    handles.remove(parent_h)

    driver.switch_to_window(handles.pop())
    popup_h = driver.current_window_handle
    driver.implicitly_wait(10)  # seconds
    print "The current popup page title : " + driver.title
    time.sleep(20)
    driver.switch_to.frame(0)
    # ele = driver.find_element_by_id('searchFrame')
    # ele.click()
    # lists = driver.find_elements_by_tag_name("input")
    # # print "*********----   " + str(len(lists))
    # # print "*********----frame   " + str(len(driver.find_elements_by_tag_name("frame")))
    # # print "*********----form   " + str(len(driver.find_elements_by_tag_name("form")))
    # # print "*********----div   " + str(len(driver.find_elements_by_tag_name("div")))
    # # print "*********----input   " + str(len(driver.find_elements_by_tag_name("input")))
    # for list in lists:
        # print "*********----framelistinput   " + str(len(list.find_elements_by_tag_name("input")))
        # print "*********----framelistdiv   " + str(len(list.find_elements_by_tag_name("div")))
        # print "*********----framelistform   " + str(len(list.find_elements_by_tag_name("form")))
        # print "*********----framelisthtml   " + str(len(list.find_elements_by_tag_name("html")))
        # print "*********" + list.get_attribute("id")
        # print "*********" + list.get_attribute("class")
    element = driver.find_element_by_id('lksrch')
    driver.execute_script("return arguments[0].scrollIntoView(true);", element)
    driver.find_element_by_id('lksrch').click()
    driver.find_element_by_id('lksrch').send_keys('India')
    lists = driver.find_elements_by_tag_name("input")


    # driver.find_element_by_id(_tag_name("INPUT")'lksrch').click()
    # driver.find_element_by_id('lksrch').sendkeys("India")
    # driver.find_element_by_xpath('/html/body/form/div/div[2]/input[1]').click()
    # driver.find_element_by_xpath('/html/body/form/div/div[2]/input[1]').sendkeys("India")
    driver.find_element_by_xpath("/html/body/form/div/div[2]/input[2]").click()
    time.sleep(10)
    driver.switch_to_window(popup_h)
    driver.implicitly_wait(10)  # seconds
    driver.switch_to.frame(1)
    time.sleep(5)
    driver.find_element_by_link_text('India').click()
    time.sleep(10)
    driver.switch_to_window(parent_h)





def Handle_Lookup_Frame(driver) :
    element = driver.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr/td[2]/form/div/div[2]/div[3]/table/tbody/tr[10]/td[2]/div/span/a/img")
    driver.execute_script("return arguments[0].scrollIntoView(true);", element)
    driver.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr/td[2]/form/div/div[2]/div[3]/table/tbody/tr[10]/td[2]/div/span/a/img").click()
    driver.switch_to_frame("searchFrame")
    driver.implicitly_wait(10)  # seconds
    driver.find_element_by_xpath('/html/body/form/div/div[2]/input[1]').click()
    driver.find_element_by_xpath('/html/body/form/div/div[2]/input[1]').sendkeys("India")



def set_text_input_column_value(driver,label,Index,fieldvalue):

    id = "-1"
    tempindex = 0
    i = 0
    tindex = "-10000"
    lists = driver.find_elements_by_tag_name("TD")
    # print "text " + str(len(lists))
    for list in lists:
        # print str(i)
        i = int(i) + int(1)
        # labelCol
        # requiredInpu t
        if tindex == i:
            # id = list.get_attribute("id")
            # webele = list.find_element_by_id(list.get_attribute("id"))
            # webele.click()
            # webele.send_keys(fieldvalue)
            inpelements = list.find_elements_by_tag_name("INPUT")


            for inpele in inpelements:
                if len(inpelements) == int(1):

                    driver.execute_script("return arguments[0].scrollIntoView(true);", inpele)
                    inpele.click()
                    inpele.send_keys(fieldvalue)

            break

        if list.get_attribute("class") == "labelCol":
            lbllists = list.find_elements_by_tag_name("LABEL")

            for lbllist in lbllists:

              if list.get_attribute("class") == "labelCol" and lbllist.text == label:

                  tempindex = int(tempindex) + int(1)

                  if int(tempindex) == int(Index):
                    tindex = int(i) + int(1)


    return  id

def Open_Required_Loopup_Window(driver,label,Index):

    id = "-1"
    tempindex = 0
    i = 0
    tindex = "-10000"
    lists = driver.find_elements_by_tag_name("TD")
    # print "text " + str(len(lists))
    for list in lists:
        # print str(i)
        i = int(i) + int(1)

        if tindex == i:
            inpelements = list.find_elements_by_tag_name("A")


            for inpele in inpelements:
                if len(inpelements) == int(1):

                    driver.execute_script("return arguments[0].scrollIntoView(true);", inpele)
                    inpele.click()


            break

        if list.get_attribute("class") == "labelCol requiredInput":
            lbllists = list.find_elements_by_tag_name("LABEL")
            # print "label : "  + str(len(lbllists))
            for lbllist in lbllists:

              if list.get_attribute("class") == "labelCol requiredInput" and int((lbllist.text).find(label)) != int('-1'):

                  tempindex = int(tempindex) + int(1)

                  if int(tempindex) == int(Index):
                    tindex = int(i) + int(1)


    return  id

def search_SFDC_Entity(driver,searchvalue):
    print "searchvalue  : "  + searchvalue
    element = driver.find_element_by_id("phSearchInput")
    driver.execute_script("return arguments[0].scrollIntoView(true);", element)
    driver.find_element_by_id("phSearchInput").click()
    driver.find_element_by_id("phSearchInput").send_keys(searchvalue)
    driver.find_element_by_id("phSearchButton").click()


def search_SFDC_Entity_Sidebar(driver,searchvalue) :
    element = driver.find_element_by_id("sbstr")
    driver.execute_script("return arguments[0].scrollIntoView(true);", element)
    driver.find_element_by_id("sbstr").click()
    driver.find_element_by_id("sbstr").send_keys(searchvalue)
    # driver.find_element_by_name("search").click()
    btntitle = 'Go!'
    click_SFDCbutton(driver, btntitle, 1)



def Navigate_to_Header(driver,searchvalue,Index):
    id = "-1"
    tempindex = 0
    i = 0
    tindex = "-10000"
    lists = driver.find_elements_by_tag_name("H3")
    print "text " + str(len(lists))
    for list in lists:
        print list.text
        if (list.text).upper() == searchvalue.upper() :
            tempindex = int(tempindex) + int(1)

            if int(tempindex) == int(Index):

                driver.execute_script("return arguments[0].scrollIntoView(true);", list)
                list.click()

def Click_Section_Button(driver,btntitle,Index) :
    id = "-1"
    tempindex = 0
    lists = driver.find_elements_by_class_name("pbButton")
    # print "pbbtn : " + str(len(lists))
    for list in lists:
        btnlists = list.find_elements_by_tag_name("INPUT")
        # print "btnlists : " + str(len(btnlists))
        if int(id) == int(1) :
            break
        for btnlist in btnlists :
            print btnlist.get_attribute("title")
            if btnlist.get_attribute("class") is not None and btnlist.get_attribute("title") is not None:
                if btnlist.get_attribute("class").upper() == ("btn").upper() and btnlist.get_attribute("title").upper() == (btntitle).upper():

                    tempindex = int(tempindex) + int(1)
                    if int(tempindex) == int(Index):
                        id = "1"
                        # print btnlist.get_attribute("title")

                        driver.execute_script("return arguments[0].scrollIntoView(true);", btnlist)
                        btnlist.click()
                        break


def Click_Section_Button1(driver,btntitle,Index) :
    id = "-1"
    tempindex = 0

    btnlists = driver.find_elements_by_tag_name("INPUT")
    # print "btnlists : " + str(len(btnlists))


    for btnlist in btnlists :
        print btnlist.get_attribute("title")
        if btnlist.get_attribute("class") is not None and btnlist.get_attribute("title") is not None:
           if btnlist.get_attribute("class").upper() == ("btn").upper() and btnlist.get_attribute("title").upper() == (btntitle).upper():

            tempindex = int(tempindex) + int(1)
            if int(tempindex) == int(Index):
               id = "1"
                        # print btnlist.get_attribute("title")

               driver.execute_script("return arguments[0].scrollIntoView(true);", btnlist)
               btnlist.click()
               break

def Search_Required_Lookup(driver,label,Index,lookupvalue) :

    handle = []
    parent_h = driver.current_window_handle
    print "The current page title : " + driver.title
    # Open_Loopup_Window(driver,label,Index)
    Open_Required_Loopup_Window(driver,label,Index)
    # driver.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr/td[2]/form/div/div[2]/div[3]/table/tbody/tr[10]/td[2]/div/span/a/img").click()
    handles = driver.window_handles  # before the pop-up window closes
    # driver.remove(parent_h)
    handles.remove(parent_h)

    driver.switch_to_window(handles.pop())
    popup_h = driver.current_window_handle
    driver.implicitly_wait(5)  # seconds
    print "The current popup page title : " + driver.title
    time.sleep(5)
    driver.switch_to.frame(0)

    driver.find_element_by_id('lksrch').click()
    driver.find_element_by_id('lksrch').send_keys(lookupvalue)

    click_SFDCbutton(driver, 'Go!', 1)

    driver.switch_to_window(popup_h)
    driver.implicitly_wait(3)  # seconds
    driver.switch_to.frame(1)
    time.sleep(2)
    driver.find_element_by_link_text(lookupvalue).click()
    time.sleep(3)
    driver.switch_to_window(parent_h)

def Search_Lookup(driver,label,Index,lookupvalue) :

    handle = []
    parent_h = driver.current_window_handle
    print "The current page title : " + driver.title
    Open_Lookup_Window(driver,label,Index)
    # Open_Required_Loopup_Window(driver,label,Index)
    # driver.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr/td[2]/form/div/div[2]/div[3]/table/tbody/tr[10]/td[2]/div/span/a/img").click()
    handles = driver.window_handles  # before the pop-up window closes

    handles.remove(parent_h)

    driver.switch_to_window(handles.pop())
    popup_h = driver.current_window_handle
    driver.implicitly_wait(5)  # seconds
    print "The current popup page title : " + driver.title
    time.sleep(5)
    driver.switch_to.frame(0)
    driver.find_element_by_id('lksrch').click()
    driver.find_element_by_id('lksrch').send_keys(lookupvalue)
    click_SFDCbutton(driver, 'Go!', 1)
    driver.switch_to_window(popup_h)
    driver.implicitly_wait(3)  # seconds
    driver.switch_to.frame(1)
    time.sleep(2)
    driver.find_element_by_link_text(lookupvalue).click()
    time.sleep(3)
    driver.switch_to_window(parent_h)


def Open_Lookup_Window(driver,label,Index):

    id = "-1"
    tempindex = 0
    i = 0
    tindex = "-10000"
    lists = driver.find_elements_by_tag_name("TD")
    print "text " + str(len(lists))
    for list in lists:
        print str(i)
        i = int(i) + int(1)

        if tindex == i:
            inpelements = list.find_elements_by_tag_name("A")


            for inpele in inpelements:
                if len(inpelements) == int(1):

                    driver.execute_script("return arguments[0].scrollIntoView(true);", inpele)
                    inpele.click()


            break

        if list.get_attribute("class") == "labelCol":
            lbllists = list.find_elements_by_tag_name("LABEL")
            # print "label : "  + str(len(lbllists))
            for lbllist in lbllists:


              if list.get_attribute("class") == "labelCol" and lbllist.text == label:

                  tempindex = int(tempindex) + int(1)

                  if int(tempindex) == int(Index):
                    tindex = int(i) + int(1)


    return  id

def Click_SFDCLink(driver,label,Index):
    id = "-1"
    tempindex = 0
    lists = driver.find_elements_by_tag_name("A")
    print "text " + str(len(lists))
    print " label " +  str(label)
    for list in lists:
        # if id != "-1" :
        #     break
        # print "**********************************************"
        # print "if  : " + str(int((list.text).find(label)))
        # print "if  : " + str(((list.text).strip()).upper() == (label.strip()).upper())
        # print "list.text : " + str(list.text)
        # print " label " + str(label)
        if (((list.text).strip()).upper() == (label.strip()).upper()):

            tempindex = int(tempindex) + int(1)

            if int(tempindex) == int(Index):
                id = list.get_attribute("Id")

                driver.execute_script("return arguments[0].scrollIntoView(true);", list)
                list.click()
                break


def select_required_input_column_value(driver, label, Index, fieldvalue):
    id = "-1"
    tempindex = 0
    i = 0
    tindex = "-10000"
    lists = driver.find_elements_by_tag_name("TD")
    print "text " + str(len(lists))
    for list in lists:
        print str(i)
        i = int(i) + int(1)

        if tindex == i:
            inpelements = list.find_elements_by_tag_name("Select")

            for inpele in inpelements:
                if len(inpelements) == int(1):

                    driver.execute_script("return arguments[0].scrollIntoView(true);", inpele)
                    inpele.click()
                    select = Select(inpele)
                    select.select_by_visible_text(fieldvalue)

            break

        if list.get_attribute("class") == "labelCol requiredInput":
            lbllists = list.find_elements_by_tag_name("LABEL")
            # print "label : "  + str(len(lbllists))
            for lbllist in lbllists:

                if list.get_attribute("class") == "labelCol requiredInput" and int((lbllist.text).find(label)) != int('-1'):

                    tempindex = int(tempindex) + int(1)

                    if int(tempindex) == int(Index):
                        tindex = int(i) + int(1)

    return id


def select_input_column_value(driver,label,Index,fieldvalue):

    id = "-1"
    tempindex = 0
    i = 0
    tindex = "-10000"
    lists = driver.find_elements_by_class_name("labelCol")
    print "lenlists  " + str(len(lists))
    for list in lists:
        if list is not None and list.get_attribute("class") is not None :
            lbllists = list.find_elements_by_tag_name("LABEL")
            print "Class  : " + str(list.get_attribute("class"))
            print "lenlists  "  + str(len(lbllists))
            if int(len(lbllists)) > 0 :
                for lbllist in lbllists:
                    if lbllist is not None and lbllist.get_attribute("for") is not None:
                     print "Class  : " + str(list.get_attribute("class"))
                     print "lbllist.text  : " + str(lbllist.text)
                     if list.get_attribute("class") == "labelCol" and lbllist.text == label:

                       tempindex = int(tempindex) + int(1)

                       if int(tempindex) == int(Index):
                              print "for  : " + str(list.get_attribute("for"))



def Get_Input_FieldID(driver,label,Index) :
 forid = "-1"
 tempindex = 0
 i = 0
 tindex = "-10000"
 lists = driver.find_elements_by_class_name("labelCol")
 # print "lenlists  " + str(len(lists))
 for list in lists:
        if list is not None and list.get_attribute("class") is not None :
            lbllists = list.find_elements_by_tag_name("LABEL")

            # print "lenlists  "  + str(len(lbllists))
            if int(len(lbllists)) > 0 :
                for lbllist in lbllists:

                    if lbllist is not None and lbllist.get_attribute("for") is not None and lbllist.text is not None :

                     if list.get_attribute("class") == "labelCol" and lbllist.text == label:
                       # print "Class  : " + str(list.get_attribute("class"))
                       # print "lbllist.text  : " + str(lbllist.text)
                       tempindex = int(tempindex) + int(1)

                       if int(tempindex) == int(Index):
                         # print "for  : " + str(lbllist.get_attribute("for"))
                         forid = lbllist.get_attribute("for")
                         break
 return forid


def Get_Required_Input_FieldID(driver,label,Index) :
 forid = "-1"
 tempindex = 0
 i = 0
 tindex = "-10000"
 classname = 'labelCol requiredInput'
 lists = driver.find_elements_by_css_selector('td[class="labelCol requiredInput"]')
 # print "lenlists  " + str(len(lists))
 for list in lists:
        # print "lenlclass  " + str(list.get_attribute("class"))
        if list is not None and list.get_attribute("class") is not None :
            lbllists = list.find_elements_by_tag_name("LABEL")

            # print "lenlists  "  + str(len(lbllists))
            if int(len(lbllists)) > 0 :
                for lbllist in lbllists:
                    # print "lbllist.text  : " + str(lbllist.text)
                    if lbllist is not None and lbllist.get_attribute("for") is not None and lbllist.text is not None :

                     if list.get_attribute("class") == "labelCol requiredInput" and int((lbllist.text).find(label)) != int('-1'):
                       # print "Class  : " + str(list.get_attribute("class"))
                       # print "lbllist.text  : " + str(lbllist.text)
                       tempindex = int(tempindex) + int(1)

                       if int(tempindex) == int(Index):
                         # print "for  : " + str(lbllist.get_attribute("for"))
                         forid = lbllist.get_attribute("for")
                         break
 return forid


def select_Required_SFDC_Dropdown_Value(driver,label,Index,vFieldvalue):
    myid = Get_Required_Input_FieldID(driver, label, Index)
    # print "Hello : " + str(myid)
    element = driver.find_element_by_id(myid)
    driver.execute_script("return arguments[0].scrollIntoView(true);", element)
    driver.find_element_by_id(myid).click()

    select = Select(driver.find_element_by_id(myid))

    # select by visible text
    select.select_by_visible_text(vFieldvalue)

def select_SFDC_Dropdown_Value(driver,label,Index,vFieldvalue):
    myid = Get_Input_FieldID(driver, label, Index)
    print "Hello : " + str(myid)
    element = driver.find_element_by_id(myid)
    driver.execute_script("return arguments[0].scrollIntoView(true);", element)
    driver.find_element_by_id(myid).click()

    select = Select(driver.find_element_by_id(myid))

    # select by visible text
    select.select_by_visible_text(vFieldvalue)

def Select_Steel_Brick_Dropdown_Value(driver,label,Index) :
    tempindex = 0
    i = 0
    tindex = "-10000"
    # driver.find_element_by_id("tsidButton").click()
    print  "Hu " + str(driver.find_element_by_id("tsidLabel").text)
    if driver.find_element_by_id("tsidLabel").text != label :
        element = driver.find_element_by_id("tsidLabel")
        driver.execute_script("return arguments[0].scrollIntoView(true);", element)
        driver.find_element_by_id("tsidLabel").click()
        driver.find_element_by_link_text(label).click()


def click_CPQ_Buttom(driver,btntitle,Index) :
    bid = "-1"
    tempindex = 0
    i = 0
    tindex = "-10000"
    lists = driver.find_elements_by_tag_name("PAPER-BUTTON")
    print "lenlists  " + str(len(lists))

    for list in lists:
        print list.text
        if list.text is not None :
            if list.text == btntitle :
                print list.text
                print list.text == btntitle
                tempindex = int(tempindex) + int(1)
                if tempindex == Index:
                    list.click()
                    bid = "1"
                    break
    return bid

def click_CPQ_Link(driver,label,Index) :
    tempindex = 0
    i = 0
    tindex = "-10000"
    lists = driver.find_elements_by_class_name("list")
    print "lenlists  " + str(len(lists))
    for list in lists:
        alists = list.find_elements_by_tag_name("A")
        for alist in alists:
            if alist.text is not None:
                if alist.text == label:
                    tempindex = int(tempindex) + int(1)
                    if tempindex == Index:
                        list.click()
                        break


def wait_CPQ_button(driver,btntitle,Index) :

    for x in  range(0,20,1) :
        btnid = click_CPQ_Buttom(driver,btntitle,Index)
        if btnid == "1" :
            break
        elif btnid == "-1" :

            time.sleep(10)

def wait_for_opty_sbl_rowid(driver,label,index) :
    id = "-1"
    val = get_text_column_value(driver,label,index)
    val11 = isNotBlank (val)
    # print "is none : " + val is None
    # print "is none val : " + str(val)
    # print "is none : " + str(val11)
    for i in range(0,900,10):
        driver.refresh()
        time.sleep(10)
        val = get_text_column_value(driver,label,index)
        # print "iThe value of  index : " + str(i)
        # print "iThe value of  val : " + str(val)
        # if val == "-1":
        if isBlank(val):
            time.sleep(10)
            val = get_text_column_value(driver, label, index)
        else :

            # print "tu nee amma true" + str(val)
            id = val
            break


    # print  "Siebel row id is  : "  + str(val)
    return id

def isNotBlank (myString):
    if myString and myString.strip():
        #myString is not None AND myString is not empty or blank
        return True
    #myString is None OR myString is empty or blank
    return False


def isBlank (myString):
    if myString and myString.strip():
        #myString is not None AND myString is not empty or blank
        return False
    #myString is None OR myString is empty or blank
    return True

def Handle_CPQQuote_Popup(driver) :
    qtext = "-1"
    quoteno = "-1"
    parent_h = driver.current_window_handle




    for i in range(0, 600, 10):

        handles = driver.window_handles
        if len(handles) == 2 :
            handles.remove(parent_h)
            driver.switch_to_window(handles.pop())
            popup_h = driver.current_window_handle
            # driver.implicitly_wait(10)  # seconds
            print "The current popup page title : " + driver.title
            # time.sleep(20)
            driver.switch_to_window(popup_h)
            qtext = driver.find_element_by_css_selector('html body span').text
            print "qtext value is : " + str(qtext)
            element = driver.find_element_by_css_selector('html body center input')
            driver.execute_script("return arguments[0].scrollIntoView(true);", element)
            driver.find_element_by_css_selector('html body center input').click()



            time.sleep(5)
            driver.switch_to_window(parent_h)
            re_prodId = re.compile(r'Quote is successfully created.Quote Number is([^"]+).')

            for m in re_prodId.findall(qtext):
                # print(m)
                quoteno = m
                quoteno = quoteno.strip()


            break
        else :
            time.sleep(10)

        print " Handles Length : " + str(len(handles))
    time.sleep(6)
    driver.refresh()
    return  quoteno

def browser_navigate_back(driver) :
    driver.execute_script("window.history.go(-1)")
    time.sleep(5)

def click_SFDCbutton_new(driver,btntitle,btnindex):
    id = "-1"
    tempindex = 0
    i = 0
    tindex = 0
    lists = driver.find_elements_by_class_name("btn")
    # print len(lists)
    for list in lists:
        # print " class  :"  + str(list.get_attribute("class"))
        print " Title  :"  + str(list.get_attribute("title"))
        if list.get_attribute("class") is not None and list.get_attribute("title") is not None :
            if list.get_attribute("class").upper() == ("btn").upper() and list.get_attribute("title").upper() == (btntitle).upper() :

                tempindex = int(tempindex) + int(1)
                if int(tempindex) == int(btnindex):
                 print " Title  :" + str(list.get_attribute("title"))
                 id = list.get_attribute("value")

                 driver.execute_script("return arguments[0].scrollIntoView(true);", list)
                 list.click()
                 break

    return id
def get_quote_number(driver,Quotelink) :
    id = "-1"
    vTarindex = 0
    vSourceindex = 0
    driver.refresh()
    time.sleep(5)
    elelink = driver.find_element_by_link_text(Quotelink)
    ahref = elelink.get_attribute("href")
    ele_splits = ahref.split("/")
    vTarindex = len(ele_splits) - int(1)
    tarstr = str((ele_splits[int(vTarindex)]))
    print "tarstr  " + str(tarstr)
    elems = driver.find_elements_by_xpath("//a[@href]")
    # print "length  : "  +  str(len(elems))
    for elem in elems:
        print "href : " + str(elem.get_attribute("href"))
        # # print "text  : " + str(elem.get_attribute("text"))
        print "text  : " + str(elem.text)
        ahref1 = elem.get_attribute("href")
        ele_splits1 = ahref1.split("/")
        vSourceindex = len(ele_splits1) - int(1)
        sourcestr = str((ele_splits1[int(vSourceindex)]))
        # print "sourcestr  " + str(sourcestr)
        if sourcestr == tarstr :
                if elem.text == Quotelink:
                    id = "-1'"
                else :
                    id = elem.text
            # print "href ++ : " + str(elem.get_attribute("href"))
            #
            #
            # print "ele len : " + str(len(ele_splits))
            # print "ele len : " + str((ele_splits[3]))
            # linkxpath = "//a[@href=/" \
            #             "" + ele_splits[3] + "]"
            # print "linkxpath  : " + str(linkxpath)
            # elements = driver.find_elements_by_xpath(linkxpath)
            # print "linlen   : " + str(len(elements))
            # for element in elements:
            #     if element.text == Quotelink:
            #         id = "-1'"
            #     else :
            #         id = element.text

    return id

def scroll_to_bottom(driver) :
    lastHeight = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        newHeight = driver.execute_script("return document.body.scrollHeight")
        if newHeight == lastHeight:
            break
        lastHeight = newHeight

def switch_to_new_tab(driver) :
    main_window = driver.current_window_handle
    driver.switch_to.window(driver.window_handles[1])
    return main_window


def CPQ_Add_Products_Handle_Errors(driver) :
    id = "-1"
    errors = CPQLib.pgselectproduct_checkfor_errors(driver)
    print "errors : "  + str(errors)
    if errors == "-1" :
        print "No Errors"
    else :
        browser_navigate_back(driver)
        time.sleep(30)
        CPQLib.pgconfigureproduts_click_add_products(driver)
    #    Wait Until Page Contains    Product Selection
        CPQLib.pgselectproduct_waitfor_Select_Button(driver)

