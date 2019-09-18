import requests
import json
import config

response = requests.get('https://api.gotinder.com/v2/matches?count=100s_tinder_u=false&locale=en&message=1', headers= config.match_head)
rr = json.loads(response.text)
#for x in range(60):
print(rr['data']['matches'][0]['person'])

'''
def send_msg(match_id, msg):
    try:
        url = 'https://api.gotinder.com' + '/user/matches/%s' % match_id
        r = requests.post(url, headers=head,
                          data=json.dumps({"message": msg}))
        return r.json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong. Could not send your message:", e)
try:
  send_msg('5d807ffa50e984e8191e719d', "hey")
  print('sent')
except:
    print('failed')
    '''
