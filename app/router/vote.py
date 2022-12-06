from fastapi import HTTPException, Response, FastAPI, status, Depends, APIRouter
from .. import schemas,models,database,oauth
from sqlalchemy.orm import Session


router = APIRouter(prefix ="/vote",tags=['vote'])


@router.post("/",status_code = status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db:Session=Depends(database.get_db), current_user:int = Depends(oauth.get_current_user)):

    post = db.query(models.Post).filter(models.Post.id == models.Vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"post{models.Post.id} does not  exit")

    vote_qurey = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id,models.Vote.user_id == current_user.id)
    found_vote = vote_qurey.first()

    if vote.dir == 1:
        if found_vote :
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail= f"user {current_user.id} has already voted for the post of {vote.post_id}")
        
        new_post = models.Vote(post_id = vote.post_id, user_id = current_user.id)
        db.add(new_post)
        db.commit()
        return {"message": "successfully added vote"}

    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f"vote does not exist")
        vote_qurey.delete(synchronize_session=False)
        db.commit()
        return {"message": "successfully deleted the post"}