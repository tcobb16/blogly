from unittest import TestCase
from mock import patch
from models import db, User
from flask import Flask
from app import show_user, edit_user, delete_user, new_user


class AppTest(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.app=Flask(__name__)
        db.init_app(self.app)
        with self.app.app_context():
            db.create_all()

    def tearDown(self) -> None:
        super().tearDown()
        self.app=Flask(__name__)
        db.init_app(self.app)
        with self.app.app_context():
            db.drop_all()

    def test_get_users(self):
        new_user = User(
        first_name="John",
        last_name="Smith",
        img_url=None)

        db.session.add(new_user)
        db.session.commit()

        show_user(1)
        with patch("app.render_template") as template_mock:
            self.assertTrue(template_mock.called)


    def test_new_user(self):
        pass

    def test_edit_user(self):
        pass

    def test_delete_user(self):
        pass
