import requests
# add del change
def modify_data(name, mode="add", total=False, data=False):
    if mode == 'change':
        res  =  requests.patch(f'http://127.0.0.1:5000/data/{name}',{"total":str(total),"change":str(data) })
        return res.json()
    elif  mode == "del":
        res  =  requests.delete(f'http://127.0.0.1:5000/data/{name}')
        return f"account {name} has been deleted"
    elif  mode == "add":
        res  =  requests.put(f'http://127.0.0.1:5000/data/{name}',{"total":str(total),"change":str(data) })
        return res.json()
    else:
        return "please enter correct attribute parameters"

# get data
def get_data(name):
    # try:
        # usage get_data('name')["change"]
        res = requests.get('http://127.0.0.1:5000/'+f"data/{name}").json()
        account_name = dict(res)["id"]
        change = eval( dict( res )["change"] )
        debits = change["debits"]
        creditss = change["credits"]
        total = dict(res)["total"]
        return {"total":total, "change":change, "name":account_name, "debits": debits, "credits":creditss}
    # except:
        # return f"user not exist or it has been deleted"

