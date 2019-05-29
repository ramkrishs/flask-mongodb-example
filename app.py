from sanic import Sanic
from sanic.response import json

app = Sanic()

@app.route("/")
async def main(request):
    return json({"name": "Hello Flask MongoDB Example"})

@app.route("/users/<name>")
async def get_user_by_id(request, name):
    user_obj = {
        'name': name
    }
    print(user_obj)
    # go find if there are any info with name rama in db and fetch and show here
    # object - name , address or email, 
    # prerequ: db connect 
    # query run select * from db where name=name
    # result convert to json and run to user

    return json(user_obj)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)