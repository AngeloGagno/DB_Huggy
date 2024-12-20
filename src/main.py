from API.get_data import get_chats_description
from Database.database import get_db,Base,engine
from Database.commit import commit_data_on_db

def main():
    # Cria as tabelas no banco de dados, se ainda não existirem
    Base.metadata.create_all(engine)
    commit_data_on_db(chat_list=get_chats_description(), db=get_db())


if __name__ == '__main__':
    main()