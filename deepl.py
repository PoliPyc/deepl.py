#!/usr/bin/python3

import sys, requests, json

URL = "https://www.deepl.com/jsonrpc"

def encodeRequest(text):
    return(json.dumps({"jsonrpc" : "2.0", "method" : "LMT_handle_jobs", "params" : { "jobs" : [ { "kind" : "default", "raw_en_sentence" : text } ], "lang" : { "user_preferred_langs" : [ "EN", "PL"], "source_lang_user_selected" : "EN", "target_lang" : "PL"}, "priority" : -1 }, }, separators=(",", ":")))

def sendRequest(json):
    return requests.post(URL, data = json)

if(len(sys.argv) < 2):
    print("deepl.py: Nie podano tekstu do przetłumaczenia")

else:
    text = sys.argv[1]
    encodedRequest = encodeRequest(text)
    response = sendRequest(encodedRequest)
    response = json.loads(response.text)
    print(response)

