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


def draw_tree(scene):
    if not TREEDATA[0]["alive"]:
        return

    scene.play(Write(TREENODES[0]), run_time=0.5)

    for idx, data in enumerate(TREEDATA[1:]):
        if data["alive"]:
            scene.play(Write(TREENODES[idx + 1]), Write(TREEEDGES[idx]), run_time=0.5)


def make_tree(scene, data=None, at=None):
    data = list(range(0, len(TREEDATA))) if data is None else data
    at = list(range(len(data))) if at is None else at

    for idx, val in zip(at, data):
        TREEDATA[idx]["data"] = val
        TREEDATA[idx]["alive"] = True
        TREENODES[idx].set_value(val)

        if idx > 0 and not TREEDATA[(idx - 1) // 2]["alive"]:
            TREEDATA[idx]["alive"] = False

    draw_tree(scene)


def focus_parent_group(parent=0):
    if parent >= len(TREENODES):
        return VGroup()

    grp = VGroup()
    grp.add(TREENODES[parent].focus())

    left = 2 * parent + 1
    right = 2 * parent + 2

    if left < len(TREENODES) and TREEDATA[left]["alive"]:
        grp.add(TREENODES[left].focus(color=BLUE))

    if right < len(TREENODES) and TREEDATA[right]["alive"]:
        grp.add(TREENODES[right].focus(color=RED))

    return grp


def swap_nodes(scene, fromx, toy):
    if fromx == toy:
        return

    arcup = ArcBetweenPoints(
        TREENODES[fromx].get_cell().get_center(),
        TREENODES[toy].get_cell().get_center(),
        angle=-PI,
    )
    arcdwn = ArcBetweenPoints(
        TREENODES[toy].get_cell().get_center(),
        TREENODES[fromx].get_cell().get_center(),
        angle=-PI,
    )
    scene.play(
        MoveAlongPath(TREENODES[fromx].get_value(), arcup),
        MoveAlongPath(TREENODES[toy].get_value(), arcdwn),
    )

    TREEDATA[fromx]["data"], TREEDATA[toy]["data"] = (
        TREEDATA[toy]["data"],
        TREEDATA[fromx]["data"],
    )
    TREENODES[fromx].set_value(TREEDATA[fromx]["data"])
    TREENODES[toy].set_value(TREEDATA[toy]["data"])


class Tree:
    def __init__(self, scene, data=None, at=None, scale=0.8):
        self.treedata = TREEDATA
        self.scene = scene
        self.rad = 0.25
        self.scale=scale

        self.nodes = self._build_nodes()
        self.edges = self._build_edges()

        VGroup(self.nodes, self.edges).scale(scale)

        self._make_tree(data, at)

    def _build_nodes(self):
        return VGroup(
            *[
                MyNode(value=data["data"], is_rect=False, radius=self.rad).move_to(
                    data["position"]
                )
                for data in self.treedata
            ]
        )

    def _build_edges(self):
        edges = VGroup()
        for i, node in enumerate(self.nodes[1:], start=1):
            parent = self.nodes[(i - 1) // 2]
            edge = Line(
                parent.get_bottom(), node.get_top(), stroke_width=3, color=WHITE
            )
            edges.add(edge)
        return edges

    def _make_tree(self, data=None, at=None):
        data = list(range(0, len(self.nodes))) if data is None else data
        at = list(range(len(data))) if at is None else at

        for idx, val in zip(at, data):
            self.treedata[idx]["data"] = val
            self.treedata[idx]["alive"] = True
            self.nodes[idx].set_value(val)

            if idx > 0 and not self.treedata[(idx - 1) // 2]["alive"]:
                self.treedata[idx]["alive"] = False

    def treegrp(self):
        return VGroup(self.nodes, self.edges)

    def focus(self, node=0):
        if node >= len(self.nodes):
            return VGroup()

        grp = VGroup()
        grp.add(self.nodes[node].focus())

        left = 2 * node + 1
        right = 2 * node + 2

        if left < len(self.nodes) and self.treedata[left]["alive"]:
            grp.add(self.nodes[left].focus(color=BLUE))

        if right < len(self.nodes) and self.treedata[right]["alive"]:
            grp.add(self.nodes[right].focus(color=RED))

        return grp


    def draw(self):
        if not self.treedata[0]["alive"]:
            return

        self.scene.play(Write(self.nodes[0]), run_time=0.5)

        for idx, data in enumerate(self.treedata[1:]):
            if data["alive"]:
                self.scene.play(
                    Write(self.nodes[idx + 1]), Write(self.edges[idx]), run_time=0.5
                )

    def swap_nodes(self, fromx, toy):
        if fromx == toy:
            return

        arcup = ArcBetweenPoints(
            self.nodes[fromx].get_cell().get_center(),
            self.nodes[toy].get_cell().get_center(),
            angle=-PI,
        )
        arcdwn = ArcBetweenPoints(
            self.nodes[toy].get_cell().get_center(),
            self.nodes[fromx].get_cell().get_center(),
            angle=-PI,
        )
        self.scene.play(
            MoveAlongPath(self.nodes[fromx].get_value(), arcup),
            MoveAlongPath(self.nodes[toy].get_value(), arcdwn),
        )
        
        self.treedata[fromx]["data"], self.treedata[toy]["data"] = (
            self.treedata[toy]["data"],
            self.treedata[fromx]["data"],
        )
        self.treedata[fromx].set_value(self.treedata[fromx]["data"])
        self.treedata[toy].set_value(self.treedata[toy]["data"])



class Test(Scene):
    def construct(self):
        # rad = 0.25

        # TREENODES.add(
        #     *[
        #         MyNode(value=data["data"], is_rect=False, radius=rad).move_to(
        #             data["position"]
        #         )
        #         for data in TREEDATA
        #     ]
        # )

        # for i, node in enumerate(TREENODES[1:], start=1):
        #     parent_index = (i - 1) // 2
        #     parent = TREENODES[parent_index]

        #     edge = Line(
        #         parent.get_bottom(), node.get_top(), stroke_width=3, color=WHITE
        #     )
        #     TREEEDGES.add(edge)

        # make_tree(self, data=[10, 3, 2, 4, 5, 1])
        # self.wait(1)

        root = Tree(self)
        root.draw()

        self.wait(1)

        self.play(root.treegrp().animate.to_edge(LEFT))
        self.wait(1)
