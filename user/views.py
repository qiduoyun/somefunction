from django.shortcuts import render,render_to_response
from  django.http import HttpResponseRedirect,HttpResponse,StreamingHttpResponse
from django.views import generic
from .models import User,UserBlog,UserFile
from .form import UserRegister,UserLogin,UserFileForm
import hashlib,os
from django.template import RequestContext


def take_sha1(content):

    ct=content.encode(encoding='UTF-8',errors='strict')
    hs=hashlib.sha224()

    result=hs.update(ct)
    return result


class UserBlogview(generic.ListView):
    template_name = 'user/index.html'
    def get_queryset(self):
        return  UserBlog.objects.order_by('blog_pud_time')[:8]




class BlogListview(generic.DetailView):
    model = UserBlog
    template_name = 'user/article.html'

class UserView(generic.ListView):

    template_name = 'user/index.html'

    def get_queryset(self):
        return User.objects.order_by('id')[:3]

def handle_upload_file(f):


    with open(os.path.join("D:\DTLFolder",f.name),"wb+") as destination:

       for chunk in f.chunks():
           destination.write(chunk)
           destination.closed


def UserFileview(request):
  if request.method=='POST':
    form=UserFileForm(request.POST,request.FILES)

    print( form.is_valid())
    if form.is_valid():






        file_name=form.cleaned_data['file_name']
        file_upload=form.cleaned_data['file_upload']
        handle_upload_file(request.FILES['file_upload'])
        #file_upload=os.path.join("D:\DTLFolder",request.FILES['file_upload'].name)
        print('111111ceshi')
        user_file=UserFile.objects.create(file_name=file_name,file_upload=file_upload)
        print('222222222211111ceshi')
        #print(request.FILES['file_upload'].name)
        user_file.save()
        print(request.FILES['file_upload'].name)

        return HttpResponse("文件上传成功")


  else:
      form=UserFileForm()
      return render(request,'user/upload.html',{form:form})
class dowmload_list(generic.ListView):
    template_name = "user/upload.html"
    def get_queryset(self):
        return UserFile.objects.order_by('id')

def download(request,id):
    f1=UserFile.objects.get(pk=id)
    def file_iterator(file_name,chunk_size=512):
       with open(file_name,'rb+') as readfile:
           while True:
            c=readfile.read(chunk_size)
            if c:
                  yield c
            else:
                  break
    file_name=f1.file_upload
    #f="D:/DTLFolder/pycharm.txt"
    f=os.path.join('C:/Users/Administrator/PycharmProjects/xuexi',file_name.path)
    print(f)
    print(file_name)
    print(os.path.dirname(__file__))
    #path='/'.join(file_name)


    response=StreamingHttpResponse(file_iterator(f))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(f)
    return response




def Register(request):
    if request.method=='POST':
        form=UserRegister(request.POST)
        if form.is_valid():
            user_name=form.cleaned_data["user_name"]
            namefilter=User.objects.filter(user_name=user_name)
            if len(namefilter)>0:
                return  render(request,'user/register.html',{'error':'用户名已经存在'}
                                           )
            else:
                user_password=form.cleaned_data['user_password']
                user_password_sure=form.cleaned_data['user_password_sure']
                if user_password !=user_password_sure:
                    return render(request,'user/register.html',{'error':'两次输入密码不一致！重新输入'}
                                              )
                else:
                  user_password=user_password_sure
                  print(take_sha1(user_password_sure))
                  print(take_sha1("mmmm"))


                  user=User.objects.create(user_name=user_name,user_password=user_password)
                  user.save()
                  return render(request,'user/success.html',{'user_name':user_name,'message':'注册成功'}
                                              )

    else:
        form = UserRegister()
        return render(request,'user/register.html', {'form': form}
                                )



def Login(request):
    if request.method=='POST':
        form=UserLogin(request.POST)
        if form.is_valid():
            user_name=form.cleaned_data['user_name']
            user_password=form.cleaned_data['user_password']
            user_password=user_password
            namefiter=User.objects.filter(user_name=user_name,user_password=user_password)
            if len(namefiter)>0:
                return render(request,'user/success.html',{'user_name':user_name,'message':'登录成功'}
                                          )
            else:
                return render(request,'user/login.html',{'error':'用户不存在，或者用户名密码不对'}
                                          )
    else:
            form=UserLogin()
            return render(request,'user/login.html',{'form':form})


# Create your views here.
