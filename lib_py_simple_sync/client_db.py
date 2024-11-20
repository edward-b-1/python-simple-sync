
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from sqlalchemy import create_engine


class Base(DeclarativeBase):
    pass


class MonitoredTarget(Base):
    __tablename__ = "monitor_targets"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    path: Mapped[str]
    md5: Mapped[str]
    sha256: Mapped[str]

    def __repr__(self) -> str:
        return f"MonitoredTarget(id={self.id!r}, name={self.name!r}, path={self.path!r}, md5={self.md5!r}, sha256={self.sha256!r})"



def create_database(engine:Engine) -> None:
    Base.metadata.create_all(engine)

