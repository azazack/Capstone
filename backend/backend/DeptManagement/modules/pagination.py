from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'meta': {
                'total_count': self.page.paginator.count,
                'total_pages': self.page.paginator.num_pages,
                'next_page': self.page.number if not self.page.has_next() else self.page.next_page_number(),
                'prev_page': self.page.number if not self.page.has_previous() else self.page.previous_page_number(),
                'current_page': self.page.number
            },
            'data': data
        })

# current_page: number;
# last_page: number;
# next_page?: number;
# total_count: number;
# prev_page?: number;
