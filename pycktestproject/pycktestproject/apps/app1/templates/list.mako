<%inherit file="/base.mako"/>

<%def name="title()">
The app1 app
</%def>

<div>
  <div class="middle align-center">
    <p class="app-welcome">
    <img src="${request.static_url(APP_BASE + ':static/webapp.png')}" />  Welcome to app1 app
    </p>
  </div>
</div>

<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />
