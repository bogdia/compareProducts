class Quality(object):
  def __init__(self):
    self.quality={}

  def set_quality_value(self,q,v):
    self.quality[q]=v
    #print ("Quality is now: ")
    #print (self.quality)


class Products(object):
  def __init__(self):
    #if not
    self.list={}

  def add_product(self,product,score):
    self.list[product]=score


