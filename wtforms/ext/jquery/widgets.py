from wtforms.widgets import TableWidget, html_params, HTMLString

__all__ = ('JqTableWidget',)

class JqTableWidget(TableWidget):
    def __init__(self, with_table_tag=True, delete_row_link=True):
        super(JqTableWidget, self).__init__(with_table_tag)

        if delete_row_link:
            self.row_pattern = u'<tr><th>%s</th><td>%s%s</td><td><a href="#">x</a></td></tr>'
        else:
            self.row_pattern = u'<tr><th>%s</th><td>%s%s</td></tr>'

    def __call__(self, field, **kwargs):
        html = []
        if self.with_table_tag:
            kwargs.setdefault('id', field.id)
            html.append(u'<table %s>' % html_params(**kwargs))
        hidden = u''
        for subfield in field:
            if subfield.type == 'HiddenField':
                hidden += unicode(subfield)
            else:
                html.append(self.row_pattern % (unicode(subfield.label), hidden, unicode(subfield)))
                hidden = u''
        if self.with_table_tag:
            html.append(u'</table>')
        if hidden:
            html.append(hidden)
        return HTMLString(u''.join(html))