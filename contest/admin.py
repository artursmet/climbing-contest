from django.contrib import admin
from .models import Contest, Group, Contestant


admin.site.register(Contest)
admin.site.register(Group)


class ContestantAdmin(admin.ModelAdmin):
    list_filter = ('group', )
    list_display = ('first_name', 'surname', 'sponsor', 'email', 'group')
    list_display_links = ('first_name', 'surname')
    search_fields = ['first_name', 'surname']

    class Meta:
        model = Contestant

admin.site.register(Contestant, ContestantAdmin)
