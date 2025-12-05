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

        status = [
            [True] * 2**0,
            [True] * 2**1,
            [True] * 2**2,
            [True] * 2**3,
            [True] * 2**4
        ]
        status[4][0] = False

        rad = 0.25

        nodes = VGroup()
        edges = VGroup()
        
        for lid, level in enumerate(levels):
            node_level = VGroup()
            for id, val in enumerate(level):
                node = MyNode(value=val, is_rect=False, radius=rad).move_to(
                    POSITIONS[lid][id]
                )
                node_level.add(node)
            nodes.add(node_level)

        for idx in range(1, len(levels)):
            cur_level  = nodes[idx]
            prev_level = nodes[idx-1]

            for i, node in enumerate(cur_level):
                parent = prev_level[i // 2]

                edge = Line(
                    parent.get_bottom(),
                    node.get_top(),
                    stroke_width=3,
                    color=WHITE
                )
                edges.add(edge)

        # make dead nodes disappear
        for lid, level_status in enumerate(status):
            for idx, alive in enumerate(level_status):
                if not alive:
                    nodes[lid][idx].set_opacity(0)
                
        self.play(Write(nodes), Write(edges))
        self.wait(1)

