from .models import SubRubric

def ak_context_processor(request):
    context = {}
    context['rubrics'] = SubRubric.objects.all()
    return context

