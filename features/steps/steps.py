from product import *
import logging


# create logger
log = logging.getLogger('compareProducts')
logging.basicConfig(filename='steps.log',level=logging.INFO)

@given(u'quality "a"')
def step_impl(context):
    context.qa = Quality()
    for row in context.table:
        context.qa.set_quality_value(row["a"], row["avalue"])
    log.info ('Loaded qualities and values: ' +str( context.qa.quality))



#@when(u'I compare products')
#def step_impl(context,product , aquality , bquality):
#    raise NotImplementedError(u'STEP: When I compare products')

@given(u'"product" with qualities')
def step_impl(context):
  products = getattr(context, "products", None)
  if not products:
    context.products = Products()

  for row in context.table:
    product=row["product"]

    #use any number of columns
    #sum the score
    score=0
    #skip the first column
    for head in context.table.headings[1:]:
      #continue
      log.debug("Headings: " + head)
      aq=row[head]

      qavalue=float (context.qa.quality[aq])
      log.debug ("qavalue" +str( qavalue))
      score+=qavalue

    context.products.add_product(product, score)
    log.info ("products are: " + str( context.products.list))

@when(u'I compare')
def step_impl(context):
  None
#@when(u'I compare "{product}" with "{aquality}" and "{bquality}"')
#@when(u'I compare <product> with <aquality> and <bquality>')


@then(u'I get "products" sorted desc by "score" (sum of values of qualities)')
def step_impl(context):
  #~ for row in context.table:
    #~ products=row["products"]
    #~ score=row["score"]
    #~ log.debug ("product: " + str(products) + " expected: " + score)
    #~ log.debug ( "got score: " + str (context.products.list[products] ) )
    #~ #assert int(score) == context.products.list[products]

  #sorting the products based on their score
  d_view = [ (v,k) for k,v in context.products.list.iteritems() ]
  log.debug ("the new view:" + str(d_view))
  d_view.sort() # natively sort tuples by first element
  for v,k in d_view:
    log.info ("Product %s has score: %.2f" % (k,v))

#@then(u'i get sorted list of products')
#def step_impl(context):
#  d_view = [ (v,k) for k,v in context.products.list.iteritems() ]
#  d_view.sort(reverse=True) # natively sort tuples by first element
#  for v,k in d_view:
#    print ("%s: %d" % (k,v))


