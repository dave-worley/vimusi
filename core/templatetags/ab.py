from django import template
import random

register = template.Library()


class ABTest(template.Node):
    def __init__(self, values):
        clean_values = [self.strip_quotes(value) for value in values]
        self.values = clean_values

    def render(self, context):
        context['choice'] = random.choice(self.values)
        return random.choice(self.values)

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
    split_token = token.split_contents()
    values = split_token[1:]
    return ABTest(values)