from django.template.response import TemplateResponse
from contest.models import Contest


def homepage(request):
    contest = Contest.objects.latest('pk')

    return TemplateResponse(request, 'core/homepage.html',
        {'contest': contest}
    )
