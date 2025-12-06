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


TREEDATA = [
    {"data": 1, "alive": False, "position": [0.0, 2.0, 0.0]},
    {"data": 2, "alive": False, "position": [-3.0, 0.75, 0.0]},
    {"data": 3, "alive": False, "position": [3.0, 0.75, 0.0]},
    {"data": 4, "alive": False, "position": [-4.5, -0.25, 0.0]},
    {"data": 5, "alive": False, "position": [-1.5, -0.25, 0.0]},
    {"data": 6, "alive": False, "position": [1.5, -0.25, 0.0]},
    {"data": 7, "alive": False, "position": [4.5, -0.25, 0.0]},
    {"data": 8, "alive": False, "position": [-5.25, -1.125, 0.0]},
    {"data": 9, "alive": False, "position": [-3.75, -1.125, 0.0]},
    {"data": 10, "alive": False, "position": [-2.25, -1.125, 0.0]},
    {"data": 11, "alive": False, "position": [-0.75, -1.125, 0.0]},
    {"data": 12, "alive": False, "position": [0.75, -1.125, 0.0]},
    {"data": 13, "alive": False, "position": [2.25, -1.125, 0.0]},
    {"data": 14, "alive": False, "position": [3.75, -1.125, 0.0]},
    {"data": 15, "alive": False, "position": [5.25, -1.125, 0.0]},
    {"data": 16, "alive": False, "position": [-5.625, -2.0, 0.0]},
    {"data": 17, "alive": False, "position": [-4.875, -2.0, 0.0]},
    {"data": 18, "alive": False, "position": [-4.125, -2.0, 0.0]},
    {"data": 19, "alive": False, "position": [-3.375, -2.0, 0.0]},
    {"data": 20, "alive": False, "position": [-2.625, -2.0, 0.0]},
    {"data": 21, "alive": False, "position": [-1.875, -2.0, 0.0]},
    {"data": 22, "alive": False, "position": [-1.125, -2.0, 0.0]},
    {"data": 23, "alive": False, "position": [-0.375, -2.0, 0.0]},
    {"data": 24, "alive": False, "position": [0.375, -2.0, 0.0]},
    {"data": 25, "alive": False, "position": [1.125, -2.0, 0.0]},
    {"data": 26, "alive": False, "position": [1.875, -2.0, 0.0]},
    {"data": 27, "alive": False, "position": [2.625, -2.0, 0.0]},
    {"data": 28, "alive": False, "position": [3.375, -2.0, 0.0]},
    {"data": 29, "alive": False, "position": [4.125, -2.0, 0.0]},
    {"data": 30, "alive": False, "position": [4.875, -2.0, 0.0]},
    {"data": 31, "alive": False, "position": [5.625, -2.0, 0.0]},
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
            [True] * 2**4,
        ]

        rad = 0.25

        # nodes = VGroup()
        # edges = VGroup()

        # for lid, level in enumerate(levels):
        #     node_level = VGroup()
        #     for id, val in enumerate(level):
        #         node = MyNode(value=val, is_rect=False, radius=rad).move_to(
        #             POSITIONS[lid][id]
        #         )
        #         node_level.add(node)
        #     nodes.add(node_level)

        # for idx in range(1, len(levels)):
        #     cur_level  = nodes[idx]
        #     prev_level = nodes[idx-1]

        #     for i, node in enumerate(cur_level):
        #         parent = prev_level[i // 2]

        #         edge = Line(
        #             parent.get_bottom(),
        #             node.get_top(),
        #             stroke_width=3,
        #             color=WHITE
        #         )
        #         edges.add(edge)

        # # make dead nodes disappear
        # for lid, level_status in enumerate(status):
        #     for idx, alive in enumerate(level_status):
        #         if not alive:
        #             nodes[lid][idx].set_opacity(0)

        # self.play(Write(nodes), Write(edges))
        # self.wait(1)

        TREENODES = VGroup(
            *[
                MyNode(value=data["data"], is_rect=False, radius=rad).move_to(
                    data["position"]
                )
                for data in TREEDATA
            ]
        )

        TREEEDGES = VGroup()
        for i, node in enumerate(TREENODES[1:], start=1):
            parent_index = (i - 1) // 2
            parent = TREENODES[parent_index]
            
            edge = Line(
                parent.get_bottom(),
                node.get_top(),
                stroke_width=3,
                color=WHITE
            )
            TREEEDGES.add(edge)



        self.play(Write(TREENODES), Write(TREEEDGES))
        self.wait(1)
