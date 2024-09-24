from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .Base import Base

class Commentaire(Base):
    __tablename__ = 'commentaires'

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    article_id = Column(Integer, ForeignKey('articles.id'), nullable=False)  # Clé étrangère vers la table Article
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relation avec l'article
    article = relationship("Article", back_populates="commentaires")