 # -*- coding: UTF-8 -*- 
from django import forms

PRODUCI_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
	quantity = forms.TypedChoiceField(label=u"数量", choices=PRODUCI_QUANTITY_CHOICES, coerce=int)
	# 让用户可以在1~20之间选择产品的数量。我们使用了带有coerce=int的TypeChoiceField字段来把输入转换为整数
	update = forms.BooleanField(required=False, initial=False, 
								widget=forms.HiddenInput)
	
