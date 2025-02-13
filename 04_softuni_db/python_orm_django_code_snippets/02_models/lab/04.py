'''
class Project(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    budget = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=10)
    duration_in_days = models.PositiveIntegerField(
        blank=True, null=True, verbose_name="Duration in Days"
    )
    estimated_hours = models.FloatField(
        blank=True, null=True, verbose_name="Estimated Hours"
    )
    start_date = models.DateField(
        blank=True, null=True, verbose_name="Start Date", default=date.today()
    )
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    last_edited_on = models.DateTimeField(auto_now=True, editable=False)
'''