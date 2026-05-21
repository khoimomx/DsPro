from sqlalchemy import create_engine

def get_engine():
    server   = 'localhost'
    database = 'student_db'
    username = 'sa'
    password = '********'
    driver   = 'ODBC Driver 18 for SQL Server'

    connect_str = (
        f"mssql+pyodbc://{username}:{password}@{server}/{database}"
        f"?driver={driver.replace(' ', '+')}"
        f"&TrustServerCertificate=yes"
    )
    return create_engine(connect_str)