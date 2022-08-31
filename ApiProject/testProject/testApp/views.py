from django.http import JsonResponse
from .models import Link


def getLink(request):
    from_date = request['from']
    to_date = request['to']
    queryset = Link.objects.filter(date__range=(from_date, to_date))
    result = {}
    if not queryset.empty:
        domains = []
        for rec in queryset:
            domains.append(rec.name)
        result['domains'] = domains
        result['status'] = 'ok'
    else:
        result['status'] = 'error'
    return JsonResponse(result)


def postLink(request):
    result = {}
    if request.method == 'POST':
        for rec in request.body['domains']:
            link = Link(rec)
            link.save()
        result['status'] = 'ok'
    else:
        result['status'] = 'error'
    return JsonResponse(result)
