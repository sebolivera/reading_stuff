from django.core.management.base import BaseCommand
from faker import Faker
from userauth.models import User
from readwrite.models import Post, TextPost, Comment
from django.utils.text import slugify
from bcrypt import hashpw
from random import randrange
from django.contrib.auth.hashers import make_password
import os
from pathlib import Path
faker = Faker()
DIR_PATH = Path(__file__).resolve().parent.parent.parent.parent


class Command(BaseCommand):
    help = "Seed database for testing (sqlite3 only)."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        print('Seeding data...')
        run_seed(self)
        print('Done.')


def clear_data():
    """Deletes all the table data"""
    try:
        print("Delete Comment instances")
        Comment.objects.all().delete()
    except:
        print("Warning: couldn't find any comments")
    try:
        print("Delete Post instances")
        Post.objects.all().delete()
    except:
        print("Warning: couldn't find any posts")
    try:
        User.objects.all().delete()
    except:
        print("Couldn't find any users")


def create_users(amount=4):
    print("Creating users")

    users = []

    for i in range(0, amount):
        pwd = faker.password()
        password = make_password(pwd)

        if os.path.exists(os.path.join(DIR_PATH, 'dummy_passwords.txt')):
            os.remove(os.path.join(DIR_PATH, 'dummy_passwords.txt'))
        f = open(os.path.join(DIR_PATH, "dummy_passwords.txt"), "a")

        username = faker.user_name()
        while username in [u.username for u in users]:
            username = faker.user_name()
        email = faker.email()
        while email in [u.email for u in users]:
            email = faker.email()
        user = User(
            pen_name=username+"_author",
            username=username,
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            is_admin=False,
            profile_picture=faker.image_url(),
            password=password,
            email=email,
            color_mode="dark")
        users.append(user)
        f.write(email+': '+pwd+'\n')
        print("User '{}' created.".format(user.pen_name))
    f.close()
    User.objects.bulk_create(users)
    return users


def create_posts(amount=10):
    print("Creating posts...")
    posts = []
    users = User.objects.all()
    for i in range(0, len(users)):
        for j in range(0, amount):
            title = " ".join(faker.words(5))
            slug = slugify(title)
            while slug in [p.slug for p in posts]:
                print(slug, posts)
                title = faker.words(5)
                slug = slugify(title)
            post = TextPost(title=title,
                            slug=slug, status=1, author=users[i], content=faker.text(max_nb_chars=2000))
            posts.append(post)
            post.save()  # can't bulk insert inherited classes :'(


def create_comments(amount=10):
    print("Creating comments...")
    comments = []
    posts = Post.objects.all()
    users = User.objects.all()
    for i in range(0, len(posts)):
        for j in range(0, 10):
            comment = Comment(post=posts[i], author=users[randrange(
                len(users))], body=faker.text(max_nb_chars=300), active=True)
            comments.append(comment)
    Comment.objects.bulk_create(comments)


def run_seed(self,):
    # Clear data from tables
    clear_data()
    create_users()
    create_posts()
    create_comments()
