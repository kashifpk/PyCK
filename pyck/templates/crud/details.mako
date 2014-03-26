<%inherit file="${context.get('base_template')}" />
<%
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

<div class="panel panel-default">
    <div class="panel-heading">
        <h1>Displaying ${friendly_name}</h1>
    </div>

    <div class="panel-body">
        <div class="btn-group">
        <%
        actions_str = ''
        for action in actions:
            actions_str += '<a class="btn btn-primary" href="' + insert_per_rec_keyword_values(action['link_url'], R) + '">' + action['link_text'] + '</a>'
        
        %>
        ${actions_str | n}
        </div>
        
        <br /><br /><br />
        
        <table class="table table-striped table-hover table-bordered">
        %for column in columns:
            <tr>
                <th>${column}</th>
                <td>${getattr(R, column)}</td>
            </tr>
        %endfor
        </table>
        
    </div>
    
    
    
</div>
<br /><br /><br /><br /><br /><br /><br /><br />
