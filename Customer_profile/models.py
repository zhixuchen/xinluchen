from django.db import models
import django_filters
from Staff_info.models import UserProfile



# Create your models here.
class Customer(models.Model):
    name = models.CharField('姓名', blank=True, default="", max_length=255)
    mobile = models.CharField('手机', blank=True, default="", max_length=255)
    wechat_name = models.CharField('微信昵称', blank=True, default="", max_length=255)
    driver_license = models.CharField('驾驶证', blank=True, default="", max_length=255)
    source = models.CharField('客户来源', blank=True, default="", max_length=255)
    type = models.CharField('客户类型', blank=True, default="", max_length=255)
    gender = models.CharField('性别', choices=(('male', '男'), ('female', '女')), blank=True, default="", max_length=255)
    birthday = models.CharField('生日', blank=True, default="", max_length=255)
    identity = models.CharField('身份证', blank=True, default="", max_length=255)
    address = models.CharField('地址', blank=True, default="", max_length=255)
    allowable_amount = models.CharField('允许挂账金额', blank=True, default="", max_length=255)
    department = models.CharField('单位', blank=True, default="", max_length=255)
    remarks = models.CharField('备注', blank=True, default="", max_length=255)
    employee_bonus = models.CharField('分红员工', blank=True, default="", max_length=255)
    car_type = models.CharField('车辆型号', blank=True, default="", max_length=255)
    licence_plate = models.CharField('车牌', blank=True, default="", max_length=255)
    belonger = models.CharField('所有人', blank=True, default="", max_length=255)
    belonger_address = models.CharField('所有人地址', blank=True, default="", max_length=255)
    last_maintenance_mileage = models.CharField('上次保养里程', blank=True, default="", max_length=255)
    next_maintenance_mileage = models.CharField('下次保养里程', blank=True, default="", max_length=255)
    driving_license = models.CharField('行驶证', blank=True, default="", max_length=255)
    chassis_number = models.CharField('车架号', blank=True, default="", max_length=255)
    engine_model = models.CharField('发动机型号', blank=True, default="", max_length=255)
    car_purchase_time = models.CharField('购车时间', blank=True, default="", max_length=255)
    expiration_of_annual_inspection_date = models.CharField('年检到期', blank=True, default="", max_length=255)
    insurance_company = models.CharField('保险公司', blank=True, default="", max_length=255)
    expiration_of_insurance_date = models.CharField('保险到期', blank=True, default="", max_length=255)
    car_price = models.CharField('车价', blank=True, default="", max_length=255)
    displacement = models.CharField('排量', blank=True, default="", max_length=255)
    brand_model = models.CharField('厂牌型号', blank=True, default="", max_length=255)
    colour = models.CharField('颜色', blank=True, default="", max_length=255)
    engine_number = models.CharField('发动机号', blank=True, default="", max_length=255)
    cumulative_consumption = models.CharField('累计消费', blank=True, default="", max_length=255)
    days_before_arrival = models.CharField('未到店天数', blank=True, default="", max_length=255)
    total_number_of_arrivals = models.CharField('总到店次数', blank=True, default="", max_length=255)



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '客户信息'
        verbose_name_plural = '客户信息'
