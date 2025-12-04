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
        levels = [
            [0],
            [1, 2],
            [3, 4, 5, 6],
            [7, 8, 9, 10, 11, 12, 13, 14],
            [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
        ]

        nodes = VGroup()
        for level in levels:
            node_level = VGroup()
            node_level.add(
                *[MyNode(value=d, is_rect=False, radius=0.25) for d in level]
            ).arrange(RIGHT)
            nodes.add(node_level)
        nodes.arrange(DOWN, buff=0.5)

        self.play(Write(nodes))
        self.wait(1)
