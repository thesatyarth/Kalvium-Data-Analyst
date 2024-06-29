# Kalvium-Data-Analyst
"KALVIUM" Online Assessment, Data Analyst role

**Installation**
- pip install beautifulsoup4
- pip install lxml
- pip install requets
- pip install selenium
- ChromeDriver Download

**Party Result- Excel**
-select column C, D Press DEL

**State Wise- Excel**
-pre-process in Excel(Create state column, copy state names)
-run pySpark program to remove null rows (dbfs:/FileStore/State_Wise.csv) //DataBricks

**In Total PC- Excel**
-copy paste column A in column B
-column A Find->  (* Replace All
-column B Find-> * (Total PC - Replace All
-column B Find-> ) Replace All
