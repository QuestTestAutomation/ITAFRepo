*** Settings ***
Library  Selenium2Library
Library  ./Utillib.py
Library  ./XLLib.py
Library  ./LoginPage.py
Library  ./Logout.py
Library  ./SFDCLib.py
Library  ./CPQLib.py


*** Variables ***
${AddProducts_xpath}  /table[@id='bodyTable']/tbody/tr/td[2]/sb-page-container/div/sb-line-editor/sb-page-header/header/div[1]/div[3]/div[2]/div/sb-custom-action[3]/paper-button
${AddProducts_css}  /html/body/div/div[2]/table/tbody/tr/td[2]/sb-page-container/div/sb-line-editor/sb-page-header/header/div[1]/div[3]/div[2]/div/sb-custom-action[3]/paper-buttonhtml.ext-strict body.hasMotif.Custom93Tab.sfdcBody.brandQuaternaryBgr.ext-gecko.ext-gecko3 div#contentWrapper div.bodyDiv.brdPalette.brandPrimaryBrd table#bodyTable.outer tbody tr td#bodyCell.oRight sb-page-container#sbPageContainer.--desktop.x-scope.sb-page-container-0 div#content.style-scope.sb-page-container sb-line-editor.--desktop.x-scope.sb-line-editor-0 sb-page-header#lineEditorPageHeader.style-scope.sb-line-editor.--desktop.x-scope.sb-page-header-0 header.header.style-scope.sb-page-header.--desktop div.layout.horizontal.style-scope.sb-page-header div.flex.layout.horizontal.wrap.end-justified.start.centered.style-scope.sb-page-header div#buttons.normal.style-scope.sb-page-header div#actions.actions.style-scope.sb-line-editor sb-custom-action.style-scope.sb-line-editor.--desktop.x-scope.sb-custom-action-0 paper-button#mainButton.notLast.--desktop.style-scope.sb-custom-action.x-scope.paper-button-0

*** Keywords ***

Load CPQQuote Data
     ${CPQQuote}=    Get XL Cell Value Using Column Header    ${testdatafile}    ${testdatasheet}    ${tcrownum}    CPQQuote
     set test variable     ${CPQQuote}    ${CPQQuote}
     ${CPQQuoteProductlist}=    Get XL Cell Value Using Column Header    ${testdatafile}    ${testdatasheet}    ${tcrownum}    Products
     set test variable     ${CPQQuoteProductlist}    ${CPQQuoteProductlist}
     ${CPQQuotePartNumber}=    Get XL Cell Value Using Column Header    ${testdatafile}    ${testdatasheet}    ${tcrownum}    PartNumber
     set test variable     ${CPQQuotePartNumber}   ${CPQQuotePartNumber}
    ${CPQQuotePartNumberValue}=    Get XL Cell Value Using Column Header    ${testdatafile}    ${testdatasheet}    ${tcrownum}    PartNumberValue
     set test variable     ${CPQQuotePartNumberValue}   ${CPQQuotePartNumberValue}


Retry adding products
     browser_navigate_back  ${webdriver}
     sleep  30
    Pgconfigureproduts click add products  ${webdriver}
#    Wait Until Page Contains    Product Selection
    pgselectproduct waitfor Select Button   ${webdriver}

Add Products to CPQQuote Old
#    Load CPQQuote Data
    Click Link    link=CPQ Quotes
    Wait Until Page Contains    CPQ Quotes
    sleep  5s
#    ${CPQQuote} =  ${gCPQQuoteno}
#    Log  ${CPQQuote}
    Search SFDC Entity  ${webdriver}  ${gCPQQuoteno}
    sleep  5s
    Log  ${gCPQQuoteno}

#    Click CPQ Link   ${webdriver}   ${gCPQQuoteno}
    Get Window Titles
    Get Window Names
    Get Window Identifiers
    Log  get title
    Click Link    link=${gCPQQuotelink}
    sleep   10s
#    switch browser  1
    switch to new tab  ${webdriver}
    Get Window Titles
    Get Window Names
    Get Window Identifiers
    Log  get title
    Wait Until Page Contains    ${gCPQQuotelink}
    Click SFDCButton  ${webdriver}   Configure Products  1
#    click element  xpath='//*[@id="topButtonRow"]/input[4]'
    sleep  30
    Pgconfigureproduts click add products  ${webdriver}
#    Wait Until Page Contains    Product Selection
    pgselectproduct waitfor Select Button   ${webdriver}
#    ${Error}  pgselectproduct_checkfor_errors   ${webdriver}
#    Log  ${Error}

    CPQ_Add_Products_Handle_Errors  ${webdriver}
#    run keyword if  ${Error} != "-1"  Retry adding products








#    ${errortext}  pgselectproduct error banner root  ${webdriver}
#    Log  ${errortext}



##    sleep  20
#    Pgselectproduct Click Filter Button  ${webdriver}
#    sleep  5
#    Pgselectproduct Enter Product Number  ${webdriver}  ${CPQQuoteProductlist}
#    sleep  5
#    pgselectproduct Click Apply Filter Button   ${webdriver}
    sleep  5
    Expand product list  ${webdriver}  ${CPQQuoteProductlist}  Select
    sleep  5
    Pgselectproduct Click Select Button  ${webdriver}
#    sleep  20
#    Pgconfigureproduts Save product  ${webdriver}
#    sleep  20
#    Pgconfigureproduts click save  ${webdriver}
    pgselectproduct waitfor Select Button   ${webdriver}
    ${errortext}  pgselectproduct error banner root  ${webdriver}
    Log  ${errortext}
    Pgselectproduct Click Select Button  ${webdriver}
    pgselectproduct waitfor Select Button   ${webdriver}
    ${errortext}  pgselectproduct error banner root  ${webdriver}
    Log  ${errortext}
    pgselectproduct close errors  ${webdriver}






#    sleep  30s
#    Wait Until Page Contains    Edit Quote
#    click element  xpath=${AddProducts_xpath}
##    click element  css=${AddProducts_css}
##    Click CPQ Buttom  ${webdriver}  Add Products    1
#    sleep  5s
#    Wait Until Page Contains    Product Selection


Add Products to CPQQuote New
   Load CPQQuote Data
    Click Link    link=CPQ Quotes
    Wait Until Page Contains    CPQ Quotes
    sleep  5s
    Log  ${CPQQuote}
#    Click CPQ Link   ${webdriver}  ${CPQQuote.strip()}
    Click Link    link=${CPQQuote}
    Wait Until Page Contains    ${CPQQuote}
    Click SFDCButton  ${webdriver}   Configure Products  1
    sleep  40
    Pgconfigureproduts click add products  ${webdriver}
    Wait Until Page Contains    Product Selection
    sleep  20
    CPQ Add Products Handle Errors  ${webdriver}
    sleep  20
    Pgselectproduct Click Filter Button  ${webdriver}
    sleep  5
    Pgselectproduct Enter Product Number  ${webdriver}  ${CPQQuoteProductlist}
    sleep  5
    pgselectproduct Click Apply Filter Button   ${webdriver}
    sleep  5
    Expand product list  ${webdriver}  ${CPQQuoteProductlist}  Select
    sleep  5
    Pgselectproduct Click Select Button  ${webdriver}
    sleep  20
    Pgconfigureproduts Save product  ${webdriver}
    sleep  20
    Pgconfigureproduts click save  ${webdriver}




#    sleep  30s
#    Wait Until Page Contains    Edit Quote
#    click element  xpath=${AddProducts_xpath}
##    click element  css=${AddProducts_css}
##    Click CPQ Buttom  ${webdriver}  Add Products    1
#    sleep  5s
#    Wait Until Page Contains    Product Selection

Add Products to CPQQuote
    Load CPQQuote Data
    Click Link    link=CPQ Quotes
    Wait Until Page Contains    CPQ Quotes
    sleep  5s
#    ${CPQQuote} =  ${gCPQQuoteno}
#    Log  ${CPQQuote}
    Search SFDC Entity  ${webdriver}  ${gCPQQuoteno}
    sleep  5s
    Log  ${gCPQQuoteno}

#    Click CPQ Link   ${webdriver}   ${gCPQQuoteno}
#    Get Window Titles
#    Get Window Names
#    Get Window Identifiers
#    Log  get title
    Click Link    link=${gCPQQuotelink}
    sleep   10s
#    switch browser  1
    switch to new tab  ${webdriver}
#    Get Window Titles
#    Get Window Names
#    Get Window Identifiers
#    Log  get title
    Wait Until Page Contains    ${gCPQQuotelink}
    Click SFDCButton  ${webdriver}   Configure Products  1
    sleep  20
    Pgconfigureproduts click add products  ${webdriver}
    Wait Until Page Contains    Product Selection
    sleep  20
    CPQ Add Products Handle Errors  ${webdriver}
    sleep  20
    Pgselectproduct Click Filter Button  ${webdriver}
    sleep  5
    Pgselectproduct Enter Product Number  ${webdriver}  ${CPQQuoteProductlist}
    sleep  5
    pgselectproduct Click Apply Filter Button   ${webdriver}
    sleep  5
    Expand product list  ${webdriver}  ${CPQQuoteProductlist}  Select
    sleep  5
    Pgselectproduct Click Select Button  ${webdriver}
    sleep  20
    Pgconfigureproduts Save product  ${webdriver}
    sleep  20
    Pgconfigureproduts click save  ${webdriver}

Add Products to CPQQuote New New
   Load CPQQuote Data
    Click Link    link=CPQ Quotes
    Wait Until Page Contains    CPQ Quotes
    sleep  5s
    Log  ${CPQQuote}
#    Click CPQ Link   ${webdriver}  ${CPQQuote.strip()}
    Click Link    link=${CPQQuote}
    Wait Until Page Contains    ${CPQQuote}
    Click SFDCButton  ${webdriver}   Configure Products  1
    sleep  20
    Pgconfigureproduts click add products  ${webdriver}
    Wait Until Page Contains    Product Selection
    sleep  10
    CPQ Add Products Handle Errors  ${webdriver}
    sleep  10
    Pgselectproduct Click Filter Button  ${webdriver}
    sleep  5
    Pgselectproduct Enter Product Number  ${webdriver}  ${CPQQuoteProductlist}
    sleep  5
    pgselectproduct Click Apply Filter Button   ${webdriver}
    sleep  5
    Expand product list  ${webdriver}  ${CPQQuoteProductlist}  Select
    sleep  5
    Pgselectproduct Click Select Button  ${webdriver}
    sleep  20
#    pg config products preconfig  ${webdriver}
#    sleep  10
#    pgconfigureproduts filter product  ${webdriver}
#    sleep  10
##    pg configure products click filter  ${webdriver}
#    sleep  10
#    pg configure products Enter product  ${webdriver}  ${CPQQuotePartNumber}
#    sleep  5
#    pg configure products filterheader click apply  ${webdriver}
#    sleep  10
#    pg config select product feature  ${webdriver}  ${CPQQuotePartNumber}
#    Pgconfigureproduts Save product  ${webdriver}
#    sleep  20
#    Pgconfigureproduts click save  ${webdriver}
    Log  ${CPQQuotePartNumberValue}
    expand pg configure products pageheader All  ${webdriver}  ${CPQQuotePartNumber}   ${CPQQuotePartNumberValue}
    sleep  10
    pg configure product Save  ${webdriver}


