## -*- coding: utf-8 -*-
%if form._use_csrf_protection:
<input type="hidden" name="csrf_token" value="${form._csrf_token}" />
%endif
%if '_csrf' in form.errors:
<div class="danger">${form.errors['_csrf'][0]}</div><br />
%endif
% for field in form:
<%
field_errors = ''
if field.errors:
    field_errors = '<span class="danger">'
    for e in field.errors:
        field_errors += e + ', '
    
    field_errors = field_errors[:-2] + '</span>'
%>

<div class="form-group">
    <div class="col-sm-3">
    ${field.label}    
    </div>
    
    <div class="col-sm-9">
      ${field(class_="form-control")}
    </div>
</div>
% endfor
