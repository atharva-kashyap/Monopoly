from flask import Flask, request, render_template, session, flash
from flask_pymongo import PyMongo
from flask import redirect

# Initializing
app = Flask(__name__)
app.url_map.strict_slashes = False
app.debug = True

app.secret_key = "sri"

app.config["MONGO_URI"] = "mongodb://skandakas:atharva13@cluster0-shard-00-00-n27aa.mongodb.net:27017,cluster0-shard-00-01-n27aa.mongodb.net:27017,cluster0-shard-00-02-n27aa.mongodb.net:27017/monopoly?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority"
#app.config["MONGO_URI"] = "mongodb+srv://skandakas:atharva13@cluster0-n27aa.mongodb.net/monopoly?retryWrites=true&w=majority"
mongo = PyMongo(app)
print(mongo.db)

@app.route("/", methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        user = request.form["email"]
        name = request.form["name"]
        date = request.form["date"]
        players = mongo.db.user.find({})
        print (players)
        for player in players:
            if player["email"] == user:
                session["user"] = user
                session["date"] = date
                return redirect("/game")
        else:
            mongo.db.user.insert_one({"name": name, "date": date, "email": user})
            session["user"] = user
            session["date"] = date
            return redirect("/game")

@app.route("/delete")
def deleteUser():
    mongo.db.user.drop()
    return render_template("login.html")

@app.route("/prop", methods = ['GET', 'POST'])
def addProp():
    if request.method == 'GET':
        result = mongo.db.property.find({})
        print(result)
        return render_template('propertyMaster.html', result = result)
    else:
        propName = request.form["pName"]
        propValue = request.form["pValue"]
        color = request.form["color"]
        rent = request.form["rent"]
        mongo.db.property.insert_one({"pName":propName, "pValue":propValue, "color":color, "rent":rent})
        return redirect("/prop")

@app.route("/game", methods = ['GET', 'POST'])
def playGame():
    if request.method == 'GET':
        if "user" in session and "date" in session:
            user = session["user"]
            date = session["date"]
            result_prop = mongo.db.property.find({})
            result_prop2 = mongo.db.property.find({})
            result_to = mongo.db.user.find({"date":date})
            result_prop3 = mongo.db.property.find({})
            result_from = mongo.db.user.find({"date":date})
            result_prop4 = mongo.db.property.find({})
            result = mongo.db.game.find({})
            # buy_value = mongo.db.game.find({})
            # sell_value = mongo.db.game.find({})
            return render_template("game.html", result=result, result_to=result_to, result_prop=result_prop, result_prop2=result_prop2,
                                   result_prop3=result_prop3, result_from=result_from, result_prop4=result_prop4, user=user, date=date)
    else:
        if "user" in session and "date" in session:
            user = session["user"]
            date = session["date"]
            buy = request.form["buy_1"]
            buy_value = request.form["buy_1_value"]
            sell = request.form["sell_1"]
            sell_value = request.form["sell_1_value"]
            penalty = request.form["penalty_1"]
            gift = request.form["gift_1"]
            whom_p = request.form["whom_p"]
            rentPaid = request.form["rentP"]
            amt1 = request.form["amt1"]
            whom_r = request.form["whom_r"]
            rentRec = request.form["rentR"]
            amt2 = request.form["amt2"]
            reverse = request.form["reverse"]
            mongo.db.game.insert_one({"user":user, "date":date, "buy_1":buy, "buy_1_value":buy_value, "sell_1":sell, "sell_1_value":sell_value, "penalty_1":penalty, "gift_1":gift, "whom_p":whom_p, "rentP":rentPaid, "amt1":amt1, "whom_r":whom_r, "rentR":rentRec, "amt2":amt2, "reverse":reverse})
            return redirect("/game")

@app.route("/logout", methods = ['GET', 'POST'])
def logout():
    if request.method == 'GET':
        session.pop("loggedin", None)
        print("logoutedddd")
        flash("User off")
        return redirect("/summary")
    else:
        print("posted")
        total = request.args["total"]
        user = request.args["user11"]
        date = request.args["date11"]
        mongo.db.user.update_one({"date":date, "email":user}, {"$set":{"total":total}})
        print(mongo.db.user.find({}))
        return redirect("/summary")

@app.route("/summary", methods = ['GET'])
def viewSummary():
    if "user" in session and "date" in session:
        date = session["date"]
        result = mongo.db.user.find({"date":date})
        for a in result:
            print(a)
        return render_template("summary.html",result=result)

# run
if __name__ == "__main__":
    app.run("")
