from django.shortcuts import redirect
from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"


class StaticialDetailsView(TemplateView):
    template_name = 'staticaldetails.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            context = self.get_context_data(**kwargs)
            return self.render_to_response(context)
        else:
            return redirect('login')
    