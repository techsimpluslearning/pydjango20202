import urllib.parse
import urllib.request

authKey = "232419AT2rwRRUo5b77e616"
Number = [9893762256, 7906971360, 7000047827]
#Number = "9893762256"
Msg = """
Hi There!
Here i am sending a msg from SMS Gateway...

Team
TechSim+
"""
sender = "TXTAPI"
route = "4"
url = "http://api.msg91.com/api/sendhttp.php"


### Dict File... Json Data

for n in Number:
    values = {
            "authkey": authKey,
            "mobiles": str(n),
            "message": Msg,
            "sender": sender,
            "route": route
        }

    data = urllib.parse.urlencode(values)
    data = data.encode("ascii")
    req = urllib.request.Request(url, data)
    response = urllib.request.urlopen(req)
    print(response)

### End of the Code...




























