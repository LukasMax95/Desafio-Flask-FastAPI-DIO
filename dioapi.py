import pandas as pd
from flask_ngrok import run_with_ngrok
import flask as flk
from fastapi import FastAPI
import nest_asyncio
from pyngrok import ngrok
import uvicorn

app = flk.Flask(__name__)
run_with_ngrok(app)

class Members:
    def __init__(self):
        self._posts = []
        self._member = {}

    def newMember(self, name, age, city, country):
        self._member = {
            "index":0,
            "name":name,
            "age":age,
            "city":city,
            "country":country
        }
        self._posts.append(self._member)
    
    def insertPost(self):
        res = {}
        for i in range (0, len(self._posts)):
            p = self._posts[i]
            p["index"] = i+1
            res[f"{i}"] = p
        return res
    
    def makePost(self):
        res = """
<h1> Showing posts </h1>
"""
        for i in range (0, len(self._posts)):
            p = self._posts[i]
            p["index"] = i+1
            res += f"""
            <p>{i+1}: <marquee>{p}</marquee></p>
            """
        res += """==================================================="""
        return res


@app.route("/")
def home():
    return """



<marquee><h3> Dio Challenge Api! </h3></marquee>

<a href="localhost:5000/input">Go to index!</a> 
<
"""

members01 = Members()
members01.newMember(
    "Mahesh",
    25,
    "Bangalore",
    "India"
)
members01.newMember(
    "Alex",
    25,
    "London",
    "UK"
)
members01.newMember(
    "David",
    27,
    "San Francisco",
    "USA"
)
members01.newMember(
    "John",
    28,
    "Toronto",
    "Canada"
)
members01.newMember(
    "Chris",
    29,
    "Paris",
    "France"
)

@app.route("/input")
def input():
    post = members01.insertPost()
    return flk.jsonify(post)

@app.route("/index", methods=['GET','POST'])
def predJson():
    return members01.makePost()

app.run()


app = FastAPI()

@app.get('/index')
async def home():
  return flk.jsonify(members01.insertPost())

ngrok_tunnel = ngrok.connect(8000)
print('Public URL:', ngrok_tunnel.public_url)
nest_asyncio.apply()
uvicorn.run(app, port=8000)