from django import template
import random

register = template.Library()


class ABTest(template.Node):
    def __init__(self, avalue, bvalue):
        self.avalue = self.strip_quotes(avalue)
        self.bvalue = self.strip_quotes(bvalue)

    def render(self, context):
        return random.choice((self.avalue, self.bvalue))

    def strip_quotes(self, quoted_string):
        char_at_front = quoted_string[0]
        char_at_back = quoted_string[1]
        quotes = ['"', '\'']
        if char_at_front in quotes or char_at_back in quotes:
            return quoted_string[1:-1]
        else:
            return quoted_string



@register.tag
def ab(parser, token):
    tag_name, val1, val2 = token.split_contents()
    return ABTest(val1, val2)