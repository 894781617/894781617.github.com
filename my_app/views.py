#coding:utf-8
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from Blog_new.models import  Blog, Category, Tag,Comment
from pure_pagination import PageNotAnInteger, Paginator
from Blog_new.forms import *

#评论留言
def comment(request):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.save()
            return render_to_response('{"status": "success"}',
                                      context_instance=RequestContext(request))
        else:
            return render_to_response('{"status": "fail"}',
                                      context_instance=RequestContext(request))

#采用提取公共部分方法 统计博客各类数据
def custom_proc(request):
    blog_nums = Blog.objects.count()
    category_nums = Category.objects.count()
    tag_nums = Tag.objects.count()
    return {
        'blog_nums': blog_nums,
      'category_nums': category_nums,
       'tag_nums': tag_nums,
    }



def index(request):
    all_blog = Blog.objects.all().order_by('-id')
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    p = Paginator(all_blog, 5, request=request)
    all_blog = p.page(page)
    # blog_nums, category_nums, tag_nums = counts()
    return render_to_response('index.html',{ 'all_blog': all_blog,
                                             }, context_instance=RequestContext(request,processors=[custom_proc]))

#归档展示
def archive(request):
    all_blog = Blog.objects.all().order_by('-create_time')
    count = all_blog.count()
    # 分页
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    p = Paginator(all_blog, 5, request=request)
    all_blog = p.page(page)
    # blog_nums, category_nums, tag_nums = counts()
    return render_to_response('archive.html',{ 'all_blog': all_blog,
                                               'count':count,
                                               },
                              context_instance=RequestContext(request,processors=[custom_proc]))


#标签详情展示
def detail( request):
    tag_id = request.GET.get('id')
    all_blog = Blog.objects.filter(tag_id=tag_id)
    tag_name = Tag.objects.filter(id=tag_id)
    count = all_blog.count()
    # 分页
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    p = Paginator(all_blog, 5, request=request)
    all_blog = p.page(page)
    tag_name = tag_name[0]
    # blog_nums, category_nums, tag_nums = counts()
    return render_to_response('blog-detail.html', {'all_blog': all_blog,
                                                   'count':count,
                                                   'tag_name':tag_name,
                                                   }, context_instance=RequestContext(request,processors=[custom_proc]))

#标签展示
def tag(request):
    all_tag = Tag.objects.all()
    count = all_tag.count()
    # blog_nums, category_nums, tag_nums = counts()
    return render_to_response('tags.html',{ 'all_tag': all_tag,
                                            'count':count},
                              context_instance=RequestContext(request,processors=[custom_proc]))


#博客详情展示
def article(request):
    article_id = request.GET.get('id')
    article = Blog.objects.get(id=article_id)
    # blog_nums, category_nums, tag_nums = counts()
    return render_to_response('article.html',{'article':article,
                                              },
                              context_instance=RequestContext(request,processors=[custom_proc]))


#统计博客各种数目
# def counts():
#     blog_nums = Blog.objects.count()
#     category_nums = Category.objects.count()
#     tag_nums = Tag.objects.count()
#     print tag_nums, category_nums
#     return blog_nums,category_nums,tag_nums


