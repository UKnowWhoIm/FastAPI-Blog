from typing import List

from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session

from .. import schemas, models
from ...auth.models import User
from fastapi import Depends
from app.db.database import get_db
from .. import crud
from ...auth.commons import get_current_user

router = APIRouter()


@router.get("/", response_model=List[schemas.Post])
async def list_posts(db: Session = Depends(get_db)):
    return crud.get_posts(db)


@router.post("/", status_code=201)
async def create_post(
        post: schemas.PostCreate,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    if not current_user:
        raise HTTPException(status_code=401)
    db_post = models.Post(title=post.title, content=post.content, author=current_user, author_uid=current_user.uid)
    await crud.create_post(db=db, post=db_post)


@router.get("/{post_id}/", response_model=schemas.Post)
async def retrieve_post(post_id: int, db: Session = Depends(get_db)):
    return crud.get_post(post_id, db)


@router.patch("/{post_id}/")
async def patch_post(
        post_id: int,
        post: schemas.PostUpdate,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db),
):
    current_post = await crud.get_post(post_id, db)
    if current_post.author_uid != current_user.uid:
        raise HTTPException(status_code=403)

    allowed_fields = ("content", "title")
    data = {key: val for key, val in post.__dict__.items() if key in allowed_fields and val is not None}
    await crud.update_post(post_id=post_id, db=db, data=data)


@router.delete("/{post_id}/")
async def delete_post(post_id: int, db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    current_post = await crud.get_post(post_id, db)
    if current_post.author_uid != current_user.uid:
        raise HTTPException(status_code=403)
    await delete_post(post_id)
