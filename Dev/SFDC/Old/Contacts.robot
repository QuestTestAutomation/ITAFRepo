*** Settings ***
Library  Selenium2Library
Library  ./Utillib.py

Library  ./XLLib.py
Library  ./LoginPage.py
Library  ./Logout.py
Library  ./SFDCLib.py
import   time



*** Variables ***
${AccountName}  acc2
${ContactLastName}
${ContactFirstName}

*** Keywords ***
Load Contact Details
   ${cdttime}=    Get Current Date Time
   ${ContactFirstName}=    Get XL Cell Value Using Column Header    ${testdatafile}    ${testdatasheet}    ${tcrownum}    ContactFirstName
   ${ContactFirstName}  catenate  ${ContactFirstName}  ${cdttime}
   set test variable     ${ContactFirstName}    ${ContactFirstName}
   ${ContactLastName}=    Get XL Cell Value Using Column Header    ${testdatafile}    ${testdatasheet}    ${tcrownum}    ContactLastName
   ${ContactLastName}  catenate  ${ContactLastName}  ${cdttime}
   set test variable     ${ContactLastName}    ${ContactLastName}
   ${SearchContact}=    Get XL Cell Value Using Column Header    ${testdatafile}    ${testdatasheet}    ${tcrownum}    ContactFullName
   set test variable     ${SearchContact}    ${SearchContact}
Add Contact Details
     Load Contact Details
     Set Text Input Column Value    ${webdriver}  First Name  1  ${ContactFirstName}
     Set Required Input Column Value    ${webdriver}  Last Name  1  ${ContactLastName}
     click element    name=save
     ${ContactFullName}  Catenate   ${ContactFirstName}  " "  ${ContactLastName}
     wait Until Page Contains    Contact Detail


Get Contact Details
     ${InputValue}  Get Text Column Value   ${webdriver}  Name  1
     ${InputValue}  catenate  Contact Name :  ${InputValue}
     ${glbl_v_TCComments}  catenate   ${glbl_v_TCComments}  ${\n}  ${InputValue}
     ${InputValue}  Get Text Column Value   ${webdriver}  Account Name  1
     ${InputValue}  catenate  Account:  ${InputValue}
     ${glbl_v_TCComments}  catenate   ${glbl_v_TCComments}  ${\n}  ${InputValue}

     ${InputValue}  Get Text Column Value   ${webdriver}  Phone  1
     ${InputValue}  catenate  Contact Phone :  ${InputValue}
     ${glbl_v_TCComments}  catenate   ${glbl_v_TCComments}  ${\n}  ${InputValue}
     set global variable  ${glbl_v_TCComments}  ${glbl_v_TCComments}

Search Contact and drilldown

#    Search SFDC Entity Sidebar  ${webdriver}  ${SearchContact}
    search SFDC Entity  ${webdriver}  ${SearchContact}
#    Click SFDCLink   ${webdriver}  ${SearchContact.strip()}  1
    Click Element  partial link=${SearchContact.strip()}
    Wait Until Page Contains    Contact Detail

Create New Contact Opportunity
     Load Contact Details
     Search Contact and drilldown
     SLEEP  5s
     scroll to bottom  ${webdriver}
     Navigate To Header   ${webdriver}  Opportunities  1
     Click Section Button  ${webdriver}   New Oppty  1
     Wait Until Page Contains    New Opportunity