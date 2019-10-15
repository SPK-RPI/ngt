# Dont Forget This

mongoimport --host localhost:27017 --db mydb --collection Restaurants --type json Restaurants.json

# Python Packages

pip install pymongo

# MongoDB 
**Write a MongoDB query to display all the documents in the collection restaurants.**


db.Rest.find().pretty()

** Write a MongoDB query to display the fields , restaurant_id, name, borough and cuisine for all the documents in the collection restaurant. **

(A)    
Import Restaurant.json into MongoDb and perform the followingqueries

1.       
Write a MongoDB query to display all the documents in thecollection restaurants.

QUERY: db.Restaurants.find().pretty()

 

2.        
Write a MongoDB query to display the fields , restaurant_id, name,
borough and cuisine for all the documents in the collectionrestaurant.

Query
: db.Restaurants.find({},{'restaurant_id':1,'name':1,'cuisine':1,'borough':1}).pretty()

 

 

3.        
Write a MongoDB query to display the fields restaurant_id, name,
borough and cuisine, but exclude the field _id for all the documents in thecollection restaurant.

Query:
db.Restaurants.find({},{'restaurant_id':1,'name':1,'_id':0,'cuisine':1,'borough':1}).pretty()

 

4.        
Write a MongoDB query to display the fields restaurant_id, name,
borough and zip code, but exclude the field _id for all the documents in the
collection restaurant.

Query:
db.Restaurants.find({},{'restaurant_id':1,'name':1,'_id':0,'cuisine':1,'address.zipcode':1,'borough':1}).pretty()

 

5.        
Write a MongoDB query to display all the restaurant which is in theborough Bronx.

Query: db.Restaurants.find({'borough':'Bronx'}).pretty()

6.       
Write a MongoDB query to find the restaurant name,borough, longitude and attitude and
cuisine for those restaurants which contains 'mon' as three letters somewhere
in itsname.

Query:db.Restaurants.find({'name':/mon.*/i},{'name':1,'borough':1,'address.cord':1,'cuisine':1}).pretty()

 

7.       
Write a MongoDB query to find the restaurant name,borough, longitude and latitude and
cuisine for those restaurants which contain 'Mad' as first three letters of itsname.

Query:
db.Restaurants.find({'name':/^Mad/i},{'name':1,'borough':1,'address.cord':1,'cuisine':1}).pretty()

 

8.       
Write a MongoDB query to find the restaurants which locatein latitude value less than-95.754168.

Query: db.Restaurants.find({"address.coord":{$lt:-95.754168}}).pretty()

 

9.       
Write a MongoDB query to find the restaurant Id, name,borough and cuisine for those restaurants
which contain 'Wil' as first three letters for itsname.

 Query: db.Restaurants.find({'name':/^Mad/},{},{'restaurant_id':1,'name':1,'borough':1,'cuisine':1}).pretty().

10.    
Write a MongoDB query to find the restaurant Id, name,borough and cuisine for those restaurants
which contain 'ces' as last three letters for itsname.\

Query: db.Restaurants.find({'name':/ces$/},{},{'restaurant_id':1,'name':1,'borough':1,'cuisine':1}).pretty()

 

11.    
Write a MongoDB
query to find the restaurant Id, name,and
cuisine for those restaurants which contains 'Reg' as three letters somewhere
in itsname.

       Query: db.Restaurants.find({'name':/Reg.*/i},{'restaurant_id':1,'name':1,'cuisine':1}).pretty()

 

12.    
Write a MongoDB
query to find the restaurants which belong to the borough Bronx and prepared
either American or Chinese.

Query
db.Restaurants.find({"borough":"Bronx",$or:[{"cuisine":"American
"},{"cuisine":"Chinese"}]}).pretty()

 

13.    
Write a MongoDB
query to find the restaurant Id, name,borough
and cuisine for those restaurants which belong to the borough Staten Island or
Queens or Bronx or Brooklyn. 

Query:db.Restaurants.find({'borough':{$in:['Staten
Island','Queens','Bronx','Brookly']}},{'restaurant_id':1,'name':1,'cuisine':1,'borough':1}).pretty()

 

14.    
Write a MongoDB
query to find the restaurant Id, name,borough
and cuisine for those restaurants which are not belonging to the borough Staten
Island or Queens or Bronx or Brooklyn. 

Query:db.Restaurants.find({'borough':{$nin:['Staten
Island','Queens','Bronx','Brookly']}},{'restaurant_id':1,'name':1,'cuisine':1,'borough':1}).pretty()

 

 

15.    
Write a MongoDB
query to find the restaurant Id, name,borough
and cuisine for those restaurants which achieved a score which is not more than
10.

db.Restaurants.find({"grades.score":{$lt:10}}).pretty()

 

(B) Create a collection
Employee with the following fields

(Eid, EName, Sal, City,
Hobbies) where hobbies is an array. Perform the following queries based on the
collection.

Use emp

db.Employee.insert({'E_id':1,'E_Name':'Ajay','Sal':20000,'City':'Ahemdabaad','Hobbies':'reading'})

db.Employee.insert({'E_id':2,'E_Name':'Anil','Sal':22000,'City':'Ahemdabaad','Hobbies':['reading','runing']})

db.Employee.insert({'E_id':3,'E_Name':'Dhruw','Sal':30000,'City':'Ahemdabaad','Hobbies':'gaming'})

 

A.    Write a MongoDB query to use
sum, avg, min and max expression.

 

**Sum**:db.Employee.aggregate({$group:{_id:"$City",totalEmployee:{$sum:1}}})

**Avg**:db.Employee.aggregate({$group:{_id:"$City",avg_Sal:{$avg:"$Sal"}}})

**Max**:db.Employee.aggregate({$group:{_id:"$City",avg_Sal:{$avg:"$Sal"}}})

**Min**: db.Employee.aggregate({$group:{_id:"$City",min_Sal:{$min:"$Sal"}}})

 

 

B.     Write a MongoDB query to use
push and addToSet expression.

**Push: **db.Employee.aggregate([{$group:{_id:"$City",Sal:{$push:"$Sal"}}}])

**AddtoSet :**db.Employee.aggregate([{$group:{_id:"$City",Sal:{$addToSet:"$Sal"}}}])

 

C.     Write a MongoDB query to use
first and last expression.

**First**:
db.Employee.aggregate({$group:{_id:"City",E_Name:{$first:"$E_Name"}}})

**Last: **db.Employee.aggregate({$group:{_id:"$City",E_Name:{$last:"$E_Name"}}})

** **

** **

** **

(C) Connect Python with MongoDB
and also insert, retrieve, update and delete

documents.

 

 

 

JQUERY

1.       
Write a jQuery to create fade-in and fade-outeffect.

2.       
Write a jQuery effect method with a callbackfunction.

3.        
Write a jQuery to Select elements by class name,id and elementname.

4.       
Write a jQuery to Create slide-up, slide-down and slide-Toggleeffect.

5.        
Write a jQuery to insert multiple HTML elements at the beginning and
end of the documents.

6.       
Write a jQuery effect method without a callbackfunction.

7.        
Write a jQuery to create animation effect.

8.       
Write a jQuery to perform Method chaining.

 

JSON

1.      Create a JSON file and parseit.

2.      Create a JSON file and
persist it in any database.

 

 

 

 (A)    
Import Restaurant.json into MongoDb and perform the followingqueries

1.       
Write a MongoDB query to display all the documents in thecollection restaurants.

QUERY: db.Restaurants.find().pretty()

 

2.        
Write a MongoDB query to display the fields , restaurant_id, name,
borough and cuisine for all the documents in the collectionrestaurant.

Query
: db.Restaurants.find({},{'restaurant_id':1,'name':1,'cuisine':1,'borough':1}).pretty()

 

 

3.        
Write a MongoDB query to display the fields restaurant_id, name,
borough and cuisine, but exclude the field _id for all the documents in thecollection restaurant.

Query:
db.Restaurants.find({},{'restaurant_id':1,'name':1,'_id':0,'cuisine':1,'borough':1}).pretty()

 

4.        
Write a MongoDB query to display the fields restaurant_id, name,
borough and zip code, but exclude the field _id for all the documents in the
collection restaurant.

Query:
db.Restaurants.find({},{'restaurant_id':1,'name':1,'_id':0,'cuisine':1,'address.zipcode':1,'borough':1}).pretty()

 

5.        
Write a MongoDB query to display all the restaurant which is in theborough Bronx.

Query: db.Restaurants.find({'borough':'Bronx'}).pretty()

6.       
Write a MongoDB query to find the restaurant name,borough, longitude and attitude and
cuisine for those restaurants which contains 'mon' as three letters somewhere
in itsname.

Query:db.Restaurants.find({'name':/mon.*/i},{'name':1,'borough':1,'address.cord':1,'cuisine':1}).pretty()

 

7.       
Write a MongoDB query to find the restaurant name,borough, longitude and latitude and
cuisine for those restaurants which contain 'Mad' as first three letters of itsname.

Query:
db.Restaurants.find({'name':/^Mad/i},{'name':1,'borough':1,'address.cord':1,'cuisine':1}).pretty()

 

8.       
Write a MongoDB query to find the restaurants which locatein latitude value less than-95.754168.

Query: db.Restaurants.find({"address.coord":{$lt:-95.754168}}).pretty()

 

9.       
Write a MongoDB query to find the restaurant Id, name,borough and cuisine for those restaurants
which contain 'Wil' as first three letters for itsname.

 Query: db.Restaurants.find({'name':/^Mad/},{},{'restaurant_id':1,'name':1,'borough':1,'cuisine':1}).pretty().

10.    
Write a MongoDB query to find the restaurant Id, name,borough and cuisine for those restaurants
which contain 'ces' as last three letters for itsname.\

Query: db.Restaurants.find({'name':/ces$/},{},{'restaurant_id':1,'name':1,'borough':1,'cuisine':1}).pretty()

 

11.    
Write a MongoDB
query to find the restaurant Id, name,and
cuisine for those restaurants which contains 'Reg' as three letters somewhere
in itsname.

       Query: db.Restaurants.find({'name':/Reg.*/i},{'restaurant_id':1,'name':1,'cuisine':1}).pretty()

 

12.    
Write a MongoDB
query to find the restaurants which belong to the borough Bronx and prepared
either American or Chinese.

Query
db.Restaurants.find({"borough":"Bronx",$or:[{"cuisine":"American
"},{"cuisine":"Chinese"}]}).pretty()

 

13.    
Write a MongoDB
query to find the restaurant Id, name,borough
and cuisine for those restaurants which belong to the borough Staten Island or
Queens or Bronx or Brooklyn. 

Query:db.Restaurants.find({'borough':{$in:['Staten
Island','Queens','Bronx','Brookly']}},{'restaurant_id':1,'name':1,'cuisine':1,'borough':1}).pretty()

 

14.    
Write a MongoDB
query to find the restaurant Id, name,borough
and cuisine for those restaurants which are not belonging to the borough Staten
Island or Queens or Bronx or Brooklyn. 

Query:db.Restaurants.find({'borough':{$nin:['Staten
Island','Queens','Bronx','Brookly']}},{'restaurant_id':1,'name':1,'cuisine':1,'borough':1}).pretty()

 

 

15.    
Write a MongoDB
query to find the restaurant Id, name,borough
and cuisine for those restaurants which achieved a score which is not more than
10.

db.Restaurants.find({"grades.score":{$lt:10}}).pretty()

 

(B) Create a collection
Employee with the following fields

(Eid, EName, Sal, City,
Hobbies) where hobbies is an array. Perform the following queries based on the
collection.

Use emp

db.Employee.insert({'E_id':1,'E_Name':'Ajay','Sal':20000,'City':'Ahemdabaad','Hobbies':'reading'})

db.Employee.insert({'E_id':2,'E_Name':'Anil','Sal':22000,'City':'Ahemdabaad','Hobbies':['reading','runing']})

db.Employee.insert({'E_id':3,'E_Name':'Dhruw','Sal':30000,'City':'Ahemdabaad','Hobbies':'gaming'})

 

A.    Write a MongoDB query to use
sum, avg, min and max expression.

 

**Sum**:db.Employee.aggregate({$group:{_id:"$City",totalEmployee:{$sum:1}}})

**Avg**:db.Employee.aggregate({$group:{_id:"$City",avg_Sal:{$avg:"$Sal"}}})

**Max**:db.Employee.aggregate({$group:{_id:"$City",avg_Sal:{$avg:"$Sal"}}})

**Min**: db.Employee.aggregate({$group:{_id:"$City",min_Sal:{$min:"$Sal"}}})

 

 

B.     Write a MongoDB query to use
push and addToSet expression.

**Push: **db.Employee.aggregate([{$group:{_id:"$City",Sal:{$push:"$Sal"}}}])

**AddtoSet :**db.Employee.aggregate([{$group:{_id:"$City",Sal:{$addToSet:"$Sal"}}}])

 

C.     Write a MongoDB query to use
first and last expression.

**First**:
db.Employee.aggregate({$group:{_id:"City",E_Name:{$first:"$E_Name"}}})

**Last: **db.Employee.aggregate({$group:{_id:"$City",E_Name:{$last:"$E_Name"}}})

** **

** **

** **

(C) Connect Python with MongoDB
and also insert, retrieve, update and delete

documents.

 

 

 

JQUERY

1.       
Write a jQuery to create fade-in and fade-outeffect.

2.       
Write a jQuery effect method with a callbackfunction.

3.        
Write a jQuery to Select elements by class name,id and elementname.

4.       
Write a jQuery to Create slide-up, slide-down and slide-Toggleeffect.

5.        
Write a jQuery to insert multiple HTML elements at the beginning and
end of the documents.

6.       
Write a jQuery effect method without a callbackfunction.

7.        
Write a jQuery to create animation effect.

8.       
Write a jQuery to perform Method chaining.

 

JSON

1.      Create a JSON file and parseit.

2.      Create a JSON file and
persist it in any database.

 

 

 

 
