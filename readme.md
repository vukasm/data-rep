This resository represents my project for the Data representation module at GMIT.


With this project I want to demonstrate my understanding of creation and usage of RESTful APIs. Therefore, I have created a web application with FLASK that has a RESTful API and which connects to a database table. Furthermore, I demonstrate application of CRUD operations on this web pages.

The topic of my project is table called Chocolates, which contains:
- Chocolate ID (auto-incremented)
- Brand
- Kind
- Price

The web page gives an option to create, update or delete a chocolate from the table.

How to run this:

1. Make sure you have Python installed.
2. Make sure you have MySQL server installed.
3. Open MySQL console.
4. Run rest-server.py
5. Run dbCreateDB.py to create datarepresentation database.
6. Run dbCreateTable.py to create chocolates table in the datarepresentation database.
7. Run link http://127.0.0.1:5000/index.html in your search engine.
8. Play with the web page and check what happens in mysql database table.



List of relevant files:
1. rest-server.py with RESTful API
2. ChocolatesDAO.py containing chocolates DAO
3. dbconfig-template.py  for the user to be able to run the code on different computers
4. dbCreateDB.py python code for creation of the database in mysql
5. dbCreateTable.py python code for creation of chocolates table in our database
6. folder staticpages containing code for the web page
7. requirements.txt containing requirenments for virtual environment


Hope you enjoy it!