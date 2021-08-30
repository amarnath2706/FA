from flask import Flask, request, jsonify

app = Flask(__name__)
#Post Method - Whatever data we are sending, this data needs to be send in the body of the call.
#Body of the call - localhost:5000/postmanpost
@app.route("/postmanpost", methods=['POST'])
def math_operation():
    if (request.method=='POST'):
        operation = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])

        if (operation =='add'):
            r = num1+num2
            result = 'the sum of '+str(num1)+' and '+str(num2) +' is '+str(r)
        if (operation == 'subtract'):
            r = num1 - num2
            result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'multiply'):
            r = num1 * num2
            result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'divide'):
            r = num1 / num2
            result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
    return jsonify(result)

#Get Method - Whatever data i'm sending from client to served side, those data's are appended inside the url and it's clearly visible in the url itself.
#ocalhost:5000/postmanget?num1=20&num2=06&operation=subtract
@app.route("/postmanget", methods=['GET'])
def math_operation_get():

    operation = request.args.get('operation')
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))

    if(operation =='add'):
        r = num1+num2
        result = 'the sum of '+str(num1)+' and '+str(num2) +' is '+str(r)
    if (operation == 'subtract'):
        r = num1 - num2
        result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
    if (operation == 'multiply'):
        r = num1 * num2
        result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
    if (operation == 'divide'):
        r = num1 / num2
        result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
    return (result)


if __name__ == '__main__':
    # app.run(debug=True, port=8000)
    app.run(debug=True)