import datetime
from datetime import timedelta
class timechange:
    def __init__(self,x):
        self.x=x
        
    def str_date(self):    # ex) '20220601' -> '2022-06-01'
        t=datetime.datetime.strptime(self.x,'%Y%m%d')
        return t.strftime('%Y-%m-%d')
    def date_str(self):    # ex) '2022-06-01' -> '20220601'
        t=datetime.datetime.strptime(self.x,'%Y-%m-%d')
        return t.strftime('%Y%m%d') 
    def str_point(self):   # ex) '20220601' -> '2022.06.01'
        t=datetime.datetime.strptime(self.x,'%Y%m%d')
        return t.strftime('%Y.%m.%d') 
  
    
class timemath:
    def __init__(self,date,days):
        self.date=date
        self.days=days
    def minus(self):    # '20220601',10 -> '20220522'
        t=datetime.datetime.strptime(self.date,'%Y%m%d')
        m=t-timedelta(days=self.days)
        return m.strftime('%Y%m%d')
    def add(self):      # '20220601',10 -> '20220611
        t=datetime.datetime.strptime(self.date,'%Y%m%d')
        m=t+timedelta(days=self.days)
        return m.strftime('%Y%m%d')        
        
    
    
