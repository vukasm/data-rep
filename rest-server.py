from logging import debug
from flask import Flask, url_for, request, redirect, abort
from flask import json
from flask.json import jsonify
from ChocolatesDAO import chocolatesDAO

app=Flask(__name__, static_url_path='',static_folder='staticpages')

chocolates=[
    {"id":1,"brand":"Lindt","kind":"dark","price":1.98},
    {"id":2,"brand":"Godiva","kind":"dark","price":2.09},
    {"id":3,"brand":"Milka","kind":"milk","price":1.58}
]
nextId=4

#selection functions

@app.route('/')
def index():
    return "hello"

#Get all.
@app.route('/chocolates')
def getAll():
    return jsonify(chocolatesDAO.getAll())

#Find by ID.
@app.route('/chocolates/<int:id>')
def findById(id):
    ##Create an array of the found books.
    #foundChocolates=list(filter(lambda t:t["id"]==id,chocolates))
    #if len(foundChocolates)==0:
    #    return jsonify({}),204
    #return jsonify(foundChocolates[0])
    #return "served by findById with id " +str(id)
    return jsonify(chocolatesDAO.findbyId(id))

#Create.
#curl -X POST -H "content-type:application/json" -d "{\"brand\":\"test\",\"kind\":\"some\",\"price\":1}" http://127.0.0.1:5000/chocolates
@app.route('/chocolates', methods=['POST'])
def create():
    global nextId

    #If theree is no json in the request, abort.
    if not request.json:
        abort(400)

    #Otherwise fill out the new objest with the passed data.
    chocolate={
        "id":nextId,
        "brand":request.json["brand"],
        "kind":request.json["kind"],
        "price":request.json["price"]
    }

    #Append the object to the list od chocolates.
    #chocolates.append(chocolate)

    #Next ID is +1.
    nextId+=1
    ##Return the appended chocolate.
    #return jsonify(chocolate)
    return jsonify(chocolatesDAO.create(chocolate))

#Update.
# curl -X PUT -H "content-type:application/json" -d "{\"brand\":\"Raw\",\"kind\":\"dark\"}" http://127.0.0.1:5000/chocolates/1
@app.route('/chocolates/<int:id>',methods=['PUT'])
def update(id):
    #Create an array of the found books.
    #foundChocolates=list(filter(lambda t:t["id"]==id,chocolates))
    foundChocolate=chocolatesDAO.findbyId(id)
    print(foundChocolate) #sanity check
    #if len(foundChocolates)==0:
    if foundChocolate=={}:
        return jsonify({}),404
    
    #currentChocolate=foundChocolates[0]
    currentChocolate=foundChocolate

    #If the brand is in the information passed up, set the brand of the current book as the brand passed.
    if "brand" in request.json:
        currentChocolate["brand"]=request.json["brand"]
    #If the kind is in the information passed up, set the kind of the current book as the kind passed.
    if "kind" in request.json:
        currentChocolate["kind"]=request.json["kind"]
    #If the price is in the information passed up, set the price of the current book as the price passed.
    if "price" in request.json:
        currentChocolate["price"]=request.json["price"]

    chocolatesDAO.update(currentChocolate)

    return jsonify(currentChocolate)

#Delete.
@app.route('/chocolates/<int:id>',methods=['DELETE'])
def delete(id):

    chocolatesDAO.delete(id)

    #foundChocolates=list(filter(lambda t:t["id"]==id,chocolates))
    #if len(foundChocolates)==0:
    #    return jsonify({}),404
    #chocolates.remove(foundChocolates[0])
    return jsonify({"done":True})




if __name__=="__main__":
    app.run(debug=True)