class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        posts = self.get_queryset()
        context['featured'] = posts[0]
        context['row_posts'] = [posts[1:][i:i + 2] for i in
                                range(0, len(posts[1:]), 2)]
        return context
