@app.route('',methods = ['POST','GET'])
# def forgotten():
#     try:
#         db = mysql.connector.connect(
#             host="127.0.0.1",
#             user="root",
#             passwd="root",
#             database="tenantapp"
#         )
#         cursor = db.cursor()
#         if request.method == 'POST':
#             username = request.form.get("username")
#             password = request.form.get("pass")
#             print("++++++++++++")
#             print(username)
#             print(password)
#             query = "UPDATE user SET password = %s WHERE username = %s"
#             values= (password,username,)
#             cursor.execute(query,values)
#             db.commit()
#             return tenant_login()