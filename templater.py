import customtkinter as ctk
from tkinter import messagebox, filedialog
import os
from PIL import Image, ImageTk

STYLE = {
    "positions": {
        "order_label": {"x": 50, "y": 20},
        "order_menu": {"x": 300, "y": 20},
        "question_label": {"x": 50, "y": 70},
        "question_entry": {"x": 300, "y": 70},
        "q_img_btn": {"x": 720, "y": 67},
        "q_img_preview": {"x": 760, "y": 70},
        "answer_label": {"x": 50, "y": 120},
        "answer_entry": {"x": 300, "y": 120},
        "a_img_btn": {"x": 720, "y": 117},
        "a_img_preview": {"x": 760, "y": 120},
        "add_btn": {"x": 300, "y": 180},
        "save_btn": {"x": 560, "y": 180},
        "preview_box": {"x": 50, "y": 240},
        "close_btn": {"x": 305, "y": 610}
    },
    "sizes": {
        "question_entry": {"width": 400},
        "answer_entry": {"width": 400},
        "preview_box": {"width": 650, "height": 360},
        "q_img_preview": {"width": 40, "height": 40},
        "a_img_preview": {"width": 40, "height": 40},
        "img_btn": {"size": 32}
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
root.resizable(False, False)

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

        # Add Image to Question Button
        self.q_img_btn = ctk.CTkButton(
            self.master,
            text="🖼️",
            command=self.add_image_to_question,
            width=STYLE["sizes"]["img_btn"]["size"],
            height=STYLE["sizes"]["img_btn"]["size"],
            corner_radius=16
        )
        self.place(self.q_img_btn, "q_img_btn")
        # Tooltip for question image button
        self.q_img_btn.bind("<Enter>", lambda e: self.show_tooltip("Add image to question", e, which="q"))
        self.q_img_btn.bind("<Leave>", lambda e: self.hide_tooltip(which="q"))
        # Image preview for question
        self.q_img_preview = ctk.CTkLabel(self.master, text="")
        self.place(self.q_img_preview, "q_img_preview")

        self.answer_label = ctk.CTkLabel(self.master, text="Answer:")
        self.place(self.answer_label, "answer_label")

        self.answer_entry = ctk.CTkEntry(self.master, textvariable=self.answer_var,
                                         width=STYLE["sizes"]["answer_entry"]["width"])
        self.place(self.answer_entry, "answer_entry")

        # Add Image to Answer Button
        self.a_img_btn = ctk.CTkButton(
            self.master,
            text="🖼️",
            command=self.add_image_to_answer,
            width=STYLE["sizes"]["img_btn"]["size"],
            height=STYLE["sizes"]["img_btn"]["size"],
            corner_radius=16
        )
        self.place(self.a_img_btn, "a_img_btn")
        # Tooltip for answer image button
        self.a_img_btn.bind("<Enter>", lambda e: self.show_tooltip("Add image to answer", e, which="a"))
        self.a_img_btn.bind("<Leave>", lambda e: self.hide_tooltip(which="a"))
        # Image preview for answer
        self.a_img_preview = ctk.CTkLabel(self.master, text="")
        self.place(self.a_img_preview, "a_img_preview")

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

        # Tooltip labels (hidden by default)
        self.q_img_btn_tooltip = ctk.CTkLabel(self.master, text="", fg_color=("#222", "#eee"), text_color=("#fff", "#000"), corner_radius=6)
        self.q_img_btn_tooltip.place_forget()
        self.a_img_btn_tooltip = ctk.CTkLabel(self.master, text="", fg_color=("#222", "#eee"), text_color=("#fff", "#000"), corner_radius=6)
        self.a_img_btn_tooltip.place_forget()

    def build_card_text(self, q, a, o):
        # Remove image path info for preview
        if o == 'Question First':
            return f"{q}\n?\n{a}\n"
        else:
            return f"{a}\n?\n{q}\n"

    def update_preview(self):
        current_q = self.question_var.get().strip()
        current_a = self.answer_var.get().strip()
        current_o = self.order_var.get()
        lines = [self.build_card_text(*card[:3]) for card in self.cards]
        # Always show the current input as a new card if either field is non-empty
        if current_q or current_a:
            lines.append(self.build_card_text(current_q, current_a, current_o))
        self.preview.configure(state="normal")
        self.preview.delete("1.0", "end")
        self.preview.insert("1.0", "\n".join(lines))
        self.preview.configure(state="disabled")

    def add_image_to_question(self):
        img_path = filedialog.askopenfilename(title="Select Image for Question", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
        if img_path:
            # Insert markdown image syntax at the end of the question
            current = self.question_var.get()
            img_name = os.path.basename(img_path)
            self._pending_q_img = img_path  # Store for copying later
            if current and not current.endswith("\n"):
                current += "\n"
            self.question_var.set(f"{current}![](images/{img_name})")
            self.show_image_preview(img_path, which="q")

    def add_image_to_answer(self):
        img_path = filedialog.askopenfilename(title="Select Image for Answer", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
        if img_path:
            # Insert markdown image syntax at the end of the answer
            current = self.answer_var.get()
            img_name = os.path.basename(img_path)
            self._pending_a_img = img_path  # Store for copying later
            if current and not current.endswith("\n"):
                current += "\n"
            self.answer_var.set(f"{current}![](images/{img_name})")
            self.show_image_preview(img_path, which="a")

    def show_image_preview(self, img_path, which="q"):
        try:
            img = Image.open(img_path)
            size = STYLE["sizes"]["q_img_preview"] if which == "q" else STYLE["sizes"]["a_img_preview"]
            img.thumbnail((size["width"], size["height"]))
            photo = ImageTk.PhotoImage(img)
            if which == "q":
                self.q_img_preview.configure(image=photo, text="")
                self.q_img_preview_img = photo  # Store reference to prevent GC
            else:
                self.a_img_preview.configure(image=photo, text="")
                self.a_img_preview_img = photo  # Store reference to prevent GC
        except Exception as e:
            if which == "q":
                self.q_img_preview.configure(image=None, text="(error)")
                self.q_img_preview_img = None
            else:
                self.a_img_preview.configure(image=None, text="(error)")
                self.a_img_preview_img = None

    def add_card(self):
        q = self.question_var.get().strip()
        a = self.answer_var.get().strip()
        o = self.order_var.get()
        q_img = getattr(self, '_pending_q_img', None)
        a_img = getattr(self, '_pending_a_img', None)
        if not q or not a:
            messagebox.showwarning("Input Error", "Both question and answer must be filled.")
            self.question_entry.focus_set()
            return
        self.cards.append((q, a, o, q_img, a_img))
        self.question_var.set("")
        self.answer_var.set("")
        self._pending_q_img = None
        self._pending_a_img = None
        self.q_img_preview.configure(image=None, text="")
        self.a_img_preview.configure(image=None, text="")
        self.q_img_preview_img = None
        self.a_img_preview_img = None
        self.question_entry.focus_set()  # Always focus question field
        self.update_preview()  # Force update preview after clearing fields

    def save_and_exit(self):
        path = filedialog.asksaveasfilename(defaultextension=".md", filetypes=[("Markdown", "*.md")])
        if not path:
            return
        q = self.question_var.get().strip()
        a = self.answer_var.get().strip()
        o = self.order_var.get()
        q_img = getattr(self, '_pending_q_img', None)
        a_img = getattr(self, '_pending_a_img', None)
        if q and a:
            self.cards.append((q, a, o, q_img, a_img))
        # Prepare images folder
        base_dir = os.path.dirname(path)
        images_dir = os.path.join(base_dir, "images")
        os.makedirs(images_dir, exist_ok=True)
        # Write markdown and copy images
        with open(path, "w", encoding="utf-8") as f:
            f.write("#Flashcards\n\n")
            for card in self.cards:
                q, a, o, q_img, a_img = card if len(card) == 5 else (*card, None, None)
                f.write(self.build_card_text(q, a, o) + "\n")
                # Copy images if present
                for img_path in [q_img, a_img]:
                    if img_path and os.path.isfile(img_path):
                        img_name = os.path.basename(img_path)
                        dest = os.path.join(images_dir, img_name)
                        if not os.path.exists(dest):
                            try:
                                import shutil
                                shutil.copy(img_path, dest)
                            except Exception as e:
                                print(f"Failed to copy image {img_path}: {e}")
        messagebox.showinfo("Saved", f"Saved {len(self.cards)} cards to {path}")
        self.master.quit()

    def close_app(self):
        self.master.quit()

    def show_tooltip(self, text, event, which="q"):
        x = event.widget.winfo_rootx() - self.master.winfo_rootx() + 45
        y = event.widget.winfo_rooty() - self.master.winfo_rooty() + 5
        if which == "q":
            self.q_img_btn_tooltip.configure(text=text)
            self.q_img_btn_tooltip.place(x=x, y=y)
        else:
            self.a_img_btn_tooltip.configure(text=text)
            self.a_img_btn_tooltip.place(x=x, y=y)

    def hide_tooltip(self, which="q"):
        if which == "q":
            self.q_img_btn_tooltip.place_forget()
        else:
            self.a_img_btn_tooltip.place_forget()

app = FlashcardApp(root)
root.mainloop()
