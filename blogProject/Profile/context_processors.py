from .models import Contact  # Adjust the import based on your actual model location

def contact_info(request):
    contact_info = Contact.objects.first()  # Assuming you have a model named Contact
    return {"contact_info": contact_info}