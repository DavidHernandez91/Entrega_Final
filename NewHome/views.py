from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from NewHome.models import Propiedades, Profile
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def index(request):
    context = {
        "propiedades": Propiedades.objects.all()
    }
    return render(request,"NewHome/index.html", context)

class PropiedadesCreate(LoginRequiredMixin, CreateView):
    model = Propiedades
    success_url = reverse_lazy("index")
    fields = ['Propiedad_Descripcion','Propiedad_Direccion',
             'Numero_Habitaciones','Propiedad_Costo','imagen']

    def form_valid(self, form):
        form.instance.publisher = self.request.user
        return super().form_valid(form)

class PropiedadesList(ListView):
    model = Propiedades
    context_object_name = "propiedades"

class PropiedadesDetail(DetailView):
    model = Propiedades

class PropiedadesUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Propiedades
    success_url = reverse_lazy("index")
    fields = '__all__'

    def test_func(self):
        user_id = self.request.user.id
        post_id = self.kwargs.get('pk')
        return Propiedades.objects.filter(publisher=user_id, id=post_id).exists()

    def handle_no_permission(self):
        return render(self.request, "NewHome/not_found.html")

class PropiedadesDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Propiedades
    success_url = reverse_lazy("index")

    def test_func(self):
        user_id = self.request.user.id
        post_id = self.kwargs.get('pk')
        return Propiedades.objects.filter(publisher=user_id, id=post_id).exists()

    def handle_no_permission(self):
        return render(self.request, "NewHome/not_found.html")

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('index')

class Login(LoginView):
    next_page = reverse_lazy("index")

class Logout(LogoutView):
    template_name = 'registration/logout.html'

class ProfileCreate(LoginRequiredMixin, CreateView):
    model = Profile
    success_url = reverse_lazy("index")
    fields = ['Nombre','Descripcion',
             'Email','Web','imagen']

class ProfileUpdate(LoginRequiredMixin,UpdateView):
    model = Profile
    fields = '__all__'

