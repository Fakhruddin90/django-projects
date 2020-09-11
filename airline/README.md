### Press Ctrl + Shift + v to preview the markdown
## Add models to django
1. Go to settings.py in project folder
2. INSTALLED_APPS and add 

## Migration
## django will check any changes in database inside project file
```
python manage.py makemigrations 
```

```
python manage.py sqlmigrate flights 0001
```

## to apply migration to the database(actually creating table inside the database)
```
python manage.py migrate
```

## run python shell
``` python manage.py shell ```

```
>>> from flights.models import Flight
>>> f = Flight(origin="New York", destination="London", duration=415)
>>> f.save()
>>> Flight.objects.all()
<QuerySet [<Flight: Flight object (1)>]>

```

## Admin site
```
python manage.py createsuperuser
```

# 3 Step to add view in django
1. Add the url, what route should happen when user click on the url or enter the route.
2. Create function in views what should the server response from user request.
3. Inside html page, use {{ }} or {% %} to display information.
