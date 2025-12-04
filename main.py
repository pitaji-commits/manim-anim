from helper import MyVector



MERGE_2_CODE = """
def merge(data, low, mid, high):
    left = data[:mid]
    right = data[mid:]
    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            data[k] = left[i]
            i += 1
        else:
            data[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        data[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        data[k] = right[j]
        j += 1
        k += 1
"""


def move_code(scene, code_string="", language="python"):
    code = Code(code_string=code_string, language=language).scale(0.8)
    scene.play(Write(code))
    scene.wait(1)

    scene.play(code.animate.scale(0.6).to_edge(UR))
    scene.wait(1)
    
    
class Test(Scene):
    def construct(self):
        move_code(self, MERGE_2_CODE)

        data = [5, 9, 12, 13, 7, 8, 10]
        sdata = sorted(data)
        
        vec  = MyVector(data=data).shift(LEFT).shift(UP*2)
        svec = MyVector(data=[" "]*len(data), index=False).next_to(vec, DOWN*1.5)

        ibg = vec.set_focus(0,1,color=YELLOW,buff=0)
        jbg = vec.set_focus(4, 5,color=YELLOW,buff=0)
        kbg = svec.set_focus(0,1,color=YELLOW,buff=0)
        width = vec[0].get_cell().width
        
        self.play(Write(vec))
        self.play(
            Write(vec.set_focus(0, 4, color=BLUE)),
            Write(vec.set_focus(4, color=RED)),
        )
        self.wait(1)

        self.play(Write(svec))
        self.wait(1)

        self.play(Write(ibg), Write(jbg), Write(kbg))
        self.wait(1)

        svec.set_value(sdata[0], 0)
        self.play(ibg.animate.shift(RIGHT*width), kbg.animate.shift(RIGHT*width))
        self.wait(0.5)
        
        svec.set_value(sdata[1], 1)
        self.play(jbg.animate.shift(RIGHT*width), kbg.animate.shift(RIGHT*width))
        self.wait(0.5)
        
        svec.set_value(sdata[2], 2)
        self.play(jbg.animate.shift(RIGHT*width), kbg.animate.shift(RIGHT*width))
        self.wait(0.5)

        svec.set_value(sdata[3], 3)
        self.play(ibg.animate.shift(RIGHT*width), kbg.animate.shift(RIGHT*width))
        self.wait(0.5)
        
        svec.set_value(sdata[4], 4)
        self.play(FadeOut(jbg), kbg.animate.shift(RIGHT*width))
        self.wait(0.5)

        svec.set_value(sdata[5], 5)
        self.play(ibg.animate.shift(RIGHT*width), kbg.animate.shift(RIGHT*width))
        self.wait(0.5)
        
        svec.set_value(sdata[6], 6)
        self.play(FadeOut(ibg), FadeOut(kbg))
        self.wait(1)

        self.play(Write(svec.set_focus()))
        self.wait(2)
        
