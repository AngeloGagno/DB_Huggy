import requests
import json

class Huggy_API:

    def __init__(self):
        self.header_v3 = self._headers_v3()
        self.header_v2 = self._headers_v2()
        self.pagination = self._pagination()
        self.channel = self._channels()
        self.raw_url = self._URL()

    def _URL(self):
        return 'https://api.huggy.app/v3/'

    def _headers_v3(self):
        return {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjgxZTVhZDNiYmZlYWJlOGQwNDIwYzJlMGNkMmVlNjA4YzgzMDk4YTczMTllODVmZDExNzQwYWU1NTk4M2YzMWU0OGNhMDg3ZTc0ZTM0ODFmIn0.eyJhdWQiOiJBUFAtMmVmNTdlZWMtY2VmNS00ZTExLTk3MmEtNGI5YzAxNjA3YmE4IiwianRpIjoiODFlNWFkM2JiZmVhYmU4ZDA0MjBjMmUwY2QyZWU2MDhjODMwOThhNzMxOWU4NWZkMTE3NDBhZTU1OTgzZjMxZTQ4Y2EwODdlNzRlMzQ4MWYiLCJpYXQiOjE3MzQ1MzA1MjcsIm5iZiI6MTczNDUzMDUyNywiZXhwIjoxNzUwMjU1MzI3LCJzdWIiOiIxMjUzNjYiLCJzY29wZXMiOlsiaW5zdGFsbF9hcHAiLCJyZWFkX2FnZW50X3Byb2ZpbGUiXX0.nBidFTLeDrud7gw49qaH_iTPjFH9M9TTHWGIIeOYyZOGldKPyFjoSB2KNjuCk8ldDDNqKXlfj0EzpkK53YmwPBnyHDMbeSJNmwkPgvo10JuDWPjqcYy6v-XAFCqBS30g2kqNSJfU7S5scVGle_k5viFE2lj-Rzb0R3QI3pejQnM' ,
    }

    def _headers_v2(self):
        return {
    'Authorization': 'Bearer ff2081a06895a3e2342f7ab16e50bce9'
        }

    def _pagination(self):
        return '?page'

    def _channels(self,channel='whatsapp'):
        return f'channel={channel}'

    def get_chat_list(self,page=1):
        url = f'{self.raw_url}/chats{self.pagination}&{self.channel}'
        return requests.get(url,headers=self.header_v3).json()

    def get_chat(self,id):
        url = f'{self.raw_url}/chats/{id}/messages'
        return requests.get(url,headers=self.header_v3).json()

    def get_feedback(self,ids):
        url = f'https://api.huggy.app/v2/chats/{ids}/feedback'
        return requests.get(url,headers=self.header_v2).json()

class Huggy_Parameters:
    def __init__(self,chat_json):
        self.chat = chat_json

    
    def chat_id(self):
        return self.chat['id']
    
    def agent_id(self):
        return self.chat.get('agentId',None)

    def tabulation_id(self):
        return self.chat.get('tabulationId',None)
    
    def client_id(self):
        return self.chat.get('contactId',None)
    
    def status_chat(self):
        return self.chat.get('situation',None)

    def creation_date(self):
        return self.chat['createdAt']
    
    def update_date(self):
        return self.chat.get('updatedAt',None)

    def attended_at_date(self):
        return self.chat.get('attendedAt',None)

    def closed_date(self):
        return self.chat.get('closedAt',None)
               
        
chat = Huggy_API().get_chat_list()[1]
print(Huggy_Parameters(chat).closed_date())