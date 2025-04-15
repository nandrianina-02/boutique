from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# DB setup
engine = create_engine("sqlite:///./ma_db.sqlite", echo=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


#Utilisateur_table
class Utilisateur(Base):
    __tablename__ = "utilisateurs"
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, index=True)
    description = Column(String)



class UtilisateurCreate(BaseModel):
    nom: str
    description: str

#Produits_table

class Produits(Base):
    __tablename__ = "produits"
    id = Column(Integer, primary_key = True, index = True)
    titre = Column(String)
    descriptions = Column(String)
    prix = Column(Integer)

class ProduitsCreate(BaseModel):
    titre: str
    descriptions: str
    prix : int


Base.metadata.create_all(bind=engine)


@app.post("/utilisateurs/")
def create_user(user: UtilisateurCreate):
    db = SessionLocal()
    nouveau = Utilisateur(nom=user.nom, description=user.description)
    db.add(nouveau)
    db.commit()
    db.refresh(nouveau)
    db.close()
    return nouveau

@app.get("/utilisateurs/")
def read_users():
    db = SessionLocal()
    users = db.query(Utilisateur).all()
    db.close()
    return users

#ajouter produits

@app.post("/produits/")
def create_produits(produit: ProduitsCreate):
    db = SessionLocal()
    add = Produits(titre = produit.titre, descriptions= produit.descriptions, prix=produit.prix)
    db.add(add)
    db.commit()
    db.refresh(add)
    db.close()
    return add

#recuperer produits

@app.get("/produits/")
def get_produits():
    db = SessionLocal()
    produits = db.query(Produits).all()
    db.close
    return produits