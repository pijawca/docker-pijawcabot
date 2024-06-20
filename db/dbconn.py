import psycopg
from config import db_params


def dbconn():
    try:
        conn = psycopg.connect(**db_params)
        with conn.cursor() as cur:
            cur.execute("SELECT version();")
            db_version = cur.fetchone()
            response = f'Подключение к базе данных PostgreSQL успешно. Версия PostgreSQL: {db_version}'
            cur.close()
    except (Exception, psycopg.Error) as error:
        response = f'Ошибка PostgreSQL: {error}'
    finally:
        conn.close()
    return response