APIS DETAIL:
-->Following APIS were created performing various request:

1)TO Get the list of all the pizza stored in the database:(In urls.py: path('api/v1/pizza_list/', views.pizza_List))
-->API CREATED: localhost:8000/api/v1/pizza_list/
-->RESPONSE RECEIVED:
[
    {
        "id": 1,
        "pid": "p1",
        "type": "Regular",
        "size": "Small",
        "toppings": "Onion"
    },
    {
        "id": 2,
        "pid": "p2",
        "type": "Square",
        "size": "Medium",
        "toppings": "Capsicum"
    },
    {
        "id": 3,
        "pid": "p3",
        "type": "Regular",
        "size": "Large",
        "toppings": "OnionandPanner"
    }
]

2)To create Pizza of size which already exits in the database and which is of type either 'Regular' or 'Square':(In urls.py: path('api/v1/pizza_list/<int:pk>/', views.pizza_Detail))
-->APIS CREATED: localhost:8000/api/v1/pizza_list/
-->RESPONSE:
{
    "id": 15,
    "pid": "p4",
    "type": "Regular",
    "size": "Small",
    "toppings": "Paneer"
}

3)To Get,Edit or Delete a particular pizza based on its id
-->API CREATED: 3.1)localhost:8000/api/v1/pizza_list/1          (GET)
                3.2)localhost:8000/api/v1/pizza_list/3/         (UPDATE)
                3.3)localhost:8000/api/v1/pizza_list/3/         (DELETE)

-->RESPONSE:
{
    "id": 1,
    "pid": "p1",                    (GET)
    "type": "Regular",
    "size": "Small",
    "toppings": "Onion"
}                
------------------------------------------------
{
    "id": 3,
    "pid": "p4",                    (UPDATE)
    "type": "Regular",
    "size": "Medium",
    "toppings": "Panner"
}
--------------------------------------------------
                                    (DELETE)
--------------------------------------------------


3)To filter the pizza based on the size and type: (In urls.py: path('api/v1/pizza_list/<slug:ty>/<slug:si>/', views.pizza_size_and_type))
-->API CREATED: localhost:8000/api/v1/pizza_list/Regular/Small/
-->RESPONSE:
[
    {
        "id": 1,
        "pid": "p1",
        "type": "Regular",
        "size": "Small",
        "toppings": "Onion"
    },
    {
        "id": 15,
        "pid": "p4", 
        "type": "Regular",
        "size": "Small",
        "toppings": "Paneer"
    }
]

STEPS TO RUN THE PROJECT:
1) Install virtualenvwrapper if it is not installed in PC using command:
    pip install virtualenvwrapper-win
    
2)Create your own virtual env using command:
    mkvirtualenv your_env_name
    
3)Now you will be inside your own created virtual env or not then use command
    workon your_env_name 
        to activate the virtual env
        
4)Now clone the project in the virtual env using command: 
    git clone repo_link
    
5)Install project requirements libraries using command:
    pip install -r requirements.txt
 
6)Update the settings.py to configure it to your local postgresql settings:
    DATABASES = {
         'default': {
        'ENGINE': 'django.db.backends.postgresql',
         'NAME': name_of_your_database,
        'USERNAME': username_in_postgres,
        'PASSWORD': password_in_postgres,
        'HOST': 'localhost' for the PC running locally or if hosted on web then its URL 
    }
}

8)Migrations are done to setup the project and create required tables:
cmd1: python manage.py makemigratons
cmd2:python manage.py migrate

7)Create superuser using command to access admin panel:
    python manage.py createsuperuser

8) Add data from Admin or directly from database intially to get some datas intitally because initially we cannot post request as there must be already some pizzas of the same size 
to create a post request

9) Now simply use the apis to perform any CRUD operations you like along with some filtering on the basis of size and type using apis

