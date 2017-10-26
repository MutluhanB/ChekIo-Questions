#%%
import datetime
default_names=["Ali","Veli","Alican","Velican"]
default_amounts=[15,78,43,40]
unf_message="Merhaba {name} ,{date} günü yaptığınız alışveriş tutarı {total} TL"
def make_message(names,amounts) :
    if len(names)==len(amounts) :
        i = 0
        today = datetime.date.today()
        text = "{today.day}/{today.month}/{today.year}".format(today=today)
        for name in names   :
                 new_amount ="%.2f" %(amounts[i])
                 new_msg =unf_message.format(
                         name=name,
                         date=text,
                         total=new_amount
                         )
                 
                 i+=1
                 print(new_msg)
                 
                 