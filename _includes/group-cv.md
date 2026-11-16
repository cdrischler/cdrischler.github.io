{% assign postdocs = site.data.group.current | where: "role", "postdoctoral researcher" -%}
{% assign grads = site.data.group.current | where: "role", "graduate student" -%}
{% assign ugrads = site.data.group.current | where: "role", "undergraduate student" -%}
**Current group members:**  
{% for p in postdocs %}{% if forloop.first %}* Postdoctoral researcher{% if postdocs.size > 1 %}s{% endif %}:
{% endif %}  * {{ p.name }}, {{ p.start }}–present, {{ p.cv }}
{% endfor %}{% for p in grads %}{% if forloop.first %}* Graduate student{% if grads.size > 1 %}s{% endif %}:
{% endif %}  * {{ p.name }}, {{ p.start }}–present, {{ p.cv }}
{% endfor %}{% for p in ugrads %}{% if forloop.first %}* Undergraduate student{% if ugrads.size > 1 %}s{% endif %}:
{% endif %}  * {{ p.name }}, {{ p.start }}–present, {{ p.cv }}
{% endfor %}
**Former group members:**  
{% for p in site.data.group.past %}* {{ p.name }}, {{ p.role }}, {{ p.period }}, {{ p.cv }}
{% endfor %}
