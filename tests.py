# -*- coding: utf-8 -*-

import re
import unittest

from genrepr import gen_repr
from collections import OrderedDict

_extract_fields_pattern = r"([a-z_A-Z]*=[\"'a-zA-Z0-9]*)"


class ReprTests(unittest.TestCase):
    def test_with_str(self):
        @gen_repr()
        class A(object):
            def __init__(self):
                self.something = "String"

        actual = repr(A())
        self.assertEquals(actual, u"<A (something='String')>")

    def test_with_unicode(self):
        @gen_repr()
        class A(object):
            def __init__(self):
                self.something = u"Unicode"

        actual = repr(A())
        self.assertEquals(actual, u"<A (something='Unicode')>")

    def test_with_int(self):
        @gen_repr()
        class A(object):
            def __init__(self):
                self.a_number = 42

        actual = repr(A())
        self.assertEquals(actual, u"<A (a_number=42)>")

    def test_with_bool(self):
        @gen_repr()
        class A(object):
            def __init__(self):
                self.a_bool = False

        actual = repr(A())
        self.assertEquals(actual, u"<A (a_bool=False)>")

    def test_with_none(self):
        @gen_repr()
        class A(object):
            def __init__(self):
                self.missing_thing = None

        actual = repr(A())
        self.assertEquals(actual, u"<A (missing_thing=None)>")

    def test_with_list(self):
        @gen_repr()
        class A(object):
            def __init__(self):
                self.names = [u"Peter", 12]

        actual = repr(A())
        self.assertEquals(actual, u"<A (names=['Peter', 12])>")

    def test_with_dict(self):
        @gen_repr()
        class A(object):
            def __init__(self):
                self.people = OrderedDict({u"Peter": 12, u"Warren": 6, u"Glen": 36.7})

        actual = repr(A())
        self.assertEquals(
            actual, u"<A (people={'Peter': 12, 'Warren': 6, 'Glen': 36.7})>"
        )

    def test_with_other_object_without_annotation(self):
        class A(object):
            def __init__(self):
                self.some_value = u"12"

        @gen_repr()
        class B(object):
            def __init__(self):
                self.ref = A()

        actual = repr(B())
        self.assertEquals(actual, u"<B (ref=<A (some_value='12')>)>")

    def test_with_other_object_with_annotation(self):
        @gen_repr()
        class A(object):
            def __init__(self):
                self.name = u"Peter"

        @gen_repr()
        class B(object):
            def __init__(self):
                self.person = A()

        actual = repr(B())
        self.assertEquals(actual, u"<B (person=<A (name='Peter')>)>")

    def test_with_private_fields(self):
        @gen_repr()
        class Http(object):
            def __init__(self):
                self._headers = {}
                self.status = 200

        actual = repr(Http())
        self.assertEquals(actual, u"<Http (status=200)>")

    def test_with_inherited_fields(self):
        class A(object):
            def __init__(self):
                self.field_a = 16

        @gen_repr()
        class B(A):
            def __init__(self):
                super(B, self).__init__()
                self.field_b = u"Hello"

        actual = repr(B())
        extracted = self._extract_fields_to_dict(actual)

        self.assertEquals(len(extracted.keys()), 2)
        self.assertEquals(extracted[u"field_a"], u"16")
        self.assertEquals(extracted[u"field_b"], u"'Hello'")

    def _extract_fields_to_dict(self, obj_repr):
        matches = re.findall(_extract_fields_pattern, obj_repr)
        if not matches:
            return {}

        result = {}
        for match in matches:
            split = match.split(u"=")
            self.assertEquals(len(split), 2)

            key = split[0]
            value = split[1]
            result[key] = value

        return result

    def test_with_multiple_fields(self):
        @gen_repr()
        class A(object):
            def __init__(self):
                self._something = u"Hide it"
                self.name = u"Python"
                self.language = u"Peter"

        actual = repr(A())
        extracted = self._extract_fields_to_dict(actual)
        self.assertEquals(len(extracted.keys()), 2)
        self.assertEquals(extracted[u"name"], u"'Python'")
        self.assertEquals(extracted[u"language"], u"'Peter'")

    def test_with_method(self):
        @gen_repr()
        class A(object):
            def __init__(self):
                self.some_field = None

            # noinspection PyMethodMayBeStatic
            def some_method(self):
                return u"I do nothing"

        actual = repr(A())
        self.assertEquals(actual, u"<A (some_field=None)>")

    def test_without_fields(self):
        @gen_repr()
        class A(object):
            pass

        actual = repr(A())
        self.assertEquals(actual, u"<A ()>")


if __name__ == "__main__":
    unittest.main()
