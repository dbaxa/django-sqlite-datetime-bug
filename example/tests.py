import datetime

import django.utils.timezone
from django.test import TestCase

from .models import ExampleModel

# Create your tests here.


class TestExampleModel(TestCase):

    def shared_test(self):
        a_date_time = django.utils.timezone.now()
        a_date = a_date_time.date()
        for i in range(0, 10):
            ExampleModel.objects.get_or_create(created_date=a_date_time +
                                               datetime.timedelta(seconds=i))
        results = ExampleModel.objects.filter(created_date__date=a_date)
        self.assertTrue(results.exists())

    def test_filter_using__date_not_none_time_zone(self):
        with self.settings(TIME_ZONE=None):
            self.shared_test()

    def test_filter_not_using__date(self):
        with self.settings(TIME_ZONE='UTC'):
            self.shared_test()
