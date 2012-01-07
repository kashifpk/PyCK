# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1325895311.124668
_template_filename='/mnt/md0/MyWork/MyProjects/PyCK/pyck/forms/templates/form_as_p.mako'
_template_uri='form_as_p.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        errors_position = context.get('errors_position', UNDEFINED)
        labels_position = context.get('labels_position', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        for field in form:
            # SOURCE LINE 2

            field_errors = ''
            if field.errors:
                field_errors = '<span class="errors">'
                for e in field.errors:
                    field_errors += e + ', '
                
                field_errors = field_errors[:-2] + '</span>'
            
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['field_errors','e'] if __M_key in __M_locals_builtin_stored]))
            # SOURCE LINE 10
            __M_writer(u'\n<p>\n')
            # SOURCE LINE 12
            if 'top' == labels_position:
                # SOURCE LINE 13
                __M_writer(unicode(field.label))
                __M_writer(u'<br /> ')
                pass
            # SOURCE LINE 16
            if field_errors and 'top'==errors_position:
                # SOURCE LINE 17
                __M_writer(unicode(field_errors))
                __M_writer(u'<br /> ')
                pass
            # SOURCE LINE 20
            if 'left' == labels_position:
                # SOURCE LINE 21
                __M_writer(unicode(field.label))
                __M_writer(u' ')
                pass
            # SOURCE LINE 24
            if field_errors and 'left'==errors_position:
                # SOURCE LINE 25
                __M_writer(unicode(field_errors))
                __M_writer(u' ')
                pass
            # SOURCE LINE 28
            __M_writer(unicode(field))
            __M_writer(u' ')
            # SOURCE LINE 29
            if 'bottom' == labels_position:
                # SOURCE LINE 30
                __M_writer(u'<br />')
                __M_writer(unicode(field.label))
                __M_writer(u' ')
                pass
            # SOURCE LINE 33
            if field_errors and 'bottom'==errors_position:
                # SOURCE LINE 34
                __M_writer(u'<br />')
                __M_writer(unicode(field_errors))
                __M_writer(u' ')
                pass
            # SOURCE LINE 37
            if 'right' == labels_position:
                # SOURCE LINE 38
                __M_writer(unicode(field.label))
                __M_writer(u' ')
                pass
            # SOURCE LINE 41
            if field_errors and 'right'==errors_position:
                # SOURCE LINE 42
                __M_writer(unicode(field_errors))
                __M_writer(u' ')
                pass
            # SOURCE LINE 44
            __M_writer(u'</p>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


