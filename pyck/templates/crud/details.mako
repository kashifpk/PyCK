<%inherit file="/base.mako"/>
<%! import itertools %>
<%
row_class_cycler = itertools.cycle(['oddrow', 'evenrow']);
def insert_keyword_values(s):
    return s.replace('{friendly_name}', friendly_name)

def insert_per_rec_keyword_values(s, R):
    pk_val = ''
    for pk in primary_key_columns:
        pk_val += str(getattr(R, pk)) + ','
    if '' != pk_val:
        pk_val = pk_val[:-1]
    
    return s.replace('{PK}', pk_val)

%>

<div class="align-center">
    <h1>Displaying ${friendly_name}</h1>
    
    <div class="list-actions">
    <%
    actions_str = ''
    for action in actions:
        actions_str += '<a href="' + insert_per_rec_keyword_values(action['link_url'], R) + '">' + action['link_text'] + '</a> | '
    if '' != actions_str:
        actions_str = actions_str[:-2]
    %>
    ${actions_str | n}
    </div>
    
    <div class="align-left">
        <table>
        %for column in columns:
            <tr class="${row_class_cycler.next()}">
                <th>${column}</th>
                <td>${getattr(R, column)}</td>
            </tr>
        %endfor
        </table>
    </div>
</div>
<br /><br /><br /><br /><br /><br /><br /><br />