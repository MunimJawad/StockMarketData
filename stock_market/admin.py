from django.contrib import admin
from . models import Data
from import_export.admin import ImportExportModelAdmin

admin.site.register(Data,ImportExportModelAdmin)