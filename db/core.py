import psycopg
from config import db_params


def add_user(user_id, nickname):
    try:
        conn = psycopg.connect(**db_params)
        with conn.cursor() as cur:
            cur.execute("INSERT INTO pijawcabot (user_id, nickname, who_is) VALUES (%s, %s, %s)",
                        (user_id, nickname, 'Пользователь'))
            conn.commit()
            response = 0
    except Exception as e:
        with psycopg.connect(**db_params) as conn:
            with conn.cursor() as cur:
                cur.execute("UPDATE pijawcabot SET user_id = %s, nickname = %s WHERE user_id = %s", 
                            (user_id, nickname, user_id))
                conn.commit()
                response = 1
    finally:
        cur.close()
        conn.close()
    return response

def dbconn():
    try:
        conn = psycopg.connect(**db_params)
        with conn.cursor() as cur:
            cur.execute("SELECT version();")
            db_version = cur.fetchone()
            response = f'Подключение к базе данных PostgreSQL успешно. \nВерсия PostgreSQL: {db_version}'
    except (Exception, psycopg.Error) as error:
        response = f'Ошибка PostgreSQL: {error}'
    finally:
        cur.close()
        conn.close()
    return response
        
def get_users(user_id):
    try:
        conn = psycopg.connect(**db_params)
        with conn.cursor() as cur:
            cur.execute("SELECT who_is FROM pijawcabot WHERE user_id = %s;", (user_id,))
            response = cur.fetchone()[0]
    except (Exception, psycopg.Error) as error:
        response = f'Ошибка PostgreSQL: {error}'
    finally:
        cur.close()
        conn.close()
    return response