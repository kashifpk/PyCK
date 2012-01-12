<%
num_cols = 2
num_rows = 2

if labels_position in ['left', 'right'] and errors_position in ['left', 'right']:
    num_cols = 3
    num_rows = 1
elif labels_position in ['top', 'bottom'] and errors_position in ['top', 'bottom']:
    num_cols = 1
    num_rows = 3
%>
%if include_table_tag:
<table>
%endif
%if form._use_csrf_protection:
    <input type="hidden" name="csrf_token" value="${form._csrf_token}" />
%endif
%if '_csrf' in form.errors:
    <tr><td class="errors" colspan="${num_cols}">${form.errors['_csrf'][0]}</td></tr>
%endif
% for field in form:
    <%
    field_label = '<td>' + str(field.label) + '</td>'
    field_content = '<td>' + str(field) + '</td>'
    field_errors = '<td></td>'
    if field.errors:
        field_errors = '<td class="errors">'
        for e in field.errors:
            field_errors += e + ', '
        
        field_errors = field_errors[:-2] + '</td>'
    %>
    %if 1 == num_rows:
    <tr>
        %if 'left'==labels_position:
        ${field_label}
        %endif
        %if 'left'==errors_position:
        ${field_errors}
        %endif
        ${field_content}
        %if 'right'==labels_position:
        ${field_label}
        %endif
        %if 'right'==errors_position:
        ${field_errors}
        %endif
    </tr>
    %elif 3 == num_rows:
    <tr>
    <td>
        <table>
        %if 'top'==labels_position:
        <tr>${field_label}</tr>
        %endif
        %if 'top'==errors_position:
        <tr>${field_errors}</tr>
        %endif
        <tr>${field_content}</tr>
        %if 'bottom'==labels_position:
        <tr>${field_label}</tr>
        %endif
        %if 'bottom'==errors_position:
        <tr>${field_errors}</tr>
        %endif
        </table>
    </td>
    </tr>
    %else: ## 2 rows and 2 cols
    <tr>
    <td>
        <table>
        %if 'top'==labels_position:
        <tr>${field_label}</tr> 
        <tr> \
        %elif 'left'==labels_position:
        <tr>${field_label} \
        %endif
        \
        %if 'top'==errors_position:
        <tr>${field_errors}</tr> 
        <tr> \
        %elif 'left'==errors_position:
        <tr>${field_errors} \
        %endif
        \
        ${field_content}
        \
        %if 'bottom'==labels_position:
        </tr>
        <tr>${field_label}</tr>
        %elif 'right'==labels_position:
        ${field_label}</tr>
        %endif
        \
        %if 'bottom'==errors_position:
        </tr>
        <tr>${field_errors}</tr>
        %elif 'right'==errors_position:
        ${field_errors}</tr>
        %endif
        </table>
    </td>
    </tr>
    %endif
    
% endfor
%if include_table_tag:
</table>
%endif