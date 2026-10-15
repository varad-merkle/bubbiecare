from typing import List

from pgvector.sqlalchemy import HALFVEC
from sqlalchemy import Integer, String, REAL, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass

class CandidateResume(Base):
    __tablename__ = "bcare_candidate_resumes"
    __table_args__ = {"schema": "varadraj_galgali"}

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String)
    age: Mapped[int] = mapped_column(Integer)
    gender: Mapped[str] = mapped_column(String)
    skills: Mapped[str] = mapped_column(String)
    experiences: Mapped[str] = mapped_column(String)
    certifications: Mapped[str] = mapped_column(String)
    summary: Mapped[str] = mapped_column(String)
    feature_vector: Mapped[list[float]] = mapped_column(HALFVEC(384))
    email: Mapped[str] = mapped_column(String)
    location: Mapped[str] = mapped_column(String)
    companion_care: Mapped[bool] = mapped_column()
    personal_care: Mapped[bool] = mapped_column()
    respite_care: Mapped[bool] = mapped_column()
    hospice_care: Mapped[bool] = mapped_column()
    total_experience: Mapped[int] = mapped_column(Integer)
    status: Mapped[str] = mapped_column(String)
    likelyhood: Mapped[float] = mapped_column(REAL)
    testscore: Mapped[float] = mapped_column(REAL)
    options: Mapped["Options"] = relationship("Options", back_populates="candidate")

class Options(Base):
    __tablename__ = "options"
    __table_args__ = {"schema": "varadraj_galgali"}

    test_id: Mapped[int] = mapped_column(Integer, ForeignKey("varadraj_galgali.bcare_candidate_resumes.id"), primary_key=True)
    q1: Mapped[str] = mapped_column(String)
    q2: Mapped[str] = mapped_column(String)
    q3: Mapped[str] = mapped_column(String)
    q4: Mapped[str] = mapped_column(String)
    q5: Mapped[str] = mapped_column(String)
    m1: Mapped[int] = mapped_column(Integer)
    m2: Mapped[int] = mapped_column(Integer)
    m3: Mapped[int] = mapped_column(Integer)
    m4: Mapped[int] = mapped_column(Integer)
    m5: Mapped[int] = mapped_column(Integer)
    candidate: Mapped["CandidateResume"] = relationship("CandidateResume", back_populates="options")
