from django.shortcuts import render
from user_report.maigret import get_maigret_data, get_yesitsme_data, get_daprofiler_data


def index(request):

    data = None
    if request.method == "POST":
        user_name = request.POST.get('user_name')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')

        prot_email = str(email).replace(str(email.split("@")[0])[1:-1], '*'*len(str(email.split("@")[0])[1:-1]))
        prot_contact = str(contact).replace(str(contact[:-2]), '*'*len(str(contact[:-2])))

        maigret = get_maigret_data(user_name)
        yesitsme = get_yesitsme_data(first_name, last_name, prot_email, prot_contact)
        daprofiler = get_daprofiler_data(first_name, last_name)

        data = {'error': 200, 'maigret': maigret, 'yesitsme': yesitsme, 'daprofiler': daprofiler}

    else:
        data = {'error': f'Error:- Invalid method call {request.method}'}
    return render(request, "index.html", data)
