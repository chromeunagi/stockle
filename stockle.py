import sys
import http.client
from html.parser import HTMLParser

# critical
# 1. http://eoddata.com/Search.aspx?s=aaplds to check if stock exists

# add-ons
# 1. set up email: https://automatetheboringstuff.com/chapter16/
# 2. command completion
# 3. 
#

# TODO
def is_valid_ticker(ticker):
    return true

def http_get(host, port, resource):
    conn = http.client.HTTPConnection(host + ":" + port)
    conn.request("GET", resource)
    resp = conn.getresponse()

    if resp.status == 400:
        error("Error: invalid ticker")
    
    s = bytearray()
    
    while not resp.closed:
        chunk = resp.read(512)
        if not chunk:
            break
        s += chunk

    print("HERE:")
    print(str(s))

def price(ticker):
    res = "/Search.aspx?s=" + ticker
    http_get("eoddata.com", "80", res)

def error(message, exit_code = 1):
    sys.stderr.write(message)
    sys.exit(exit_code)

def main():
    args = sys.argv[1:]
    argc = len(args)
    if argc < 2:
        error("Invalid args. Try \"stockle help\" to get list of valid commands\n")

    cmd = args[0]

    if cmd == "price":
        if argc != 2:
            error("Invalid args to plot.")
        price(args[1])
    else:
        error("Invalid command")

if __name__ == "__main__":
    main()

