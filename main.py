from manim import *
from helper import MyVector
from helper import MyNode


def move_code(scene, code_string="", language="python"):
    code = Code(code_string=code_string, language=language).scale(0.8)
    scene.play(Write(code))
    scene.wait(1)

    scene.play(code.animate.scale(0.6).to_edge(UR))
    scene.wait(1)


class Test(Scene):
    def construct(self):
        data = [1, 2, 3, 4, 5, 6, 7, 8]
        nodes = VGroup(*[MyNode(value=val, is_rect=False) for val in data]).arrange(
            RIGHT
        )
        self.play(Write(nodes))
        self.wait(1)
