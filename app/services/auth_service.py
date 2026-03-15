from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import create_access_token


class AuthService:

    def login(self, db: Session, email: str):

        user = db.query(User).filter(User.email == email).first()

        if not user:
            return None

        token = create_access_token({"user_id": user.id})

        return token
