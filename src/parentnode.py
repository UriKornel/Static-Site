from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag=tag,value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent node cannot be without a tag")
        if self.children is None:
            raise ValueError(f"invalid html: no children")

        html_children = ""
        for child in self.children:
            html_children += child.to_html()

        return f"<{self.tag}{self.props_to_html()}>{html_children}</{self.tag}>"
        # return f"<{self.tag}>" + html_children + f"</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
