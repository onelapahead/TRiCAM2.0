import requests

asyncurl = "http://api.idolondemand.com/1/api/async/{}/v1"

syncurl = "http://api.idolondemand.com/1/api/sync/{}/v1"

APIKEY = "b34cabbd-239e-45e4-af2b-44b449493096"

joburl = "http://api.idolondemand.com/1/job/{}/{}?apikey=" + APIKEY

def post_async_api_request(function, data={}, files={}):
  callurl = asyncurl.format(function)
  data['apikey'] = APIKEY
  r = requests.post(callurl, data=data, files=files)
  return r.json()

def post_api_request(function, data={}, files={}):
  callurl = syncurl.format(function)
  data['apikey'] = APIKEY
  r = requests.post(callurl, data=data, files=files)
  return r.json()

def audio_to_str(audiofilepath):
  with open(audiofilepath, 'rb') as f:
    return post_async_api_request('recognizespeech', files={'file': f})

def determine_sentiment(text):
  return post_api_request('analyzesentiment', data={'text': text})

def get_job_request(function, jobID):
  callurl = joburl.format(function, jobID)
  r = requests.get(callurl)
  return r.json()

def get_job_status(jobID):
  return get_job_request('status', jobID)

def get_job_result(jobID):
  return get_job_request('result', jobID)  

def recognize_logos(imgfile):
  return post_async_api_request('recognizeimages', data={'image_type': 'complex_2d'}, files={'file': imgfile})

def get_logos_result(jobID):
  results = get_job_result(jobID)
  if results['actions'][0]['status'] == 'finished':
    logos = []
    for logo in results['actions'][0]['result']['object']:
      logos.append(logo['name'])
    return logos
  else:
    return None
