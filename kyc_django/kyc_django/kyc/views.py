import smtplib
import random
import urllib
from email.message import EmailMessage

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Kyc_Info, Kyc_Infotemp, Id_Info, Image, Kyc_Reject
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError
from .forms import update_forms, accept_form, ImageForm, reject_forms
# import alert

# import alert
#
# if __name__ == '__main__':
#     alert.email_alert("password", "in kyc", "dmhashanmd@gmail.com")
#
#



# define method for calling pages
# -----------------------------------------------------------------------------------------------------------------------


def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = "kyc064810@gmail.com"
    msg['from'] = user
    password = "qtmwyfuyknyvvtag"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()



def index(request):
    return render(request, 'kyc/index.html')

def verify(request):

    # if request.session.get('id'):

    # id = format(request.session.get('id'))

    # if request.GET[id]:
    # id=request.GET['id']
    if request.method == "POST":
        input_number = request.POST["code"]
        
        print(input_number)
        
        if Kyc_Infotemp.objects.filter(email_add_verification=input_number).exists():
            
            messages.success(request, "verified sucessfully")
            return render(request, "kyc/search.html")

        else:
            messages.error(request, "Invalid code, Please enter the received code")

        

    """dbObj = Kyc_Infotemp.objects.get(id=id)
    dbNum = dbObj.email_add_verification
    emNum = request.GET["ecode"]
    if(dbNum==emNum):
        Kyc_Infotemp.objects.filter(id=id).update(email_add_verification='verifiede')
        print("ok")
        return render(request,'kyc/ok.html')"""
    return render(request, "kyc/verify.html")

def verify2(request):

    # # if request.session.get('id'):
    #
    # # id = format(request.session.get('id'))
    #
    # # if request.GET[id]:
    # id=request.GET['id']
    #
    # dbObj = Kyc_Infotemp.objects.get(id=id)
    # dbNum = dbObj.email_add_verification
    # emNum = request.GET["ecode"]
    # if(dbNum==emNum):
    #     Kyc_Infotemp.objects.filter(id=id).update(email_add_verification='verifiede')
    #     print("ok")
    messages.success(request, 'Mobile number verified')
    return render(request,'kyc/index.html')

def account(request):
    return render(request, 'kyc/(2nd)AccEmp.html')


def personal(request):
    return render(request, 'kyc/(3rd)Declaration.html')


def office(request):
    return render(request, 'kyc/(4th)office.html')


# defining function to filter and display flagged records in update.html
def update(request):
    result = Kyc_Infotemp.objects.filter(green_flag_temp=True)
    result2 = Kyc_Infotemp.objects.filter(blue_flag_temp=True)
    result3 = Kyc_Infotemp.objects.filter(red_flag_temp=True)
    result4 = Kyc_Infotemp.objects.filter(red_flag_temp=False, blue_flag_temp=False, green_flag_temp=False)
    productnames = Kyc_Infotemp.objects.all()

    # get the form output using get method
    if request.method == 'GET':
        p = request.GET.getlist('select_user')
        # print(p)
        # k = request.GET('parameters[]')
        productnames = Kyc_Infotemp.objects.all()
        context = {
            "Kyc_Infotemp1": result, "Kyc_Infotemp2": result2,
            "Kyc_Infotemp3": result3, "Kyc_Infotemp4": result4,
            'userList': p, 'all_info': productnames,
        }

    else:

        context = {
            "Kyc_Infotemp1": result, "Kyc_Infotemp2": result2,
            "Kyc_Infotemp3": result3, "Kyc_Infotemp4": result4,
            "all_info": productnames,
        }
    # passing variables to the update.html using dictionary
    return render(request, "kyc/update.html", context)


# this was defined to check a branch of a program only for devoloping purposes
def productList(request):
    if request.method == 'GET':
        p = request.GET.getlist('select_user')
        print(p)
        # k = request.GET('parameters[]')
        productnames = Kyc_Infotemp.objects.all()
        context = {
            'userList': p, 'all_info': productnames,
        }
        # --- logic later for chart ------

    return render(request, 'kyc/select.html', context)


# defining function to get records using id through the database and display in editing
def edit_val(request, id):
    update_val = Kyc_Infotemp.objects.get(id=id)

    return render(request, "kyc/edit.html", {"Kyc_Infotemp": update_val})


# defining database update function when click on update button
def update_data(request, id):
    if request.method == 'POST' and 'update_db' in request.POST:

        updates_data = Kyc_Infotemp.objects.get(id=id)
        form = update_forms(request.POST, instance=updates_data)

        rejected_temp = request.POST["rejected_temp"]

        if rejected_temp == 'reject_val':

            salutation = request.POST["salutation_temp"]
            full_name = request.POST["full_name_temp"]
            name_init = request.POST["name_init_temp"]
            profile_pic = request.POST["profile_pic_temp"]
            live_video = request.POST["live_video_temp"]
            id_type = request.POST["id_type_temp"]

            try:
                nics_no = request.POST["nics_no_temp"]
                date_of_birth = request.POST["date_of_birth_temp"]
            except MultiValueDictKeyError:
                nics_no = ''
                date_of_birth = ''

            try:
                drive_lic = request.POST.get("driv_lic_temp")
                driv_exp = request.POST["driv_exp_temp"]
            except MultiValueDictKeyError:
                drive_lic = ''
                driv_exp = ''

            try:
                pass_no = request.POST["pass_no_temp"]
                pass_exp = request.POST["pass_exp_temp"]
            except MultiValueDictKeyError:
                pass_no = ''
                pass_exp = ''

            try:
                birth_cernum = request.POST["birth_cernum_temp"]
            except MultiValueDictKeyError:
                birth_cernum = ''

            try:
                post_id = request.POST["post_id_temp"]
            except MultiValueDictKeyError:
                post_id = ''

            try:
                oafsc = request.POST["oafsc_temp"]
            except MultiValueDictKeyError:
                oafsc = ''

            try:
                visa_copy = request.POST["visa_copy_temp"]
            except MultiValueDictKeyError:
                visa_copy = ''

            try:
                othe_identity_doc = request.POST["othe_identity_doc_temp"]
            except MultiValueDictKeyError:
                othe_identity_doc = ''

            nationality = request.POST["nationality_temp"]

            try:
                nationality_other = request.POST["nationality_other_temp"]
                type_of_visa = request.POST["type_of_visa_temp"]
                visa_exp = request.POST["visa_exp_temp"]
                other_types = request.POST["other_types_temp"]
                other_exp = request.POST["other_exp_temp"]
                foreign_addre = request.POST["foreign_addre_temp"]

            except MultiValueDictKeyError:
                nationality_other = ''
                type_of_visa = ''
                visa_exp = ''
                other_types = ''
                other_exp = ''
                foreign_addre = ''

            vari_doc_type = request.POST["vari_doc_type_temp"]
            vari_doc = request.POST["vari_doc_temp"]
            pep_person = request.POST["pep_person_temp"]
            us_city = request.POST["us_city_temp"]

            # calling variables for form inputs in residential detail section
            resident_sri = request.POST["resident_sri_temp"]

            try:
                country_resident = request.POST["country_resident_temp"]
            except MultiValueDictKeyError:
                country_resident = ''

            house_no_per = request.POST["house_no_per_temp"]
            street_per = request.POST["street_per_temp"]
            city_per = request.POST["city_per_temp"]
            postal_code_per = request.POST["postal_code_per_temp"]

            house_no = request.POST["house_no_temp"]
            street = request.POST["street_temp"]
            city = request.POST["city_temp"]
            postal_code = request.POST["postal_code_temp"]
            state_address = request.POST["state_address_temp"]

                    # calling variables for form inputs in contact detail section
            mob_no = request.POST["mob_no_temp"]
            office_num = request.POST["office_num_temp"]
            home_num = request.POST["home_num_temp"]
            email_add = request.POST["email_add_temp"]
            email_add_verification = request.POST["email_add_verification"]

            date_now_temp = request.POST["date_now_temp"]
            staff_member_temp = request.POST["staff_member_temp"]
            file_note_temp = request.POST["file_note_temp"]
            file_attachment_temp = request.POST["file_attachment_temp"]
            reason_for_rej_temp = request.POST["reason_for_rej_temp"]
            rejected_temp = request.POST["rejected_temp"]
            flag_1 = request.POST["red_flag_temp"]
            flag_2 = request.POST["green_flag_temp"]
            flag_3 = request.POST["blue_flag_temp"]

            submit_kyc_temp = Kyc_Reject(salutation_temp=salutation, full_name_temp=full_name,
                                        name_init_temp=name_init, profile_pic_temp=profile_pic,
                                        live_video_temp=live_video,
                                        id_type_temp=id_type,
                                        nics_no_temp=nics_no, date_of_birth_temp=date_of_birth,
                                        driv_lic_temp=drive_lic, driv_exp_temp=driv_exp,
                                        pass_no_temp=pass_no, pass_exp_temp=pass_exp,
                                        birth_cernum_temp=birth_cernum,
                                        post_id_temp=post_id, oafsc_temp=oafsc, visa_copy_temp=visa_copy,
                                        othe_identity_doc_temp=othe_identity_doc,
                                        nationality_temp=nationality,
                                        nationality_other_temp=nationality_other,
                                        type_of_visa_temp=type_of_visa,
                                        visa_exp_temp=visa_exp, other_types_temp=other_types,
                                        other_exp_temp=other_exp, foreign_addre_temp=foreign_addre,
                                        vari_doc_type_temp=vari_doc_type, vari_doc_temp=vari_doc,
                                        pep_person_temp=pep_person,
                                        us_city_temp=us_city,
                                        resident_sri_temp=resident_sri,
                                        country_resident_temp=country_resident,
                                        house_no_temp=house_no, street_temp=street, city_temp=city,
                                        postal_code_temp=postal_code, state_address_temp=state_address,
                                        house_no_per_temp=house_no_per, street_per_temp=street_per,
                                        city_per_temp=city_per, postal_code_per_temp=postal_code_per,
                                        mob_no_temp=mob_no, office_num_temp=office_num,
                                        home_num_temp=home_num, email_add_verification=email_add_verification,
                                        email_add_temp=email_add, red_flag_temp=flag_1,
                                        green_flag_temp=flag_2, blue_flag_temp=flag_3, date_now_temp=date_now_temp,
                                        staff_member_temp=staff_member_temp, file_note_temp=file_note_temp,
                                        reason_for_rej_temp=reason_for_rej_temp, rejected_temp=rejected_temp,
                                        file_attachment_temp=file_attachment_temp)

                    
            submit_kyc_temp.save()
            Kyc_Infotemp.objects.filter(id=id).delete()
            messages.success(request, 'successfully submitted')
            result = Kyc_Infotemp.objects.filter(green_flag_temp=True)
            result2 = Kyc_Infotemp.objects.filter(blue_flag_temp=True)
            result3 = Kyc_Infotemp.objects.filter(red_flag_temp=True)
            result4 = Kyc_Infotemp.objects.filter(red_flag_temp=False, blue_flag_temp=False, green_flag_temp=False)
            productnames = Kyc_Infotemp.objects.all()

            # get the form output using get method
            if request.method == 'GET':
                p = request.GET.getlist('select_user')
                # print(p)
                # k = request.GET('parameters[]')
                productnames = Kyc_Infotemp.objects.all()
                context = {
                    "Kyc_Infotemp1": result, "Kyc_Infotemp2": result2,
                    "Kyc_Infotemp3": result3, "Kyc_Infotemp4": result4,
                    'userList': p, 'all_info': productnames,
                }

            else:

                context = {
                    "Kyc_Infotemp1": result, "Kyc_Infotemp2": result2,
                    "Kyc_Infotemp3": result3, "Kyc_Infotemp4": result4,
                    "all_info": productnames,
                }
            # passing variables to the update.html using dictionary
            return render(request, "kyc/update.html", context)
        
        else:

            updates_data = Kyc_Infotemp.objects.get(id=id)
            form = update_forms(request.POST, instance=updates_data)

            # print(form.errors)

            # print(updates_data)

            print(form.is_valid())

            if form.is_valid():
                form.save()
                messages.warning(request, "record update sucessfully, please select Reject before rejecting")
                return render(request, "kyc/edit.html", {"Kyc_Infotemp": updates_data})

    if request.method == 'POST' and 'accept_rec' in request.POST:

        new_entry = request.POST["nics_no_temp"]
        flag_1 = request.POST["red_flag_temp"]
        flag_2 = request.POST["green_flag_temp"]
        flag_3 = request.POST["blue_flag_temp"]

        if Kyc_Info.objects.filter(nics_no_temp=new_entry).exists():

            place = Kyc_Info.objects.get(nics_no_temp=new_entry)
            updates_origin = Kyc_Info.objects.get(id=place.id)

            if (flag_1 == 'False' and flag_2 == 'False' and flag_3 == 'False'):
                form = accept_form(request.POST, instance=updates_origin)

                if form.is_valid():
                    form.save()

                    updates_data = Kyc_Infotemp.objects.get(id=id)
                    form = update_forms(request.POST, instance=updates_data)
                    # Kyc_Infotemp.objects.filter(id=id).delete()
                    Kyc_Infotemp.objects.filter(id=id).delete()

                    result = Kyc_Infotemp.objects.filter(green_flag_temp=True)
                    result2 = Kyc_Infotemp.objects.filter(blue_flag_temp=True)
                    result3 = Kyc_Infotemp.objects.filter(red_flag_temp=True)
                    result4 = Kyc_Infotemp.objects.filter(red_flag_temp=False, blue_flag_temp=False, green_flag_temp=False)
                    productnames = Kyc_Infotemp.objects.all()

                    # get the form output using get method
                    if request.method == 'GET':
                        p = request.GET.getlist('select_user')
                        # print(p)
                        # k = request.GET('parameters[]')
                        productnames = Kyc_Infotemp.objects.all()
                        context = {
                            "Kyc_Infotemp1": result, "Kyc_Infotemp2": result2,
                            "Kyc_Infotemp3": result3, "Kyc_Infotemp4": result4,
                            'userList': p, 'all_info': productnames,
                        }

                    else:

                        context = {
                            "Kyc_Infotemp1": result, "Kyc_Infotemp2": result2,
                            "Kyc_Infotemp3": result3, "Kyc_Infotemp4": result4,
                            "all_info": productnames,
                        }
                    # passing variables to the update.html using dictionary
                    return render(request, "kyc/update.html", context)


            else:
                updates_data = Kyc_Infotemp.objects.get(id=id)
                form = update_forms(request.POST, instance=updates_data)
                messages.error(request, 'please remove flags before adding to main database')
                return render(request, "kyc/edit.html", {"Kyc_Infotemp": updates_data})

            new_entry = request.POST["salutation_temp"]
            print(new_entry)
        # updates_data = Kyc_Infotemp.objects.get(id=id)
        # form = update_forms(request.POST, instance=updates_data)
        # print(form)
        else:

            if (flag_1 == 'False' and flag_2 == 'False' and flag_3 == 'False'):

                salutation = request.POST["salutation_temp"]
                full_name = request.POST["full_name_temp"]
                name_init = request.POST["name_init_temp"]
                profile_pic = request.POST["profile_pic_temp"]
                live_video = request.POST["live_video_temp"]
                id_type = request.POST["id_type_temp"]

                try:
                    nics_no = request.POST["nics_no_temp"]
                    date_of_birth = request.POST["date_of_birth_temp"]
                except MultiValueDictKeyError:
                    nics_no = ''
                    date_of_birth = ''

                try:
                    drive_lic = request.POST.get("driv_lic_temp")
                    driv_exp = request.POST["driv_exp_temp"]
                except MultiValueDictKeyError:
                    drive_lic = ''
                    driv_exp = ''

                try:
                    pass_no = request.POST["pass_no_temp"]
                    pass_exp = request.POST["pass_exp_temp"]
                except MultiValueDictKeyError:
                    pass_no = ''
                    pass_exp = ''

                try:
                    birth_cernum = request.POST["birth_cernum_temp"]
                except MultiValueDictKeyError:
                    birth_cernum = ''

                try:
                    post_id = request.POST["post_id_temp"]
                except MultiValueDictKeyError:
                    post_id = ''

                try:
                    oafsc = request.POST["oafsc_temp"]
                except MultiValueDictKeyError:
                    oafsc = ''

                try:
                    visa_copy = request.POST["visa_copy_temp"]
                except MultiValueDictKeyError:
                    visa_copy = ''

                try:
                    othe_identity_doc = request.POST["othe_identity_doc_temp"]
                except MultiValueDictKeyError:
                    othe_identity_doc = ''

                nationality = request.POST["nationality_temp"]

                try:
                    nationality_other = request.POST["nationality_other_temp"]
                    type_of_visa = request.POST["type_of_visa_temp"]
                    visa_exp = request.POST["visa_exp_temp"]
                    other_types = request.POST["other_types_temp"]
                    other_exp = request.POST["other_exp_temp"]
                    foreign_addre = request.POST["foreign_addre_temp"]

                except MultiValueDictKeyError:
                    nationality_other = ''
                    type_of_visa = ''
                    visa_exp = ''
                    other_types = ''
                    other_exp = ''
                    foreign_addre = ''

                vari_doc_type = request.POST["vari_doc_type_temp"]
                vari_doc = request.POST["vari_doc_temp"]
                pep_person = request.POST["pep_person_temp"]
                us_city = request.POST["us_city_temp"]

                # calling variables for form inputs in residential detail section
                resident_sri = request.POST["resident_sri_temp"]

                try:
                    country_resident = request.POST["country_resident_temp"]
                except MultiValueDictKeyError:
                    country_resident = ''

                house_no_per = request.POST["house_no_per_temp"]
                street_per = request.POST["street_per_temp"]
                city_per = request.POST["city_per_temp"]
                postal_code_per = request.POST["postal_code_per_temp"]

                house_no = request.POST["house_no_temp"]
                street = request.POST["street_temp"]
                city = request.POST["city_temp"]
                postal_code = request.POST["postal_code_temp"]
                state_address = request.POST["state_address_temp"]

                # calling variables for form inputs in contact detail section
                mob_no = request.POST["mob_no_temp"]
                office_num = request.POST["office_num_temp"]
                home_num = request.POST["home_num_temp"]
                email_add = request.POST["email_add_temp"]
                email_add_verification = request.POST["email_add_verification"]

                submit_kyc_temp = Kyc_Info(salutation_temp=salutation, full_name_temp=full_name,
                                           name_init_temp=name_init, profile_pic_temp=profile_pic,
                                           live_video_temp=live_video,
                                           id_type_temp=id_type,
                                           nics_no_temp=nics_no, date_of_birth_temp=date_of_birth,
                                           driv_lic_temp=drive_lic, driv_exp_temp=driv_exp,
                                           pass_no_temp=pass_no, pass_exp_temp=pass_exp,
                                           birth_cernum_temp=birth_cernum,
                                           post_id_temp=post_id, oafsc_temp=oafsc, visa_copy_temp=visa_copy,
                                           othe_identity_doc_temp=othe_identity_doc,
                                           nationality_temp=nationality,
                                           nationality_other_temp=nationality_other,
                                           type_of_visa_temp=type_of_visa,
                                           visa_exp_temp=visa_exp, other_types_temp=other_types,
                                           other_exp_temp=other_exp, foreign_addre_temp=foreign_addre,
                                           vari_doc_type_temp=vari_doc_type, vari_doc_temp=vari_doc,
                                           pep_person_temp=pep_person,
                                           us_city_temp=us_city,
                                           resident_sri_temp=resident_sri,
                                           country_resident_temp=country_resident,
                                           house_no_temp=house_no, street_temp=street, city_temp=city,
                                           postal_code_temp=postal_code, state_address_temp=state_address,
                                           house_no_per_temp=house_no_per, street_per_temp=street_per,
                                           city_per_temp=city_per, postal_code_per_temp=postal_code_per,
                                           mob_no_temp=mob_no, office_num_temp=office_num,
                                           home_num_temp=home_num, email_add_verification=email_add_verification,
                                           email_add_temp=email_add, red_flag_temp=flag_1,
                                           green_flag_temp=flag_2, blue_flag_temp=flag_3)

                
                submit_kyc_temp.save()
                Kyc_Infotemp.objects.filter(id=id).delete()
                messages.success(request, 'successfully submitted')
                result = Kyc_Infotemp.objects.filter(green_flag_temp=True)
                result2 = Kyc_Infotemp.objects.filter(blue_flag_temp=True)
                result3 = Kyc_Infotemp.objects.filter(red_flag_temp=True)
                result4 = Kyc_Infotemp.objects.filter(red_flag_temp=False, blue_flag_temp=False, green_flag_temp=False)
                productnames = Kyc_Infotemp.objects.all()

                # get the form output using get method
                if request.method == 'GET':
                    p = request.GET.getlist('select_user')
                    # print(p)
                    # k = request.GET('parameters[]')
                    productnames = Kyc_Infotemp.objects.all()
                    context = {
                        "Kyc_Infotemp1": result, "Kyc_Infotemp2": result2,
                        "Kyc_Infotemp3": result3, "Kyc_Infotemp4": result4,
                        'userList': p, 'all_info': productnames,
                    }

                else:

                    context = {
                        "Kyc_Infotemp1": result, "Kyc_Infotemp2": result2,
                        "Kyc_Infotemp3": result3, "Kyc_Infotemp4": result4,
                        "all_info": productnames,
                    }
                # passing variables to the update.html using dictionary
                return render(request, "kyc/update.html", context)

            else:
                updates_data = Kyc_Infotemp.objects.get(id=id)
                form = update_forms(request.POST, instance=updates_data)
                messages.error(request, 'please remove flags before adding to main database')
                return render(request, "kyc/edit.html", {"Kyc_Infotemp": updates_data})



# -----------------------------------------------------------------------------------------------------------------------


# defining method to call accounts page and applying values to the variables
"""def insertkyc1(request):
    # *************variables of second form********************
    global occu_state

    occu_state = request.POST["Occutation_Status"]
    print(occu_state)
    print(full_name)
    print(name_init)

    if Kyc_Info.objects.filter(nics_no=nics_no).exists():
        submit_kyc_temp = Kyc_Infotemp(full_name_temp=full_name, name_init_temp=name_init, id_type_temp=id_type,
                                       nics_no_temp=nics_no, driv_lic_temp=driv_lic,
                                       pass_no_temp=pass_no, nationality_temp=nationality,
                                       nationality_other_temp=nationality_other, house_no_temp=house_no,
                                       street_temp=street,
                                       city_temp=city, mob_no_temp=mob_no, office_num_temp=office_num,
                                       home_num_temp=home_num,
                                       email_add_temp=email_add,
                                       occu_state_temp=occu_state, date_of_birth_temp=date_of_birth,
                                       driv_exp_temp=driv_exp,
                                       green_flag_temp=green_flag, blue_flag_temp=blue_flag, profile_pic=profile_pic)
        submit_kyc_temp.save()
        messages.success(request, 'saved look')
        return render(request, 'kyc/(2nd)AccEmp.html')

    else:

        if Id_Info.objects.filter(nic_no=nics_no, name_full=full_name, birth_day=date_of_birth,
                                  house_num=house_no,
                                  street_add=street, city_ref=city).exists():

            submit_kyc = Kyc_Info(full_name=full_name, name_init=name_init, id_type=id_type, nics_no=nics_no,
                                  driv_lic=driv_lic,
                                  pass_no=pass_no, nationality=nationality,
                                  nationality_other=nationality_other, house_no=house_no, street=street,
                                  city=city, mob_no=mob_no, office_num=office_num, home_num=home_num,
                                  email_add=email_add,
                                  occu_state=occu_state, date_of_birth=date_of_birth, driv_exp=driv_exp, profile_pic=profile_pic)
            submit_kyc.save()
            messages.success(request, 'Successfully saved')

            return render(request, 'kyc/(2nd)AccEmp.html')
        else:

            submit_kyc_temp = Kyc_Infotemp(full_name_temp=full_name, name_init_temp=name_init, id_type_temp=id_type,
                                           nics_no_temp=nics_no, driv_lic_temp=driv_lic,
                                           pass_no_temp=pass_no, nationality_temp=nationality,
                                           nationality_other_temp=nationality_other, house_no_temp=house_no,
                                           street_temp=street,
                                           city_temp=city, mob_no_temp=mob_no, office_num_temp=office_num,
                                           home_num_temp=home_num,
                                           email_add_temp=email_add,
                                           occu_state_temp=occu_state, date_of_birth_temp=date_of_birth,
                                           driv_exp_temp=driv_exp, red_flag_temp=red_flag,
                                           green_flag_temp=green_flag, blue_flag_temp=blue_flag)
            submit_kyc_temp.save()
            messages.success(request, 'saved look')
            return render(request, 'kyc/(2nd)AccEmp.html')"""
# def verify(request):


def insertkyc(request):
    print("successfully completed")


    # definging global variables
    # -----------------------------------------------------------------------------------------------------------------------

    # ***************** variables of personal information first form ***************

    global salutation, full_name, name_init, profile_pic, id_type, nics_no, date_of_birth, drive_lic, driv_exp, pass_no, pass_exp
    global birth_cernum, post_id, oafsc, visa_copy, othe_identity_doc, nationality, nationality_other, type_of_visa, visa_exp
    global other_types, other_exp, foreign_addre, vari_doc_type, vari_doc, pep_person, us_city

    # global full_name_temp, name_init_temp, date_of_birth_temp

    # variables of residential details
    global resident_sri, country_resident, house_no, street, city, postal_code, state_address, house_no_per, street_per
    global city_per, postal_code_per

    # variables of contact information
    global mob_no, office_num, home_num, email_add

    # variable for flags
    global green_flag, blue_flag, red_flag
    green_flag = False
    blue_flag = False
    red_flag = False

    # calling variables for form inputs in personal detail section
    salutation = request.POST["salutation"]
    full_name = request.POST["fullname"]
    name_init = request.POST["name_init"]
    profile_pic = request.FILES["self_nic"]
    live_video = request.FILES["live_video"]
    id_type = request.POST["id_types"]

    try:
        nics_no = request.POST["nic_no"]
        date_of_birth = request.POST["birth_day"]
    except MultiValueDictKeyError:
        nics_no = ''
        date_of_birth = ''

    try:
        drive_lic = request.POST.get("drive_lice")
        driv_exp = request.POST["drive_exp"]
    except MultiValueDictKeyError:
        drive_lic = ''
        driv_exp = ''

    try:
        pass_no = request.POST["passport_num"]
        pass_exp = request.POST["passport_exp"]
    except MultiValueDictKeyError:
        pass_no = ''
        pass_exp = ''

    try:
        birth_cernum = request.POST["birth_certi"]
    except MultiValueDictKeyError:
        birth_cernum = ''

    try:
        post_id = request.POST["postal_iden"]
    except MultiValueDictKeyError:
        post_id = ''

    try:
        oafsc = request.POST["oafsc"]
    except MultiValueDictKeyError:
        oafsc = ''

    try:
        visa_copy = request.POST["img_visa"]
    except MultiValueDictKeyError:
        visa_copy = ''

    try:
        othe_identity_doc = request.POST["img_other"]
    except MultiValueDictKeyError:
        othe_identity_doc = ''

    nationality = request.POST["nationality"]

    try:
        nationality_other = request.POST["nationality_other"]
        type_of_visa = request.POST["visa_type"]
        visa_exp = request.POST["visa_exp"]
        other_types = request.POST["type_of_visa"]
        other_exp = request.POST["visa_other_exp"]
        foreign_addre = request.POST["foreign_address"]

    except MultiValueDictKeyError:
        nationality_other = ''
        type_of_visa = ''
        visa_exp = ''
        other_types = ''
        other_exp = ''
        foreign_addre = ''

    vari_doc_type = request.POST["Verification_addres"]
    vari_doc = request.FILES["vari_image"]
    pep_person = request.POST["pep"]
    us_city = request.POST["us_city"]

    # calling variables for form inputs in residential detail section
    resident_sri = request.POST["residence_sri"]

    try:
        country_resident = request.POST["resident_contry"]
    except MultiValueDictKeyError:
        country_resident = ''

    house_no_per = request.POST["house_number_per"]
    street_per = request.POST["street_per"]
    city_per = request.POST["city_per"]
    postal_code_per = request.POST["postal_code_per"]

    house_no = request.POST["house_number"]
    street = request.POST["street"]
    city = request.POST["city"]
    postal_code = request.POST["postal_code"]
    state_address = request.POST["state_of_address"]

    # calling variables for form inputs in contact detail section
    mob_no = request.POST["mobile_number"]
    office_num = request.POST["office_number"]
    home_num = request.POST["home_number"]
    email_add = request.POST["email_add"]
    email_add_verification=round(100000*random.random())
    masegEmail = "you submit kyc information success\n"
    codeEmail = str(email_add_verification)





    # checking is there ID exists in Identity information database
    if Id_Info.objects.filter(nic_no=nics_no).exists():

        # if exists id number proceed to next step
        #messages.success(request, 'NIC validated successfully')

        # check whether there are existing kyc in the database to the given id number
        if Kyc_Infotemp.objects.filter(nics_no_temp=nics_no).exists():

            # if true for existing kyc
            # messages.success(request, 'existing kyc')

            # check whether the full name is similar to id info database
            if Id_Info.objects.filter(nic_no=nics_no, name_full=full_name).exists():

                # return to next page
                # return render(request, 'kyc/(2nd)AccEmp.html')

                # give an message if name is true
                # messages.success(request, 'existing kyc, name true')

                # check if birthday is true according to id info database
                if Id_Info.objects.filter(nic_no=nics_no, name_full=full_name, birth_day=date_of_birth).exists():

                    # giving a message if dob is true
                    # messages.success(request, 'existing kyc, name true,dob ture')

                    if Id_Info.objects.filter(nic_no=nics_no, name_full=full_name, birth_day=date_of_birth,
                                              house_num=house_no,
                                              street_add=street, city_ref=city).exists():
                        green_flag = 'True'

                        #messages.success(request, 'existing kyc, name true, dob ture, address true')

                        submit_kyc_temp = Kyc_Infotemp(salutation_temp=salutation, full_name_temp=full_name,
                                                       name_init_temp=name_init, profile_pic_temp=profile_pic,
                                                       live_video_temp=live_video,
                                                       id_type_temp=id_type,
                                                       nics_no_temp=nics_no, date_of_birth_temp=date_of_birth,
                                                       driv_lic_temp=drive_lic, driv_exp_temp=driv_exp,
                                                       pass_no_temp=pass_no, pass_exp_temp=pass_exp,
                                                       birth_cernum_temp=birth_cernum,
                                                       post_id_temp=post_id, oafsc_temp=oafsc, visa_copy_temp=visa_copy,
                                                       othe_identity_doc_temp=othe_identity_doc,
                                                       nationality_temp=nationality,
                                                       nationality_other_temp=nationality_other,
                                                       type_of_visa_temp=type_of_visa,
                                                       visa_exp_temp=visa_exp, other_types_temp=other_types,
                                                       other_exp_temp=other_exp, foreign_addre_temp=foreign_addre,
                                                       vari_doc_type_temp=vari_doc_type, vari_doc_temp=vari_doc,
                                                       pep_person_temp=pep_person,
                                                       us_city_temp=us_city,
                                                       resident_sri_temp=resident_sri,
                                                       country_resident_temp=country_resident,
                                                       house_no_temp=house_no, street_temp=street, city_temp=city,
                                                       postal_code_temp=postal_code, state_address_temp=state_address,
                                                       house_no_per_temp=house_no_per, street_per_temp=street_per,
                                                       city_per_temp=city_per, postal_code_per_temp=postal_code_per,
                                                       mob_no_temp=mob_no, office_num_temp=office_num,
                                                       home_num_temp=home_num,
                                                       email_add_temp=email_add,
                                                       email_add_verification=email_add_verification, red_flag_temp=red_flag,
                                                       green_flag_temp=green_flag, blue_flag_temp=blue_flag)
                        submit_kyc_temp.save()
                        messages.success(request, 'successfully submitted, Document is processing')
                        idS =  str(submit_kyc_temp.id)
                        request.session['id'] = submit_kyc_temp.id

                        email_alert("BANK", masegEmail + "http://127.0.0.1:8000/verify?ecode=" + codeEmail + "&id=" + idS, email_add)

                        return render(request, 'kyc/verify.html')
                        print(green_flag)

                    else:

                        """messages.warning(request, 'existing kyc, name true,dob true, address false attach proof '
                                                  'document')"""

                        blue_flag = 'True'
                        submit_kyc_temp = Kyc_Infotemp(salutation_temp=salutation, full_name_temp=full_name,
                                                       name_init_temp=name_init, profile_pic_temp=profile_pic,
                                                       live_video_temp=live_video,
                                                       id_type_temp=id_type,
                                                       nics_no_temp=nics_no, date_of_birth_temp=date_of_birth,
                                                       driv_lic_temp=drive_lic, driv_exp_temp=driv_exp,
                                                       pass_no_temp=pass_no, pass_exp_temp=pass_exp,
                                                       birth_cernum_temp=birth_cernum,
                                                       post_id_temp=post_id, oafsc_temp=oafsc, visa_copy_temp=visa_copy,
                                                       othe_identity_doc_temp=othe_identity_doc,
                                                       nationality_temp=nationality,
                                                       nationality_other_temp=nationality_other,
                                                       type_of_visa_temp=type_of_visa,
                                                       visa_exp_temp=visa_exp, other_types_temp=other_types,
                                                       other_exp_temp=other_exp, foreign_addre_temp=foreign_addre,
                                                       vari_doc_type_temp=vari_doc_type, vari_doc_temp=vari_doc,
                                                       pep_person_temp=pep_person,
                                                       us_city_temp=us_city,
                                                       resident_sri_temp=resident_sri,
                                                       country_resident_temp=country_resident,
                                                       house_no_temp=house_no, street_temp=street, city_temp=city,
                                                       postal_code_temp=postal_code, state_address_temp=state_address,
                                                       house_no_per_temp=house_no_per, street_per_temp=street_per,
                                                       city_per_temp=city_per, postal_code_per_temp=postal_code_per,
                                                       mob_no_temp=mob_no, office_num_temp=office_num,
                                                       home_num_temp=home_num,
                                                       email_add_temp=email_add,
                                                       email_add_verification=email_add_verification, red_flag_temp=red_flag,
                                                       green_flag_temp=green_flag, blue_flag_temp=blue_flag)
                        submit_kyc_temp.save()
                        messages.success(request, 'Submitted successfully, processing')
                        idS =  str(submit_kyc_temp.id)
                        request.session['id'] = submit_kyc_temp.id

                        email_alert("BANK", masegEmail + "http://127.0.0.1:8000/verify?ecode=" + codeEmail + "&id=" + idS, email_add)

                        return render(request, 'kyc/verify.html')

                # if date of birth is false
                else:
                    # give an error message
                    messages.error(request, 'Date of birth is invalid, please check again')
                    return render(request, 'kyc/verify.html')
            else:
                # give an message if name is false
                messages.error(request, 'Invalid name, please check again')
                return render(request, 'kyc/verify.html')

        else:

            print(drive_lic)
            print(driv_exp)
            print(id_type)
            print(nics_no)
            print(date_of_birth)
            # print(driv_exp)

            # check whether the full name is similar to id info database
            if Id_Info.objects.filter(nic_no=nics_no, name_full=full_name).exists():

                # return to next page
                # return render(request, 'kyc/(2nd)AccEmp.html')

                # give an message if name is true
                # messages.success(request, 'no kyc, name true')

                # check if birthday is true according to id info database
                if Id_Info.objects.filter(nic_no=nics_no, name_full=full_name, birth_day=date_of_birth).exists():

                    # giving a message if dob is true
                    # messages.success(request, 'no kyc, name true,dob ture')

                    if Id_Info.objects.filter(nic_no=nics_no, name_full=full_name, birth_day=date_of_birth,
                                              house_num=house_no,
                                              street_add=street, city_ref=city).exists():

                        #messages.success(request, 'no kyc, name true, dob ture, address true')

                        submit_kyc_temp = Kyc_Infotemp(salutation_temp=salutation, full_name_temp=full_name,
                                                       name_init_temp=name_init, profile_pic_temp=profile_pic,
                                                       live_video_temp=live_video,
                                                       id_type_temp=id_type,
                                                       nics_no_temp=nics_no, date_of_birth_temp=date_of_birth,
                                                       driv_lic_temp=drive_lic, driv_exp_temp=driv_exp,
                                                       pass_no_temp=pass_no, pass_exp_temp=pass_exp,
                                                       birth_cernum_temp=birth_cernum,
                                                       post_id_temp=post_id, oafsc_temp=oafsc, visa_copy_temp=visa_copy,
                                                       othe_identity_doc_temp=othe_identity_doc,
                                                       nationality_temp=nationality,
                                                       nationality_other_temp=nationality_other,
                                                       type_of_visa_temp=type_of_visa,
                                                       visa_exp_temp=visa_exp, other_types_temp=other_types,
                                                       other_exp_temp=other_exp, foreign_addre_temp=foreign_addre,
                                                       vari_doc_type_temp=vari_doc_type, vari_doc_temp=vari_doc,
                                                       pep_person_temp=pep_person,
                                                       us_city_temp=us_city,
                                                       resident_sri_temp=resident_sri,
                                                       country_resident_temp=country_resident,
                                                       house_no_temp=house_no, street_temp=street, city_temp=city,
                                                       postal_code_temp=postal_code, state_address_temp=state_address,
                                                       house_no_per_temp=house_no_per, street_per_temp=street_per,
                                                       city_per_temp=city_per, postal_code_per_temp=postal_code_per,
                                                       mob_no_temp=mob_no, office_num_temp=office_num,
                                                       home_num_temp=home_num,
                                                       email_add_temp=email_add,
                                                       email_add_verification=email_add_verification, red_flag_temp=red_flag,
                                                       green_flag_temp=green_flag, blue_flag_temp=blue_flag)
                        submit_kyc_temp.save()
                        messages.success(request, 'Successfully submitted, Document is processing')
                        idS =  str(submit_kyc_temp.id)
                        request.session['id'] = submit_kyc_temp.id

                        email_alert("BANK", masegEmail + "http://127.0.0.1:8000/verify?ecode=" + codeEmail + "&id=" + idS, email_add)

                        return render(request, 'kyc/verify.html')

                    else:

                        """messages.warning(request, 'no kyc, name true,dob true, address false attach proof '
                                                  'document')"""

                        red_flag = True

                        submit_kyc_temp = Kyc_Infotemp(salutation_temp=salutation, full_name_temp=full_name,
                                                       name_init_temp=name_init, profile_pic_temp=profile_pic,
                                                       live_video_temp=live_video,
                                                       id_type_temp=id_type,
                                                       nics_no_temp=nics_no, date_of_birth_temp=date_of_birth,
                                                       driv_lic_temp=drive_lic, driv_exp_temp=driv_exp,
                                                       pass_no_temp=pass_no, pass_exp_temp=pass_exp,
                                                       birth_cernum_temp=birth_cernum,
                                                       post_id_temp=post_id, oafsc_temp=oafsc, visa_copy_temp=visa_copy,
                                                       othe_identity_doc_temp=othe_identity_doc,
                                                       nationality_temp=nationality,
                                                       nationality_other_temp=nationality_other,
                                                       type_of_visa_temp=type_of_visa,
                                                       visa_exp_temp=visa_exp, other_types_temp=other_types,
                                                       other_exp_temp=other_exp, foreign_addre_temp=foreign_addre,
                                                       vari_doc_type_temp=vari_doc_type, vari_doc_temp=vari_doc,
                                                       pep_person_temp=pep_person,
                                                       us_city_temp=us_city,
                                                       resident_sri_temp=resident_sri,
                                                       country_resident_temp=country_resident,
                                                       house_no_temp=house_no, street_temp=street, city_temp=city,
                                                       postal_code_temp=postal_code, state_address_temp=state_address,
                                                       house_no_per_temp=house_no_per, street_per_temp=street_per,
                                                       city_per_temp=city_per, postal_code_per_temp=postal_code_per,
                                                       mob_no_temp=mob_no, office_num_temp=office_num,
                                                       home_num_temp=home_num,
                                                       email_add_temp=email_add,
                                                       email_add_verification=email_add_verification, red_flag_temp=red_flag,
                                                       green_flag_temp=green_flag, blue_flag_temp=blue_flag)
                        submit_kyc_temp.save()
                        messages.success(request, 'successfully submitted, Document is processing')
                        return render(request, 'kyc/verify.html')




                # If date of birth is false
                else:
                    # give an error message
                    messages.warning(request, 'Invalid date of birth, please check again')
                    return render(request, 'kyc/verify.html')
            else:
                # give an message if name is false
                messages.error(request, 'Invalid name, please check again')
                return render(request, 'kyc/index.html')

            # messages.success(request, 'Successfully submitted')
            # return to next page
            # return render(request, 'kyc/(2nd)AccEmp.html')
            # return render(request, 'kyc/index.html')

    # it there is no id number in id information system give error message
    else:

        messages.error(request, 'Invalid NIC Number. please check again')
        return render(request, 'kyc/verify.html')

    """if request.method=='POST':
        if request.POST.get('ID_type'):
            savekyc = Kyc_info()
            savekyc = request.POST.get('ID_type')
            savekyc.save()
            messages.success(request, 'successful')
            return render(request, 'kyc/index.html')

    else:
        return render(request, 'kyc/index.html')"""

def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'kyc/home.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'kyc/home.html', {'form': form})


def search_val(request):
    if request.method == "POST":
        nic_no = request.POST["nics_no_temp"]

        if Kyc_Info.objects.filter(nics_no_temp=nic_no).exists():
            messages.success(request, 'Successfully load your data')

            
            finded_user = Kyc_Info.objects.get(nics_no_temp=nic_no)
            form = accept_form(request.POST, instance=finded_user)


            #print(finded_user)
            #print(form.errors)
            if form.is_valid():
                print(form.is_valid())
                form.save()
            
            
            
            context = {
                "Kyc_Infotemp": finded_user,
            }


            return render(request, 'kyc/search.html', context)
        else:
            messages.success(request, 'Please fill the above details')
            return render(request, 'kyc/index.html')

    return render(request, 'kyc/search.html')

def update_main(request):
    return render(request, "kyc/update_main.html")