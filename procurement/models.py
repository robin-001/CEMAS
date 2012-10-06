from django.db import models

class ArticleCategoryDetails(models.Model):
    products_id = models.IntegerField(primary_key=True)
    categories_id = models.IntegerField(null=False)
    class Meta:
        db_table = u'article_category_details'

class AssignGrInvoice(models.Model):
    user_gr_invoice_id = models.IntegerField(db_column='User_Gr_Invoice_Id')
    user_id = models.IntegerField(db_column='User_Id')
    gr_invoice_mode = models.CharField(max_length=15, db_column='GR_Invoice_Mode', blank=True)
    class Meta:
        db_table = u'assign_gr_invoice'

class AuditDetails(models.Model):
    user_id = models.IntegerField(null=True, db_column='User_Id', blank=True)
    transaction_mode = models.CharField(max_length=150, db_column='Transaction_Mode', blank=True)
    table_name = models.CharField(max_length=300, db_column='Table_Name', blank=True)
    field_name = models.CharField(max_length=300, db_column='Field_Name', blank=True)
    row_number = models.IntegerField(null=True, db_column='Row_Number', blank=True)
    date_modified = models.DateTimeField(null=True, db_column='Date_Modified', blank=True)
    class Meta:
        db_table = u'audit_details'

class BuyerBillAddress(models.Model):
    buyer_supplier_id = models.IntegerField(db_column='Buyer_Supplier_Id')
    bill_address_name = models.CharField(max_length=765, db_column='Bill_Address_Name')
    bill_mailbox = models.CharField(max_length=150, db_column='Bill_Mailbox', blank=True)
    bill_street = models.CharField(max_length=150, db_column='Bill_Street', blank=True)
    bill_postal_code = models.CharField(max_length=75, db_column='Bill_Postal_Code', blank=True)
    bill_city = models.CharField(max_length=300, db_column='Bill_City', blank=True)
    bill_country = models.CharField(max_length=300, db_column='Bill_Country', blank=True)
    bill_phone_no = models.CharField(max_length=75, db_column='Bill_Phone_No', blank=True)
    bill_mode = models.CharField(max_length=30, db_column='Bill_Mode')
    class Meta:
        db_table = u'buyer_bill_address'

class BuyerCatalogue(models.Model):
    buyer_id = models.IntegerField(db_column='Buyer_Id')
    catalogue_id = models.IntegerField(db_column='Catalogue_Id')
    class Meta:
        db_table = u'buyer_catalogue'

class BuyerDeliveryAddress(models.Model):
    buyer_supplier_id = models.IntegerField(db_column='Buyer_Supplier_Id')
    delivery_address_name = models.CharField(max_length=765, db_column='Delivery_Address_Name')
    delivery_street = models.CharField(max_length=150, db_column='Delivery_Street', blank=True)
    delivery_postal_code = models.CharField(max_length=75, db_column='Delivery_Postal_Code', blank=True)
    delivery_city = models.CharField(max_length=300, db_column='Delivery_City', blank=True)
    delivery_country = models.CharField(max_length=300, db_column='Delivery_Country', blank=True)
    delivery_phone_no = models.CharField(max_length=75, db_column='Delivery_Phone_No', blank=True)
    del_mode = models.CharField(max_length=30, db_column='Del_Mode')
    class Meta:
        db_table = u'buyer_delivery_address'

class BuyerSupplierLogoDetails(models.Model):
    buyer_supplier_id = models.IntegerField(db_column='Buyer_Supplier_Id')
    logo_image_path = models.CharField(max_length=600, db_column='Logo_Image_Path', blank=True)
    logo_mode = models.CharField(max_length=15, db_column='Logo_Mode', blank=True)
    logo_image_type = models.CharField(max_length=135, db_column='Logo_Image_Type')
    logo_image_size = models.IntegerField(db_column='Logo_Image_Size')
    logo_image_name = models.CharField(max_length=765, db_column='Logo_Image_Name')
    class Meta:
        db_table = u'buyer_supplier_logo_details'

class BuyerSupplierSetting(models.Model):
    supplier_id = models.IntegerField(unique=True, db_column='Supplier_Id')
    buyer_id = models.IntegerField(unique=True, db_column='Buyer_Id')
    po_generation_type = models.CharField(max_length=150, db_column='PO_Generation_Type', blank=True)
    class Meta:
        db_table = u'buyer_supplier_setting'

class CatalogueActivate(models.Model):
    buyer_id = models.IntegerField(db_column='Buyer_Id')
    catalogue_id = models.IntegerField(db_column='Catalogue_Id')
    ct_type = models.CharField(max_length=15)
    class Meta:
        db_table = u'catalogue_activate'

class CatalogueApprove(models.Model):
    catalogue_approve_id = models.IntegerField(db_column='Catalogue_Approve_Id')
    buyer_id = models.IntegerField(db_column='Buyer_Id')
    supplier_id = models.IntegerField(db_column='Supplier_Id')
    catalogue_id = models.IntegerField(db_column='Catalogue_Id')
    catalogue_status = models.CharField(max_length=15, db_column='Catalogue_Status', blank=True)
    rejection_reason = models.CharField(max_length=765, db_column='Rejection_reason', blank=True)
    class Meta:
        db_table = u'catalogue_approve'

class CatalogueApproveDetails(models.Model):
    catalogue_approve_id = models.IntegerField(db_column='Catalogue_Approve_Id')
    article_id = models.IntegerField(db_column='Article_Id')
    article_last_price = models.FloatField(null=True, db_column='Article_Last_Price', blank=True)
    article_current_price = models.FloatField(null=True, db_column='Article_Current_Price', blank=True)
    article_price_diff = models.FloatField(null=True, db_column='Article_Price_Diff', blank=True)
    article_rejection_reason = models.CharField(max_length=765, db_column='Article_Rejection_reason', blank=True)
    class Meta:
        db_table = u'catalogue_approve_details'

class CatalogueCostcode(models.Model):
    catalogue_id = models.IntegerField()
    category_id = models.IntegerField(db_column='Category_Id')
    cost_id = models.IntegerField(db_column='Cost_Id')
    ct_mode = models.CharField(max_length=15)
    buyer_id = models.IntegerField(db_column='Buyer_Id')
    class Meta:
        db_table = u'catalogue_costcode'

class CatalogueGroupDetails(models.Model):
    catalogue_group_id = models.IntegerField(db_column='Catalogue_Group_Id')
    catalogue_id = models.IntegerField(db_column='Catalogue_Id')
    class Meta:
        db_table = u'catalogue_group_details'

class CatalogueUpdateDetails(models.Model):
    supplier_id = models.IntegerField(db_column='Supplier_Id')
    catalogue_id = models.IntegerField(db_column='Catalogue_Id')
    update_count = models.IntegerField(null=True, db_column='Update_Count', blank=True)
    update_date = models.DateTimeField(null=True, db_column='Update_Date', blank=True)
    class Meta:
        db_table = u'catalogue_update_details'

class CategoriesDescription(models.Model):
    categories_id = models.IntegerField()
    language_id = models.IntegerField()
    categories_name = models.CharField(max_length=600)
    catalogue_id = models.IntegerField(db_column='Catalogue_Id')
    class Meta:
        db_table = u'categories_description'

class Configuration(models.Model):
    configuration_id = models.IntegerField(primary_key=True)
    configuration_title = models.CharField(max_length=765)
    configuration_key = models.CharField(max_length=765)
    configuration_value = models.CharField(max_length=765)
    configuration_description = models.CharField(max_length=765)
    configuration_group_id = models.IntegerField()
    sort_order = models.IntegerField(null=True, blank=True)
    last_modified = models.DateTimeField(null=True, blank=True)
    date_added = models.DateTimeField()
    use_function = models.CharField(max_length=765, blank=True)
    set_function = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'configuration'

class ConfigurationGroup(models.Model):
    configuration_group_id = models.IntegerField(primary_key=True)
    configuration_group_title = models.CharField(max_length=192)
    configuration_group_description = models.CharField(max_length=765)
    sort_order = models.IntegerField(null=True, blank=True)
    visible = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'configuration_group'

class CostCentreLimit(models.Model):
    user_id = models.IntegerField(db_column='User_Id')
    cost_centre_id = models.IntegerField(db_column='Cost_Centre_Id')
    limit_value = models.FloatField(null=True, db_column='Limit_Value', blank=True)
    limit_type = models.CharField(max_length=60, db_column='Limit_Type', blank=True)
    class Meta:
        db_table = u'cost_centre_limit'

class Counter(models.Model):
    startdate = models.CharField(max_length=24, blank=True)
    counter = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'counter'

class Countries(models.Model):
    countries_id = models.IntegerField(primary_key=True)
    countries_name = models.CharField(max_length=192)
    countries_iso_code_2 = models.CharField(max_length=6)
    countries_iso_code_3 = models.CharField(max_length=9)
    address_format_id = models.IntegerField()
    class Meta:
        db_table = u'countries'

class Currencies(models.Model):
    currencies_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=96)
    code = models.CharField(max_length=9)
    symbol_left = models.CharField(max_length=36, blank=True)
    symbol_right = models.CharField(max_length=36, blank=True)
    decimal_point = models.CharField(max_length=3, blank=True)
    thousands_point = models.CharField(max_length=3, blank=True)
    decimal_places = models.CharField(max_length=3, blank=True)
    value = models.FloatField(null=True, blank=True)
    last_updated = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'currencies'

class CustomersBasket(models.Model):
    customers_basket_id = models.IntegerField(primary_key=True)
    customers_id = models.IntegerField()
    products_id = models.TextField()
    customers_basket_quantity = models.IntegerField()
    final_price = models.DecimalField(null=True, max_digits=17, decimal_places=4, blank=True)
    customers_basket_date_added = models.CharField(max_length=24, blank=True)
    class Meta:
        db_table = u'customers_basket'

class CustomersBasketAttributes(models.Model):
    customers_basket_attributes_id = models.IntegerField(primary_key=True)
    customers_id = models.IntegerField()
    products_id = models.TextField()
    products_options_id = models.IntegerField()
    products_options_value_id = models.IntegerField()
    class Meta:
        db_table = u'customers_basket_attributes'

class GeoZones(models.Model):
    geo_zone_id = models.IntegerField(primary_key=True)
    geo_zone_name = models.CharField(max_length=96)
    geo_zone_description = models.CharField(max_length=765)
    last_modified = models.DateTimeField(null=True, blank=True)
    date_added = models.DateTimeField()
    class Meta:
        db_table = u'geo_zones'
#language class1
class Languages(models.Model):
    languages_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=96)
    code = models.CharField(max_length=6)
    image = models.CharField(max_length=192, blank=True)
    directory = models.CharField(max_length=96, blank=True)
    sort_order = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'languages'

class Manufacturers(models.Model):
    manufacturers_id = models.IntegerField(primary_key=True)
    manufacturers_name = models.CharField(max_length=96)
    manufacturers_image = models.CharField(max_length=192, blank=True)
    date_added = models.DateTimeField(null=True, blank=True)
    last_modified = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'manufacturers'

class ManufacturersInfo(models.Model):
    manufacturers_id = models.IntegerField(primary_key=True)
    languages_id = models.ForeignKey(Languages)
    manufacturers_url = models.CharField(max_length=765)
    url_clicked = models.IntegerField()
    date_last_click = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'manufacturers_info'

class Article(models.Model):
    products_id = models.IntegerField(unique=True)
    products_quantity = models.IntegerField()
    products_model = models.CharField(max_length=36, blank=True)
    products_image = models.CharField(max_length=192, blank=True)
    products_price = models.FloatField()
    products_date_added = models.DateTimeField()
    products_last_modified = models.DateTimeField(null=True, blank=True)
    products_date_available = models.DateTimeField(null=True, blank=True)
    products_weight = models.CharField(max_length=192)
    products_status = models.IntegerField()
    products_tax_class_vat = models.FloatField()
    manufacturers_id = models.IntegerField(null=True, blank=True)
    products_ordered = models.IntegerField()
    article_uom = models.CharField(max_length=192)
    products_weight_add_info = models.CharField(max_length=3000)
    products_weight_tech = models.CharField(max_length=3000)
    products_deli_date = models.CharField(max_length=300)
    products_weight_no = models.CharField(max_length=765)
    products_ord_qnt = models.IntegerField()
    products_min_add_qnt = models.IntegerField()
    products_cnt_unt = models.CharField(max_length=150)
    products_code = models.CharField(max_length=765)
    catalogue_id = models.IntegerField(unique=True, null=True, db_column='Catalogue_Id', blank=True)
    class Meta:
        db_table = u'master_article'

class Buyer(models.Model):
    buyer_id = models.IntegerField(primary_key=True, db_column='Buyer_Id')
    buyer_name = models.CharField(max_length=450, db_column='Buyer_Name', blank=True)
    buyer_delivery_address = models.CharField(max_length=450, db_column='Buyer_Delivery_Address', blank=True)
    buyer_bill_address = models.CharField(max_length=450, db_column='Buyer_Bill_Address', blank=True)
    lang_id = models.IntegerField(null=True, db_column='Lang_Id', blank=True)
    buyer_postal_code = models.CharField(max_length=75, db_column='Buyer_Postal_Code', blank=True)
    buyer_city = models.CharField(max_length=300, db_column='Buyer_City', blank=True)
    buyer_country = models.CharField(max_length=300, db_column='Buyer_Country', blank=True)
    buyer_contact = models.CharField(max_length=300, db_column='Buyer_Contact', blank=True)
    buyer_phone_no = models.CharField(max_length=75, db_column='Buyer_Phone_No', blank=True)
    buyer_fax = models.CharField(max_length=75, db_column='Buyer_Fax', blank=True)
    buyer_email = models.CharField(max_length=150, db_column='Buyer_Email', blank=True)
    buyer_active = models.CharField(max_length=12, db_column='Buyer_Active', blank=True)
    buyer_login = models.CharField(max_length=150, db_column='Buyer_Login')
    buyer_status = models.CharField(max_length=18, db_column='Buyer_Status')
    buyer_reg_status = models.CharField(max_length=18, db_column='Buyer_Reg_Status')
    class Meta:
        db_table = u'master_buyer'

class Catalogue(models.Model):
    catalogue_id = models.IntegerField(primary_key=True, db_column='Catalogue_Id')
    catalogue_name = models.CharField(max_length=450, db_column='Catalogue_Name', blank=True)
    catalogue_type = models.CharField(max_length=60, db_column='Catalogue_Type', blank=True)
    unspsc_code = models.CharField(max_length=150, db_column='UNSPSC_Code', blank=True)
    catalogue_description = models.CharField(max_length=3000, db_column='Catalogue_Description', blank=True)
    date_added = models.DateField(null=True, db_column='Date_Added', blank=True)
    class Meta:
        db_table = u'master_catalogue'

class CatalogueGroup(models.Model):
    buyer_id = models.IntegerField(null=False, db_column='Buyer_Id')
    catalogue_group_id = models.IntegerField(primary_key=True, db_column='Catalogue_Group_Id')
    catalogue_group_name = models.CharField(max_length=450, db_column='Catalogue_Group_Name', blank=True)
    catalogue_group_description = models.CharField(max_length=750, db_column='Catalogue_Group_Description', blank=True)
    class Meta:
        db_table = u'master_catalogue_group'

class CostCentre(models.Model):
    buyer_id = models.IntegerField(db_column='Buyer_Id')
    cost_centre_id = models.IntegerField(primary_key=True, db_column='Cost_Centre_Id')
    cost_centre_name = models.CharField(max_length=150, db_column='Cost_Centre_Name', blank=True)
    cost_centre_desc = models.CharField(max_length=300, db_column='Cost_Centre_Desc', blank=True)
    class Meta:
        db_table = u'master_cost_centre'

class CostCode(models.Model):
    buyer_id = models.IntegerField(db_column='Buyer_Id')
    cost_id = models.IntegerField(primary_key=True, db_column='Cost_Id')
    cost_code_name = models.CharField(max_length=150, db_column='Cost_Code_Name', blank=True)
    cost_code_desc = models.CharField(max_length=300, db_column='Cost_Code_Desc', blank=True)
    class Meta:
        db_table = u'master_cost_code'
#language class2
class Language(models.Model):
    lang_id = models.IntegerField(db_column='lang_Id')
    lang_desc = models.CharField(max_length=300, db_column='lang_Desc')
    class Meta:
        db_table = u'master_language'

class Location(models.Model):
    buyer_supplier_id = models.IntegerField(db_column='Buyer_Supplier_Id')
    location_id = models.IntegerField(db_column='Location_Id')
    location_name = models.CharField(max_length=300, db_column='Location_Name')
    location_desc = models.CharField(max_length=1500, db_column='Location_Desc')
    location_mode = models.CharField(max_length=15, db_column='Location_Mode')
    class Meta:
        db_table = u'master_location'

class Modules(models.Model):
    module_id = models.IntegerField(primary_key=True, db_column='Module_Id')
    module_description = models.CharField(max_length=300, db_column='Module_Description', blank=True)
    module_mode = models.CharField(max_length=15, db_column='Module_Mode', blank=True)
    module_description_dutch = models.CharField(max_length=300, db_column='Module_Description_Dutch', blank=True)
    class Meta:
        db_table = u'master_modules'

class Po(models.Model):
    po_id = models.IntegerField(primary_key=True, db_column='PO_Id')
    po_no = models.CharField(max_length=300, db_column='PO_No', blank=True)
    po_date = models.DateField(null=True, db_column='PO_Date', blank=True)
    requisition_id = models.IntegerField(null=True, db_column='Requisition_Id', blank=True)
    user_id = models.IntegerField(db_column='User_Id')
    cost_centre_id = models.IntegerField(null=True, db_column='Cost_Centre_Id', blank=True)
    supplier_id = models.IntegerField(null=True, db_column='Supplier_Id', blank=True)
    po_cost = models.FloatField(null=True, db_column='PO_Cost', blank=True)
    po_ref_no = models.CharField(max_length=300, db_column='PO_Ref_No', blank=True)
    po_payment_terms = models.CharField(max_length=750, db_column='PO_Payment_Terms', blank=True)
    po_delivery_period = models.CharField(max_length=450, db_column='PO_Delivery_Period', blank=True)
    po_remarks = models.TextField(db_column='PO_Remarks', blank=True)
    po_delivery_address = models.CharField(max_length=450, db_column='PO_Delivery_Address', blank=True)
    po_invoice_address = models.CharField(max_length=450, db_column='PO_Invoice_Address', blank=True)
    po_status = models.CharField(max_length=12, db_column='PO_Status', blank=True)
    po_type = models.CharField(max_length=12, db_column='PO_Type', blank=True)
    po_mode = models.CharField(max_length=12, db_column='PO_Mode', blank=True)
    fin_year_id = models.IntegerField(db_column='Fin_Year_Id')
    po_cancellation_reason = models.TextField(db_column='PO_Cancellation_Reason', blank=True)
    class Meta:
        db_table = u'master_po'

class Requisition(models.Model):
    requisition_id = models.IntegerField(primary_key=True, db_column='Requisition_Id')
    requisition_no = models.CharField(max_length=150, db_column='Requisition_No', blank=True)
    requisition_date = models.DateField(null=True, db_column='Requisition_Date', blank=True)
    user_id = models.IntegerField(null=True, db_column='User_Id', blank=True)
    cost_centre_id = models.IntegerField(null=True, db_column='Cost_Centre_Id', blank=True)
    supplier_id = models.IntegerField(null=True, db_column='Supplier_Id', blank=True)
    requisitiont_cost = models.FloatField(null=True, db_column='Requisitiont_Cost', blank=True)
    requisition_description = models.TextField(db_column='Requisition_Description', blank=True)
    requisition_purpose = models.TextField(db_column='Requisition_Purpose', blank=True)
    requisition_remarks = models.TextField(db_column='Requisition_Remarks', blank=True)
    req_delivery_address = models.CharField(max_length=450, db_column='Req_Delivery_Address', blank=True)
    req_invoice_address = models.CharField(max_length=450, db_column='Req_Invoice_Address', blank=True)
    requisition_status = models.CharField(max_length=12, db_column='Requisition_Status', blank=True)
    req_type = models.CharField(max_length=150, db_column='Req_Type', blank=True)
    req_mode = models.CharField(max_length=150, db_column='Req_Mode', blank=True)
    fin_year_id = models.IntegerField(db_column='Fin_Year_Id')
    rejection_reason = models.TextField(db_column='Rejection_Reason', blank=True)
    requisition_approved_date = models.DateField(null=True, db_column='Requisition_approved_Date', blank=True)
    class Meta:
        db_table = u'master_requisition'

class Roles(models.Model):
    role_id = models.IntegerField(primary_key=True, db_column='Role_Id')
    role_description = models.CharField(max_length=300, db_column='Role_Description', blank=True)
    role_mode = models.CharField(max_length=15, db_column='Role_Mode', blank=True)
    role_description_dutch = models.CharField(max_length=300, db_column='Role_Description_Dutch', blank=True)
    class Meta:
        db_table = u'master_roles'

class Service(models.Model):
    supplier_id = models.IntegerField(db_column='Supplier_Id')
    service_id = models.IntegerField(primary_key=True, db_column='Service_Id')
    service_name = models.CharField(max_length=150, db_column='Service_Name', blank=True)
    service_description = models.CharField(max_length=765, db_column='Service_Description', blank=True)
    service_uom = models.CharField(max_length=150, db_column='Service_UOM', blank=True)
    service_unit_rate = models.FloatField(null=True, db_column='Service_Unit_Rate', blank=True)
    class Meta:
        db_table = u'master_service'

class Supplier(models.Model):
    supplier_id = models.IntegerField(primary_key=True, db_column='Supplier_Id')
    supplier_name = models.CharField(max_length=450, db_column='Supplier_Name', blank=True)
    supplier_address = models.CharField(max_length=600, db_column='Supplier_Address', blank=True)
    lang_id = models.IntegerField(null=True, db_column='Lang_Id', blank=True)
    supplier_postal_code = models.CharField(max_length=75, db_column='Supplier_Postal_Code', blank=True)
    supplier_city = models.CharField(max_length=300, db_column='Supplier_City', blank=True)
    supplier_country = models.CharField(max_length=300, db_column='Supplier_Country', blank=True)
    supplier_contact = models.CharField(max_length=300, db_column='Supplier_Contact', blank=True)
    supplier_phone_no = models.CharField(max_length=75, db_column='Supplier_Phone_No', blank=True)
    supplier_fax = models.CharField(max_length=75, db_column='Supplier_Fax', blank=True)
    supplier_email = models.CharField(max_length=150, db_column='Supplier_Email', blank=True)
    supplier_active = models.CharField(max_length=12, db_column='Supplier_Active', blank=True)
    supplier_profile = models.TextField(db_column='Supplier_Profile', blank=True)
    supplier_login = models.CharField(max_length=150, db_column='Supplier_Login')
    supplier_duns = models.CharField(max_length=150, db_column='Supplier_DUNS')
    supplier_type = models.CharField(max_length=150, db_column='Supplier_Type')
    supplier_website = models.CharField(max_length=150, db_column='Supplier_Website')
    supplier_status = models.CharField(max_length=18, db_column='Supplier_Status')
    supplier_reg_status = models.CharField(max_length=18, db_column='Supplier_Reg_Status')
    buyer_id = models.IntegerField(null=True, db_column='Buyer_Id', blank=True)
    class Meta:
        db_table = u'master_supplier'

class Unit(models.Model):
    buyer_supplier_id = models.IntegerField(db_column='Buyer_Supplier_Id')
    unit_id = models.IntegerField(db_column='Unit_Id')
    unit_name = models.CharField(max_length=300, db_column='Unit_Name')
    unit_desc = models.CharField(max_length=1500, db_column='Unit_Desc')
    unit_mode = models.CharField(max_length=15, db_column='Unit_Mode')
    class Meta:
        db_table = u'master_unit'

class User(models.Model):
    buyer_supplier_id = models.IntegerField(null=True, db_column='Buyer_Supplier_Id', blank=True)
    user_id = models.IntegerField(primary_key=True, db_column='User_Id')
    user_fname = models.CharField(max_length=150, db_column='User_FName', blank=True)
    user_lname = models.CharField(max_length=150, db_column='User_LName', blank=True)
    user_title = models.CharField(max_length=60, db_column='User_Title', blank=True)
    user_login = models.CharField(max_length=75, db_column='User_Login', blank=True)
    user_pwd = models.CharField(max_length=75, db_column='User_Pwd', blank=True)
    lang_id = models.IntegerField(null=True, db_column='Lang_Id', blank=True)
    user_email = models.CharField(max_length=150, db_column='User_Email', blank=True)
    user_phone_no = models.CharField(max_length=75, db_column='User_Phone_No', blank=True)
    user_delivery_address = models.CharField(max_length=450, db_column='User_Delivery_Address', blank=True)
    user_bill_address = models.CharField(max_length=450, db_column='User_Bill_Address', blank=True)
    user_status = models.CharField(max_length=30, db_column='User_Status', blank=True)
    user_mode = models.CharField(max_length=15, db_column='User_Mode', blank=True)
    user_admin = models.CharField(max_length=15, db_column='User_Admin', blank=True)
    user_unit = models.IntegerField(null=True, db_column='User_Unit', blank=True)
    user_location = models.IntegerField(null=True, db_column='User_Location', blank=True)
    class Meta:
        db_table = u'master_user'

class ModuleActivation(models.Model):
    buyer_supplier_id = models.IntegerField(unique=True, db_column='Buyer_Supplier_Id')
    module_id = models.IntegerField(unique=True, db_column='Module_Id')
    module_active = models.CharField(max_length=15, db_column='Module_Active', blank=True)
    class Meta:
        db_table = u'module_activation'

class PoDetails(models.Model):
    po_id = models.IntegerField(null=True, db_column='PO_Id', blank=True)
    article_sr_no = models.IntegerField(null=True, db_column='Article_Sr_No', blank=True)
    article_id = models.IntegerField(null=True, db_column='Article_Id', blank=True)
    article_code = models.CharField(max_length=150, db_column='Article_Code', blank=True)
    article_description = models.TextField(db_column='Article_Description', blank=True)
    article_qty = models.FloatField(null=True, db_column='Article_Qty', blank=True)
    article_uom = models.CharField(max_length=150, db_column='Article_UOM', blank=True)
    article_unit_price = models.FloatField(null=True, db_column='Article_Unit_Price', blank=True)
    article_line_total = models.FloatField(null=True, db_column='Article_Line_Total', blank=True)
    cost_id = models.IntegerField(null=True, db_column='Cost_Id', blank=True)
    class Meta:
        db_table = u'po_details'

class RequisitionDetails(models.Model):
    requisition_id = models.IntegerField(null=True, db_column='Requisition_Id', blank=True)
    article_sr_no = models.IntegerField(null=True, db_column='Article_Sr_No', blank=True)
    article_id = models.IntegerField(null=True, db_column='Article_Id', blank=True)
    article_code = models.CharField(max_length=150, db_column='Article_Code', blank=True)
    article_description = models.TextField(db_column='Article_Description', blank=True)
    article_qty = models.FloatField(null=True, db_column='Article_Qty', blank=True)
    article_uom = models.CharField(max_length=150, db_column='Article_UOM', blank=True)
    article_unit_price = models.FloatField(null=True, db_column='Article_Unit_Price', blank=True)
    article_line_total = models.FloatField(null=True, db_column='Article_Line_Total', blank=True)
    cost_id = models.IntegerField(null=True, db_column='Cost_Id', blank=True)
    class Meta:
        db_table = u'requisition_details'

class Orders(models.Model):
    orders_id = models.IntegerField(primary_key=True)
    customers_id = models.IntegerField()
    customers_name = models.CharField(max_length=192)
    customers_company = models.CharField(max_length=96, blank=True)
    customers_street_address = models.CharField(max_length=192)
    customers_suburb = models.CharField(max_length=96, blank=True)
    customers_city = models.CharField(max_length=96)
    customers_postcode = models.CharField(max_length=30)
    customers_state = models.CharField(max_length=96, blank=True)
    customers_country = models.CharField(max_length=96)
    customers_telephone = models.CharField(max_length=96)
    customers_email_address = models.CharField(max_length=288)
    customers_address_format_id = models.IntegerField()
    delivery_name = models.CharField(max_length=192)
    delivery_company = models.CharField(max_length=96, blank=True)
    delivery_street_address = models.CharField(max_length=192)
    delivery_suburb = models.CharField(max_length=96, blank=True)
    delivery_city = models.CharField(max_length=96)
    delivery_postcode = models.CharField(max_length=30)
    delivery_state = models.CharField(max_length=96, blank=True)
    delivery_country = models.CharField(max_length=96)
    delivery_address_format_id = models.IntegerField()
    billing_name = models.CharField(max_length=192)
    billing_company = models.CharField(max_length=96, blank=True)
    billing_street_address = models.CharField(max_length=192)
    billing_suburb = models.CharField(max_length=96, blank=True)
    billing_city = models.CharField(max_length=96)
    billing_postcode = models.CharField(max_length=30)
    billing_state = models.CharField(max_length=96, blank=True)
    billing_country = models.CharField(max_length=96)
    billing_address_format_id = models.IntegerField()
    payment_method = models.CharField(max_length=96)
    cc_type = models.CharField(max_length=60, blank=True)
    cc_owner = models.CharField(max_length=192, blank=True)
    cc_number = models.CharField(max_length=96, blank=True)
    cc_expires = models.CharField(max_length=12, blank=True)
    last_modified = models.DateTimeField(null=True, blank=True)
    date_purchased = models.DateTimeField(null=True, blank=True)
    orders_status = models.IntegerField()
    orders_date_finished = models.DateTimeField(null=True, blank=True)
    currency = models.CharField(max_length=9, blank=True)
    currency_value = models.DecimalField(null=True, max_digits=16, decimal_places=6, blank=True)
    class Meta:
        db_table = u'orders'

class OrdersProducts(models.Model):
    user_id = models.IntegerField(db_column='User_Id')
    article_sr_no = models.IntegerField(db_column='Article_Sr_No')
    article_id = models.IntegerField(db_column='Article_id')
    article_code = models.CharField(max_length=300, db_column='Article_Code', blank=True)
    article_description = models.CharField(max_length=3000, db_column='Article_Description')
    article_qty = models.FloatField(db_column='Article_Qty')
    article_uom = models.CharField(max_length=300, db_column='Article_UOM')
    article_unit_price = models.FloatField(db_column='Article_Unit_Price')
    article_line_total = models.FloatField(db_column='Article_Line_Total')
    cost_id = models.IntegerField(db_column='Cost_Id')
    r_mode = models.CharField(max_length=30, db_column='R_Mode')
    supplier_id = models.IntegerField(db_column='Supplier_Id')
    cost_centre_id = models.IntegerField(db_column='Cost_Centre_Id')
    class Meta:
        db_table = u'orders_products'

class PoBasketFavourite(models.Model):
    user_id = models.IntegerField(null=True, db_column='User_Id', blank=True)
    basket_id = models.IntegerField(null=True, db_column='Basket_Id', blank=True)
    basket_name = models.CharField(max_length=300, db_column='Basket_Name', blank=True)
    basket_create_date = models.DateTimeField(null=True, db_column='Basket_Create_Date', blank=True)
    cost_centre_id = models.IntegerField(null=True, db_column='Cost_Centre_Id', blank=True)
    supplier_id = models.IntegerField(null=True, db_column='Supplier_Id', blank=True)
    basket_cost = models.FloatField(db_column='Basket_Cost')
    class Meta:
        db_table = u'po_basket_favourite'

class PoBasketFavouriteDetails(models.Model):
    basket_id = models.IntegerField(null=True, db_column='Basket_Id', blank=True)
    article_id = models.IntegerField(null=True, db_column='Article_Id', blank=True)
    article_code = models.CharField(max_length=150, db_column='Article_Code', blank=True)
    article_description = models.TextField(db_column='Article_Description', blank=True)
    article_total_qty = models.FloatField(null=True, db_column='Article_Total_Qty', blank=True)
    article_line_value = models.FloatField(null=True, db_column='Article_Line_Value', blank=True)
    class Meta:
        db_table = u'po_basket_favourite_details'

class PoCatalog(models.Model):
    user_id = models.IntegerField(db_column='User_Id')
    article_sr_no = models.IntegerField(db_column='Article_Sr_No')
    article_id = models.IntegerField(db_column='Article_id')
    article_code = models.CharField(max_length=300, db_column='Article_Code', blank=True)
    article_description = models.CharField(max_length=3000, db_column='Article_Description')
    article_qty = models.FloatField(db_column='Article_Qty')
    article_uom = models.CharField(max_length=300, db_column='Article_UOM')
    article_unit_price = models.FloatField(db_column='Article_Unit_Price')
    article_line_total = models.FloatField(db_column='Article_Line_Total')
    cost_id = models.IntegerField(db_column='Cost_Id')
    r_mode = models.CharField(max_length=30, db_column='R_Mode')
    supplier_id = models.IntegerField(db_column='Supplier_Id')
    cost_centre_id = models.IntegerField(db_column='Cost_Centre_Id')
    po_date = models.DateField(db_column='PO_Date')
    po_cost = models.FloatField(db_column='PO_Cost')
    po_ref_no = models.CharField(max_length=300, db_column='PO_Ref_No')
    po_payment_terms = models.CharField(max_length=750, db_column='PO_Payment_Terms')
    po_delivery_period = models.CharField(max_length=450, db_column='PO_Delivery_Period')
    po_remarks = models.CharField(max_length=3000, db_column='PO_Remarks')
    po_delivery_address = models.CharField(max_length=1500, db_column='PO_Delivery_Address')
    po_invoice_address = models.CharField(max_length=1500, db_column='PO_Invoice_Address')
    po_status = models.CharField(max_length=15, db_column='PO_Status')
    fin_year_id = models.IntegerField(db_column='Fin_Year_Id')
    class Meta:
        db_table = u'po_catalog'

class PoCostcentreFavourite(models.Model):
    cost_centre_id = models.IntegerField(null=True, db_column='Cost_Centre_Id', blank=True)
    article_id = models.IntegerField(null=True, db_column='Article_Id', blank=True)
    article_code = models.CharField(max_length=150, db_column='Article_Code', blank=True)
    article_description = models.TextField(db_column='Article_Description', blank=True)
    article_total_qty = models.FloatField(null=True, db_column='Article_Total_Qty', blank=True)
    class Meta:
        db_table = u'po_costcentre_favourite'

class PoDeliveryPlace(models.Model):
    po_id = models.IntegerField(null=True, db_column='PO_Id', blank=True)
    po_delivery_place = models.CharField(max_length=450, db_column='PO_Delivery_Place', blank=True)
    class Meta:
        db_table = u'po_delivery_place'

class PoOrders(models.Model):
    user_id = models.IntegerField(db_column='User_Id')
    article_sr_no = models.IntegerField(db_column='Article_Sr_No')
    article_id = models.IntegerField(db_column='Article_id')
    article_code = models.CharField(max_length=300, db_column='Article_Code', blank=True)
    article_description = models.CharField(max_length=3000, db_column='Article_Description')
    article_qty = models.FloatField(db_column='Article_Qty')
    article_uom = models.CharField(max_length=300, db_column='Article_UOM')
    article_unit_price = models.FloatField(db_column='Article_Unit_Price')
    article_line_total = models.FloatField(db_column='Article_Line_Total')
    cost_id = models.IntegerField(db_column='Cost_Id')
    r_mode = models.CharField(max_length=30, db_column='R_Mode')
    supplier_id = models.IntegerField(db_column='Supplier_Id')
    cost_centre_id = models.IntegerField(db_column='Cost_Centre_Id')
    class Meta:
        db_table = u'po_orders'

class PoProductFavourite(models.Model):
    user_id = models.IntegerField(null=True, db_column='User_Id', blank=True)
    article_id = models.IntegerField(null=True, db_column='Article_Id', blank=True)
    article_code = models.CharField(max_length=150, db_column='Article_Code', blank=True)
    article_description = models.TextField(db_column='Article_Description', blank=True)
    article_qty = models.FloatField(null=True, db_column='Article_Qty', blank=True)
    article_uom = models.CharField(max_length=300, db_column='Article_UOM', blank=True)
    article_unit_price = models.FloatField(null=True, db_column='Article_Unit_Price', blank=True)
    cost_id = models.IntegerField(db_column='Cost_Id')
    cost_centre_id = models.IntegerField(db_column='Cost_Centre_Id')
    products_image = models.CharField(max_length=300)
    r_mode = models.CharField(max_length=30, db_column='R_Mode')
    class Meta:
        db_table = u'po_product_favourite'

class PoService(models.Model):
    po_id = models.IntegerField(primary_key=True, db_column='PO_Id')
    po_no = models.CharField(max_length=300, db_column='PO_No', blank=True)
    po_date = models.DateTimeField(null=True, db_column='PO_Date', blank=True)
    requisition_id = models.IntegerField(null=True, db_column='Requisition_Id', blank=True)
    supplier_id = models.IntegerField(null=True, db_column='Supplier_Id', blank=True)
    user_id = models.IntegerField(null=True, db_column='User_Id', blank=True)
    cost_centre_id = models.IntegerField(null=True, db_column='Cost_Centre_Id', blank=True)
    po_ref_no = models.CharField(max_length=300, db_column='PO_Ref_No', blank=True)
    po_payment_terms = models.CharField(max_length=750, db_column='PO_Payment_Terms', blank=True)
    po_total_amount = models.FloatField(null=True, db_column='PO_Total_Amount', blank=True)
    po_delivery_period = models.CharField(max_length=450, db_column='PO_Delivery_Period', blank=True)
    po_delivery_address = models.CharField(max_length=450, db_column='PO_Delivery_Address', blank=True)
    po_invoice_address = models.CharField(max_length=450, db_column='PO_Invoice_Address', blank=True)
    po_remarks = models.TextField(db_column='PO_Remarks', blank=True)
    po_type = models.CharField(max_length=150, db_column='PO_Type', blank=True)
    class Meta:
        db_table = u'po_service'

class PoServiceDetails(models.Model):
    po_id = models.IntegerField(null=True, db_column='PO_Id', blank=True)
    service_sr_no = models.IntegerField(null=True, db_column='Service_Sr_No', blank=True)
    service_description = models.TextField(db_column='Service_Description', blank=True)
    service_qty = models.FloatField(null=True, db_column='Service_Qty', blank=True)
    service_unit = models.CharField(max_length=150, db_column='Service_Unit', blank=True)
    service_unit_price = models.FloatField(null=True, db_column='Service_Unit_Price', blank=True)
    service_line_total = models.FloatField(null=True, db_column='Service_Line_Total', blank=True)
    cost_id = models.IntegerField(null=True, db_column='Cost_Id', blank=True)
    class Meta:
        db_table = u'po_service_details'

class ProductsAttributes(models.Model):
    products_attributes_id = models.IntegerField(primary_key=True)
    products_id = models.IntegerField()
    options_id = models.IntegerField()
    options_values_id = models.IntegerField()
    options_values_price = models.DecimalField(max_digits=17, decimal_places=4)
    price_prefix = models.CharField(max_length=3)
    class Meta:
        db_table = u'products_attributes'

class ProductsDescription(models.Model):
    products_id = models.IntegerField(primary_key=True)
    language_id = models.ForeignKey(Languages)
    products_name = models.CharField(max_length=300)
    products_description = models.CharField(max_length=3000, blank=True)
    products_url = models.CharField(max_length=765, blank=True)
    products_viewed = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'products_description'

class ProductsOptions(models.Model):
    products_options_id = models.IntegerField(primary_key=True)
    language_id = models.ForeignKey(Language)
    products_options_name = models.CharField(max_length=96)
    class Meta:
        db_table = u'products_options'

class ProductsOptionsValues(models.Model):
    products_options_values_id = models.IntegerField(primary_key=True)
    language_id = models.ForeignKey(Language)
    products_options_values_name = models.CharField(max_length=192)
    class Meta:
        db_table = u'products_options_values'

class ReqBasketFavourite(models.Model):
    user_id = models.IntegerField(null=True, db_column='User_Id', blank=True)
    basket_id = models.IntegerField(null=True, db_column='Basket_Id', blank=True)
    basket_name = models.CharField(max_length=150, db_column='Basket_Name', blank=True)
    basket_create_date = models.DateTimeField(null=True, db_column='Basket_Create_Date', blank=True)
    cost_centre_id = models.IntegerField(null=True, db_column='Cost_Centre_Id', blank=True)
    supplier_id = models.IntegerField(null=True, db_column='Supplier_Id', blank=True)
    basket_cost = models.FloatField(null=True, db_column='Basket_Cost', blank=True)
    class Meta:
        db_table = u'req_basket_favourite'

class ReqBasketFavouriteDetails(models.Model):
    basket_id = models.IntegerField(null=True, db_column='Basket_Id', blank=True)
    article_id = models.IntegerField(null=True, db_column='Article_Id', blank=True)
    article_code = models.CharField(max_length=150, db_column='Article_Code', blank=True)
    article_description = models.TextField(db_column='Article_Description', blank=True)
    article_total_qty = models.FloatField(null=True, db_column='Article_Total_Qty', blank=True)
    article_line_value = models.FloatField(null=True, db_column='Article_Line_Value', blank=True)
    class Meta:
        db_table = u'req_basket_favourite_details'

class ReqCatalog(models.Model):
    user_id = models.IntegerField(db_column='User_Id')
    article_sr_no = models.IntegerField(db_column='Article_Sr_No')
    article_id = models.IntegerField(db_column='Article_id')
    article_code = models.CharField(max_length=300, db_column='Article_Code', blank=True)
    article_description = models.CharField(max_length=3000, db_column='Article_Description')
    article_qty = models.FloatField(db_column='Article_Qty')
    article_uom = models.CharField(max_length=300, db_column='Article_UOM')
    article_unit_price = models.FloatField(db_column='Article_Unit_Price')
    article_line_total = models.FloatField(db_column='Article_Line_Total')
    cost_id = models.IntegerField(db_column='Cost_Id')
    r_mode = models.CharField(max_length=30, db_column='R_Mode')
    supplier_id = models.IntegerField(db_column='Supplier_Id')
    cost_centre_id = models.IntegerField(db_column='Cost_Centre_Id')
    requisition_date = models.DateField(db_column='Requisition_Date')
    requisitiont_cost = models.FloatField(db_column='Requisitiont_Cost')
    requisition_description = models.CharField(max_length=3000, db_column='Requisition_Description')
    requisition_purpose = models.CharField(max_length=3000, db_column='Requisition_Purpose')
    requisition_remarks = models.CharField(max_length=3000, db_column='Requisition_Remarks')
    req_delivery_address = models.CharField(max_length=1500, db_column='Req_Delivery_Address')
    req_invoice_address = models.CharField(max_length=1500, db_column='Req_Invoice_Address')
    requisition_status = models.CharField(max_length=15, db_column='Requisition_Status')
    fin_year_id = models.IntegerField(db_column='Fin_Year_Id')
    class Meta:
        db_table = u'req_catalog'

class ReqCostcentreFavourite(models.Model):
    cost_centre_id = models.IntegerField(null=True, db_column='Cost_Centre_Id', blank=True)
    article_id = models.IntegerField(null=True, db_column='Article_Id', blank=True)
    article_code = models.CharField(max_length=150, db_column='Article_Code', blank=True)
    article_description = models.TextField(db_column='Article_Description', blank=True)
    article_total_qty = models.FloatField(null=True, db_column='Article_Total_Qty', blank=True)
    class Meta:
        db_table = u'req_costcentre_favourite'

class ReqProductFavourite(models.Model):
    user_id = models.IntegerField(null=True, db_column='User_Id', blank=True)
    article_id = models.IntegerField(null=True, db_column='Article_Id', blank=True)
    article_code = models.CharField(max_length=150, db_column='Article_Code', blank=True)
    article_description = models.TextField(db_column='Article_Description', blank=True)
    article_qty = models.FloatField(null=True, db_column='Article_Qty', blank=True)
    article_uom = models.CharField(max_length=300, db_column='Article_UOM', blank=True)
    article_unit_price = models.FloatField(null=True, db_column='Article_Unit_Price', blank=True)
    cost_id = models.IntegerField(db_column='Cost_Id')
    cost_centre_id = models.IntegerField(db_column='Cost_Centre_Id')
    products_image = models.CharField(max_length=300)
    r_mode = models.CharField(max_length=15, db_column='R_Mode')
    class Meta:
        db_table = u'req_product_favourite'

class RequisitionServiceDetails(models.Model):
    requisition_id = models.IntegerField(null=True, db_column='Requisition_Id', blank=True)
    service_sr_no = models.IntegerField(null=True, db_column='Service_Sr_No', blank=True)
    service_description = models.TextField(db_column='Service_Description', blank=True)
    service_qty = models.FloatField(null=True, db_column='Service_Qty', blank=True)
    service_unit = models.CharField(max_length=150, db_column='Service_Unit', blank=True)
    service_unit_price = models.FloatField(null=True, db_column='Service_Unit_Price', blank=True)
    service_line_total = models.FloatField(null=True, db_column='Service_Line_Total', blank=True)
    cost_id = models.IntegerField(null=True, db_column='Cost_Id', blank=True)
    class Meta:
        db_table = u'requisition_service_details'

class Reviews(models.Model):
    reviews_id = models.IntegerField(primary_key=True)
    products_id = models.IntegerField()
    customers_id = models.IntegerField(null=True, blank=True)
    customers_name = models.CharField(max_length=192)
    reviews_rating = models.IntegerField(null=True, blank=True)
    date_added = models.DateTimeField(null=True, blank=True)
    last_modified = models.DateTimeField(null=True, blank=True)
    reviews_read = models.IntegerField()
    class Meta:
        db_table = u'reviews'

class ReviewsDescription(models.Model):
    reviews_id = models.IntegerField(primary_key=True)
    languages_id = models.ForeignKey(Languages)
    reviews_text = models.TextField()
    class Meta:
        db_table = u'reviews_description'

class RoleModule(models.Model):
    buyer_supplier_id = models.IntegerField(db_column='Buyer_Supplier_Id')
    role_id = models.IntegerField(db_column='Role_Id')
    role_module_id = models.IntegerField(db_column='Role_Module_Id')
    module_id = models.IntegerField(db_column='Module_Id')
    rm_mode = models.CharField(max_length=15, db_column='RM_Mode', blank=True)
    class Meta:
        db_table = u'role_module'

class Specials(models.Model):
    specials_id = models.IntegerField(primary_key=True)
    products_id = models.IntegerField()
    specials_new_products_price = models.DecimalField(max_digits=17, decimal_places=4)
    specials_date_added = models.DateTimeField(null=True, blank=True)
    specials_last_modified = models.DateTimeField(null=True, blank=True)
    expires_date = models.DateTimeField(null=True, blank=True)
    date_status_change = models.DateTimeField(null=True, blank=True)
    status = models.IntegerField()
    class Meta:
        db_table = u'specials'

class SupplierCatalogueDetails(models.Model):
    categories_id = models.IntegerField(unique=True)
    categories_image = models.CharField(max_length=192, blank=True)
    parent_id = models.IntegerField()
    sort_order = models.IntegerField(null=True, blank=True)
    date_added = models.DateTimeField(null=True, blank=True)
    last_modified = models.DateTimeField(null=True, blank=True)
    catalogue_id = models.IntegerField(unique=True)
    class Meta:
        db_table = u'supplier_catalogue_details'

class SupplierCatalogueLink(models.Model):
    supplier_id = models.IntegerField(primary_key=True, db_column='Supplier_Id')
    catalogue_id = models.IntegerField(null=False, db_column='Catalogue_Id')
    catalogue_path = models.CharField(max_length=765, db_column='Catalogue_Path', blank=True)
    class Meta:
        db_table = u'supplier_catalogue_link'

class SupplierSettingDetails(models.Model):
    payment_mode = models.CharField(max_length=150, db_column='Payment_Mode', blank=True)
    po_generation = models.CharField(max_length=150, db_column='PO_Generation', blank=True)
    limit_type = models.CharField(max_length=150, db_column='Limit_Type')
    catalogue_type = models.CharField(max_length=300, db_column='Catalogue_Type')
    class Meta:
        db_table = u'supplier_setting_details'

class TaxClass(models.Model):
    tax_class_id = models.IntegerField(primary_key=True)
    tax_class_title = models.CharField(max_length=96)
    tax_class_description = models.CharField(max_length=765)
    last_modified = models.DateTimeField(null=True, blank=True)
    date_added = models.DateTimeField()
    class Meta:
        db_table = u'tax_class'

class TaxRates(models.Model):
    tax_rates_id = models.IntegerField(primary_key=True)
    tax_zone_id = models.IntegerField()
    tax_class_id = models.IntegerField()
    tax_priority = models.IntegerField(null=True, blank=True)
    tax_rate = models.DecimalField(max_digits=9, decimal_places=4)
    tax_description = models.CharField(max_length=765)
    last_modified = models.DateTimeField(null=True, blank=True)
    date_added = models.DateTimeField()
    class Meta:
        db_table = u'tax_rates'

class Tmplcatalogue(models.Model):
    buyer_supplier_id = models.IntegerField(db_column='Buyer_Supplier_Id')
    content_type = models.CharField(max_length=75)
    file_name = models.CharField(max_length=300)
    file_info = models.CharField(max_length=300)
    creation_date = models.DateField()
    checksum = models.CharField(max_length=75)
    ct_mode = models.CharField(max_length=15, db_column='ct_Mode')
    ct_type = models.CharField(max_length=15)
    class Meta:
        db_table = u'tmplcatalogue'

class UserCatalogueGroup(models.Model):
    user_id = models.IntegerField(db_column='User_Id')
    catalog_group_id = models.IntegerField(db_column='Catalog_Group_Id')
    catalog_id = models.IntegerField(db_column='Catalog_Id')
    class Meta:
        db_table = u'user_catalogue_group'

class UserCostCentre(models.Model):
    user_id = models.IntegerField(unique=True, db_column='User_Id')
    cost_centre_id = models.IntegerField(unique=True, db_column='Cost_Centre_Id')
    class Meta:
        db_table = u'user_cost_centre'

class UserDeliveryAddress(models.Model):
    user_id = models.IntegerField(db_column='User_Id')
    del_address_name = models.CharField(max_length=450, db_column='Del_Address_Name', blank=True)
    active = models.CharField(max_length=12, db_column='Active', blank=True)
    buyer_id = models.IntegerField(db_column='Buyer_Id')
    class Meta:
        db_table = u'user_delivery_address'

class UserGroupDetails(models.Model):
    user_group_id = models.IntegerField(db_column='User_Group_Id')
    user_id = models.IntegerField(db_column='User_Id')
    class Meta:
        db_table = u'user_group_details'

class UserInvoiceAddress(models.Model):
    user_id = models.IntegerField(db_column='User_Id')
    inv_address_name = models.CharField(max_length=450, db_column='Inv_Address_Name', blank=True)
    active = models.CharField(max_length=12, db_column='Active', blank=True)
    buyer_id = models.IntegerField(db_column='Buyer_Id')
    class Meta:
        db_table = u'user_invoice_address'

class UserLanguage(models.Model):
    user_id = models.IntegerField(db_column='User_Id')
    lang_id = models.IntegerField(null=True, db_column='Lang_Id', blank=True)
    class Meta:
        db_table = u'user_language'

class UserRoleModules(models.Model):
    user_id = models.IntegerField(db_column='User_Id')
    role_module_id = models.IntegerField(db_column='Role_Module_Id')
    class Meta:
        db_table = u'user_role_modules'

class UserRoles(models.Model):
    user_id = models.IntegerField(db_column='User_Id')
    role_id = models.IntegerField(null=True, db_column='Role_Id', blank=True)
    class Meta:
        db_table = u'user_roles'


