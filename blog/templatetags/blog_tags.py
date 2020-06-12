from django import template
from ..models import Post
#markdown
from django.utils.safestring import mark_safe
import markdown

register = template.Library()

@register.simple_tag
def total_posts():
    return Post.published.count()

@register.simple_tag
def show_latest_posts(count=3):
    #latest_posts = Post.published.order_by('-publish')[:count]

    return Post.published.order_by('-publish')[:count]

@register.simple_tag
def get_most_popular():
    pass


# custom filters
@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))