from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Parent node cannot be without a tag")
        if self.children is None or len(self.children) == 0:
            raise ValueError(f"{self.tag}'s children are missing!")

        html_children = ""
        for child in self.children:
            html_children += child.to_html()

        return f"<{self.tag}>" + html_children + f"</{self.tag}>"
