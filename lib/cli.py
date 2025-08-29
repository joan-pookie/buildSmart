# lib/cli.py
import click
from sqlalchemy.orm import Session
from lib.models.base import engine, init_db  # <-- import init_db
from lib.models.client import Client
from lib.models.worker import Worker
from lib.models.project import Project
from lib.models.project_assignment import ProjectAssignment

# Ensure all tables exist before doing anything
init_db()

# Optional REPL
try:
    from click_repl import repl
    CLICK_REPL_AVAILABLE = True
except ImportError:
    CLICK_REPL_AVAILABLE = False

@click.group()
def cli():
    """BuildSmart CLI"""
    pass

# -------- CLIENTS --------
@cli.group()
def client():
    """Manage clients"""
    pass

@client.command("add")
@click.argument("name")
@click.argument("email")
def add_client(name, email):
    with Session(engine) as session:
        client = Client(name=name, email=email)
        session.add(client)
        session.commit()
        click.echo(f"Added client: {name} (email: {email})")

@client.command("list")
def list_clients():
    with Session(engine) as session:
        clients = session.query(Client).all()
        if clients:
            for c in clients:
                click.echo(f"{c.id}: {c.name} (email: {c.email})")
        else:
            click.echo("No clients found.")

@client.command("delete")
@click.argument("client_id", type=int)
def delete_client(client_id):
    with Session(engine) as session:
        client = session.get(Client, client_id)
        if not client:
            click.echo(f"No client with id {client_id}")
            return
        session.delete(client)
        session.commit()
        click.echo(f"Deleted client {client_id}")

# -------- WORKERS --------
@cli.group()
def worker():
    """Manage workers"""
    pass

@worker.command("add")
@click.argument("name")
@click.argument("role")
def add_worker(name, role):
    with Session(engine) as session:
        worker = Worker(name=name, role=role)
        session.add(worker)
        session.commit()
        click.echo(f"Added worker: {name} (role: {role})")

@worker.command("list")
def list_workers():
    with Session(engine) as session:
        workers = session.query(Worker).all()
        if workers:
            for w in workers:
                click.echo(f"{w.id}: {w.name} (role: {w.role})")
        else:
            click.echo("No workers found.")

@worker.command("delete")
@click.argument("worker_id", type=int)
def delete_worker(worker_id):
    with Session(engine) as session:
        worker = session.get(Worker, worker_id)
        if not worker:
            click.echo(f"No worker with id {worker_id}")
            return
        session.delete(worker)
        session.commit()
        click.echo(f"Deleted worker {worker_id}")

# -------- PROJECTS --------
@cli.group()
def project():
    """Manage projects"""
    pass

@project.command("add")
@click.argument("name")
@click.argument("client_id", type=int)
@click.option("--description", default=None, help="Project description")
def add_project(name, client_id, description):
    with Session(engine) as session:
        project = Project(name=name, client_id=client_id, description=description)
        session.add(project)
        session.commit()
        click.echo(f"Added project: {name} (client_id: {client_id})")

@project.command("list")
def list_projects():
    with Session(engine) as session:
        projects = session.query(Project).all()
        if projects:
            for p in projects:
                click.echo(f"{p.id}: {p.name} (client_id: {p.client_id}, description: {p.description})")
        else:
            click.echo("No projects found.")

@project.command("delete")
@click.argument("project_id", type=int)
def delete_project(project_id):
    with Session(engine) as session:
        project = session.get(Project, project_id)
        if not project:
            click.echo(f"No project with id {project_id}")
            return
        session.delete(project)
        session.commit()
        click.echo(f"Deleted project {project_id}")

# -------- ASSIGNMENTS --------
@cli.group()
def assignment():
    """Manage project assignments"""
    pass

@assignment.command("add")
@click.argument("project_id", type=int)
@click.argument("worker_id", type=int)
def add_assignment(project_id, worker_id):
    with Session(engine) as session:
        assignment = ProjectAssignment(project_id=project_id, worker_id=worker_id)
        session.add(assignment)
        session.commit()
        click.echo(f"Assigned worker {worker_id} to project {project_id}")

@assignment.command("list")
def list_assignments():
    with Session(engine) as session:
        assignments = session.query(ProjectAssignment).all()
        if assignments:
            for a in assignments:
                click.echo(f"Project {a.project_id} -> Worker {a.worker_id}")
        else:
            click.echo("No assignments found.")

@assignment.command("delete")
@click.argument("project_id", type=int)
@click.argument("worker_id", type=int)
def delete_assignment(project_id, worker_id):
    with Session(engine) as session:
        assignment = session.query(ProjectAssignment).filter_by(
            project_id=project_id, worker_id=worker_id
        ).first()
        if not assignment:
            click.echo(f"No assignment found for project {project_id} and worker {worker_id}")
            return
        session.delete(assignment)
        session.commit()
        click.echo(f"Deleted assignment: worker {worker_id} from project {project_id}")

if __name__ == "__main__":
    if CLICK_REPL_AVAILABLE:
        # optional interactive REPL
        import sys
        if len(sys.argv) > 1 and sys.argv[1] == "repl":
            repl(cli)
        else:
            cli()
    else:
        cli()
