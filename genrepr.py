# -*- coding: utf-8 -*-


__author__ = u"Peter Morawski"
__version__ = u"0.1.0"


def gen_repr():
    def decorator(target_cls):
        class GenReprWrapper(target_cls):
            def __repr__(self):
                return "Peter"

        return GenReprWrapper

    return decorator


class _GenReprUtils(object):
    @classmethod
    def extract_public_fields(cls, target):
        # TODO(pmo): Needs to be implemented
        pass
