from fastapi import status,Depends, HTTPException,responses,APIRouter
from .. import database,schemas,models,utils,oauth
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

router = APIRouter(tags = ['Authentication'])
@router.post('/login',response_model=schemas.Token)
def login(User_credintials : OAuth2PasswordRequestForm = Depends(), db:Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == User_credintials.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credintials")

    if not utils.Verify(User_credintials.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credinatials")

    
    access_token = oauth.create_access_token(data = {"user_id": user.id})

    return {"access_token":access_token,"token_type": "bearer"}
