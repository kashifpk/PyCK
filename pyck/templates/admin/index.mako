<%inherit file="${context.get('base_template')}" />

<div class="align-center">
<h1>Welcome to Admin Section</h1>
<center>
<table class="table table-hover">
<tbody>
%if dict == type(models):
    %for appname, app_models in models.iteritems():
		%for model in models[appname]:
            <tr class="${loop.cycle('oddrow', 'evenrow')}">
                <td style="width: 65%;">${model.__tablename__.replace("_", " ").title()}</td>
                <td style="text-align: right;">
                    <a class="btn btn-success" href="${request.route_url(route_prefix + model.__name__ + 'CRUD', action="add")}" class="button medium green">Add Record</a>
                    <a class="btn btn-primary" href="${request.route_url(route_prefix + model.__name__ + 'CRUD_list')}" class="button medium black">View Records</a>
                </td>
            </tr>
        %endfor
    %endfor
%else:
    %for model in models:
        <tr class="${loop.cycle('oddrow', 'evenrow')}">
            <td style="width: 65%;">${model.__tablename__.replace("_", " ").title()}</td>
            <td style="text-align: right;">
                <a class="btn btn-success" href="${request.route_url(route_prefix + model.__name__ + 'CRUD', action="add")}" class="button medium green">Add Record</a>
                <a class="btn btn-primary" href="${request.route_url(route_prefix + model.__name__ + 'CRUD_list')}" class="button medium black">View Records</a>
            </td>
        </tr>
    %endfor
%endif
</tbody>
</table>
</center>
</div>
