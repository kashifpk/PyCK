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
<br />${field.label} \
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