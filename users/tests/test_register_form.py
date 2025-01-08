from django.test import TestCase
from users.forms import RegisterForm
from parameterized import parameterized
from django.core.exceptions import ValidationError

class RegisterFormTestCase(TestCase):
    def setUp(self):
        self.form_data = {
            'username': 'testuser',
            'email': 'testuser@email.com',
            'first_name': 'Carl',
            'last_name': 'Sagan',
            'password': 'Test1234',
            'password2': 'Test1234',
        }
        self.form = RegisterForm(data=self.form_data)

    @parameterized.expand([
        ('username','Your username'),
        ('email','Your e-mail'),
        ('first_name','Ex.: Carl'),
        ('last_name','Ex.: Sagan'),
        ('password','Type your password'),
        ('password2','Repeat your password'),
    ])
    def test_placeholders(self, field, placeholder):
        fields_placeholder = self.form.fields[field].widget.attrs.get('placeholder')
        self.assertEqual(fields_placeholder, placeholder)

    def test_email_is_unique(self):
        user = self.form.save()
        user.email = 'testuser@email.com'
        user.save()
        form2 = RegisterForm(data={
            'username': 'testuser2', 
            'email': 'testuser@email.com',
            'first_name': 'Carl',
            'last_name': 'Sagan',
            'password': 'Test1234',
            'password2': 'Test1234',
        })
        self.assertEqual({'email': ['This email is already in use']}, form2.errors)
    def test_passwords_ere_equal(self):
        form2 = RegisterForm(data={
            'username': 'testuser2', 
            'email': 'testuser@email.com',
            'first_name': 'Carl',
            'last_name': 'Sagan',
            'password': 'Test1234',
            'password2': 'DifferentPassword1234',
        })
        
        self.assertFalse(form2.is_valid()) 
        self.assertIn('The passwords must be equal', form2.errors.get('password', []))
        self.assertIn('The passwords must be equal', form2.errors.get('password2', []))