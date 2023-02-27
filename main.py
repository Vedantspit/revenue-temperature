import pickle 
from flask import Flask,request,render_template


app=Flask(__name__);
model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def index():
    print("YO BRO")
    return render_template('index.html');

@app.route('/predict',methods=['GET','POST'])
def predict():
    myq=float(request.form.get('temperature'))
    ans=model.predict([[myq]]);
    output=round(ans[0],2)
    print(output)
    return render_template('index.html',result=f"Total revenue generated is Rs {output}/-");
    










if __name__=="__main__":
    app.run(debug=True);
