<%inherit file="${context.get('base_template')}" />
<%! import itertools %>
<%
row_class_cycler = itertools.cycle(['oddrow', 'evenrow']);
%>

<div class="align-center">
<h1>Welcome to Admin Section</h1>
<table>
%for model in models:
    <tr class="${row_class_cycler.next()}">
        <td>${model.__tablename__.replace("_", " ").title()}</td>
        <td></td>
    </tr>
%endfor
</table>
</div>
