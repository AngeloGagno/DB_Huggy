import requests
import json
from dotenv import load_dotenv
import os
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

class Huggy_API:

    def __init__(self):
        self.api_key_v3 = self._API_key_v3()
        self.api_key_v2 = self._API_key_v2() 
        self.header_v3 = self._headers_v3()
        self.header_v2 = self._headers_v2()     
        self.pagination = self._pagination()
        self.channel = self._channels()
        self.raw_url = self._URL()

    def _API_key_v3(self):
        load_dotenv()
        return os.getenv('Huggy_API_V3')

    def _API_key_v2(self):
        load_dotenv()
        return os.getenv('Huggy_API_V2')
        
    def _URL(self):
        return 'https://api.huggy.app/v3/'

    def _headers_v3(self):
        auth = f'Bearer {self.api_key_v3}'
        return {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': auth,
    }

    def _headers_v2(self):
        auth = f'Bearer {self.api_key_v2}'
        return {
    'Authorization': auth
        }

    def _pagination(self):
        return '?page='

    def _channels(self,channel='whatsapp'):
        return f'channel={channel}'

    def get_chat_list(self,page:int):
        session = requests.Session()
        retry = Retry(
            total=5,  # Tenta até 5 vezes
            backoff_factor=1,  # Atraso entre tentativas: 1s, 2s, 4s, etc.
            status_forcelist=[429, 500, 502, 503, 504], 
        )
        adapter = HTTPAdapter(max_retries=retry)
        session.mount("https://", adapter)
        url = f'{self.raw_url}chats{self.pagination}{page}&{self.channel}'
        return session.get(url,headers=self.header_v3).json()

    def get_chat(self,id):
        url = f'{self.raw_url}chats/{id}/messages'
        return requests.get(url,headers=self.header_v3).json()


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
               
if __name__ == "__main__":
    print(len(Huggy_API().get_chat(id=197960766)))