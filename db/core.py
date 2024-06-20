import psycopg
from config import db_params


def add_user(user_id, nickname, who_is):
    try:
        conn = psycopg.connect(**db_params)
        with conn.cursor() as cur:
            cur.execute("INSERT INTO pijawcabot (user_id, nickname, who_is) VALUES (%s, %s, %s)",
                        (user_id, nickname, who_is))
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
        conn.close()
    return response

def get_user_data(user_id):
    try:
        conn = psycopg.connect(**db_params)
        with conn.cursor() as cur:
            cur.execute("SELECT who_is FROM pijawcabot WHERE user_id = %s", (user_id,))
            result = cur.fetchone()
    except Exception as e:
        print(e) 
    finally:
        conn.close()
    return result[0]