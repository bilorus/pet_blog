from django.core.paginator import Paginator


class DataMixin:
    def listing(self):
        paginator = Paginator(self.get_queryset(), 3)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return page_obj

    def get_user_context(self, **kwargs):
        context = kwargs
        posts = self.listing()

        context['featured'] = posts[0]
        context['row_posts'] = [posts[1:][i:i + 2] for i in
                                range(0, len(posts[1:]), 2)]
        return context
