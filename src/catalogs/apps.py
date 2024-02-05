from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CatalogsConfig(AppConfig):

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'src.catalogs'
    app_label = 'catalogs'
    verbose_name = _('Справочники')

