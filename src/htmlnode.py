class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_htlm(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props == None:
            return ""
        keys = self.props.keys()
        attr = ""
        for key in keys:
            attr += f' {key}="{self.props[key]}"'
        return attr

    def __repr__(self):
        return f"tag: {self.tag} value: {self.value} children: {self.children} props: {self.props}"

