from sqlalchemy import String,Integer,Boolean
from app.database.base import Base
from sqlalchemy.orm import mapped_column,Mapped



class Profile(Base):
    __tablename__ = "profile"
    id: Mapped[int] = mapped_column(Integer, primary_key=True,index=True)
    first_name: Mapped[String] = mapped_column(String(50),nullable=False)
    last_name: Mapped[String] = mapped_column(String(50))
    phone_number: Mapped[String] = mapped_column(Integer(15),nullable=False,unique=True)
    city: Mapped[String] = mapped_column(String(50),nullable=False)
    address: Mapped[String] = mapped_column(String(50),nullable=False)
