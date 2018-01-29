*ORIGINAL AUTHOR: NEIL SEAWARD: https://github.com/sealneaward/template-py/

Purpose
-------
A python project that returns SHOOTOUT results in a single NHL game of a player via a csv file.

Setup - Windows
---------------
1) *REFER TO AUTHOR'S INSTRUCTIONS:
    https://github.com/sealneaward/template-py/blob/master/README.md#windows-setup

2) In the project root folder (SOFE-4620-Assignment-1), run cmd as admin to create a Virtual Environment

        pip install virtualenv virtualenvwrapper
        virtualenv venv
        venv\Scripts\activate
        pip install -r requirements.txt
        deactivate
    
3)  Skip DB installation

4) Install additional modules:

    pandas
    matplotlib
    requests
    
        pip install pandas


Usage Example
-------------
Scrape data for game Tampa vs Philadelphia

              home  away
    attempts     0     0
    scores       0     0
    
----------------------------------------------------------------------------------------------
Code Instructions to Retrieve Data

1) Open Developer Tools > Network > XHR > pageWithAPIData
2) To retrieve HEADER info to be put on the HEADER function of the application:
    Refer to the image below:
    
    ![alt text](https://github.com/Jonas-Albaira/SOFE-4620-Assignment-1/blob/master/requestHeader.PNG)
    
3) To retrieve data from the API (in this case shootout info):
    Refer to the image below:
    
    ![alt text](https://github.com/Jonas-Albaira/SOFE-4620-Assignment-1/blob/master/retrieveData.PNG)
    
4) Run application. Saves automatically to a csv file
    
    

