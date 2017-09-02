import sys, requests, json

URL = "https://www.deepl.com/jsonrpc"

text = sys.argv[1]

def encodeRequest(text):
    return(json.dumps({"jsonrpc" : "2.0", "method" : "LMT_handle_jobs", "params" : { "jobs" : [ { "kind" : "default", "raw_en_sentence" : text } ], "lang" : { "user_preferred_langs" : [ "EN", "PL"], "source_lang_user_selected" : "EN", "target_lang" : "PL"}, "priority" : -1 }, }, separators=(",", ":")))

def sendRequest(json):
    return requests.post(URL, data = json)



json = encodeRequest(text)
response = sendRequest(json)
print(response.encoding)
print(response.text.encode('utf-8'))
