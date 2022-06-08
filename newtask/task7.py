#The first thing is to close the server and migrate to the command
#prompt using "python manage.py shell" to migrate to the shell interface

"""
1 INSERTING A NEW RECORD
    To insert a new record, we use the model name imported:
    For example: we can use a variable "" to hold the action
    y= Product(productId="Buerre",Product_id="01", Man_date="08/06/2022", Exp_date="08/08/2022", Trademark="love")
    y.save()


2 GETTING ALL RECORDS
    from task.models import Product
    Then we can assign the output to a variable (x) and print(x) to display our table
    all_records = Product.objects.all()
    all_records to display the values(what is in the field).


3  FILTERING THE PRODUCT BY ITS productId
    product.objects.filter(productId="01")
    

4  GETTING A SINGLE PRODUCT BY ID OR NAME
    one_entry = Product.objects.get(productId=04)
    one_entry to display the values(what is in the field).


"""