from rest_framework import serializers

class FormattedPhoneNumberField(serializers.Field):
    def to_representation(self, value):
        if not value:
            return None
        formatted_number = '({}) {}-{}'.format(value[:3], value[3:6], value[6:])
        return formatted_number

    def to_internal_value(self, data):
        return data.replace("(", "").replace(")", "").replace(" ", "").replace("-", "")
