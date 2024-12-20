from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        email = 'test@example.com'
        password = 'test@123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        # since the password is hashed we need to use
        # password throuth the hashing sys

    def test_new_user_email_normalized(self):
        sample_emails = [
            ['test1@EXAMPLE.COM', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'samplepwd')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'samplepwd')

    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(
            'test1@example.com',
            'superpwd',
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
