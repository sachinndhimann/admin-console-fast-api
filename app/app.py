from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from starlette.applications import Starlette
from starlette_admin.contrib.sqla import Admin, ModelView

Base = declarative_base()
engine = create_engine("sqlite:///test.db", connect_args={"check_same_thread": False})

# Define your model
class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()

Base.metadata.create_all(engine)

app = Starlette()

# Create admin
admin = Admin(engine, title="Example: SQLAlchemy")

# Add view
admin.add_view(ModelView(Post))

# Mount admin to your app
admin.mount_to(app)
