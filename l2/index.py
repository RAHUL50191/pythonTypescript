import requests
from secret import API_KEY
import sys
upload_url="https://api.assemblyai.com/v2/upload"
transcribe_url = "https://api.assemblyai.com/v2/transcript"
headers = {'authorization': API_KEY}
filename = sys.argv[1]
###upload
def upload(filename):
    def read_file(filename, chunk_size=5242880):
        with open(filename, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data
                
    response = requests.post(upload_url,
                            headers=headers,
                            data=read_file(filename))

    # print(response.json())
    audio_url=response.json()["upload_url"]
    return audio_url


###transcribe
def transcribe(audio_url):
    json = { "audio_url": audio_url }
    response = requests.post(transcribe_url, json=json, headers=headers)
    # print(response.json()) 
    return response.json()["id"]

audio_url =upload(filename)

job_id = transcribe(audio_url)
print(job_id)

###polling
