import requests

def get_chapter(chapter):
  url = "http://statutes.agc.gov.sg/aol/search/display/viewPrint.w3p;page=0;query=Status%3Ainforce%20CapAct%3A{cap}%20Depth%3A0;rec=0;resUrl=http%3A%2F%2Fstatutes.agc.gov.sg%2Faol%2Fsearch%2Fsummary%2Fresults.w3p%3Bquery%3DStatus%253Ainforce%2520CapAct%253A{cap}%2520Depth%253A0;whole=yes".format(cap=chapter)
  res = requests.get(url)
  try:
    res.raise_for_status()
  except Exception as exc:
    print(exc)
    return False
  if(res.status_code == requests.codes.ok):
    return res.text
  else:
    print("Error: %s" % res.status_code)
    return False

def fake_get_chapter(chapter):
  if chapter == '224':
    pc = open('pc.html', 'r')
    return pc.read().encode().decode('utf-8', 'ignore')
  else:
    return False