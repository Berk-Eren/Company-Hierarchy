from rest_framework.filters import BaseFilterBackend
from rest_framework import status
from rest_framework.exceptions import APIException

from django.utils.translation import gettext_lazy as _


class PositionDepartmentTogetherFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        query_params = request.query_params
        allowed_fields = getattr( PositionDepartmentTogetherFilter,
                                    "get_search_fields")(view)

        abundant_fields = set(query_params)-set(allowed_fields)

        if abundant_fields:
            raise NotAllowedField(allowed_fields, abundant_fields)

        position_title = request.query_params.get("position", None)
        department_title = request.query_params.get("department", None)

        if position_title:
            queryset = queryset.filter(title__iexact=position_title)
        if department_title:
            queryset = queryset.filter(department__title__iexact=department_title)

        return queryset

    @staticmethod
    def get_search_fields(view):
        return view.allowed_fields


class NotAllowedField(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Unallowed search fields'
    default_code = 'unallowed_search_fields'
    str_method = lambda x: "'%s'"%(x)
    
    def __init__(self, allowed_fields, abundant_fields):
        msg = (
            "The fields '%s' aren\'t allowed for the querying. " 
            "Allowed fields are %s"
        )

        allowed_fields_str = ', '.join(map(NotAllowedField.str_method, 
                                            allowed_fields) )
        abundant_fields_str = ', '.join(map(NotAllowedField.str_method, 
                                             abundant_fields) )
        
        detail = msg % (abundant_fields_str, allowed_fields_str)
        
        self.detail = _(detail)