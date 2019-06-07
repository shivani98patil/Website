#The template and static folder should be made separately otherwise error occurs.
#In html careful about the <> may cause unnecessary output, whereas in css styling once changed check in incognito mode.


from flask import Flask,render_template
app=Flask(__name__,template_folder='templates')

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/about/')
def about():
    return render_template('about.html')

if __name__=="__main__":
    app.run(debug=True)
