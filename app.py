from recommendation import recommend_movie
from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/",methods=['POST','GET'])
def home():
    if request.method == "POST":
        movie_name=request.form['movie']
        try:
            movies=recommend_movie(movie_name)
        except:
            movies=recommend_movie("Avatar")
        return render_template("index2.html",movies=movies)
    return render_template("index.html")
    
if __name__=="__main__":
    app.run(debug=True)