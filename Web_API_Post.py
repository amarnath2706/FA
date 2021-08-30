#1.Import flask
from flask import Flask, request, jsonify

# I have created an object here for the Flask class and it represents the init function
app = Flask(__name__)

@app.route("/postman", methods = ['POST'])
#def math_operation(num1, num2, operation):
def math_operation():
    if (request.method == 'POST'):
        operation = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        if (operation == 'add'):
            r = num1 + num2
            result = 'The sum of '  +str(num1)  +' and '  +str(num2)  +' is : '  +str(r)
        if (operation == 'subtract'):
            r = num1-num2
            result = 'The Differecce of' +str(num1) +'and' +str(num2) +'is' +str(r)
        if (operation == 'multiply'):
            r = num1*num2
            result = 'The Product of' +str(num1) +'and' +str(num2) +'is' +str(r)
        if (operation == 'divide'):
            r = num1/num2
            result = 'The division of' +str(num1) +'and' +str(num2) +'is' +str(r)
        return jsonify(result)
#route - it tries to read the function
@app.route('/details',methods=['POST'])
def user_det():
    if(request.method=='POST'):
        name = request.json['name']
        email = request.json['mail']
        phno = request.json['phno']
        #return jsonify("Name:" + name,'Email:' +email, 'Phno:' +str(phno))
        return jsonify(name+email+str(phno))
#Output = math_operation(20,6,'add')
#print(Output)

@app.route('/urltest')
def url_test():
    #args - send the values or datas through URL (kind of get operation) and displays the result in the same web page
    #Append my data or query in the url
    test1 = request.args.get('val1')
    test2 = request.args.get('val2')
    test3 = test1 + test2
    #return the output in the form og heading
    return '''<h1>My result is : {}</h1>'''.format(test3)

#Entry point of our code
if __name__ == '__main__':
    #default posrt no : 5000
    app.run(debug=True, port=2018)
    #app.run(debug=True)