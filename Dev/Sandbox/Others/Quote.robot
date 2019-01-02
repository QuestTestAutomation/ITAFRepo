*** Settings ***
Library  Selenium2Library
Library  ./Utillib.py
Library  ./XLLib.py
Library  ./LoginPage.py
Library  ./CPQLib.py
Resource  ./Common.robot
Resource  ./Account.robot
Resource  ./Opportunity.robot
Resource  ./Contacts.robot
Resource  ./CPQQuote.robot
Suite Setup  Common.Initialize Test Suite
Suite Teardown  Common.Finalize Test Suite
Test Setup  Common.Initialize Test Case Run
Test Teardown  Common.Finalize Test Case Run


*** Test Cases ***
#SFDCTC01
#
#
#    POC_Keywords.Lauch Browser
#    POC_Keywords.Login into Application
#    sleep  10s
#    Account.Navigate To Accounts
#    Account.Add New Account
#    Logout of Application
#
#
#SFDCTC02py
#    POC_Keywords.Lauch Browser
#    POC_Keywords.Login into Application
#    Account.Create New Account Contact
#    Contacts.Add Contact Details
#    Contacts.Get Contact Details
#    Logout of Application
#
##SFDCTC03
###    POC_Keywords.Lauch Browser
##    POC_Keywords.Login into Application
##    Contacts.Create New Contact Opportunity
##    Opportunity.Add Opportunity Dteails
##    Opportunity.Get Opportunity Detail
##    Logout of Application
SFDCTC04
    Common.Lauch Browser
    Common.Login into Application
    Click On Steel Brick Button
#    Add Products to CPQQuote
#    Add Products to CPQQuote New
    Add Products to CPQQuote New New