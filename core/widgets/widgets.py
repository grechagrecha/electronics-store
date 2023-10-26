from django_filters.widgets import RangeWidget


class RangeWidgetWith2Placeholders(RangeWidget):
    def __init__(self, from_attrs=None, to_attrs=None, attrs=None):
        super().__init__(attrs)
        self.template_name = 'core/widgets/range_widget_with_2_placeholders.html'

        if from_attrs:
            self.widgets[0].attrs.update(from_attrs)
        if to_attrs:
            self.widgets[1].attrs.update(to_attrs)
