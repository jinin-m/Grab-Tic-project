from django.shortcuts import render,redirect

from django.views import View

from .models import Movies,CastChoices,GenreChoices,LanguageChoices,CertificationChoices

from .forms import MovieForm

from django.db.models import Q

from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator

from authentication.permissions import user_role_permission

# Create your views here.

# @method_decorator(login_required(login_url='user-login'),name='dispatch')


class HomeView(View) :

    template = 'shows/home.html'

    def get(self,request,*args,**kwargs) :

        movies = Movies.objects.filter(active_status=True)

        data = {'movies' : movies,'page':'Home'}

        query = request.GET.get('query')

        if query:

            search_results = movies.filter(Q(name__icontains=query)|
                                           Q(description__icontains=query)|
                                           Q(certification__name__icontains=query)| #bcz it is forign key
                                           Q(languages__name__icontains=query)|
                                           Q(cast__name__icontains=query)|
                                           Q(genre__name__icontains=query)
                                           ).distinct()#avoid duplicates
            
            data.update({'search_results':search_results,'query':query})




        return render(request,self.template,context=data)
    
# class MovieCreateView(View) :

#     template = 'shows/movie-create.html'

#     def get(self,request,args,*kwargs) :

#         data = {'languages_choices' : LanguagesChoices,
#                 'cast_choices' : CastChoices,
#                 'genre_choices' : GenreChoices,
#                 'certification_choices' : CertificationChoices
#                 }

#         return render(request,self.template,context=data)
    
#     def post(self,request,args,*kwargs) :

#         name = request.POST.get('name')

#         description = request.POST.get('description')

#         photo = request.FILES.get('photo')

#         runtime = request.POST.get('runtime')

#         release_date = request.POST.get('release_date')

#         certification = request.POST.get('certification')

#         cast = request.POST.get('cast')

#         languages = request.POST.get('languages')

#         genre = request.POST.get('genre')

#         # print(name,description,photo,runtime,release_date,certification,cast,languages,genre)

#         Movies.objects.create(name=name,
#                               photo=photo,
#                               description=description,
#                               runtime=runtime,
#                               certification=certification,
#                               release_date=release_date,
#                               cast=cast,
#                               languages=languages,
#                               genre=genre)

#         return redirect('home')

@method_decorator(user_role_permission(roles=['Admin'],redirect_url='home'),name='dispatch')

class MovieCreateView(View) :

    template = 'shows/movie-create.html'

    form_class = MovieForm

    def get(self,request,*args,**kwargs) :

        form = self.form_class()

        data = {'form':form,'page':'Create a view'}

        return render(request,self.template,context=data)
    
    def post(self,request,*args,**kwargs) :

        form = self.form_class(request.POST,request.FILES)

        if form.is_valid() :

            form.save()
            
            return redirect('home')

        data = {'form' : form,'page':'Create a view'}
        
        return render(request,self.template,context=data)
    
class MovieDetailsView(View) :

    template = 'shows/movie-details.html'

    def get(self,request,*args,**kwargs) :

        uuid = kwargs.get('uuid')

        movie = Movies.objects.get(uuid=uuid)

        data = {'movie' : movie,'page':'Movie details'}

        return render(request,self.template,context=data)
    
@method_decorator(user_role_permission(roles=['Admin'],redirect_url='home'),name='dispatch')

class MovieEditView(View) :

    template = 'shows/movie-edit.html'

    form_class = MovieForm

    def get(self,request,*args,**kwargs) :

        uuid = kwargs.get('uuid')

        movie = Movies.objects.get(uuid=uuid)

        form = self.form_class(instance=movie)

        data = {'form' : form,'page':'edit movie'}

        return render(request,self.template,context=data)
    
    def post(self,request,*args,**kwargs) :

        uuid = kwargs.get('uuid')

        movie = Movies.objects.get(uuid=uuid)

        form = self.form_class(request.POST,request.FILES,instance=movie)

        if form.is_valid() :

            form.save()

            return redirect('home')
        
        data = {'form' : form,'page':'edit movie'}

        return render(request,self.template,context=data)
    
@method_decorator(user_role_permission(roles=['Admin'],redirect_url='home'),name='dispatch')
    
class MovieDeleteView(View) :

    def get(self,request,*args,**kwargs) :

        uuid = kwargs.get('uuid')

        movie = Movies.objects.get(uuid=uuid)

        #hard delete

        # movie.delete()

        #soft delete

        movie.active_status = False

        movie.save()

        return redirect('home')