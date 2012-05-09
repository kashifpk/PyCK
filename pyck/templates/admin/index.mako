<%inherit file="${context.get('base_template')}" />

<div class="align-center">
<h1>Welcome to Admin Section</h1>
<center>
<table style="width: 60%">
%for model in models:
    <tr class="${loop.cycle('oddrow', 'evenrow')}">
        <td style="width: 65%;">${model.__tablename__.replace("_", " ").title()}</td>
        <td style="text-align: right;">
            <a href="${request.route_url(route_prefix + model.__name__ + 'CRUD', action="add")}" class="button medium green">Add Record</a>
            <a href="${request.route_url(route_prefix + model.__name__ + 'CRUD_list')}" class="button medium black">View Records</a>
        </td>
    </tr>
%endfor
</table>
</center>
</div>
