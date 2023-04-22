from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from NewHome.models import Propiedades, Profile, Mensaje
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def about(request):
    return render(request, "NewHome/about.html")

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
        propiedades_id = self.kwargs.get('pk')
        return Propiedades.objects.filter(publisher=user_id, id=propiedades_id).exists()

    def handle_no_permission(self):
        return render(self.request, "NewHome/not_found.html")

class PropiedadesDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Propiedades
    success_url = reverse_lazy("index")

    def test_func(self):
        user_id = self.request.user.id
        propiedades_id = self.kwargs.get('pk')
        return Propiedades.objects.filter(publisher=user_id, id=propiedades_id).exists()

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

    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.user = self.request.user
        profile.save()
        return super().form_valid(form)

class ProfileUpdate(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Profile
    fields = '__all__'

    def test_func(self):
        user_id = self.request.user.id
        profile_id = self.kwargs.get('pk')
        return Profile.objects.filter(user=user_id, id=profile_id).exists()

    def handle_no_permission(self):
        return render(self.request, "NewHome/profile_notfound.html")

class MensajeCreate(CreateView):
    model = Mensaje
    fields = '__all__'
    success_url = reverse_lazy("index")


class  MensajeList(LoginRequiredMixin, ListView):
    model = Mensaje
    context_object_name = "mensajes"
    
    def get_queryset(self):
        return Mensaje.objects.filter(destinatario=self.request.user.id).all()
    

class MensajeDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model= Mensaje
    success_url = reverse_lazy("mensaje-list")

    def test_func(self):
        user_id = self.request.user.id
        mensaje_id = self.kwargs.get('pk')
        return Mensaje.objects.filter(destinatario=user_id).exists()