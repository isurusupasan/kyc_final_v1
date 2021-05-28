from django.db import models
from datetime import datetime, date
from simple_history.models import HistoricalRecords


# Create your models here.
class Kyc_Info(models.Model):
    salutation_temp = models.CharField(max_length=5)
    full_name_temp = models.CharField(max_length=200)
    name_init_temp = models.CharField(max_length=100)
    profile_pic_temp = models.FileField(upload_to='per/images/id_self/%Y/%m/%d/', null=True, blank=True)
    live_video_temp = models.FileField(upload_to='per/videos/liv_vid/%Y/%m/%d/', null=True)
    id_type_temp = models.CharField(max_length=50)
    nics_no_temp = models.CharField(max_length=50)
    date_of_birth_temp = models.CharField(max_length=20)
    driv_lic_temp = models.CharField(max_length=50, blank=True, null=True)
    driv_exp_temp = models.CharField(max_length=20, blank=True, null=True)
    pass_no_temp = models.CharField(max_length=50, blank=True, null=True)
    pass_exp_temp = models.CharField(max_length=20, blank=True, null=True)
    birth_cernum_temp = models.CharField(max_length=10, blank=True, null=True)
    post_id_temp = models.CharField(max_length=10, blank=True, null=True)
    oafsc_temp = models.CharField(max_length=10, blank=True, null=True)
    visa_copy_temp = models.ImageField(null=True, blank=True, upload_to="per/images/visa_copy/%Y/%m/%d/")
    othe_identity_doc_temp = models.ImageField(null=True, blank=True, upload_to="per/images/other_doc/%Y/%m/%d/")
    nationality_temp = models.CharField(max_length=50)
    nationality_other_temp = models.CharField(max_length=50, blank=True, null=True)
    type_of_visa_temp = models.CharField(max_length=20,blank=True)
    visa_exp_temp = models.CharField(max_length=20, blank=True, null=True)
    other_types_temp = models.CharField(max_length=20,blank=True)
    other_exp_temp = models.CharField(max_length=20, blank=True, null=True)
    foreign_addre_temp = models.CharField(max_length=200, blank=True, null=True)
    vari_doc_type_temp = models.CharField(max_length=200, blank=True, null=True)
    vari_doc_temp = models.ImageField(null=True, blank=True, upload_to="per/images/vari_doc/%Y/%m/%d/")
    pep_person_temp = models.CharField(max_length=200, blank=True, null=True)
    us_city_temp = models.CharField(max_length=200, blank=True, null=True)

    # residential information
    resident_sri_temp = models.CharField(max_length=10, blank=True, null=True)
    country_resident_temp =models.CharField(blank=True, max_length=50)

    # current Address
    house_no_temp = models.CharField(max_length=100)
    street_temp = models.CharField(max_length=100)
    city_temp = models.CharField(max_length=50)
    postal_code_temp = models.CharField(max_length=10, blank=True, null=True)
    state_address_temp = models.CharField(max_length=40, blank=True, null=True)

    # permenent Address
    house_no_per_temp = models.CharField(max_length=100)
    street_per_temp = models.CharField(max_length=100)
    city_per_temp = models.CharField(max_length=50)
    postal_code_per_temp = models.CharField(max_length=10, blank=True, null=True)
    
    # contact infromation
    mob_no_temp = models.CharField(max_length=20)
    office_num_temp = models.CharField(max_length=20, blank=True, null=True)
    home_num_temp = models.CharField(max_length=20, blank=True, null=True)
    email_add_temp = models.CharField(max_length=100, blank=True, null=True)
    email_add_verification = models.CharField(max_length=50, blank=True, null=True)
    red_flag_temp = models.CharField(max_length=5, blank=True, null=True)
    green_flag_temp = models.CharField(max_length=5, blank=True, null=True)
    blue_flag_temp = models.CharField(max_length=5, blank=True, null=True)
    history = HistoricalRecords(excluded_fields=['blue_flag_temp','green_flag_temp','red_flag_temp'])
    profile_rating_temp = models.CharField(max_length=50)

    # rejection /acceptance variables
    

    class Meta:
        db_table = "Kyc_Info"




    """company_name = models.CharField(max_length=50)
    address_full = models.CharField(max_length=250)
    email_add = models.CharField(max_length=250)
    phone_num = models.CharField(max_length=12)
    long_text = models.TextField(max_length=255)"""


    def __str__(self):
        return self.full_name_temp

class Kyc_Infotemp(models.Model):
    
    salutation_temp = models.CharField(max_length=5, null=True, blank=True)
    full_name_temp = models.CharField(max_length=200, null=True, blank=True)
    name_init_temp = models.CharField(max_length=100, null=True, blank=True)
    profile_pic_temp = models.ImageField(upload_to='temp/images/id_self/%Y/%m/%d/', null=True, blank=True)
    live_video_temp = models.FileField(upload_to='temp/videos/liv_vid/%Y/%m/%d/', null=True, blank=True)
    id_type_temp = models.CharField(max_length=50, null=True, blank=True)
    nics_no_temp = models.CharField(max_length=50, null=True, blank=True)
    date_of_birth_temp = models.CharField(max_length=20, null=True, blank=True)
    driv_lic_temp = models.CharField(max_length=50, blank=True, null=True)
    driv_exp_temp = models.CharField(max_length=20, blank=True, null=True)
    pass_no_temp = models.CharField(max_length=50, blank=True, null=True)
    pass_exp_temp = models.CharField(max_length=20, blank=True, null=True)
    birth_cernum_temp = models.CharField(max_length=10, blank=True, null=True)
    post_id_temp = models.CharField(max_length=10, blank=True, null=True)
    oafsc_temp = models.CharField(max_length=10, blank=True, null=True)
    visa_copy_temp = models.ImageField(null=True, blank=True, upload_to="temp/images/visa_copy/%Y/%m/%d/")
    othe_identity_doc_temp = models.ImageField(null=True, blank=True, upload_to="temp/images/other_doc/%Y/%m/%d/")
    nationality_temp = models.CharField(max_length=50, null=True, blank=True)
    nationality_other_temp = models.CharField(max_length=50, blank=True, null=True)
    type_of_visa_temp = models.CharField(max_length=20,blank=True, null=True)
    visa_exp_temp = models.CharField(max_length=20, blank=True, null=True)
    other_types_temp = models.CharField(max_length=20,blank=True)
    other_exp_temp = models.CharField(max_length=20, blank=True, null=True)
    foreign_addre_temp = models.CharField(max_length=200, blank=True, null=True)
    vari_doc_type_temp = models.CharField(max_length=200, blank=True, null=True)
    vari_doc_temp = models.ImageField(null=True, blank=True, upload_to="temp/images/vari_doc/%Y/%m/%d/")
    pep_person_temp = models.CharField(max_length=200, blank=True, null=True)
    us_city_temp = models.CharField(max_length=200, blank=True, null=True)

    # residential information
    resident_sri_temp = models.CharField(max_length=10, blank=True, null=True)
    country_resident_temp =models.CharField(blank=True, max_length=50, null=True)

    # current Address
    house_no_temp = models.CharField(max_length=100, null=True, blank=True)
    street_temp = models.CharField(max_length=100, null=True, blank=True)
    city_temp = models.CharField(max_length=50, null=True, blank=True)
    postal_code_temp = models.CharField(max_length=10, blank=True, null=True)
    state_address_temp = models.CharField(max_length=50, blank=True, null=True)

    # permenent Address
    house_no_per_temp = models.CharField(max_length=100, null=True, blank=True)
    street_per_temp = models.CharField(max_length=100, null=True, blank=True)
    city_per_temp = models.CharField(max_length=50, null=True, blank=True)
    postal_code_per_temp = models.CharField(max_length=10, blank=True, null=True)
    
    # contact infromation
    mob_no_temp = models.CharField(max_length=20)
    office_num_temp = models.CharField(max_length=20, blank=True, null=True)
    home_num_temp = models.CharField(max_length=20, blank=True, null=True)
    email_add_temp = models.CharField(max_length=100, blank=True, null=True)
    email_add_verification = models.CharField(max_length=50, blank=True, null=True)
    red_flag_temp = models.CharField(max_length=5, blank=True, null=True)
    green_flag_temp = models.CharField(max_length=5, blank=True, null=True)
    blue_flag_temp = models.CharField(max_length=5, blank=True, null=True)
    profile_rating_temp = models.CharField(max_length=50, null=True, blank=True)
    
    #flag

    submited_form = models.IntegerField(null=True)
    check_city = models.IntegerField(null=True)
    check_name = models.IntegerField(null=True)
    check_home = models.IntegerField(null=True)
    check_street = models.IntegerField(null=True)

    # rejection acceptance variables

    

    class Meta:
        db_table = "Kyc_Infotemp"
    def __str__(self):
        return self.full_name_temp

class Id_Info(models.Model):
    nic_no = models.CharField(max_length=50)
    name_full = models.CharField(max_length=200)
    birth_day = models.DateField('%Y-%m-%d')
    house_num = models.CharField(max_length=100)
    street_add = models.CharField(max_length=100)
    city_ref = models.CharField(max_length=50)

    def __str__(self):
        return self.name_full


class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title


class Kyc_Reject(models.Model):
    
    salutation_temp = models.CharField(max_length=5)
    full_name_temp = models.CharField(max_length=200)
    name_init_temp = models.CharField(max_length=100)
    profile_pic_temp = models.ImageField(upload_to='rej/images/id_self/%Y/%m/%d/', null=True)
    live_video_temp = models.FileField(upload_to='rej/videos/liv_vid/%Y/%m/%d/', null=True)
    id_type_temp = models.CharField(max_length=50)
    nics_no_temp = models.CharField(max_length=50)
    date_of_birth_temp = models.CharField(max_length=20)
    driv_lic_temp = models.CharField(max_length=50, blank=True, null=True)
    driv_exp_temp = models.CharField(max_length=20, blank=True, null=True)
    pass_no_temp = models.CharField(max_length=50, blank=True, null=True)
    pass_exp_temp = models.CharField(max_length=20, blank=True, null=True)
    birth_cernum_temp = models.CharField(max_length=10, blank=True, null=True)
    post_id_temp = models.CharField(max_length=10, blank=True, null=True)
    oafsc_temp = models.CharField(max_length=10, blank=True, null=True)
    visa_copy_temp = models.ImageField(null=True, blank=True, upload_to="rej/images/visa_copy/%Y/%m/%d/")
    othe_identity_doc_temp = models.ImageField(null=True, blank=True, upload_to="rej/images/other_doc/%Y/%m/%d/")
    nationality_temp = models.CharField(max_length=50)
    nationality_other_temp = models.CharField(max_length=50, blank=True, null=True)
    type_of_visa_temp = models.CharField(max_length=20,blank=True)
    visa_exp_temp = models.CharField(max_length=20, blank=True, null=True)
    other_types_temp = models.CharField(max_length=20,blank=True)
    other_exp_temp = models.CharField(max_length=20, blank=True, null=True)
    foreign_addre_temp = models.CharField(max_length=200, blank=True, null=True)
    vari_doc_type_temp = models.CharField(max_length=200, blank=True, null=True)
    vari_doc_temp = models.ImageField(null=True, blank=True, upload_to="rej/images/vari_doc/%Y/%m/%d/")
    pep_person_temp = models.CharField(max_length=200, blank=True, null=True)
    us_city_temp = models.CharField(max_length=200, blank=True, null=True)

    # residential information
    resident_sri_temp = models.CharField(max_length=10, blank=True, null=True)
    country_resident_temp =models.CharField(blank=True, max_length=50)

    # current Address
    house_no_temp = models.CharField(max_length=100)
    street_temp = models.CharField(max_length=100)
    city_temp = models.CharField(max_length=50)
    postal_code_temp = models.CharField(max_length=10, blank=True, null=True)
    state_address_temp = models.CharField(max_length=50, blank=True, null=True)

    # permenent Address
    house_no_per_temp = models.CharField(max_length=100)
    street_per_temp = models.CharField(max_length=100)
    city_per_temp = models.CharField(max_length=50)
    postal_code_per_temp = models.CharField(max_length=10, blank=True, null=True)
    
    # contact infromation
    mob_no_temp = models.CharField(max_length=20)
    office_num_temp = models.CharField(max_length=20, blank=True, null=True)
    home_num_temp = models.CharField(max_length=20, blank=True, null=True)
    email_add_temp = models.CharField(max_length=100, blank=True, null=True)
    email_add_verification = models.CharField(max_length=50, blank=True, null=True)
    red_flag_temp = models.CharField(max_length=5, blank=True, null=True)
    green_flag_temp = models.CharField(max_length=5, blank=True, null=True)
    blue_flag_temp = models.CharField(max_length=5, blank=True, null=True)
    
    # rejection acceptance variables
    date_now_temp = models.CharField(max_length=150, null=True, blank= True)
    staff_member_temp = models.CharField(null=True, max_length=50, blank=True)
    file_note_temp = models.TextField(max_length=250, null=True, blank=True)
    rejected_temp = models.CharField(max_length=40, null=True, blank=True)
    reason_for_rej_temp = models.CharField(max_length=100, null=True, blank=True)
    file_attachment_temp = models.FileField(upload_to='rej/videos/liv_vid/%Y/%m/%d/', null=True)
    profile_rating_temp = models.CharField(max_length=50)
    

    class Meta:
        db_table = "Kyc_Reject"
    def __str__(self):
        return self.full_name_temp


class Kyc_front(models.Model):

    salutation_temp = models.CharField(max_length=5, null=True, blank=True)
    full_name_temp = models.CharField(max_length=200, null=True, blank=True)
    mob_no_temp = models.CharField(max_length=20, null=True, blank=True)
    office_num_temp = models.CharField(max_length=20, blank=True, null=True)
    home_num_temp = models.CharField(max_length=20, blank=True, null=True)
    email_add_temp = models.CharField(max_length=100, blank=True, null=True)
    email_add_verification = models.CharField(max_length=50, blank=True, null=True)
