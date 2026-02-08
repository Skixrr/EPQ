from manim import *
import numpy as np


class DerivativeSketchClean(Scene):
    def construct(self):
        # ------------------
        # Title
        # ------------------
        title = Text(
            "Structural Growth of P vs NP Under Resource Perturbation",
            font_size=34
        )
        title.to_edge(UP)
        self.add(title)

        # ------------------
        # Axes
        # ------------------
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 11, 1],
            x_length=10,
            y_length=5.5,
            tips=False,
        ).to_edge(DOWN).shift(UP * 0.5)

        x_label = Tex(r"\text{input size / resource bound } n", font_size=26)
        x_label.next_to(axes, DOWN, buff=0.3).shift(UP * 0.25)

        y_label = Tex(r"\text{problems entering class}", font_size=26)
        y_label.rotate(PI / 2)
        y_label.next_to(axes, LEFT, buff=0.35).shift(UP * 0.25)

        self.play(Create(axes), FadeIn(x_label), FadeIn(y_label))

        # ------------------
        # P curve (smooth, baseline)
        # ------------------
        def p_func(x):
            return 1.4 + 2.0 * np.log1p(x)

        p_graph = axes.plot(
            p_func,
            x_range=[0.2, 10],
            stroke_width=5,
            color=BLUE,
        )

        p_dots = VGroup(*[
            Dot(axes.c2p(x, p_func(x)), radius=0.04, color=BLUE)
            for x in np.linspace(0.6, 9.4, 11)
        ])

        # ------------------
        # NP curve (always above P)
        # ------------------
        np_x = np.array([0.6, 1.4, 2.2, 2.6, 3.3, 4.1, 4.5, 5.3, 5.9, 6.6, 7.4, 8.1, 9.0, 9.6])
        # Positive offsets ensure NP ≥ P everywhere
        np_offsets = np.array([0.6, 0.7, 0.9, 1.6, 1.2, 1.5, 2.2, 2.0, 2.6, 2.4, 2.7, 3.3, 3.2, 3.4])

        np_y = np.array([p_func(x) + d for x, d in zip(np_x, np_offsets)])

        np_points = [axes.c2p(x, y) for x, y in zip(np_x, np_y)]
        np_graph = VMobject(stroke_width=5, color=RED)
        np_graph.set_points_as_corners(np_points)

        # ------------------
        # Legend (top-right)
        # ------------------
        legend_p = VGroup(
            Line(color=BLUE).set_length(0.6),
            Tex(r"$P$", font_size=28),
        ).arrange(RIGHT, buff=0.3)

        legend_np = VGroup(
            Line(color=RED).set_length(0.6),
            Tex(r"$NP$", font_size=28),
        ).arrange(RIGHT, buff=0.3)

        legend = VGroup(legend_p, legend_np).arrange(DOWN, buff=0.25)
        legend.to_corner(UR, buff=0.6).shift(DOWN * 1.2)

        # ------------------
        # Disclaimer (pushed well below plot)
        # ------------------
        disclaimer = Tex(
            r"\textit{Heuristic illustration (not a proof)}",
            font_size=22
        )
        disclaimer.next_to(axes, DOWN, buff=0.9)

        # ------------------
        # Animate
        # ------------------
        self.play(Create(p_graph), FadeIn(p_dots))
        self.play(Create(np_graph))
        self.play(FadeIn(legend), FadeIn(disclaimer))
        self.wait(2)
