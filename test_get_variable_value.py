import unittest
from get_variable_value import get_variable_value_from_source_code


class TestGetVariableValueFromSourceCode(unittest.TestCase):
    """Test `get_variable_value_from_source_code()` function """

    SOURCE_CODE = '''
a = 0
a = 1
b = c = 2
d, e = 3, 4
f = 'string1'
g, h, i = 'string2', 5, 'string3'
j = [1, 2, 3]
k = ['string4', 'string5', 'string6']
l = ('string7', 'string8', 'string9')

    '''

    VARS_AND_RESULTS = (
        ('a', 1),
        ('b', 2),
        ('c', 2),
        ('d', 3),
        ('e', 4),
        ('f', 'string1'),
        ('g', 'string2'),
        ('h', 5),
        ('i', 'string3'),
        ('j', [1, 2, 3]),
        ('k', ['string4', 'string5', 'string6']),
        ('l', ('string7', 'string8', 'string9')),
    )

    def test_get_variable_value_from_source_code(self):
        for var, result in self.VARS_AND_RESULTS:
            self.assertEqual(
                get_variable_value_from_source_code(source_code=self.SOURCE_CODE, variable_name=var),
                result
            )
