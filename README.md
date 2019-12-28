# MostUsefulHttpServer

## Running

    gradle startService

## Task1 
    

    request: GET http://localhost?year=2017
    response: {"errorCode": 200, "dataMessage": "13/09/2017"}
    
    request: GET http://localhost?year=2020
    response: {"errorCode": 200, "dataMessage": "12/09/2020"}
    
    request: GET  http://localhost?year=2017s
    response: {"errorCode": 1, "dataMessage": "BAD YEAR NUMBER"}
    
    request: GET http://localhost?yssdear=2017
    response: {"errorCode": 2, "dataMessage": "BAD REQUEST"}
    
## Task2

    request: GET http://localhost?currentDate=100917
    response:{"errorCode": 200, "dataMessage": 3}
    
    request: GET http://localhost?currentDate=100917ww
    response:{"errorCode": 1,"dataMessage": "BAD YEAR NUMBER"}
    
    request: GET http://localhost?curresntDate=100917
    response:{"errorCode": 2, "dataMessage": "BAD REQUEST"}