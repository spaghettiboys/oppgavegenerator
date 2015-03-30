# predefined tables to be rendered with django-tables
__author__ = 'eirikk'

import django_tables2 as tables
from oppgavegen.models import Template

class TemplateTable(tables.Table):
    View = tables.TemplateColumn('<a href="../task/{{record.id}}">View</a>', orderable=False)

    class Meta:
        model = Template
        attrs = {"class": "paleblue"} # add class="paleblue" (table theme) to <table> tag
        # fields to include in table (displayed in this order)
        fields = ("id","question_text", "creator", "topic", "type", "rating")

class BootstrapTemplateTable(tables.Table):
    View = tables.TemplateColumn('<a href="../task/{{record.id}}/">View</a>', orderable=False)

    class Meta:
        model = Template
        template = ("bstable.html")
        #attrs = {"class": "paleblue"} # add class="paleblue" (table theme) to <table> tag
        # fields to include in table (displayed in this order)
        fields = ("id","question_text", "creator", "topic", "type", "rating")

