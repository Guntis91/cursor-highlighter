import tkinter as tk
from PIL import Image, ImageTk
import pyautogui
import win32api
import win32con
import time
from screeninfo import get_monitors

# === CONFIG ===
IMAGE_FILE = "assets/yellow_ring_small.png"
CLICK_COLOR = "red"
CLICK_WIDTH = 2
UPDATE_DELAY = 10  # ms

RING_SIZE = 30
CLICK_START = 40
CLICK_END = 5
CLICK_STEP = 6
CLICK_DELAY = 0.015

class CursorHighlighter:
    def __init__(self, root):
        self.root = root
        self.root.attributes('-topmost', True)
        self.root.overrideredirect(True)
        self.root.attributes('-transparentcolor', 'white')
        self.root.config(bg='white')

        # ✅ Detect entire virtual screen area (all monitors)
        monitors = get_monitors()
        min_x = min(monitor.x for monitor in monitors)
        min_y = min(monitor.y for monitor in monitors)
        max_x = max(monitor.x + monitor.width for monitor in monitors)
        max_y = max(monitor.y + monitor.height for monitor in monitors)

        total_width = max_x - min_x
        total_height = max_y - min_y

        self.offset_x = -min_x
        self.offset_y = -min_y

        self.root.geometry(f"{total_width}x{total_height}+{min_x}+{min_y}")

        self.canvas = tk.Canvas(self.root, bg='white', highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.ring_image = Image.open(IMAGE_FILE)
        self.tk_ring = ImageTk.PhotoImage(self.ring_image)

        self.ring_id = None
        self.click_id = None
        self.last_click_state = win32api.GetKeyState(win32con.VK_LBUTTON)
        self.click_animation_running = False

        self.update_loop()

    def show_ring(self, x, y):
        if self.ring_id:
            self.canvas.delete(self.ring_id)
        # Adjust position for full screen layout
        self.ring_id = self.canvas.create_image(x + self.offset_x, y + self.offset_y, image=self.tk_ring)

    def animate_click(self, x, y):
        self.click_animation_running = True
        x += self.offset_x
        y += self.offset_y
        for r in range(CLICK_START, CLICK_END, -CLICK_STEP):
            self.canvas.delete("click")
            self.canvas.create_oval(x - r, y - r, x + r, y + r, outline=CLICK_COLOR, width=CLICK_WIDTH, tags="click")
            self.root.update()
            time.sleep(CLICK_DELAY)
        self.canvas.delete("click")
        self.click_animation_running = False

    def update_loop(self):
        x, y = pyautogui.position()
        self.canvas.delete("all")
        self.show_ring(x, y)

        current_click = win32api.GetKeyState(win32con.VK_LBUTTON)
        if current_click != self.last_click_state and current_click < 0 and not self.click_animation_running:
            self.animate_click(x, y)
        self.last_click_state = current_click

        self.root.after(UPDATE_DELAY, self.update_loop)

# === MAIN ===
if __name__ == "__main__":
    root = tk.Tk()
    app = CursorHighlighter(root)
    root.mainloop()
