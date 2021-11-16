from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import IrisDataset

# Register your models here.
@admin.register(IrisDataset)
class IrisDatasetAdmin(ImportExportModelAdmin):
    model = IrisDataset
    list_display = ["id", "name", "parameter1", "parameter2", "parameter3", "parameter4"]