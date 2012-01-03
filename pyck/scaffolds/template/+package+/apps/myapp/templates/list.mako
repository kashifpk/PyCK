<%inherit file="/base.mako"/>

<%def name="title()">
The PyCK Blog app
</%def>

<div >
  <div class="middle align-center">
    <p class="app-welcome">
    <img src="${request.static_url(APP_BASE + ':static/webapp.png')}" /> Welcome to Blog app
    </p>
  </div>
  <h1>${post.title}</h1>
  <p>${post.content}</p>
</div>
<br /><br /><br /><br /><br /><br /><br /><br /><br /><br />

