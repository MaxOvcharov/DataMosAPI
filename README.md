## DataMosAPI  [**FULL DOCUMENTATION**](https://apidata.mos.ru/Docs)

##### This is an async web client to the REST API: [**DataMosAPI**](https://apidata.mos.ru).
This REST service contains open data sets of Moscow: streets, buildings, organisations and etc.   

##### 1) Get API version: *GET* 
```bash
https://apidata.mos.ru/version
```

##### 2) Get token-key for using DataMosAPI service: [**token-key**](https://apidata.mos.ru/Account/Login)

##### 3) Using the API key: The key is transferred via the query string as follows: 
```bash
?api_key=<your key>
```
##### 4) List of data sets: Query to the /datasets resource returns the list of data sets. *GET*
```bash
https://apidata.mos.ru/v1/datasets?$skip=10&$top=5&$inlinecount=allpages 
```
You can add an optional parameter ***foreign*** that takes values true/false:

**true** - return list of english datasets;

**false** - return list of russian datasets (default value);

###### Format of returned object. 

The answer provides an array of elements of the following format:

**Id** - is the data set ID

**CategoryId** - is the ID of the subject category to which the dataset corresponds

**DepartmentId** - is the ID of the department responsible for data set

**Caption** - is the name of the data set

### Information about data set: 
##### 5) Data set structure
A query to the ***/datasets/{id}*** resource returns a data set description,
including the list of attributes. **GET**
```bash
https://apidata.mos.ru/v1/datasets/658 
```
###### Format of returned object
The answer consists of one element of the following format:

**Idis** - is the data set ID

**IdentificationNumberis** - is the data set Identification number

**CategoryId** - is the ID of the subject category

**CategoryCaptionis** - is the name of the subject category

**DepartmentId** - is the ID of the department responsible for data set

**DepartmentCaption** - is the name of the department

**Caption** - is the data set name

**Descriptionis** - a brief data set description

**ContainsGeodata** - indicates that the data set includes geographic data

**VersionNumberis** - an actual version number

**VersionDateis** - a date of last update

**ItemsCountis** - a rows count in data set

**Columnsis** - the list of data set attributes represented as an array of the following elements:

 + **Name** - is the name or key of the attribute
 + **Captionis** - is the attribute description
 + **Visibleis** - is the attribute visibility
 + **Typeis** - is the attribute type
 + **SubColumnsis** - is the list children columns
 
##### 6) Data set count: A query to the ***/datasets/{id}/count*** resource returns a row count. **GET**
 ```bash
https://apidata.mos.ru/v1/datasets/493/count 
```
###### Format of returned object

The answer consists count of rows.

##### 7) Actual bersion and release numbers

A query to the ***/datasets/{id}/version*** resource returns an actual version and release numbers of data set. **GET**
```bash
https://apidata.mos.ru/v1/datasets/655/version 
```
###### Format of returned object

The answer consists of one element of the following format:

**VersionNumber** — data set version number;

**ReleaseNumber** — data set release number;

### Data set content

A query to the ***/datasets/{id}/rows*** resource returns the list of rows of the specified data set. **GET**
```bash
https://apidata.mos.ru/v1/datasets/658/rows?$top=3&$orderby=Number
```
###### Format of returned object

The answer provides an array of elements of the following format:

**Id** - is the ID of the data row in GUID format
**Number** - is the sequence number of the data row
**Cells** - is an object with attribute values for a given row

### GEO DATA from data set  

A query to the ***/datasets/{id}/features*** resource returns the list of rows of the specified data ***GeoJSON***

You also can used parametr ***bbox={bbox}.*** **GET**
```bash
https://apidata.mos.ru/v1/datasets/1786/features
OR
https://apidata.mos.ru/v1/features/1786
OR
https://apidata.mos.ru/v1/features/1786/features?bbox=37.49711036682129,55.86543869723485,37.5490379333496,55.89110103788533 
```

Whole example you can try with the help of [**Postman APP**](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop)
 
Download --> [**EXAMPLES FILE**](https://apidata.mos.ru/Content/Docs/postman_collection.json) 








