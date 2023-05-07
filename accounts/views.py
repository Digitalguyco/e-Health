from .forms import CustomUserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
# Create your views here.

# def register(request):
    
#     if request.method == "POST":
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.user_type = form.cleaned_data.get('user_type')
#             user.save()
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'register.html', {'form':form})

        
class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.user_typr = self.request.POST.get('user_type')
        return super().form_valid(form)
    
class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy()