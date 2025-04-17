from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:monVraiMotDePasse@aws-0-eu-west-3.pooler.supabase.com:6543/postgres"

engine = create_engine(DATABASE_URL)

with engine.connect() as conn:
    result = conn.execute("SELECT 1;")
    print(result.fetchone())
