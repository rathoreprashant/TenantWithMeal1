from flask import Flask, render_template, request,session, redirect, url_for
import os
import mysql.connector

app=Flask(__name__)
app.secret_key=os.urandom(24)



@app.route('/forgottent',methods = ['POST','GET'])
def forgotten():
    try:
        db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="root",
            database="tenantapp"
        )
        cursor = db.cursor()
        if request.method == 'POST':
            username = request.form.get("username")
            password = request.form.get("pass")
            repass = request.form.get("passre")
            print("++++++++++++")
            print(username)
            print(password)
            if password != repass:
                return render_template("Password Do not match")
            query = "UPDATE tenant SET password = %s WHERE tname = %s"
            values= (password,username,)
            cursor.execute(query,values)
            db.commit()
            return render_template("password_changed_successfully_tenant.html")
        return render_template("forgot_tenant.html")
    except Exception as e:
            return(str(e))


@app.route('/forgotuserr', methods=['POST','GET'])
def forgotuser():
    try:
        db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="root",
            database="tenantapp"
        )
        cursor = db.cursor()
        if request.method == 'POST':
            username = request.form.get("username")
            password = request.form.get("pass")
            repass = request.form.get("passre")
            print("++++++++++++")
            print(username)
            print(password)
            print(repass)
            if password != repass:
                return render_template("Password do not match")
            query = "UPDATE users SET password = %s WHERE username = %s"
            values= (password,username,)
            cursor.execute(query,values)
            db.commit()
            return render_template("password_changed_successfully_user.html")
        return render_template("forgot_user.html")
    except Exception as e:
            return(str(e))


        
@app.route('/flight/<string:t_id>/<string:username>/filter',  methods = ['POST','GET'])
def search_flight(t_id,username):
    try:
        db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="root",
            database="tenantapp"
        )
        details1=None
        cursor = db.cursor()
        if request.method == 'POST':
            Fromcity = request.form.get("from")
            tocity = request.form.get("to")
            print("++++++++++++")
            print(Fromcity)
            print(tocity)
            print("-------------")
            if Fromcity == tocity:
                return "Duplicate City Entered !!"
            query = "Select * from flight where from_city=%s and to_city=%s"
            values = (Fromcity,tocity,)
            cursor.execute(query,values,)
            details = cursor.fetchall()
            print(details)
            details1 = details
            if len(details):
                # return render_template('flight.html',flights=details, tidd=t_id,username=username)
                return flight(t_id,username,details)
            else:
                return "Flight Not Found"
        return render_template('flight_search.html',flights=details1, tidd=t_id,username=username)
    except Exception as e:
            return(str(e))

#---------------------------------------------------------------------------------------------------------------



@app.route('/taxi/<string:t_id>/<string:username>/filter',  methods = ['POST','GET'])
def search_taxi(t_id,username):
    try:
        db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="root",
            database="tenantapp"
        )
        details1=None
        cursor = db.cursor()
        if request.method == 'POST':
            Fromcity = request.form.get("from")
            print("++++++++++++")
            print(Fromcity)
            print("-------------")
            query = "Select * from taxi where oper_city=%s"
            values = (Fromcity,)
            cursor.execute(query,values,)
            details = cursor.fetchall()
            print("Printing Details")
            print(details)
            print(type(details))
            details1 = details
            if len(details):
                return taxi(t_id,username,details)
            else:
                return "Taxi Not Found"
            # return render_template('taxi.html',taxis=details, tidd=t_id,username=username)
        return render_template('taxi_search.html',taxis=details1, tidd=t_id,username=username)
    except Exception as e:
            return(str(e))


#-------------------------------------------------------------------------------------------------------------

@app.route('/hotel/<string:t_id>/<string:username>/filter',  methods = ['POST','GET'])
def search_hotel(t_id,username):
    try:
        db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="root",
            database="tenantapp"
        )
        details1=None
        cursor = db.cursor()
        if request.method == 'POST':
            Fromcity = request.form.get("from")
            print("++++++++++++")
            print(Fromcity)
            print("-------------")
            query = "Select * from hotel where city=%s"
            values = (Fromcity,)
            cursor.execute(query,values,)
            details = cursor.fetchall()
            print(details)
            details1 = details
            if len(details):
                # return render_template('hotel.html',hotels=details, tidd=t_id,username=username)
                return hotel(t_id, username, details)
            else:
                return "Hotel Not Found"
        return render_template('hotel_search.html',hotels=details1, tidd=t_id,username=username)
    except Exception as e:
            return(str(e))

print("------------------------------------------------------------------------------")
    

@app.route('/train/<string:t_id>/<string:username>/filter',  methods = ['POST','GET'])
def search_train(t_id,username):
    try:
        db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="root",
            database="tenantapp"
        )
        details1=None
        cursor = db.cursor()
        if request.method == 'POST':
            Fromcity = request.form.get("from")
            tocity = request.form.get("to")
            print("++++++++++++")
            print(Fromcity)
            print(tocity)
            if Fromcity == tocity:
                return "Duplicate Cities Entered !!"
            print("-------------")
            query = "Select * from train where from_city=%s and to_city=%s"
            values = (Fromcity,tocity,)
            cursor.execute(query,values,)
            details = cursor.fetchall()
            print(details)
            details1 = details
            if len(details):
            # return render_template('train.html',trains=details, tidd=t_id,username=username)
                return train(t_id, username, details)
            else :
                return "Train Not Found"
        return render_template('train_search.html',trains=details1, tidd=t_id,username=username)
    except Exception as e:
            return(str(e))






print("-------------------------------------------------------------------------------")

@app.route('/mealcnf/addmeal/<int:fl_id>/<int:m_id>/<string:t_id>/<string:username>', methods=['GET','POST'])
def display_selected_meal(fl_id,m_id,t_id,username):
        db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="root",
            database="tenantapp"
        )

        cursor = db.cursor()
        print("------------------------------------------------------------------------------------------------------------------")
        print(username)
        print("------------------------------------------------------------------------------------------------------------------")
        query_mealname = "select meal_name ,meal_price from meal where meal_id=%s"
        value_mid=(m_id,)
        cursor.execute(query_mealname,value_mid)
        meal=cursor.fetchall()[0]

        return render_template("meal_confirm.html", mealid = m_id, fl_id=fl_id,t_id=t_id,username=username,mealname=meal[0],price=meal[1])



@app.route('/dropsessionuserlogin')
def dropsession1():
    session.pop('user', None)
    return render_template("user_login.html")

@app.route('/dropsessiontenantlogin')
def dropsession2():
    session.pop('user', None)
    return render_template("tenant_login.html")


@app.route('/flightconfirmation')
def final():
    return render_template("flight_confirm2.html")

@app.route('/taxiconfirmation')
def final2():
    return render_template("taxi_confirm2.html")

@app.route('/trainconfirmation')
def final3():
    return render_template("train_confirm2.html")

@app.route('/hotelconfirmation')
def final4():
    return render_template("hotel_confirm2.html")


@app.route('/addmeal/<int:fl_id>/<int:m_id>/<string:t_id>/<string:username>', methods=['GET','POST'])
def add_meal(fl_id,m_id,t_id,username):
        db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="root",
            database="tenantapp"
        )
        print("Something")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(username)
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(t_id)
        print(fl_id)
        cursor = db.cursor()
        query2="insert into user_flight_meal (username, fl_id, meal_id) values (%s,%s,%s)"
        values2=(username,fl_id,m_id,)
        cursor.execute(query2,values2)
        db.commit()
        return render_template("meal_confirm2.html")
        

@app.route('/<string:tid>/food/<string:fid>/<string:username>',methods=['GET','POST'])
def meal(tid,fid,username):
    try:
    # Establish a connection to the MySQL server
        db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="root",
            database="tenantapp"
        )

        cursor = db.cursor()

    # Create a new database
        cursor = db.cursor()
        # query1 = "select username from user_flight where fl_id=%s"
        # value=(fid,)
        # cursor.execute(query1,value)
        # ans = cursor.fetchall()
        # username = ans[len(ans)-1][0]
        cursor.execute("select * from meal")
        foods = cursor.fetchall()
        for i in foods:
            print(i)
        return render_template("food.html",foods=foods,tid=tid,fid=fid,username=username)
    except Exception as e:
        print(e)
        return f"{e}"


@app.route('/delete/flight/<int:fid>')
def deleteflight(fid):
        db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="root",
            database="tenantapp"
        )
        cursor = db.cursor()
        query = "delete from flight where fl_id=%s"
        values=(fid,)
        cursor.execute(query,values)
        db.commit()
        return redirect("/all_flight")

@app.route('/delete/taxi/<int:taxiid>')
def deletetaxi(taxiid):
        db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="root",
            database="tenantapp"
        )
        cursor = db.cursor()
        query = "delete from taxi where tx_id=%s"
        values=(taxiid,)
        cursor.execute(query,values)
        db.commit()
        return redirect("/all_taxi")

@app.route('/delete/train/<int:trainid>')
def deletetrain(trainid):
        db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="root",
            database="tenantapp"
        )
        cursor = db.cursor()
        query = "delete from train where tr_id=%s"
        values=(trainid,)
        cursor.execute(query,values)
        db.commit()
        return redirect("/all_train")

@app.route('/delete/hotel/<int:hid>')
def deleteHotel(hid):
        db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="root",
            database="tenantapp"
        )
        cursor = db.cursor()
        query = "delete from hotel where ht_id=%s"
        values=(hid,)
        cursor.execute(query,values)
        db.commit()
        return redirect("/all_hotel")


# Edit
@app.route('/addflight', methods=['GET','POST'])
def addFlight():
        db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="root",
            database="tenantapp"
        )
        cursor = db.cursor()
        if request.method == 'POST':
            flightName = request.form.get("name")
            From = request.form.get("from")
            to = request.form.get("to")
            seats = request.form.get("seats")
            if flightName != None and From != None and to != None and seats != None:
                seat = int(seats)
                print(flightName)
                print(From)
                print(to)
                print(type(seat))
                if From == to:
                    return "Duplicate City Entered !!!"
                query = "insert into flight (airline_serv, from_city, to_city, avail_seats) values (%s, %s, %s, %s)"
                values = (flightName,From,to,seats,)
                cursor.execute(query, values)
                db.commit()
                return allflight()
            # return render_template("add_flight.html")
        return render_template("add_flight.html")

@app.route('/addhotel', methods=['GET','POST'])
def addHotel():
        db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="root",
            database="tenantapp"
        )
        cursor = db.cursor()
        if request.method == 'POST':
            hotelName = request.form.get("name")
            city = request.form.get("city")
            room = request.form.get("avail_room")
            price = request.form.get("price")
            if hotelName != None and city != None and room != None and price != None:
                price = int(price)
                room = int(room)
                print(hotelName)
                print(city)
                print(room)
                print(type(price))
                query = "insert into hotel (hotel_name, city, avail_rooms, price) values (%s, %s, %s, %s)"
                values = (hotelName,city,room,price,)
                cursor.execute(query, values)
                db.commit() 
            # return render_template("add_hotel.html")
                return allhotel()
        return render_template("add_hotel.html")

@app.route('/addtaxi', methods=['GET','POST'])
def addTaxi():
        db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="root",
            database="tenantapp"
        )
        cursor = db.cursor()
        if request.method == 'POST':
            taxiNumber = request.form.get("name")
            city = request.form.get("city")
            rate = request.form.get("rate")
            if taxiNumber != None and city != None and rate != None :
                rate = int(rate)
                print(taxiNumber)
                print(city)
                print(rate)
                query = "insert into taxi (taxi_number, oper_city, rate_km) values (%s, %s, %s)"
                values = (taxiNumber,city,rate,)
                cursor.execute(query, values)
                db.commit() 
                return alltaxi()
            # return render_template("add_taxi.html")
        return render_template("add_taxi.html")

@app.route('/addtrain', methods=['GET','POST'])
def addTrain():
        db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="root",
            database="tenantapp"
        )
        cursor = db.cursor()
        if request.method == 'POST':
            trainName = request.form.get("name")
            fromcity = request.form.get("from")
            tocity = request.form.get("to")
            price = request.form.get("price")
            seats = request.form.get("seats")
            if trainName != None and fromcity != None and tocity != None and price != None  and seats != None:
                seats = int(seats)
                price = int(price)
                print(trainName)
                print(fromcity)
                print(tocity)
                print(seats)
                if fromcity == tocity:
                    return "Duplicate city Entered !!!"
                query = "insert into train (train_name, from_city, to_city, price, avail_seats) values (%s, %s, %s, %s, %s)"
                values = (trainName,fromcity,tocity,price,seats,)
                cursor.execute(query, values)
                db.commit() 
                return alltrain()
            # return render_template("add_train.html")
        return render_template("add_train.html")


# @app.route('/checkip')
# def checkip():
#         f = requests.request('GET', 'http://myip.dnsomatic.com')
#         ip = f.text
#         return ip

@app.route('/',methods = ['POST','GET'])
def home1():
    try:
        return render_template("home.html")
    except Exception as e:
        return(str(e))

@app.route('/toSignup', methods = ['POST','GET'])
def home2():
    try:
        return render_template("tenant_signup.html")
    except Exception as e:
        return(str(e))

@app.route('/toLogin', methods = ['POST','GET'])
def home3():
    try:
        return render_template("tenant_login.html")
    except Exception as e:
        return(str(e)) 
curr_user = ""
curr_user_type=""

@app.route('/toSignup_user',methods=['GET','POST'])
def user_signup():
    try:
        mydb = mysql.connector.connect(host="127.0.0.1",
                                user="root",
                                password="root",
                                database="tenantapp",
                                auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()
        query="select t_id,tname from tenant"
        mycursor.execute(query)
        tenants=mycursor.fetchall()
        
        return render_template("user_signup.html",len=len(tenants),tenants=tenants)
    except Exception as e:
        return(str(e))

@app.route('/toLogin_user',methods=['GET','POST'])
def user_login():
    try:
        return render_template("user_login.html")
    except Exception as e:
        return(str(e))



@app.route('/signUp_user', methods = ['POST', 'GET'])
def signUp_user():
    try:
        mydb = mysql.connector.connect(host="127.0.0.1",
                                user="root",
                                password="root",
                                database="tenantapp",
                                auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()
        if request.method == 'POST':
        # name = request.form["name"]
            username = request.form["username"]
            password = request.form["password"]
            confirmPassword = request.form["cnfpassword"]
            t_id=request.form["t_id"]
            
            #print(name, username, password)

            myquery = "select exists(select * from users where username=%s)"
            rec_tup = (username,)
            mycursor.execute(myquery, rec_tup)
            if mycursor.fetchone()[0]==1:
                return render_template('Username already exists', message="Username already exists")
            elif password!=confirmPassword:
                return render_template('Password do not Match', message="Passwords Don't Match")
            else:
                mysql_query = "insert into users(t_id,username,password) values(%s, %s, %s)"
                records = (t_id, username, password)
                mycursor.execute(mysql_query, records)
                mydb.commit()
            return render_template("user_login.html")
    except Exception as e:
        return(str(e))

@app.route('/login_user', methods = ['POST', 'GET'])
def signIn_user():
    try:
        mydb = mysql.connector.connect(host="127.0.0.1",
                                user="root",
                                password="root",
                                database="tenantapp",
                                auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()
        global curr_user
        global curr_user_type
        if request.method == 'POST':
        
            if 'user' in session:
                    username=session['user']
                    query1="select t_id from users where username=%s"
                    query_tname="select tname from tenant where t_id=%s"
                    rec_tup=(username,)
                    mycursor.execute(query1,rec_tup)
                    tid=mycursor.fetchone()[0]
                    print(tid)
                    value=(tid,)
                    mycursor.execute(query_tname,value)
                    tname=mycursor.fetchall()[0]
                    print(username)
                    print(tname)
                    query2="select service_type from tenant_service where t_id=%s"
                    rec_tup=(tid,)
                    mycursor.execute(query2,rec_tup)
                    servicess=mycursor.fetchall()
                    print(servicess)
                    return render_template("user_home.html",user=curr_user,tid=tid,services=servicess,tname=tname,username=username)

            username = request.form["username"]
            password = request.form["password"]
            
            myquery = "select exists(select * from users where username=%s)"
            rec_tup = (username,)
            mycursor.execute(myquery, rec_tup)

            if mycursor.fetchone()[0]==1:
                new_query = "select password from users where username=%s"
                mycursor.execute(new_query, rec_tup)
                if mycursor.fetchone()[0]==password:
                    session['user']=username
                    query1="select t_id from users where username=%s"
                    rec_tup=(username,)
                    mycursor.execute(query1,rec_tup)
                    tid=mycursor.fetchone()[0]
                    query2="select service_type from tenant_service where t_id=%s"
                    rec_tup=(tid,)
                    mycursor.execute(query2,rec_tup)
                    servicess=mycursor.fetchall()
                    return render_template("user_home.html",user=session['user'],tid=tid,services=servicess,username=username)
                else:
                    print("username password wrong")
                    return render_template('Username/Password Wrong', message="Username/Password Wrong")
            else:
                print("outer error")
                return render_template('Username/Password Wrong', message="Username/Password Wrong")
    except Exception as e:
        return(str(e))

@app.route('/login_tenant', methods = ['POST', 'GET'])
def signIn():
    try:
        mydb = mysql.connector.connect(host="127.0.0.1",
                                user="root",
                                password="root",
                                database="tenantapp",
                                auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()
        global curr_user
        global curr_user_type
        if request.method == 'POST':
            username = request.form["username"]
            password = request.form["password"]
            
            myquery = "select exists(select * from tenant where userId=%s)"
            rec_tup = (username,)
            mycursor.execute(myquery, rec_tup)
        # return render_template("tenant_home.html",user=mycursor.fetchone())

            if mycursor.fetchone()[0]==1:
                new_query = "select password from tenant where userId=%s"
                mycursor.execute(new_query, rec_tup)
                if mycursor.fetchone()[0]==password:
                    curr_user = username
                    session['user']=username
                    query0="select t_id from tenant where userId=%s"
                    rec_tup=(username,)
                    mycursor.execute(query0,rec_tup)
                    tid=mycursor.fetchone()[0]
                    query="select * from users where t_id=%s"
                    rec_tup=(tid,)
                    mycursor.execute(query,rec_tup)
                    users=mycursor.fetchall()
                    #services now
                    query2="select service_type from tenant_service where t_id=%s"
                    mycursor.execute(query2,rec_tup)
                    service_list=mycursor.fetchall()
                    print(service_list)
                    return render_template("tenant_home.html",user=users,services_list=service_list)
                else:
                    print("username password wrong")
                    return render_template('Username/Password Wrong', message="Username/Password Wrong")
            else:
                print("outer error")
                return render_template('Username/Password Wrong', message="Username/Password Wrong")
    except Exception as e:
        return(str(e))

@app.route('/signUp_tenant', methods = ['POST', 'GET'])
def signUp_tenant():
    try:
        mydb = mysql.connector.connect(host="127.0.0.1",
                                user="root",
                                password="root",
                                database="tenantapp",
                                auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()
        if request.method == 'POST':
            name = request.form["name"]
            username = request.form["userId"]
            password = request.form["password"]
            confirmPassword = request.form["cnfpassword"]
            service_array=request.form.getlist('service')
            print(name, username, password)
            
            myquery = "select exists(select * from tenant where userId=%s)"
            rec_tup = (username,)
            mycursor.execute(myquery, rec_tup)
            if mycursor.fetchone()[0]==1:
                return render_template('Username already exists', message="Username already exists")
            elif password!=confirmPassword:
                return render_template('Passwords do not Match', message="Passwords Don't Match")
            else:
                mysql_query = "insert into tenant(tname,userId,password) values(%s, %s, %s)"
                records = (name, username, password)
                mycursor.execute(mysql_query, records)
                mydb.commit()
                query="select t_id from tenant where userId=%s"
                rec_tup=(username,)
                mycursor.execute(query,rec_tup)
                tid=mycursor.fetchone()[0]
                for service in service_array:
                    query1="insert into tenant_service(t_id,service_type) values(%s,%s)"
                    records=(tid,service)
                    mycursor.execute(query1,records)
                    mydb.commit()
            return render_template("tenant_login.html")

    except Exception as e:
        return(str(e))


@app.route('/all_taxi',methods=['GET'])
def alltaxi():
    try:
        mydb = mysql.connector.connect(host="127.0.0.1",
                                user="root",
                                password="root",
                                database="tenantapp",
                                auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()
        if 'user' in session:
            query="select * from taxi"
            mycursor.execute(query)
            f=mycursor.fetchall()
            return render_template('all_taxi.html',taxis=f)
        else:
            return render_template('home.html')
    except Exception as e:
        return(str(e))

@app.route('/all_flight',methods=['GET'])
def allflight():
    try:
        mydb = mysql.connector.connect(host="127.0.0.1",
                                user="root",
                                password="root",
                                database="tenantapp",
                                auth_plugin='mysql_native_password')

        mycursor = mydb.cursor()
        if 'user' in session:
            query="select * from flight"
            mycursor.execute(query)
            f=mycursor.fetchall()
            return render_template('all_flight.html',flights=f)
        else:
            return render_template('home.html')
    except Exception as e:
        return(str(e))


@app.route('/all_train',methods=['GET'])
def alltrain():
    try:
        mydb = mysql.connector.connect(host="127.0.0.1",
                                user="root",
                                password="root",
                                database="tenantapp",
                                auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()
        if 'user' in session:
            query="select * from train"
            mycursor.execute(query)
            f=mycursor.fetchall()
            return render_template('all_train.html',trains=f)
        else:
            return render_template('home.html')
    except Exception as e:
        return(str(e))

@app.route('/all_hotel',methods=['GET'])
def allhotel():
    try:
        mydb = mysql.connector.connect(host="127.0.0.1",
                                user="root",
                                password="root",
                                database="tenantapp",
                                auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()
        if 'user' in session:
            query="select * from hotel"
            mycursor.execute(query)
            f=mycursor.fetchall()
            return render_template('all_hotel.html',hotels=f)
        else:
            return render_template('home.html')
    except Exception as e:
        return(str(e))
#break

@app.route('/all_usertaxi',methods=['GET'])
def allusertaxi():
    try:
        mydb = mysql.connector.connect(host="127.0.0.1",
                                user="root",
                                password="root",
                                database="tenantapp",
                                auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()
        if 'user' in session:
            query0="select t_id from tenant where userId=%s"
            rec_tup=(session['user'],)
            mycursor.execute(query0,rec_tup)
            tid=mycursor.fetchone()[0]
            query="select * from user_taxi where t_id=%s"
            rec_tup=(tid,)
            mycursor.execute(query,rec_tup)
            f=mycursor.fetchall()
            return render_template('all_usertaxi.html',taxis=f)
        else:
            return render_template('home.html')
    except Exception as e:
        return(str(e))

@app.route('/all_usertrain',methods=['GET'])
def allusertrain():
    try:
        mydb = mysql.connector.connect(host="127.0.0.1",
                                user="root",
                                password="root",
                                database="tenantapp",
                                auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()
        if 'user' in session:
            query0="select t_id from tenant where userId=%s"
            rec_tup=(session['user'],)
            mycursor.execute(query0,rec_tup)
            tid=mycursor.fetchone()[0]
            query="select * from user_train where t_id=%s"
            rec_tup=(tid,)
            mycursor.execute(query,rec_tup)
            f=mycursor.fetchall()
            return render_template('all_usertrain.html',trains=f)
        else:
            return render_template('home.html')
    except Exception as e:
        return(str(e))

@app.route('/all_userhotel',methods=['GET'])
def alluserhotel():
    try:
        mydb = mysql.connector.connect(host="127.0.0.1",
                                user="root",
                                password="root",
                                database="tenantapp",
                                auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()
        if 'user' in session:
            query0="select t_id from tenant where userId=%s"
            rec_tup=(session['user'],)
            mycursor.execute(query0,rec_tup)
            tid=mycursor.fetchone()[0]
            query="select * from user_hotel where t_id=%s"
            rec_tup=(tid,)
            mycursor.execute(query,rec_tup)
            f=mycursor.fetchall()
            return render_template('all_userhotel.html',hotels=f)
        else:
            return render_template('home.html')
    except Exception as e:
        return(str(e))

@app.route('/all_userflight',methods=['GET'])
def alluserflight():
    try:
        mydb = mysql.connector.connect(host="127.0.0.1",
                                user="root",
                                password="root",
                                database="tenantapp",
                                auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()
        if 'user' in session:
            query0="select t_id from tenant where userId=%s"
            rec_tup=(session['user'],)
            mycursor.execute(query0,rec_tup)
            tid=mycursor.fetchone()[0]
            query="select * from user_flight where t_id=%s"
            rec_tup=(tid,)
            mycursor.execute(query,rec_tup)
            f=mycursor.fetchall()
            return render_template('all_userflight.html',flights=f)
        else:
            return render_template('home.html')
    except Exception as e:
        return(str(e))

#break

@app.route('/hotel/<string:tid>/<string:username>',methods=['POST','GET'])
def hotel(tid,username,details):
    try:
        mydb = mysql.connector.connect(host="127.0.0.1",
                                user="root",
                                password="root",
                                database="tenantapp",
                                auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()
        if True:
            query="select * from hotel"
            mycursor.execute(query)
            f=mycursor.fetchall()
            return render_template('hotel.html',hotels=details,tidd=tid,username=username)
        else:
            return render_template('home.html')

    except Exception as e:
        return(str(e))

@app.route('/flight/<string:tid>/<string:username>',methods=['POST','GET'])
def flight(tid,username,details):
    try:
        mydb = mysql.connector.connect(host="127.0.0.1",
                                user="root",
                                password="root",
                                database="tenantapp",
                                auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()
        if True:
            query="select * from flight"
            mycursor.execute(query)
            f=mycursor.fetchall()
            return render_template('flight.html',flights=details, tidd=tid,username=username)
        else:
            return render_template('home.html')
    except Exception as e:
        return(str(e))


@app.route('/taxi/<string:tid>/<string:username>',methods=['POST','GET'])
def taxi(tid,username,details):
    try:
        mydb = mysql.connector.connect(host="127.0.0.1",
                                user="root",
                                password="root",
                                database="tenantapp",
                                auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()
        if True:
            query="select * from taxi"
            mycursor.execute(query)
            f=mycursor.fetchall()
            return render_template('taxi.html',taxis=details, tidd=tid,username=username)
        else:
            return render_template('home.html')
    except Exception as e:
        return(str(e))

@app.route('/train/<string:tid>/<string:username>',methods=['POST','GET'])
def train(tid,username,details):
    try:
        mydb = mysql.connector.connect(host="127.0.0.1",
                                user="root",
                                password="root",
                                database="tenantapp",
                                auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()
        if True:
            query="select * from train"
            mycursor.execute(query)
            f=mycursor.fetchall()
            return render_template('train.html',trains=details, tidd=tid,username=username)
        else:
            return render_template('home.html')
    except Exception as e:
        return(str(e))

@app.route('/api/<string:t_id>/book/flight/<string:flightid>/<string:username>',methods=['GET','POST'])
def book_flight(t_id,flightid,username):
    try:
        mydb = mysql.connector.connect(host="127.0.0.1",
                                user="root",
                                password="root",
                                database="tenantapp",
                                auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()
        if True :
            query="select from_city,to_city,avail_seats from flight where fl_id=%s"
            rec_tup=(flightid,)
            mycursor.execute(query,rec_tup)
            f=mycursor.fetchone()
            fromCity=f[0]
            toCity=f[1]
            availSeats=f[2]
            query_tname="select tname from tenant where t_id=%s"
            tname_value=(t_id,)
            mycursor.execute(query_tname,tname_value)
            tname = mycursor.fetchone()[0]
            if availSeats>0:
                #availSeats=availSeats-1
                #query1="update flight set avail_seats=%s where fl_id=%s"
                #rec_tup=(availSeats,flightid)
                #mycursor.execute(query1,rec_tup)
                # query_username = "select username from users"
                # mycursor.execute(query_username)
                # ans = mycursor.fetchall()
                # username = ans[len(ans)-1][0]
                query2="insert into user_flight(username,fl_id,from_city,to_city,t_id) values (%s,%s,%s,%s,%s)"
                rec_tup=(username,flightid,fromCity,toCity,t_id)
                mycursor.execute(query2,rec_tup)
                mydb.commit()
                query3="select t_id from user_flight where username=%s"
                rec_tup1=(username,)
                mycursor.execute(query3,rec_tup1)
                records=mycursor.fetchall()
                length=len(records)
                last_record=records[length-1]
                return render_template('flight_confirm.html',id=last_record[0],other=rec_tup,tname=tname,fid=flightid,tid=t_id,username=username)
            else:
                return 'no seats available'
        else:
            return render_template('home.html')

    except Exception as e:
        return(str(e))

@app.route('/api/<string:t_id>/book/taxi/<string:taxiid>/<string:username>',methods=['GET','POST'])
def book_taxi(taxiid,t_id,username):
    try:
        mydb = mysql.connector.connect(host="127.0.0.1",
                                user="root",
                                password="root",
                                database="tenantapp",
                                auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()
        if True :
            query="select taxi_number,oper_city,rate_km from taxi where tx_id=%s"
            rec_tup=(taxiid,)
            tenant_query="select tname from tenant where t_id=%s"
            value=(t_id,)
            mycursor.execute(tenant_query,value)
            tname=mycursor.fetchall()[0]
            mycursor.execute(query,rec_tup)
            t=mycursor.fetchone()
            taxi_number=t[0]
            oper_city=t[1]
            rate_km=t[2]
            query2="insert into user_taxi(username,tx_id,taxi_number,oper_city,rate_km,t_id) values (%s,%s,%s,%s,%s,%s)"
            rec_tup=(username,taxiid,taxi_number,oper_city,rate_km,t_id)
            mycursor.execute(query2,rec_tup)
            mydb.commit()
            query3="select t_id from user_taxi where username=%s"
            rec_tup1=(username,)
            mycursor.execute(query3,rec_tup1)
            records=mycursor.fetchall()
            length=len(records)
            last_record=records[length-1]
            return render_template('taxi_confirm.html',id=last_record[0],other=rec_tup,tname=tname,username=username)
        else:
            return render_template('home.html')

    except Exception as e:
        return(str(e))

@app.route('/api/<string:t_id>/book/train/<string:trainid>/<string:username>',methods=['GET','POST'])
def book_train(trainid,t_id,username):
    try:
        mydb = mysql.connector.connect(host="127.0.0.1",
                                user="root",
                                password="root",
                                database="tenantapp",
                                auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()
        if True :
            query="select from_city,to_city,avail_seats,price from train where tr_id=%s"
            rec_tup=(trainid,)
            mycursor.execute(query,rec_tup)
            f=mycursor.fetchone()
            fromCity=f[0]
            toCity=f[1]
            availSeats=f[2]
            #price = f[3]
            if availSeats>0:
                tenant_query="select tname from tenant where t_id=%s"
                value=(t_id,)
                mycursor.execute(tenant_query,value)
                t_name=mycursor.fetchall()[0]
                #availSeats=availSeats-1
                #query1="update train set avail_seats=%s where tr_id=%s"
                #rec_tup=(availSeats,trainid)
                #mycursor.execute(query1,rec_tup)
                query2="insert into user_train(username,tr_id,from_city,to_city,t_id) values (%s,%s,%s,%s,%s)"
                rec_tup=(username,trainid,fromCity,toCity,t_id)
                mycursor.execute(query2,rec_tup)
                mydb.commit()
                query3="select t_id from user_train where username=%s"
                rec_tup1=(username,)
                mycursor.execute(query3,rec_tup1)
                records=mycursor.fetchall()
                length=len(records)
                last_record=records[length-1]
                return render_template('train_confirm.html',id=last_record[0],other=rec_tup,tname=t_name,username=username)
            else:
                return 'no seats available'
        else:
            return render_template('home.html')

    except Exception as e:
        return(str(e))


@app.route('/api/<string:t_id>/book/hotel/<string:hotelid>/<string:username>',methods=['GET','POST'])
def book_hotel(hotelid,t_id,username):
    try:
        mydb = mysql.connector.connect(host="127.0.0.1",
                                user="root",
                                password="root",
                                database="tenantapp",
                                auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()
        if True :
            query="select hotel_name,city,avail_rooms,price from hotel where ht_id=%s"
            rec_tup=(hotelid,)
            mycursor.execute(query,rec_tup)
            f=mycursor.fetchone()
            tenant_query="select tname from tenant where t_id=%s"
            value=(t_id,)
            mycursor.execute(tenant_query,value)
            tname=mycursor.fetchall()[0]
            #hotelName=f[0]
            city=f[1]
            availrooms=f[2]
            if availrooms>0:
                #availrooms=availrooms-1
                #query1="update hotel set avail_rooms=%s where ht_id=%s"
                #rec_tup=(availrooms,hotelid)
                #mycursor.execute(query1,rec_tup)
                query2="insert into user_hotel(username,ht_id,city,t_id) values (%s,%s,%s,%s)"
                rec_tup=(username,hotelid,city,t_id)
                mycursor.execute(query2,rec_tup)
                mydb.commit()
                query3="select t_id from user_hotel where username=%s"
                rec_tup1=(username,)
                mycursor.execute(query3,rec_tup1)
                records=mycursor.fetchall()
                length=len(records)
                last_record=records[length-1]
                return render_template('hotel_confirm.html',id=last_record[0],other=rec_tup,tname=tname,username=username)
            else:
                return 'no rooms available'
        else:
            return render_template('home.html')
    except Exception as e:
        return(str(e))


@app.route('/logout', methods = ['POST', 'GET'])
def logout():
    try:
        session.pop('user',None)
        return render_template('home.html')
    except Exception as e:
        return(str(e))

if __name__ == "__main__":
    app.run(debug=True)
