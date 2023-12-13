import django_filters
from .models import Job


class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='iexact')
    location = django_filters.CharFilter(lookup_expr='iexact')
    salary = django_filters.CharFilter(lookup_expr='icontain')
    type = django_filters.CharFilter(lookup_expr='iexact')
    
    
    class Meta:
        model = Job
        fields = ['title', 'location', 'salary', 'type']
    
    