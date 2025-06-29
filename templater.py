import customtkinter as ctk
from tkinter import messagebox, filedialog
import os

STYLE = {
    "positions": {
        "order_label": {"x": 50, "y": 20},
        "order_menu": {"x": 300, "y": 20},
        "question_label": {"x": 50, "y": 70},
        "question_entry": {"x": 300, "y": 70},
        "answer_label": {"x": 50, "y": 120},
        "answer_entry": {"x": 300, "y": 120},
        "add_btn": {"x": 300, "y": 180},
        "save_btn": {"x": 560, "y": 180},
        "preview_box": {"x": 50, "y": 240},
        "close_btn": {"x": 305, "y": 610}
    },
    "sizes": {
        "question_entry": {"width": 400},
        "answer_entry": {"width": 400},
        "preview_box": {"width": 650, "height": 360}
    }
}

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
window_width = 750
window_height = 651
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int((screen_width / 2) - (window_width / 2))
center_y = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
root.overrideredirect(True)
root.attributes("-topmost", True)

class FlashcardApp:
    def __init__(self, master):
        self.master = master
        master.title("Flashcard Creator")

        self.cards = []
        self.order_var = ctk.StringVar(value="Question First")
        self.question_var = ctk.StringVar()
        self.answer_var = ctk.StringVar()

        self.question_var.trace_add("write", lambda *args: self.update_preview())
        self.answer_var.trace_add("write", lambda *args: self.update_preview())
        self.order_var.trace_add("write", lambda *args: self.update_preview())

        self.build_ui()

    def place(self, widget, key):
        pos = STYLE["positions"].get(key, {})
        widget.place(x=pos.get("x", 0), y=pos.get("y", 0))

    def build_ui(self):
        self.order_label = ctk.CTkLabel(self.master, text="Card Order (Questions or Answers First):")
        self.place(self.order_label, "order_label")

        self.order_menu = ctk.CTkOptionMenu(self.master, variable=self.order_var, values=["Question First", "Answer First"])
        self.place(self.order_menu, "order_menu")

        self.question_label = ctk.CTkLabel(self.master, text="Question/Definition:")
        self.place(self.question_label, "question_label")

        self.question_entry = ctk.CTkEntry(self.master, textvariable=self.question_var,
                                           width=STYLE["sizes"]["question_entry"]["width"])
        self.place(self.question_entry, "question_entry")

        self.answer_label = ctk.CTkLabel(self.master, text="Answer:")
        self.place(self.answer_label, "answer_label")

        self.answer_entry = ctk.CTkEntry(self.master, textvariable=self.answer_var,
                                         width=STYLE["sizes"]["answer_entry"]["width"])
        self.place(self.answer_entry, "answer_entry")

        self.add_btn = ctk.CTkButton(self.master, text="➕ Add Card", command=self.add_card)
        self.place(self.add_btn, "add_btn")

        self.save_btn = ctk.CTkButton(self.master, text="💾 Save and Exit", command=self.save_and_exit)
        self.place(self.save_btn, "save_btn")

        self.preview = ctk.CTkTextbox(self.master,
                                      width=STYLE["sizes"]["preview_box"]["width"],
                                      height=STYLE["sizes"]["preview_box"]["height"])
        self.preview.configure(state="disabled")
        self.place(self.preview, "preview_box")

        self.close_btn = ctk.CTkButton(self.master, text="❌ Close", command=self.close_app)
        self.place(self.close_btn, "close_btn")

    def build_card_text(self, q, a, o):
        return f"{q}\n?\n{a}\n" if o == 'Question First' else f"{a}\n?\n{q}\n"

    def update_preview(self):
        current_q = self.question_var.get().strip()
        current_a = self.answer_var.get().strip()
        current_o = self.order_var.get()
        lines = [self.build_card_text(*card) for card in self.cards]
        if current_q or current_a:
            lines.append(self.build_card_text(current_q, current_a, current_o))
        self.preview.configure(state="normal")
        self.preview.delete("1.0", "end")
        self.preview.insert("1.0", "\n".join(lines))
        self.preview.configure(state="disabled")

    def add_card(self):
        q = self.question_var.get().strip()
        a = self.answer_var.get().strip()
        o = self.order_var.get()
        if not q or not a:
            messagebox.showwarning("Input Error", "Both question and answer must be filled.")
            return
        self.cards.append((q, a, o))
        self.question_var.set("")
        self.answer_var.set("")
        self.update_preview()
        self.question_entry.focus_set()

    def save_and_exit(self):
        path = filedialog.asksaveasfilename(defaultextension=".md", filetypes=[("Markdown", "*.md")])
        if not path:
            return
        q = self.question_var.get().strip()
        a = self.answer_var.get().strip()
        o = self.order_var.get()
        if q and a:
            self.cards.append((q, a, o))
        with open(path, "w", encoding="utf-8") as f:
            f.write("#Flashcards\n\n")
            for card in self.cards:
                f.write(self.build_card_text(*card) + "\n")
        messagebox.showinfo("Saved", f"Saved {len(self.cards)} cards to {path}")
        self.master.quit()

    def close_app(self):
        self.master.quit()

app = FlashcardApp(root)
root.mainloop()
