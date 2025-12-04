from manim import *
from helper import MyVector



def move_code(scene, code_string="", language="python"):
    code = Code(code_string=code_string, language=language).scale(0.8)
    scene.play(Write(code))
    scene.wait(1)

    scene.play(code.animate.scale(0.6).to_edge(UR))
    scene.wait(1)
    
    
class Test(Scene):
    def construct(self):
        sq = Square()
        self.play(Write(sq))
        self.wait(1)
