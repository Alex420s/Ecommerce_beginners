# Ecommerce_test

Hi this is a system is implemented using Python’s web framework Django. To develop an e-commerce website, it is necessary to study and understand many technologies. <br>
***
## Prerequisites
>Python=>3.10 
(and requirements.txt for the project)

### Django_examples
Django has a built-in tool that help us deal with the complexities of managing and authenticating users. 
>from django.contrib.auth.models import User
***
Django includes a “signal dispatcher” which helps decoupled applications get notified when actions occur elsewhere in the framework. In a nutshell, signals allow certain senders to notify a set of receivers that some action has taken place. 
>from django.db.models.signals import post_save

The signal needs to be registered so that it is run every time a user signs up
````
from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        import users.signals
````
They’re especially useful when many pieces of code may be interested in the same events. 
***
***Authentication***<br>

writing the logic to enable users to sign up, sign in and sign out of our application. This will require us to write forms, views, URL's and Django templates.
We´re only extending the default code.

````
    class UserForm(UserCreationForm):
	'''
	Form that uses built-in UserCreationForm to handel user creation
	'''
	username = forms.CharField(max_length=150, required=True, widget=forms.TextInput())
	password1 = forms.CharField(required=True, widget=forms.PasswordInput())
	password2 = forms.CharField(required=True, widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'password1', 'password2')
````


***
Django template language gives us access to a whole range of variables, filters and tags that help us add logic to our HTML files.
Sometimes it gets confusing:
````
{% extends 'base/base.html' %}

{% block content %}
<h1>Sign up</h1>
<form method="POST">
    {% csrf_token %}
    {{form.as_p}}
    <button type="submit">Submit!</button>
</form>
<br>
<a href="{% url 'users:sign-in' %}">Sign in</a>
{% endblock %}
````
<!-- But now I know what i´m doing.  -->


## Technologies used in the project: 
* Django framework and SQLite database which comes by default with Django.
* Stripe API 