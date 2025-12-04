from manim import *


class MyNode(VGroup):
    def __init__(
        self,
        value=" ",
        label=" ",
        label_pos=UP,
        is_label=True,
        is_rect=True,
        width=0.6,
        height=0.6,
        radius=0.3,
        font_size=20,
        **kwargs,
    ):
        super().__init__(**kwargs)

        self.value = value
        self.label = label
        self.label_pos = label_pos
        self.is_label = is_label
        self.is_rect = is_rect
        self.shape = (width, height) if is_rect else radius
        self.font_size = font_size
        self.label_font_size = font_size * 0.7

        node = (
            Rectangle(width=width, height=height).set_fill(BLACK, opacity=1)
            if is_rect
            else Circle(radius=radius, color=WHITE).set_fill(BLACK, opacity=1)
        )
        node_text = Text(str(value), font_size=font_size).move_to(node.get_center())
        node_label = Text(str(label), font_size=self.label_font_size).next_to(
            node, label_pos
        )

        if is_label:
            self.add(node, node_text, node_label)
        else:
            self.add(node, node_text)
