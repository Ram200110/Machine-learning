from flask import Flask,render_template,request
import pickle
import numpy as np

app=Flask(__name__)


with open('heart.pkl', 'rb') as file:
    classifier = pickle.load(file)

@app.route('/')
def home():
    return render_template('index1.html')
@app.route('/value')
def value():
    return render_template('home.html')



@app.route('/predict' ,methods=["POST","GET"])
def predict():

    result = ""

    if request.method == 'POST':
        AGE = float(request.form['age'])
        SEX = int(request.form['sex'])
        CHEST_PAIN_TYPE = int(request.form['chest'])
        RESTING_BP = float(request.form['resting'])
        CHOLESTROL = float(request.form['chol'])
        FASTING_BLOOD_SUGAR = float(request.form['fasting'])
        RESTECGE = int(request.form['rest'])
        MAX_HR = float(request.form['max'])
        EXANG = int(request.form['ex'])
        OLDPEAK = float(request.form['old'])
        SLOPE = int(request.form['slope'])
        NUM_MAJOR_VESSELS = float(request.form['num'])
        THAL = int(request.form['thal'])

        features = np.array([[AGE, SEX,CHEST_PAIN_TYPE,RESTING_BP,CHOLESTROL,FASTING_BLOOD_SUGAR,RESTECGE,MAX_HR,EXANG,OLDPEAK,SLOPE,NUM_MAJOR_VESSELS,THAL]])
        prediction = classifier.predict(features)
       

    if (prediction[0]==0) :
        result=" does not have heart disease"
        return render_template("happy.html" , result=result)
    
    elif (prediction[0]==1):
        result=" You MIGHT have heart disease"

    return render_template("sad.html" , result=result)



@app.route('/Physical')
def Physical():
    return render_template('Physical.html')

@app.route('/Physicalresult',methods=['POST','GET'])
def Physicalresult():
    if request.method=="POST":
        value1=request.form.get("chestPain")
        value2=request.form.get("shortOfBreath")
        value3=request.form.get("irregularHeartbeats")
        value4=request.form.get("highBloodPressure")
        value5=request.form.get("dizziness")
        yes_count = [value1, value2, value3, value4, value5].count("yes")
        if yes_count >= 3:
            result_message = "The person might have heart disease."
        else:
            result_message = "The person may not have heart disease."

        return render_template('Physical.html',result_message=result_message)
    
    return render_template('Physical.html')




@app.route('/physcologicaly')
def physcologicaly():
    return render_template('physcologicaly.html')

@app.route('/physcologicalyresult', methods=['POST', 'GET'])
def physcologicalyresult():
    if request.method == "POST":
        value1 = request.form.get("sadness")
        value2 = request.form.get("worry")
        value3 = request.form.get("appetite")
        value4 = request.form.get("impendingDoom")
        value5 = request.form.get("stress")

        print(value1)
        print(value2)
        print(value3)
        print(value4)
        print(value5)

        yes_count = [value1, value2, value3, value4, value5].count("yes")
        if yes_count > 3:
            result_message = "The person might have heart disease."
        else:
            result_message = "The person may not have heart disease."

        return render_template('physcologicaly.html', result_message=result_message)
    
    return render_template('physcologicaly.html')








if __name__=="__main__":
    app.run(debug=True)