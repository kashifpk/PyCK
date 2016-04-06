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

<div class="panel panel-primary">
    <div class="panel-heading">
        <h1>Displaying ${friendly_name}</h1>
    </div>

    <div class="panel-body">
        <div class="btn-group">
        <%
        actions_str = ''
        for action in actions:
            css_class_str = ' class="btn btn-primary"'
            if 'css_class' in action:
                css_class_str = ' class="' + action['css_class'] + '"'
            
            actions_str += '<a href="' + insert_per_rec_keyword_values(action['link_url'], R) + '"' + css_class_str + '>' + action['link_text'] + '</a>'
            
            
        
        %>
        ${actions_str | n}
        </div>
        
        <br /><br /><br />
        
        <table class="table table-striped table-hover table-bordered">
        %for column in columns:
            <tr>
                <th>
                %if field_translations and column in field_translations and 'header' in field_translations[column]:
                    ${field_translations[column]['header']}
                %else:
                    ${column.replace("_", " ").title()}
                %endif
                </th>
                <td>
                <%
                col_value = getattr(R, column)
                if field_translations and column in field_translations:
                  col_value = field_translations[column]['translator'](col_value)
                endif
                %>

                %if isinstance(col_value, str):
                  ${col_value|n}
                %else:
                  ${col_value}
                %endif
                </td>
            </tr>
        %endfor
        </table>
        
    </div>
    
    
    
</div>
<br /><br /><br /><br /><br /><br /><br /><br />
