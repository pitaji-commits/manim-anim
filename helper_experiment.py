from manim import *

WIDTH           = 0.6
HEIGHT          = 0.6
RADIUS          = 0.25
FONT_SIZE       = 22
LABEL_FONT_SIZE = FONT_SIZE * 0.7

ARRAY_DATA = [{"data": i, "alive": False} for i in range(16)]


class Array(VGroup):
    pass

def _make_node(value=" ", label=" ", label_pos=UP, is_rect=True):
    node = (
        Rectangle(width=WIDTH, height=HEIGHT).set_fill(BLACK, opacity=1)
        if is_rect
        else Circle(radius=RADIUS, color=WHITE).set_fill(BLACK, opacity=1)
    )
    node_text = Text(str(value), font_size=FONT_SIZE).move_to(node.get_center())
    node_label = Text(str(label), font_size=LABEL_FONT_SIZE).next_to(
        node, label_pos
    )

    return VGroup(node, node_text, node_label)
    
        
        
def make_array(data=None, dir_right=True, index=True, index_pos=UP):
    pass


class Test(Scene):
    def construct(self):
        r = Rectangle(width=WIDTH, height=HEIGHT)
        t = Text(str(10)).move_to(r.get_center())
        g = VGroup(r, t)
        self.play(Write(g))
        self.wait(1)

        r.stretch_to_fit_width(4)
        self.wait(1)

        self.play(g.animate.to_edge(UP))
        self.wait(1)
