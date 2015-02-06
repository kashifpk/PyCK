<%def name="show_items(records, ignore_prefix, indent='', parent_key=None)">
    <%
    extra_css_class = ""
    table_id = ""
    if parent_key:
        extra_css_class = 'collapse'
        table_id = 'id="{}_subitems"'.format(parent_key)
    %>
    <table class="table table-condensed table-hover table-stripped ${extra_css_class}" ${table_id}>
    %for k, v in records.items():
        ## Ignore static routes (route name starts with __)
        <%
        if ignore_prefix is not None and k.startswith(ignore_prefix):
            continue
        %>
        
        %if not isinstance(v, dict):
            <tr>
                <td>
                    %if indent:
                    ${indent}
                    %endif
                    <input type="checkbox" data-dojo-type="dijit/form/CheckBox" name="routenames" value="${k}" />
                    ${v}
                </td>
            </tr>
        %else:
            <tr>
                <td class="bg-info" data-toggle="collapse" data-target="#${k}_subitems">
                    ${k}
                </td>
            </tr>
            <tr>
                <td>
                    ${show_items(v, ignore_prefix=ignore_prefix, parent_key=k, indent=indent+'&nbsp;'*4)}
                </td>
            </tr>
        %endif
    %endfor
    </table>
</%def>

${show_items(items, ignore_prefix, '')}
