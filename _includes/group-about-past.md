{% for p in site.data.group.past %}* {{ p.name }}, {{ p.role }}, {{ p.period }}{% if p.about %}, {{ p.about }}{% endif %}
{% endfor %}
