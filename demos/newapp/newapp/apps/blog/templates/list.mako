<%inherit file="/base.mako"/>

<%def name="title()">
The Blog app
</%def>

<div>
  <div class="middle align-center">
    <p class="app-welcome">
    <img src="${request.static_url(APP_BASE + ':static/webapp.png')}" />  Welcome to Blog app
    </p>
    <a href="${request.route_url(APP_NAME + '.add')}">Add a post</a> 
  </div>
  %for post in posts:
  <h1>${post.title}</h1>
  <p>${post.content}</p>
  <br /><br />
  %endfor
</div>

<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />