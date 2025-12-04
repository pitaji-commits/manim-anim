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

        rad = 0.25
        buff=0.5

        nodes = VGroup()
        for level in levels:
            node_level = VGroup()
            node_level.add(
                *[MyNode(value=d, is_rect=False, radius=rad) for d in level]
            ).arrange(RIGHT)
            nodes.add(node_level)
        nodes.arrange(DOWN, buff=buff)

        nodes[3][0].next_to(nodes[4][0], UP*1.5).shift(RIGHT*buff).shift(LEFT * rad/2)
        nodes[3][1].next_to(nodes[4][2], UP*1.5).shift(RIGHT*buff).shift(LEFT * rad/2)
        nodes[3][2].next_to(nodes[4][4], UP*1.5).shift(RIGHT*buff).shift(LEFT * rad/2)
        nodes[3][3].next_to(nodes[4][6], UP*1.5).shift(RIGHT*buff).shift(LEFT * rad/2)
        nodes[3][4].next_to(nodes[4][8], UP*1.5).shift(RIGHT*buff).shift(LEFT * rad/2)
        nodes[3][5].next_to(nodes[4][10], UP*1.5).shift(RIGHT*buff).shift(LEFT * rad/2)
        nodes[3][6].next_to(nodes[4][12], UP*1.5).shift(RIGHT*buff).shift(LEFT * rad/2)
        nodes[3][7].next_to(nodes[4][14], UP*1.5).shift(RIGHT*buff).shift(LEFT * rad/2)

        nodes[2][0].next_to(nodes[4][1], UP).shift(RIGHT*buff).shift(LEFT * rad/2).shift(UP)
        nodes[2][1].next_to(nodes[4][5], UP).shift(RIGHT*buff).shift(LEFT * rad/2).shift(UP)
        nodes[2][2].next_to(nodes[4][9], UP).shift(RIGHT*buff).shift(LEFT * rad/2).shift(UP)
        nodes[2][3].next_to(nodes[4][13], UP).shift(RIGHT*buff).shift(LEFT * rad/2).shift(UP)

        nodes[1][0].next_to(nodes[4][3], UP).shift(RIGHT*buff).shift(LEFT * rad/2).shift(2*UP)
        nodes[1][1].next_to(nodes[4][11], UP).shift(RIGHT*buff).shift(LEFT * rad/2).shift(2*UP)
        
        self.play(Write(nodes))
        self.wait(1)
