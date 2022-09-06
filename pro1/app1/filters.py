import django_filters as df
from .models import blogPost

class myfilter(df.FilterSet):

    title=df.CharFilter(lookup_expr='icontains')
    class Meta:
        model=blogPost
        fields=['title']