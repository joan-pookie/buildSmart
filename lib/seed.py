from sqlalchemy.orm import Session
from lib.models.base import engine, init_db
from lib.models.client import Client
from lib.models.worker import Worker
from lib.models.project import Project
from lib.models.project_assignment import ProjectAssignment

# Ensure tables exist
init_db()

# Open a session
session = Session(engine)

# ---- Clear old data (optional, for fresh seeding) ----
session.query(ProjectAssignment).delete()
session.query(Project).delete()
session.query(Worker).delete()
session.query(Client).delete()
session.commit()

# ---- Seed Clients ----
client1 = Client(name="Joan Construction Ltd", email="joan@construction.com")
client2 = Client(name="GreenBuild Co", email="contact@greenbuild.com")

# ---- Seed Workers ----
worker1 = Worker(name="Alice", role="Engineer")
worker2 = Worker(name="Bob", role="Architect")
worker3 = Worker(name="Charlie", role="Site Manager")

# ---- Seed Projects ----
project1 = Project(name="Smart Building Project", description="AI-powered office building", client=client1)
project2 = Project(name="Eco Housing Estate", description="Sustainable housing with solar panels", client=client2)

# ---- Seed Assignments ----
assignment1 = ProjectAssignment(project=project1, worker=worker1)
assignment2 = ProjectAssignment(project=project1, worker=worker2)
assignment3 = ProjectAssignment(project=project2, worker=worker3)

# Add everything to the session
session.add_all([client1, client2, worker1, worker2, worker3, project1, project2, assignment1, assignment2, assignment3])

# Commit changes
session.commit()
session.close()

print("✅ Database seeded successfully with sample data!")
