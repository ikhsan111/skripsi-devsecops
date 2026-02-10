from django.db import models
from django.db import connection
from django.db import connections
from django.db.models.expressions import RawSQL

value = input()


class MyUser(models.Model):
    name = models.CharField(max_length=200)


def query_my_user(request, params, value):
    with connection.cursor() as cursor:
        cursor.execute("{0}".format(value))  # Sensitive

    # https://docs.djangoproject.com/en/2.1/ref/models/expressions/#raw-sql-expressions

    RawSQL("select col from %s where mycol = %s and othercol = " + value, ("test",))  # Sensitive

    # https://docs.djangoproject.com/en/2.1/ref/models/querysets/#extra

    MyUser.objects.extra(
        select={
            'mycol':  "select col from sometable here mycol = %s and othercol = " + value}, # Sensitive
           select_params=(someparam,),
        },
    )
