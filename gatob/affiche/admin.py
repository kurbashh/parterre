from dal import autocomplete
from django.contrib import admin
from .forms import PerformanceCreativesForm, PerformanceConductorForm, PerformancePerformersForm
from .models import MainImages, Performers, Performance, Creatives, Conductor, Backstage, PerformanceFiles, Row, Seat, \
    Ticket, PerformancePerformers, PerformanceCreatives, PerformanceConductor, BackstageBlock, Theater


class TheaterAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(admins=request.user)


admin.site.register(Theater, TheaterAdmin)


class CreativesAdmin(admin.ModelAdmin):
    search_fields = ['name']
    ordering = ['name']
    readonly_fields = ('theater',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(theater__admins=request.user)


admin.site.register(Creatives, CreativesAdmin)


class PerformersAdmin(admin.ModelAdmin):
    search_fields = ['name']
    ordering = ['name']
    readonly_fields = ('theater',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(theater__admins=request.user)


admin.site.register(Performers, PerformersAdmin)


class ConductorsAdmin(admin.ModelAdmin):
    search_fields = ['name']
    ordering = ['name']
    readonly_fields = ('theater',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(theater__admins=request.user)


admin.site.register(Conductor, ConductorsAdmin)


class PerformancePerformersInline(admin.TabularInline):
    readonly_fields = ('theater',)
    model = PerformancePerformers
    form = PerformancePerformersForm
    extra = 0

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'performer':
            kwargs['queryset'] = Performers.objects.order_by('name')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    verbose_name_plural = 'Исполнители'


class PerformanceCreativesInline(admin.TabularInline):
    readonly_fields = ('theater',)
    model = PerformanceCreatives
    form = PerformanceCreativesForm
    extra = 0
    verbose_name_plural = 'Постановщики'


class PerformanceConductorInline(admin.TabularInline):
    readonly_fields = ('theater',)
    model = PerformanceConductor
    form = PerformanceConductorForm
    extra = 0
    verbose_name_plural = 'Дирижер'


class PerformanceAdmin(admin.ModelAdmin):
    readonly_fields = ('theater',)
    inlines = [
        PerformancePerformersInline,
        PerformanceConductorInline,
        PerformanceCreativesInline,
    ]
    list_display = ["title", "datetime1", "datetime2"]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(theater__admins=request.user)

    def has_change_permission(self, request, obj=None):
        if obj is None or request.user.is_superuser:
            return True
        return obj.theater.admins.filter(id=request.user.id).exists()

    def has_delete_permission(self, request, obj=None):
        if obj is None or request.user.is_superuser:
            return True
        return obj.theater.admins.filter(id=request.user.id).exists()

    def has_view_permission(self, request, obj=None):
        if obj is None or request.user.is_superuser:
            return True
        return obj.theater.admins.filter(id=request.user.id).exists()


admin.site.register(Performance, PerformanceAdmin)


class BackstageBlockInline(admin.TabularInline):
    readonly_fields = ('theater',)
    model = BackstageBlock
    fields = ('block_type', 'text_content', 'image_content', 'video_content', 'audio_content')
    extra = 0

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        form = formset.form
        if 'block_type' in form.base_fields:
            block_type_field = form.base_fields['block_type']
            block_type_field.widget.attrs.update({'style': 'width: 150px'})
        return formset


class BackstageAdmin(admin.ModelAdmin):
    readonly_fields = ('theater',)
    list_display = ('title', 'date', 'content_type', 'performance')
    list_filter = ('content_type', 'date', 'performance')
    inlines = [BackstageBlockInline]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(theater__admins=request.user)

    def has_change_permission(self, request, obj=None):
        if obj is None or request.user.is_superuser:
            return True
        return obj.theater.admins.filter(id=request.user.id).exists()

    def has_delete_permission(self, request, obj=None):
        if obj is None or request.user.is_superuser:
            return True
        return obj.theater.admins.filter(id=request.user.id).exists()

    def has_view_permission(self, request, obj=None):
        if obj is None or request.user.is_superuser:
            return True
        return obj.theater.admins.filter(id=request.user.id).exists()


admin.site.register(Backstage, BackstageAdmin)


class MainImagesAdmin(admin.ModelAdmin):
    readonly_fields = ('theater',)
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(theater__admins=request.user)


admin.site.register(MainImages, MainImagesAdmin)


class PerformanceFilesAdmin(admin.ModelAdmin):
    readonly_fields = ('theater',)
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(theater__admins=request.user)


admin.site.register(PerformanceFiles, PerformanceFilesAdmin)


class RowAdmin(admin.ModelAdmin):
    readonly_fields = ('theater',)
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(theater__admins=request.user)


admin.site.register(Row, RowAdmin)


class SeatAdmin(admin.ModelAdmin):
    readonly_fields = ('theater',)
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(theater__admins=request.user)


admin.site.register(Seat, SeatAdmin)


class TicketAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(seat__row__theater__admins=request.user)


admin.site.register(Ticket, TicketAdmin)
