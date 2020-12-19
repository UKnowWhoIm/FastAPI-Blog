from fastapi import APIRouter
from sqlalchemy.orm import Session
from . import models, schemas
from fastapi import Depends
from ..commons import get_db
router = APIRouter()


@router.get("/posts/")
async def list_posts(db: Session = Depends(get_db)):
    return db.query(models.Post).all()


@router.post("/posts/")
async def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    pass


@router.get("/posts/{post_id}/")
async def retrieve_post(db:Session, post_id: int):
    db.query(models.Post).filter(models.Post.uid == post_id).first()


@router.patch("/posts/{post_id}/")
async def patch_post(post_id: int):
    pass


@router.delete("/posts/{post_id}/")
async def delete_post(post_id: int):
    pass


@router.put("/posts/{post_id}/")
async def patch_post(post_id: int):
    pass
