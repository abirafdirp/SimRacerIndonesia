class TimeStampedModelAdminMixin:
    def get_readonly_fields(self, request, obj=None):
        return self.readonly_fields + ('created_date', 'update_date')
