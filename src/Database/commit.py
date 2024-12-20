from Database.models import DB_huggy
from sqlalchemy.orm import Session

def commit_data_on_db(chat_list,db:Session):
    for item in chat_list:
        registros = DB_huggy(
                id = item['chat_id'],
                agent_id=item['agent_id'],
                tabulation_id = item['tabulation_id'],
                client_id = item['client_id'],
                status_chat=item['status'],
                creation_date=item['creation_date'],
                update_date=item['updated_at'],
                attended_at_date=item['attended_at'],
                closed_date=item['closed_at'],
        )
        db.merge(registros)
    db.commit()
    print("Dados inseridos com sucesso!")