from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag=tag, value=value, children=None,  props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Invalid HTML: No Value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

        # keys = self.props.keys()
        # html = f"<{self.tag}"
        # for key in keys:
        #     html+= f' {key}="{self.props[key]}"'
        # return html + f"<{self.value}</{self.tag}>"

    def __repr__(self):
        return f"tag: {self.tag}\n value: {self.value}\n props: {self.props}"

