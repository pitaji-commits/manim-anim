from manim import *
from helper import MyNode


def move_code(scene, code_string="", language="python"):
    code = Code(code_string=code_string, language=language).scale(0.8)
    scene.play(Write(code))
    scene.wait(1)

    scene.play(code.animate.scale(0.6).to_edge(UR))
    scene.wait(1)


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

TREENODES = VGroup()
TREEEDGES = VGroup()


def get_tree_level(level=0):
    level = min(level, 4)

    tree_level = VGroup()
    if level == 0:
        tree_level.add(VGroup(TREENODES[0]))
    elif level == 1:
        tree_level.add(VGroup(TREENODES[1:3]), VGroup(TREEEDGES[:2]))
    elif level == 2:
        tree_level.add(VGroup(TREENODES[3:7]), VGroup(TREEEDGES[2:6]))
    elif level == 3:
        tree_level.add(VGroup(TREENODES[7:15]), VGroup(TREEEDGES[6:14]))
    else:
        tree_level.add(VGroup(TREENODES[15:]), VGroup(TREEEDGES[14:]))
            

class Test(Scene):
    def construct(self):
        rad = 0.25

        TREENODES.add(
            *[
                MyNode(value=data["data"], is_rect=False, radius=rad).move_to(
                    data["position"]
                )
                for data in TREEDATA
            ]
        )

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
