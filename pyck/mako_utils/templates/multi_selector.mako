<%def name="show_items(records, fname=None, ignore_prefix=None, indent='', parent_key=None)">
    <%
    extra_css_class = ""
    table_id = ""
    if parent_key:
        extra_css_class = 'collapse'
        table_id = 'id="{}_subitems"'.format(parent_key)
    %>
    <table class="table table-condensed table-hover table-striped ${extra_css_class}" ${table_id}>
    %for k, v in records.items():
        ## Ignore static routes (route name starts with __)
        <%
        if ignore_prefix is not None and k.startswith(ignore_prefix):
            continue
        %>
        
        %if not isinstance(v, dict):
            <tr>
                <td colspan="2">
                    %if indent:
                    ${indent}
                    %endif
                    <input type="checkbox" data-dojo-type="dijit/form/CheckBox" name="${fname}" id="" value="${k}" />
                    ${v}
                </td>
            </tr>
        %else:
            <tr>
                <td style="width: 4%;">
                    <input data-dojo-type="dijit/form/CheckBox" id="${k}_parent" type="checkbox" onclick="toggle_selection('${k}_parent', '#${k}_subitems');" />
                </td>
                <td class="bg-info" data-toggle="collapse" data-target="#${k}_subitems">
                    <b>${k}</b>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    ${show_items(records=v, fname=fname, ignore_prefix=ignore_prefix, parent_key=k, indent=indent+'&nbsp;'*4)}
                </td>
            </tr>
        %endif
    %endfor
    </table>
    
    
</%def>

<script type="application/x-javascript">
    //dojo.query('#main2 > input[type=checkbox]:checked')
    
    function toggle_selection(chkbox, target_container){
        require([ "dijit/registry", "dojo/query"], function(registry, query){  
            query(target_container + " input").forEach(function(node, index, arr){
              registry.byId(node.id).set("checked", registry.byId(chkbox).checked);
            });
          });
    }
</script>

${show_items(items, field_name, ignore_prefix, '')}
