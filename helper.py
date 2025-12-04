from manim import *


class MyNode(VGroup):
    def __init__(
        self,
        value=" ",
        label=" ",
        label_pos=UP,
        is_label=True,
        is_rect=True,
        width=0.6,
        height=0.6,
        radius=0.3,
        font_size=20,
        **kwargs,
    ):
        super().__init__(**kwargs)

        self.value = value
        self.label = label
        self.label_pos = label_pos
        self.is_label = is_label
        self.is_rect = is_rect
        self.shape = (width, height) if is_rect else radius
        self.font_size = font_size
        self.label_font_size = font_size * 0.7

        node = (
            Rectangle(width=width, height=height).set_fill(BLACK, opacity=1)
            if is_rect
            else Circle(radius=radius, color=WHITE).set_fill(BLACK, opacity=1)
        )
        node_text = Text(str(value), font_size=font_size).move_to(node.get_center())
        node_label = Text(str(label), font_size=self.label_font_size).next_to(
            node, label_pos
        )

        if is_label:
            self.add(node, node_text, node_label)
        else:
            self.add(node, node_text)

    def get_cell(self):
        return self[0]

    def get_value(self):
        return self[1]

    def get_label(self):
        return self[2]

    def set_value(self, new_value=" "):
        if new_value == self.value:
            return

        new_text = Text(str(new_value), font_size=self.font_size, z_index=1).move_to(
            self[0].get_center()
        )
        self.value = new_value
        self[1].become(new_text)

    def set_label(self, new_label=" ", label_pos=None):
        if self.is_label:
            label_pos = label_pos if label_pos is not None else self.label_pos
            new_label = Text(
                str(new_label), font_size=self.label_font_size, z_index=1
            ).next_to(self[0], label_pos)
            self.label_pos = label_pos
            self.label = new_label
            self[2].become(new_label)



class MyVector(VGroup):
    def __init__(
        self,
        data=None,
        dir_right=True,
        index=True,
        index_from=0,
        index_step=1,
        index_pos=UP,
        buff=0,
        **kwargs,
    ):
        super().__init__(**kwargs)

        self.data = [] if data is None else data
        self.dir_right = dir_right
        self.dir_pos = RIGHT if dir_right else UP
        self.index = index
        self.index_from = index_from
        self.index_step = index_step
        self.index_pos = index_pos
        self.buff = buff

        cells = self.__create_cells(self.data)
        for cell in cells:
            self.add(cell)
        self.__update_indices()

    def __create_cells(self, data=None):
        if data is None:
            return VGroup()

        cells = VGroup()
        for id, val in enumerate(data):
            cells.add(
                MyNode(
                    value=val, label=id, label_pos=self.index_pos, is_label=self.index
                )
            )
        cells.arrange(self.dir_pos, buff=self.buff)
        return cells

    def __update_indices(self):
        indices = range(
            self.index_from,
            self.index_from + (len(self.data) * self.index_step),
            self.index_step,
        )
        for idx, index in enumerate(indices):
            self[idx].set_label(index)

    def set_value(self, data=None, at=None):
        data = self.data if data is None else data
        at = range(len(self.data)) if at is None else at

        if isinstance(data, (int, float, str)):
            data = [data]

        if isinstance(at, int):
            at = [at]
        
        for idx, val in zip(at, data):
            self.data[idx] = val
            self[idx].set_value(val)

    def set_focus(self, start=None, end=None, color=GREEN, buff=0.1):
        start = 0 if start is None else start
        end = len(self.data) if end is None else end

        return (
            SurroundingRectangle(
                *[node.get_cell() for node in self[start:end]], buff=buff
            )
            .set_fill(color, opacity=0.3)
            .set_stroke(color=color, width=2)
        )

    def extend(self, scene, values=None, at=None):
        if values is None:
            return

        cells = self.__create_cells(values)
        at = len(self.data) if at is None else min(at, len(self.data))

        if at == 0:
            cells.next_to(self[0], LEFT, aligned_edge=RIGHT).shift(LEFT * 0.05)
        elif at == len(self.data):
            cells.next_to(self[-1], aligned_edge=LEFT).shift(RIGHT * 0.05)
        else:
            scene.play(
                self[at:]
                .animate.shift(RIGHT * self[0].width * len(values))
                .shift(LEFT * 0.05)
            )
            cells.next_to(self[at - 1], aligned_edge=LEFT)

        for idx, val in enumerate(values):
            self.data.insert(at + idx, val)
            self.insert(at + idx, cells[idx])

        scene.play(Write(cells))
        self.__update_indices()

    def swap(self, scene, fromx, toy):
        if fromx == toy:
            return

        arcup = ArcBetweenPoints(
            self[fromx].get_cell().get_center(),
            self[toy].get_cell().get_center(),
            angle=-PI,
        )
        arcdwn = ArcBetweenPoints(
            self[toy].get_cell().get_center(),
            self[fromx].get_cell().get_center(),
            angle=-PI,
        )
        scene.play(
            MoveAlongPath(self[fromx].get_value(), arcup),
            MoveAlongPath(self[toy].get_value(), arcdwn),
        )

        self.data[fromx], self.data[toy] = self.data[toy], self.data[fromx]
        self[fromx].set_value(self.data[fromx])
        self[toy].set_value(self.data[toy])
