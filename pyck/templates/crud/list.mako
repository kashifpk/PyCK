<%!
from pyck.lib.urls import url_add, url_without
%>

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
    <h1>${friendly_name}</h1>
  </div>
    
  <div class="panel-body">
    <div class="row">
      <div class="col-md-8 col-lg-8 col-sm-8 col-xs-12">
        
        <form action="${url_without(request.current_route_url(), qs='q')}"
              method="GET">
          
          <input type="text" name="q" data-dojo-type="dijit/form/TextBox" placeholder="serach"
                 %if 'q' in request.GET:
                 value="${request.GET['q']}"
                 %endif
                  />
          <button type="submit" class="btn btn-primary">Search</button>
          <br />
          <a href="#search_controls"data-toggle="collapse">
            Search Options <span class="caret"></span>
          </a>
          <div class="collapse" id="search_controls">
            <div class="well">
            Search Fields:
            <div class="row">
            %for column in columns:
              
              <div class="col-md-3">
              <span class="label label-primary">
                <input type="checkbox" name="search_field_${column}"
                       data-dojo-type="dijit/form/CheckBox"
                       value="${column}"
                       %if 'search_field_{}'.format(column) in request.GET:
                       checked="checked"
                       %endif
                       />
                       ${column.replace("_", " ").title()}
              </span>
              </div>
            %endfor
            </div>
            </div>
          </div>
        </form>
      </div>
    
      <div class="col-md-4 col-lg-4 col-sm-4 col-xs-12 text-right">
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
            
                <li class="active">
                  <a href="${url_add(url_without(request.current_route_url(), qs='p'), qs='p={}'.format(p))}">
                  ${p}
                  </a>
                </li>
                
            %else:
                <li>
                  <a href="${url_add(url_without(request.current_route_url(), qs='p'), qs='p={}'.format(p))}">
                  ${p}
                  </a>
                </li> 
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
            <th style="font-weight: bold; font-size: larger; overflow: hidden; white-space: nowrap;">
            ${column.replace("_", " ").title()}
            <a href="${url_add(url_without(request.current_route_url(), qs=['sa', 'sd']), qs='sa=' + column)}" class="glyphicon glyphicon-arrow-down"></a>
            <a href="${url_add(url_without(request.current_route_url(), qs=['sa', 'sd']), qs='sd=' + column)}" class="glyphicon glyphicon-arrow-up"></a>
            </th>
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

