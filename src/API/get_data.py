from API.request import Huggy_API,Huggy_Parameters
import pandas as pd

def get_chats_description():
    request = Huggy_API()
    pag = 1
    chats = request.get_chat_list(page=pag)   
    chats_list = []
    while chats:
        chats = request.get_chat_list(page=pag)
        for chat in chats:
            parameters = Huggy_Parameters(chat)
            chat_id = parameters.chat_id()
            agent_id = parameters.agent_id()
            tabulation_id = parameters.tabulation_id()
            client_id = parameters.client_id()
            status_chat = parameters.status_chat()
            creation_date = parameters.creation_date()
            update_date = parameters.update_date()
            attended_at_date = parameters.attended_at_date()
            closed_date = parameters.closed_date()
            chat = {'chat_id':str(chat_id),'agent_id':agent_id,'tabulation_id':tabulation_id,
            'client_id':client_id,'status':status_chat,'creation_date':creation_date,'updated_at':update_date,'attended_at':attended_at_date,
            'closed_at':closed_date}

            chats_list.append(chat)
        pag +=1
    return chats_list

if __name__ == '__main__':
    print(get_chats_description())