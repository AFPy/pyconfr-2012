import logging
from django.http import HttpResponse
from django.views.decorators.http import require_POST

from biblion import creole_parser
logger = logging.getLogger('django.request')
logger.setLevel(logging.DEBUG)

@require_POST
def creole_preview(request):
    if "raw" not in request.POST:
        logger.debug("raw in request.POST: no good")
        return HttpResponse("no good")
    logger.debug("lets debug something")
    return HttpResponse(creole_parser.parse(request.POST["raw"]))
