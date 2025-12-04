from manim import *
from helper import MyVector
from helper import MyNode


def move_code(scene, code_string="", language="python"):
    code = Code(code_string=code_string, language=language).scale(0.8)
    scene.play(Write(code))
    scene.wait(1)

    scene.play(code.animate.scale(0.6).to_edge(UR))
    scene.wait(1)


POSITIONS = [
    [[0.0, 2.0, 0.0]],
    [([-3.0, 0.75, 0.0]), ([3.0, 0.75, 0.0])],
    [
        ([-4.5, -0.25, 0.0]),
        ([-1.5, -0.25, 0.0]),
        ([1.5, -0.25, 0.0]),
        ([4.5, -0.25, 0.0]),
    ],
    [
        ([-5.25, -1.125, 0.0]),
        ([-3.75, -1.125, 0.0]),
        ([-2.25, -1.125, 0.0]),
        ([-0.75, -1.125, 0.0]),
        ([0.75, -1.125, 0.0]),
        ([2.25, -1.125, 0.0]),
        ([3.75, -1.125, 0.0]),
        ([5.25, -1.125, 0.0]),
    ],
    [
        ([-5.625, -2.0, 0.0]),
        ([-4.875, -2.0, 0.0]),
        ([-4.125, -2.0, 0.0]),
        ([-3.375, -2.0, 0.0]),
        ([-2.625, -2.0, 0.0]),
        ([-1.875, -2.0, 0.0]),
        ([-1.125, -2.0, 0.0]),
        ([-0.375, -2.0, 0.0]),
        ([0.375, -2.0, 0.0]),
        ([1.125, -2.0, 0.0]),
        ([1.875, -2.0, 0.0]),
        ([2.625, -2.0, 0.0]),
        ([3.375, -2.0, 0.0]),
        ([4.125, -2.0, 0.0]),
        ([4.875, -2.0, 0.0]),
        ([5.625, -2.0, 0.0]),
    ],
]


class Test(Scene):
    def construct(self):
        levels = [
            [0],
            [1, 2],
            [3, 4, 5, 6],
            [7, 8, 9, 10, 11, 12, 13, 14],
            [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
        ]

        rad = 0.25

        nodes = VGroup()
        for lid, level in enumerate(levels):
            node_level = VGroup()
            for id, val in enumerate(level):
                node = MyNode(value=val, is_rect=False, radius=rad).move_to(
                    POSITIONS[lid][id]
                )
                node_level.add(node)
            nodes.add(node_level)

        self.play(Write(nodes))
        self.wait(1)

