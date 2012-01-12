%if form._use_csrf_protection:
<input type="hidden" name="csrf_token" value="${form._csrf_token}" />
%endif
%if '_csrf' in form.errors:
<div class="errors">${form.errors['_csrf'][0]}</div><br />
%endif
% for field in form:
<%
field_errors = ''
if field.errors:
    field_errors = '<span class="errors">'
    for e in field.errors:
        field_errors += e + ', '
    
    field_errors = field_errors[:-2] + '</span>'
%>
<p>
% if 'top' == labels_position:
${field.label}<br /> \
% endif
\
% if field_errors and 'top'==errors_position:
${field_errors}<br /> \
% endif
\
% if 'left' == labels_position:
${field.label} \
% endif
\
% if field_errors and 'left'==errors_position:
${field_errors} \
% endif
\
${field} \
% if 'bottom' == labels_position:
${field.label} \
% endif
\
% if field_errors and 'bottom'==errors_position:
<br />${field_errors} \
% endif
\
% if 'right' == labels_position:
${field.label} \
% endif
\
% if field_errors and 'right'==errors_position:
${field_errors} \
% endif
</p>
% endfor