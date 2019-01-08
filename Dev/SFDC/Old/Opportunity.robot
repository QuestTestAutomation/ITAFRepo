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
${Sel_OppotunityType_name}  opp5


*** Keywords ***

Load Opportunity Data
   ${cdttime}=    Get Current Date Time
   ${OptyType}=    Get XL Cell Value Using Column Header    ${testdatafile}    ${testdatasheet}    ${tcrownum}    OpportunityType

   set test variable     ${OptyType}    ${OptyType}
   ${OptyChannelStatus}=    Get XL Cell Value Using Column Header    ${testdatafile}    ${testdatasheet}    ${tcrownum}    OptyChannelStatus
   set test variable     ${OptyChannelStatus}    ${OptyChannelStatus}
   ${OptyCompetitorStatus}=    Get XL Cell Value Using Column Header    ${testdatafile}    ${testdatasheet}    ${tcrownum}    OptyCompetitorStatus
   set test variable     ${OptyCompetitorStatus}    ${OptyCompetitorStatus}






Navigate To Opportunities

    Click Link    link=Opportunities
    sleep    10s
    Wait Until Page Contains    Recent Accounts

Add Opportunity Dteails
    Load Opportunity Data
#    Select Input Column Value  ${webdriver}   Type  1  ${OptyType}
    Wait Until Page Contains      New Opportunity
    sleep  10s
#    click element  name=${Sel_OppotunityType_name}
#    Select From List By label  name=${Sel_OppotunityType_name}  ${OptyType}
#    Select Required SFDC Dropdown Value  ${webdriver}   Type  1  ${OptyType}
#    scroll to bottom  ${webdriver}
    Select SFDC Dropdown Value  ${webdriver}   Type  1  ${OptyType}
    Select SFDC Dropdown Value  ${webdriver}   Channel Status  1  ${OptyChannelStatus}
    Select SFDC Dropdown Value  ${webdriver}   Competitor Status  1  ${OptyCompetitorStatus}
    Click SFDCButton  ${webdriver}   Save  1
#    click element    name=save
    sleep  5s
    Wait Until Page Contains  Opportunity Detail
    ${optyurl}=   Get Location

Wait for opportunity row id
    ${optyrowid} =  wait for opty sbl rowid  ${webdriver}  Siebel Row Id  1
    ${glbl_v_TCComments}  catenate   ${glbl_v_TCComments}  ${\n}  ${optyrowid}
    set global variable  ${glbl_v_TCComments}  ${glbl_v_TCComments}

Get Opportunity Detail
     ${InputValue}  Get Text Column Value   ${webdriver}  Opportunity Name  1
     ${InputValue}  catenate  Opportunity Name :  ${InputValue}
     ${glbl_v_TCComments}  catenate   ${glbl_v_TCComments}  ${\n}  ${InputValue}

     set global variable  ${glbl_v_TCComments}  ${glbl_v_TCComments}

Create CPQQuote
#    Navigate To Header   ${webdriver}  CPQ Quotes  1
    Click Section Button  ${webdriver}   CPQ Quote  1
#    Click SFD CButton    ${webdriver}   CPQ Quote  1
    ${CPQQuote} =  Handle CPQQuote Popup  ${webdriver}
    Log  ${CPQQuote}
    ${InputValue}  Get Text Column Value   ${webdriver}  Opportunity Name  1
    Log  ${InputValue}
    sleep  6s
    ${CPQQuoteno}  Get quote number  ${webdriver}  ${CPQQuote}
    Set Global Variable    ${gCPQQuoteno}    ${CPQQuoteno}
    Set Global Variable    ${gCPQQuotelink}    ${CPQQuote}
    Log  ${CPQQuoteno}
#    Click Link    link=${CPQQuote.strip()}
#    sleep    20s
#    Wait Until Page Contains    ${CPQQuote}


