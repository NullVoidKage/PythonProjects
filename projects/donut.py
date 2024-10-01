import tkinter as tk
import math


class DonutAnimation:
    def __init__(self, root):
        self.root = root
        self.root.title("3D Donut Animation")
        self.canvas = tk.Canvas(root, width=800, height=400, bg="black")
        self.canvas.pack()
        self.A = 0.0
        self.B = 0.0
        self.animate()

    def animate(self):
        self.canvas.delete("all")
        z = [0] * 1760
        b = [' '] * 1760

        for j in range(0, 628, 7):
            for i in range(0, 628, 2):
                phi = i / 100.0
                theta = j / 100.0
                c = math.sin(phi)
                d = math.cos(theta)
                e = math.sin(self.A)
                f = math.sin(theta)
                g = math.cos(self.A)
                h = d + 2
                D = 1 / (c * h * e + f * g + 5)
                l = math.cos(phi)
                m = math.cos(self.B)
                n = math.sin(self.B)
                t = c * h * g - f * e

                x = int(40 + 30 * D * (l * h * m - t * n))
                y = int(12 + 15 * D * (l * h * n + t * m))

                if x < 0 or x >= 80 or y < 0 or y >= 22:
                    continue

                o = x + 80 * y

                if o < 0 or o >= 1760:
                    continue

                N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))

                if D > z[o]:
                    z[o] = D
                    b[o] = ".,-~:;=!*#$@"[N if N > 0 else 0]

        for k in range(1760):
            if k % 80 == 0 and k != 0:
                self.canvas.create_text(0, (k // 80) * 20, text="", fill="white", anchor="nw")
            self.canvas.create_text((k % 80) * 10, (k // 80) * 20, text=b[k], fill="white", anchor="nw")

        self.A += 0.04
        self.B += 0.02
        self.root.after(30, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    app = DonutAnimation(root)
    root.mainloop()
