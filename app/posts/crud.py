from datetime import datetime

from sqlalchemy.orm import Session

from .models import Post


def get_post(post_id: int, db: Session):
    return db.query(Post).get(post_id)


def get_posts(db: Session):
    return db.query(Post).all()


async def update_post(post_id: int, db: Session, data: dict):
    data['time_stamp'] = datetime.now()
    a = db.query(Post).filter(Post.uid == post_id).update(data)
    db.commit()
    print(a)


async def create_post(db: Session, post: Post, set_time=True):
    if set_time:
        post.time_stamp = datetime.now()
    db.add(post)
    db.commit()
    db.refresh(post)


async def delete_post(db: Session, post_id: int):
    db.delete(get_post(post_id=post_id, db=db))
