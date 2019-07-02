# -*- coding: utf-8 -*-

import sys
import inspect


__author__ = u"Peter Morawski"
__version__ = u"0.1.0"

_PY2 = 2


def gen_repr():
    """
    """

    def decorator(target_cls):
        class GenReprWrapper(target_cls):
            def __repr__(self):
                return _GenReprUtils.get_object_repr(self)

        return GenReprWrapper

    return decorator


class _GenReprUtils(object):
    @classmethod
    def get_object_repr(cls, obj):
        return u"<{class_name} ({fields})>".format(
            class_name=obj.__name__,
            fields=u", ".join(_GenReprUtils.extract_public_field_reprs(obj)),
        )

    @classmethod
    def extract_public_fields(cls, target):
        result = {}
        if not len(target.__dict__.keys()):
            return result

        for key, value in target.__dict__.items():
            if not key.startswith(u"_") and not key.startswith(u"__"):
                result[key] = value

        return result

    @classmethod
    def extract_public_field_reprs(cls, target):
        public_fields = cls.extract_public_fields(target)
        if not public_fields:
            return []

        result = []
        for key, value in public_fields.items():
            result.append(u"{}={}".format(key, cls.serialize_value(value)))

        return result

    @classmethod
    def serialize_value(cls, value):
        if sys.version_info.major == _PY2:
            if isinstance(value, unicode):
                return u"'{}'".format(value)

        if isinstance(value, str):
            return u"'{}'".format(value)

        if isinstance(value, dict):
            return u"{{{}}}".format(
                u", ".join(
                    [
                        u"{}: {}".format(
                            cls.serialize_value(key), cls.serialize_value(value)
                        )
                        for key, value in value.items()
                    ]
                )
            )

        if cls.value_is_iterable(value):
            return u"[{}]".format(
                u", ".join(cls.serialize_value(item) for item in value)
            )

        if inspect.isclass(value):
            return

        return u"{}".format(value)

    @classmethod
    def value_is_iterable(cls, value):
        try:
            iter(value)
        except TypeError:
            return False

        return True
