from django.shortcuts import render
from hello_app.services.sendmailservice import sendmail
# Create your views here.

def index(request):
    context = {'latest_question_list': ''}
    return render(request, 'index.html', context)

def save_customer(request):
    print(request.POST)
    select_type = request.POST.get('select_type')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    telephone = request.POST.get('telephone')
    car_type = request.POST.get('car_type')
    license_plate = request.POST.get('license_plate')
    agent_name = request.POST.get('agent_name')
    agent_last_name = request.POST.get('agent_last_name')
    remark = request.POST.get('remark')

    subject = "%s" %('รายงานลูกค้า')
    message = "%s %s ของ %s %s สนใจ %s \n ประเภทรภ : %s\n ทะเบียน : %s\n เบอร์โทร : %s \n %s" \
    %(first_name, last_name, agent_name, agent_last_name, select_type,car_type, license_plate, telephone, remark)

    sendmail(subject ,message ,send_to='tongmakchu@gmail.com' )

    context = {'latest_question_list': ''}
    return render(request, 'sample_template.html', context)