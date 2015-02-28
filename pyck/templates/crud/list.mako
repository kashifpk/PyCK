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

def get_col_value(col_name, R):
    parts = col_name.split('.')
    
    obj = R
    
    for p in parts:
        obj = getattr(obj, p)
        if not obj:
            return ''

    return obj
%>

<div class="panel panel-default">
  <!-- Default panel contents -->
  <div class="panel-heading">
    <h1>Displaying ${friendly_name}</h1>
  </div>
    
  <div class="panel-body">
    <div class="text-right">
    <%
    
    actions_str = ''
    for action in actions:
        css_class_str = ' class="btn btn-primary"'
        if 'css_class' in action:
            css_class_str = ' class="' + action['css_class'] + '"'
    
        actions_str += '<a href="' + action['link_url'] + '"' + css_class_str + '>' + insert_keyword_values(action['link_text']) + '</a> | '
    
    if '' != actions_str:
        actions_str = actions_str[:-2]
    %>
    ${actions_str | n}
    </div>
    
    %if len(pages)>1:
    
        <div class="text-right">
            <br />
            <%
            last_record = current_page*records_per_page;
            if last_record>total_records:
                  last_record=total_records
            %>
            Displaying records <b>${(current_page*records_per_page)-(records_per_page-1)}</b> to <b>${last_record}</b> of <b>${total_records}</b>
        </div>
        
    <ul class="pagination">
        %for p in pages:
        
            %if p==current_page:
                <li class="active"><a href="${'?p=' + str(p)}">${p}</a> </li>
            %else:
                <li><a href="${'?p=' + str(p)}">${p}</a></li> 
            %endif
            
        %endfor
        
        
    </ul>
    %endif
    
    <br />
  </div>
    
  <table class="table table-stripped table-hover table-bordered">
    %if records.count()>0:
    <thead>
        <tr>
        %for column in columns:
            <th style="font-weight: bold; font-size: larger;">${column.replace("_", " ").title()}</th>
        %endfor
        %if len(per_record_actions)>0:
            <th>   </th>
        %endif
        </tr>
    </thead>
    %endif

    <tbody>
    %for R in records:
        <tr>
        %for column in columns:
          
            %if column in list_field_args and 'display_field' in list_field_args[column]:
            <td>${get_col_value(list_field_args[column]['display_field'], R)}</td>
            %else:
            <td>
              
              %if isinstance(getattr(R, column), (str, unicode)):
                ${getattr(R, column)|n}
              %else:
                ${getattr(R, column)}
              %endif
            </td>
            %endif
            
        %endfor
        %if len(per_record_actions)>0:
            <td style="text-align: right;">
            <%
            actions_str = ''
            for action in per_record_actions:
                css_class_str = ''
                if 'css_class' in action:
                    css_class_str = ' class="' + action['css_class'] + '"'
                actions_str += '<a href="' + insert_per_rec_keyword_values(action['link_url'], R) + '"' + css_class_str + '>' + action['link_text'] + '</a> | '
            
            if '' != actions_str:
                actions_str = actions_str[:-2]
            %>
            ${actions_str | n}
            </td>
        %endif
        </tr>
    %endfor
    </tbody>
  </table>
</div>

