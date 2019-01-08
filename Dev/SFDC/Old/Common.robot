*** Settings ***
Library  Selenium2Library
Library  ./Utillib.py
Library  ./XLLib.py
Library  ./LoginPage.py
Library  ./Logout.py
Library  ./SFDCLib.py

*** Variables ***
${testdatafile}   C:/QSTAF/DataBank/DataSheet_Sales_SFDC.xlsx
${testdatasheet}  DataSheet_Sales
${testresfolder}  C:/QSTAF/TestResults/sales

*** Keywords ***

Initialize Test Suite
    Set Global Variable    ${browser}    gc
    Set Global Variable    ${glbl_v_TrialRun}    N
    Set Global Variable    ${glbl_v_CaptureDetailResults}    Y
    Set Global Variable    ${glbl_v_TCComments}    Y
    ${dt}=    Get Current Date
    ${dttime}=    Get Current Date Time
    Set Global Variable    ${dt}    ${dt}
    Set Global Variable    ${dttime}    ${dttime}
    ${testresultssheetname}    Catenate    TestResults_    ${dt}
    ${testresultsfilename}    Catenate    TestResults_    ${dt}    .xlsx
    ${testresultsfoldername}    Catenate    TestResults_    ${dt}
    ${testresultsfolder}=    Build File Path    ${testresfolder}    ${testresultsfoldername.strip()}
    Set Global Variable    ${testresultsmainfolder}    ${testresultsfolder}
    Create Directory    ${testresultsmainfolder}
    Sleep    3s
    ${testresultsfoldername}=    Build File Path    ${testresultsmainfolder}    ${testresultsfoldername}
    Set Global Variable    ${testresultsfoldername}    ${testresultsfoldername}
    Create Directory    ${testresultsfoldername}
    ${testresultsfile}    Build File Path    ${testresultsfoldername}    ${testresultsfilename}
    Set Global Variable    ${testresultsfile}    ${testresultsfile}
    Set Global Variable    ${testresultssheetname}    ${testresultssheetname}
    Create Run Test Results File    ${testresultsfile}    ${testresultssheetname}

Initialize Test Case Run
    [Documentation]    This is TC1 Documentation
    Set Global Variable    ${glbl_v_TCComments}    ${EMPTY}
    Set Global Variable    ${glbl_v_Object_Wait_Time}    900
    Set Global Variable    ${tst_step}    0

    ${tcrownum}=    Get Test Case Row Number    ${testdatafile}    ${testdatasheet}    ${TEST NAME}
    Set Global Variable    ${tcrownum}    ${tcrownum}
    Log    ${TEST NAME}
    log    ${tcrownum}
    ${URL}=    Get XL Cell Value Using Column Header    ${testdatafile}    ${testdatasheet}    ${tcrownum}    Url_SFDC
    set test variable      ${URL}    ${URL}
    ${UserName}=    Get XL Cell Value Using Column Header    ${testdatafile}    ${testdatasheet}    ${tcrownum}    UserName
    set test variable    ${UserName}    ${UserName}
    ${Password}=    Get XL Cell Value Using Column Header    ${testdatafile}    ${testdatasheet}    ${tcrownum}    Password
    set test variable     ${Password}    ${Password}
#    Initialize TestCase variables
Lauch Browser
    Log  ${browser}
    Open Browser    about:blank    ${browser}
    Maximize Browser Window
    ${webdriver}    Get webdriver instance
    Set Global variable    ${webdriver}    ${webdriver}

Intitalize Webdriver
    ${webdriver}=    Open Browser And Launch Application    ${browser}
    Set Global Variable    ${webdriver}    ${webdriver}

Finalize Test Case Run
    ${cdttime}=    Get Current Date Time
    ${getresultslastrow}=    Get XL Row Count    ${testresultsfile}    ${testresultssheetname}
    ${resultscurrentrow}=    Increment Step Number    ${getresultslastrow}
    Set Global Variable    ${resultscurrentrow}    ${resultscurrentrow}
    Update Run Test Results File    ${testresultsfile}    ${testresultssheetname}    ${resultscurrentrow}    ${TEST NAME}    ${TEST DOCUMENTATION}    ${TEST STATUS}
    ...    ${cdttime}    ${glbl_v_TCComments}
    Set Global Variable    ${glbl_v_TCComments}    ${EMPTY}

Finalize Test Suite
    Log    Finalize test run

Login into Application
    Go To    ${URL}
    Login into SFDC    ${webdriver}   ${UserName}    ${Password}
    wait Until Page Contains    salesforce
    sleep  5s
Click On Steel Brick Button
#    Click Element  id=tsidButton
    Select Steel Brick Dropdown Value  ${webdriver}  SteelBrick CPQ  1
#    SLEEP   10
#    Select Steel Brick Dropdown Value  ${webdriver}  Service  1
#*** Test Cases ***

#SFDCTC01
#    Log  Ne amma
#    Initialize Test Suite
#    Initialize Test Case Run
#    Lauch Browser
#    Login into Application
Logout of Application
     Logout of SFDC  ${webdriver}

Initialize TestCase variables
    ${testcasefilename}=    Catenate    ${TEST NAME}    _    ${dttime}    .xlsx
    Set Global Variable    ${testcasefilename}    ${testcasefilename}
    ${testcasefolder}    Catenate    ${TEST NAME}    _    ${dttime}
    ${testcasesheetname}    Catenate    ${TEST NAME}    _    ${dttime}
    ${testcaseresultsfoldername}=    Build File Path    ${testresultsfoldername}    ${TEST NAME}
    ${testcaseresultsfoldername}=    Build File Path    ${testcaseresultsfoldername}    ${testcasefolder}
    Set Global Variable    ${testcaseresultsfoldername}    ${testcaseresultsfoldername}
    Create Directory    ${testcaseresultsfoldername}
    ${testcaseresultsfile}    Build File Path    ${testcaseresultsfoldername}    ${testcasefilename}
    Set Global Variable    ${testcaseresultsfile}    ${testcaseresultsfile}
    Set Global Variable    ${testcasesheetname}    ${testcasesheetname}
    Create Test Case Results File    ${testcaseresultsfile}    ${testcasesheetname}    ${TEST NAME}    ${TEST DOCUMENTATION}
#    ${testdatafile} =  'C:/ART Framework/DataBank/DataSheet_Sales_SFDC.xlsx'
    Set Global Variable    ${testdatafile}    ${testdatafile}
#    ${testdatasheet}  DataSheet_Sales
    Set Global Variable    ${testdatasheet}    ${testdatasheet}