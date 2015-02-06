<table class="table table-condensed table-hover table-stripped">
%for k, v in items.items():
    ## Ignore static routes (route name starts with __)
    <%
    if ignore_prefix is not None and k.startswith(ignore_prefix):
        continue
    %>
    <tr>
        <td>
            <input type="checkbox" data-dojo-type="dijit/form/CheckBox" name="routenames" value="${k}" />
            ${v}
        </td>
    </tr>
    
%endfor
</table>