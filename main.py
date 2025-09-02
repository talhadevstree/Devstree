from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db.db import Base, engine, SessionLocal
from passlib.context import CryptContext
from usermodel.regischema import Registeruser
from usermodel.userschema import Userresponse, Userlogin
from usermodel.usermodel import User
from menumodel.menumodel import MenuItem
from menumodel.menuschema import Menu

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
Base.metadata.create_all(bind=engine)

api = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@api.get("/")
def index():
    return {"Hello ": "Welcome to Food Chain"}


# register user
@api.post("/api/auth/register", response_model=Userresponse)
def register(user: Registeruser, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.name == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="User Already Register")

    # creating a hash pass
    hash_pass = pwd_context.hash(user.password)
    user.password = hash_pass
    # create the new user if the user if not register
    new_user = User(name=user.username, password=user.password, jwt=None)
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


#login user
@api.post("/api/auth/login", response_model=Userresponse)
def login(user: Userlogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.name == user.name).first()
    
    if not db_user:
        raise HTTPException(status_code=400, detail="Wrong username")
    
    if not pwd_context.verify(user.password , db_user.password): 
        raise HTTPException(status_code=400, detail="Wrong Password")
    else:
        raise HTTPException(status_code=200 , detail="Login success")
    
#add item in menu
@api.post("/api/menu/add")
def add_menu(menu: Menu, db:Session = Depends(get_db)):
    new_item = MenuItem(
        name=menu.name,
        description=menu.description,
        price=menu.price,
        quantity=menu.quantity,
        ingredientid = menu.ingredientid,
        category=menu.category,
    )
    db.add(new_item)
    db.commit()
    raise HTTPException(status_code=200, detail="Item added in menu")
