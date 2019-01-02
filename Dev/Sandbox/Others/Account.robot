*** Settings ***
Library  Selenium2Library
Library  ./Utillib.py
Library  ./XLLib.py
Library  ./LoginPage.py
Library  ./Logout.py
Library  ./SFDCLib.py




*** Variables ***
${AccountName}  acc2
${Accountstreet}  acc2
${Lookupxpath}  /html/body/div/div[2]/table/tbody/tr/td[2]/form/div/div[2]/div[3]/table/tbody/tr[10]/td[2]/div/span/a/img
${SelAccountType}  p3
${btn_continue_xpath}  /html/body/div/div[2]/table/tbody/tr/td[2]/form/div/div[3]/table/tbody/tr/td[2]/input[1]
${inp_country_id}  lksrch #lookup field
${inp_country_xpath}  /html/body/form/div/div[2]/input[1]

${AccountSite}
*** Keywords ***


Load Account Test Data
    ${SearchAccount}=    Get XL Cell Value Using Column Header    ${testdatafile}    ${testdatasheet}    ${tcrownum}    Account

    set test variable     ${SearchAccount}  ${SearchAccount}



Navigate To Accounts

    Click Link    link=Accounts
    sleep    10s
    Wait Until Page Contains    Recent Accounts



Click On New Account
    click element    name=new
#    Wait Until Page Contains  Account Edit
    Wait Until Page Contains    Select Account Record Type

Select Account Type Partner
    click element  id=${SelAccountType}
    select from list by label  id=${SelAccountType}  Partner Account Record Type
    Click SFDCButton  ${webdriver}   continue  1

     Wait Until Page Contains    Account Name
     sleep  5s

Select Account Type Default
    click element  id=${SelAccountType}
    Select From List By label  id=${SelAccountType}  Default Account Record Type
    SLEEP  5s
    Click SFDCButton  ${webdriver}   continue  1
    Wait Until Page Contains    Account Name
    sleep  5s

Enter Account Details

    ${cdttime}=    Get Current Date Time
    ${Account}=  Catenate  Test_Account  ${cdttime}
    ${AccountSite}=  Catenate  United States    ${cdttime}
    ${AccountCity}=  Catenate  DUBLIN    ${cdttime}
    ${phone} =  generate phonenum
    Set Required Input Column Value    ${webdriver}  Account Name  1  ${Account}
    Set Required Input Column Value    ${webdriver}  City  1  ${AccountCity}
    Set Required Input Column Value    ${webdriver}  Street  1  5523 Tuttle Crossing Blvd
    Set Required Input Column Value    ${webdriver}  Phone  1  ${phone}
    Set Text Input Column Value    ${webdriver}  Account Site  1   ${AccountSite}
    Set Text Input Column Value    ${webdriver}  Zip/Postal Code  1  43016

    Search Required Lookup  ${webdriver}  Country  1  United States
    Search Lookup  ${webdriver}  State/Province  1  Ohio
    Set Text Input Column Value    ${webdriver}  Local County/Prefecture  1  DELAWARE
#    Search Account Country Lookup  ${webdriver}

    click element    name=save
    wait Until Page Contains    ${Account}
Get Account Details
     ${AccountNameValue}  Get Text Column Value   ${webdriver}  Account Name  1
     ${AccountNameValue}  catenate  Account  ${AccountNameValue}  created successfully
     ${glbl_v_TCComments}  catenate   ${glbl_v_TCComments}  ${\n}  ${AccountNameValue}

     ${AccountNameValue}  Get Text Column Value   ${webdriver}  SFDC Account ID  1
     ${AccountNameValue}  catenate  SFDC Account ID :  ${AccountNameValue}
     ${glbl_v_TCComments}  catenate   ${glbl_v_TCComments}  ${\n}  ${AccountNameValue}


     set global variable  ${glbl_v_TCComments}  ${glbl_v_TCComments}

Navigate To Accounts Contacts

    Click Link    link=Contacts
    sleep    3s
    Wait Until Page Contains    Account Detail


Add New Account
    Click On New Account
    Select Account Type Default
    sleep  3s
    Enter Account Details
    Get Account Details

Search Account

#    Search SFDC Entity Sidebar  ${webdriver}  ${SearchAccount}
     Search SFDC Entity  ${webdriver}  ${SearchAccount}
     Wait Until Page Contains    ${SearchAccount}

Drilldown on Account Name
    Log  ${SearchAccount}
#    ${SearchAccount}=  ${SearchAccount.strip()}
#    Log  ${SearchAccount}
    Click SFDCLink   ${webdriver}  ${SearchAccount.strip()}  1
#    Wait Until Page Co
#    Click Link    link=${SearchAccount}
    Wait Until Page Contains    Account Detail

Create New Account Contact
     Search and Navigate to Account Detail
     Navigate To Header   ${webdriver}  Contacts  1
     Click Section Button1  ${webdriver}   New Contact  1
     Wait Until Page Contains   New Contact

Search and Navigate to Account Detail
    Load Account Test Data
    Search Account
    sleep  5s
    Drilldown on Account Name