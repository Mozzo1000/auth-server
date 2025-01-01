from flask import Blueprint
import click
from getpass import getpass
import sys
import re
from api.models import User

user_command = Blueprint('user', __name__)

def _validate_email(ctx, param, value):
    if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", value):
        raise click.UsageError('Incorrect email address given')
    else:
        return value

def _validate_role(ctx, param, value):
    valid_roles = ["user", "admin"]
    if value in valid_roles:
        return value
    else:
        raise click.UsageError(f"Incorrect role given, valid roles are: {valid_roles}")


@user_command.cli.command("create")
@click.argument('email', type=str, callback=_validate_email)
@click.argument('name', type=str)
@click.argument('role', type=str, callback=_validate_role)
@click.option("--password", type=str)
def create_user(email, name, role, password):
    print("Creating user..")
    if password:
        set_password = password
    else:
        password = getpass("Set a password: ")
        password_again = getpass("Confirm password: ")
        if password == password_again:
            set_password = password
        else:
            print("Passwords do not match, try again.")
            sys.exit(1)
    existing_user = User.query.filter(User.email==email).first()
    if existing_user:
        print(f"User with email {email} already exists.")
        sys.exit(1)
    
    new_user = User(email=email, password=User.generate_hash(set_password), name=name, role=role)
    try:
        new_user.save_to_db()
        print(f"Successfully created a new user:\n\tEmail: {email}\n\tName: {name}\n\tRole: {role}")
    except:
        print("Could not save new user to database.")
    