## Script (Python) "validate_add_criterion"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##
from Products.ATContentTypes import ATCTMessageFactory as _

request = context.REQUEST
indexId=request.get('field')
criterion_type=request.get('criterion_type')

if criterion_type not in context.allowedCriteriaForField(indexId):
    msg = _(u'Criterion of type '
            '${type} not added, it does not work with index ${index}.',
            mapping={'type' : criterion_type, 'index' : indexId})
    context.plone_utils.addPortalMessage(msg, 'error')
    return state.set(status='failure')
else:
    return state.set(status='success')
