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
        actions_str += '<a href="' + action['link_url'] + '">' + insert_keyword_values(action['link_text']) + '</a> | '
    if '' != actions_str:
        actions_str = actions_str[:-2]
    %>
    ${actions_str | n}
    </div>
    
    %if pages>1:
    <div class="page_links">
        Pages: 
        %for i in range(pages):
        <a href="${'?p=' + str(i+1)}">${i+1}</a> 
        %endfor
    </div>
    %endif
    
    <div class="align-left">
        <table>
        %if records.count()>0:
            <tr class="tr_heading">
            %for column in columns:
                <th>${column.title()}</th>
            %endfor
            %if len(per_record_actions)>0:
                <th>   </th>
            %endif
            </tr>
        %endif
        %for R in records:
            <tr class="${row_class_cycler.next()}">
            %for column in columns:
                <td>${getattr(R, column)}</td>
            %endfor
            %if len(per_record_actions)>0:
                <td>
                <%
                actions_str = ''
                for action in per_record_actions:
                    actions_str += '<a href="' + insert_per_rec_keyword_values(action['link_url'], R) + '">' + action['link_text'] + '</a> | '
                if '' != actions_str:
                    actions_str = actions_str[:-2]
                %>
                ${actions_str | n}
                </td>
            %endif
            </tr>
        %endfor
        </table>
    </div>
</div>
<br /><br /><br /><br /><br /><br /><br /><br />