"""Juno desktop prototype for Windows, built with Python and Tkinter."""

from __future__ import annotations

import random
import re
import tkinter as tk
from datetime import datetime
from pathlib import Path
from tkinter import filedialog, messagebox, ttk

from PIL import Image, ImageDraw, ImageTk


APP_DIR = Path(__file__).resolve().parent
ART_SIZE = 32
SCALE = 10


class JunoApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Juno — AI Lab")
        self.geometry("1100x740")
        self.minsize(820, 600)
        self.configure(bg="#0b1020")

        self.colors = {
            "bg": "#0b1020",
            "sidebar": "#121a2c",
            "panel": "#141e33",
            "panel2": "#192640",
            "line": "#2a3650",
            "text": "#edf3ff",
            "muted": "#a2afd1",
            "blue": "#829eff",
            "mint": "#5ae0c9",
            "gold": "#f5b65d",
        }
        self._setup_style()
        self._build_layout()
        self._show_welcome()
        self.show_chat()

    def _setup_style(self) -> None:
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("TFrame", background=self.colors["bg"])
        style.configure("Sidebar.TFrame", background=self.colors["sidebar"])
        style.configure("TLabel", background=self.colors["bg"], foreground=self.colors["text"], font=("Segoe UI", 10))
        style.configure("Muted.TLabel", background=self.colors["bg"], foreground=self.colors["muted"], font=("Segoe UI", 9))
        style.configure("Title.TLabel", background=self.colors["bg"], foreground=self.colors["text"], font=("Segoe UI Semibold", 21))
        style.configure("SidebarTitle.TLabel", background=self.colors["sidebar"], foreground=self.colors["text"], font=("Segoe UI Semibold", 20))
        style.configure("Card.TFrame", background=self.colors["panel"])
        style.configure("TButton", font=("Segoe UI Semibold", 10), padding=(12, 9), background=self.colors["panel2"], foreground=self.colors["text"], borderwidth=0)
        style.map("TButton", background=[("active", "#263755")])
        style.configure("Accent.TButton", background=self.colors["blue"], foreground="#08111d")
        style.map("Accent.TButton", background=[("active", "#a4b7ff")])
        style.configure("TEntry", fieldbackground="#0d1526", foreground=self.colors["text"], insertcolor=self.colors["text"], padding=12, bordercolor=self.colors["line"])

    def _build_layout(self) -> None:
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        sidebar = ttk.Frame(self, style="Sidebar.TFrame", padding=22, width=235)
        sidebar.grid(row=0, column=0, sticky="nsew")
        sidebar.grid_propagate(False)
        sidebar.columnconfigure(0, weight=1)

        brand = ttk.Frame(sidebar, style="Sidebar.TFrame")
        brand.grid(row=0, column=0, sticky="ew", pady=(0, 30))
        mark = tk.Label(brand, text="J", bg=self.colors["mint"], fg="#071522", font=("Segoe UI Black", 18), width=2, height=1)
        mark.pack(side="left", padx=(0, 12))
        title_area = ttk.Frame(brand, style="Sidebar.TFrame")
        title_area.pack(side="left")
        tk.Label(title_area, text="AI LAB", bg=self.colors["sidebar"], fg=self.colors["muted"], font=("Segoe UI", 8, "bold")).pack(anchor="w")
        ttk.Label(title_area, text="Juno", style="SidebarTitle.TLabel").pack(anchor="w")

        ttk.Label(sidebar, text="WORKSPACE", style="Muted.TLabel").grid(row=1, column=0, sticky="w", pady=(0, 10))
        self.chat_nav = ttk.Button(sidebar, text="  Chat", command=self.show_chat)
        self.chat_nav.grid(row=2, column=0, sticky="ew", pady=4)
        self.art_nav = ttk.Button(sidebar, text="  Experiments", command=self.show_experiments)
        self.art_nav.grid(row=3, column=0, sticky="ew", pady=4)

        ttk.Separator(sidebar).grid(row=4, column=0, sticky="ew", pady=24)
        ttk.Label(sidebar, text="AVAILABLE MODELS", style="Muted.TLabel").grid(row=5, column=0, sticky="w", pady=(0, 10))
        self._model_card(sidebar, "Juno Core", "v0.1 · Simple chat", 6)
        self._model_card(sidebar, "Juno Imagine", "v0.1 · Pixel art", 7)
        spacer = ttk.Frame(sidebar, style="Sidebar.TFrame")
        spacer.grid(row=8, column=0, sticky="nsew")
        sidebar.rowconfigure(8, weight=1)
        ttk.Label(sidebar, text="Local prototype · no cloud AI", style="Muted.TLabel", wraplength=185).grid(row=9, column=0, sticky="w")

        self.content = ttk.Frame(self, padding=(30, 24))
        self.content.grid(row=0, column=1, sticky="nsew")
        self.content.rowconfigure(1, weight=1)
        self.content.columnconfigure(0, weight=1)
        self.header = ttk.Frame(self.content)
        self.header.grid(row=0, column=0, sticky="ew", pady=(0, 20))
        self.header.columnconfigure(0, weight=1)
        self.heading = ttk.Label(self.header, text="Juno Core v0.1", style="Title.TLabel")
        self.heading.grid(row=0, column=0, sticky="w")
        self.subheading = ttk.Label(self.header, text="A friendly, simple assistant", style="Muted.TLabel")
        self.subheading.grid(row=1, column=0, sticky="w", pady=(3, 0))
        self.view = ttk.Frame(self.content)
        self.view.grid(row=1, column=0, sticky="nsew")
        self.view.rowconfigure(0, weight=1)
        self.view.columnconfigure(0, weight=1)

    def _model_card(self, parent: ttk.Frame, name: str, version: str, row: int) -> None:
        card = tk.Frame(parent, bg=self.colors["panel"], padx=12, pady=10, highlightthickness=1, highlightbackground=self.colors["line"])
        card.grid(row=row, column=0, sticky="ew", pady=5)
        tk.Label(card, text=name, bg=self.colors["panel"], fg=self.colors["text"], font=("Segoe UI Semibold", 10)).pack(anchor="w")
        tk.Label(card, text=version, bg=self.colors["panel"], fg=self.colors["muted"], font=("Segoe UI", 9)).pack(anchor="w", pady=(3, 0))

    def _clear_view(self) -> None:
        for child in self.view.winfo_children():
            child.destroy()

    def show_chat(self) -> None:
        self.heading.configure(text="Juno Core v0.1")
        self.subheading.configure(text="A friendly, simple assistant")
        self._clear_view()
        self.view.rowconfigure(0, weight=1)
        self.view.rowconfigure(1, weight=0)
        self.chat_log = tk.Text(self.view, wrap="word", bg=self.colors["panel"], fg=self.colors["text"], insertbackground=self.colors["text"], relief="flat", padx=22, pady=20, font=("Segoe UI", 11), spacing1=5, spacing3=12, state="disabled")
        self.chat_log.grid(row=0, column=0, sticky="nsew")
        self.chat_log.tag_configure("assistant", foreground=self.colors["mint"], font=("Segoe UI Semibold", 10))
        self.chat_log.tag_configure("user", foreground=self.colors["blue"], font=("Segoe UI Semibold", 10))
        self.chat_log.tag_configure("body", foreground=self.colors["text"], font=("Segoe UI", 11), lmargin1=8, lmargin2=8, spacing3=15)

        composer = ttk.Frame(self.view, padding=(0, 14, 0, 0))
        composer.grid(row=1, column=0, sticky="ew")
        composer.columnconfigure(0, weight=1)
        self.chat_entry = ttk.Entry(composer, font=("Segoe UI", 11))
        self.chat_entry.grid(row=0, column=0, sticky="ew", padx=(0, 10))
        self.chat_entry.insert(0, "Ask Juno something...")
        self.chat_entry.bind("<FocusIn>", self._clear_placeholder)
        self.chat_entry.bind("<Return>", self._send_message)
        ttk.Button(composer, text="Send", style="Accent.TButton", command=self._send_message).grid(row=0, column=1)
        self._append_chat("Juno", "Hi! I'm Juno Core v0.1. I'm a small offline demo, ready to chat. Try asking for help, a joke, or an idea.")
        self.chat_entry.focus_set()

    def _clear_placeholder(self, _event: tk.Event) -> None:
        if self.chat_entry.get() == "Ask Juno something...":
            self.chat_entry.delete(0, tk.END)

    def _append_chat(self, speaker: str, text: str) -> None:
        self.chat_log.configure(state="normal")
        self.chat_log.insert(tk.END, f"{speaker}\n", "assistant" if speaker == "Juno" else "user")
        self.chat_log.insert(tk.END, text + "\n\n", "body")
        self.chat_log.configure(state="disabled")
        self.chat_log.see(tk.END)

    def _send_message(self, _event: tk.Event | None = None) -> None:
        text = self.chat_entry.get().strip()
        if not text or text == "Ask Juno something...":
            return
        self._append_chat("You", text)
        self.chat_entry.delete(0, tk.END)
        self._append_chat("Juno", self._reply(text))

    @staticmethod
    def _reply(message: str) -> str:
        text = message.lower()
        if re.search(r"\b(hi|hello|hey|hiya)\b", text):
            return "Hello! What would you like to talk about?"
        if "your name" in text or "who are you" in text:
            return "I'm Juno Core v0.1, a simple assistant running in this desktop prototype."
        if "help" in text:
            return "I can answer a few simple questions, suggest ideas, and keep a local chat. Try asking for a joke or a brainstorming idea."
        if "joke" in text:
            return "Why did the pixel go to therapy? It had too many unresolved layers."
        if any(word in text for word in ("idea", "brainstorm", "create", "story")):
            return "Here’s a starting point: imagine a tiny robot who runs a night-time library for lost stars. Want to build on that?"
        if "time" in text:
            return f"Your computer's current time is {datetime.now().strftime('%I:%M %p')} (local time)."
        if "pixel" in text or "art" in text or "imagine" in text:
            return "Try the Experiments tab to create an original pixel-art scene from a prompt."
        return "I'm still a simple offline prototype, so I don't know that one yet. Try asking for help, a joke, or an idea. A real language model can be connected later."

    def show_experiments(self) -> None:
        self.heading.configure(text="Juno Imagine v0.1")
        self.subheading.configure(text="Create an original pixel-art scene · generated locally")
        self._clear_view()
        self.view.rowconfigure(0, weight=1)
        self.view.columnconfigure(0, weight=1)
        self.view.columnconfigure(1, weight=1)

        form = tk.Frame(self.view, bg=self.colors["panel"], padx=20, pady=20, highlightthickness=1, highlightbackground=self.colors["line"])
        form.grid(row=0, column=0, sticky="nsew", padx=(0, 12))
        tk.Label(form, text="Describe your scene", bg=self.colors["panel"], fg=self.colors["text"], font=("Segoe UI Semibold", 12)).pack(anchor="w")
        tk.Label(form, text="Juno creates original pixel art; no external art assets are used.", bg=self.colors["panel"], fg=self.colors["muted"], font=("Segoe UI", 9), wraplength=340, justify="left").pack(anchor="w", pady=(6, 14))
        self.prompt_box = tk.Text(form, height=6, wrap="word", bg="#0d1526", fg=self.colors["text"], insertbackground=self.colors["text"], relief="flat", padx=12, pady=10, font=("Segoe UI", 10))
        self.prompt_box.pack(fill="x")
        self.prompt_box.insert("1.0", "A quiet forest shrine under a bright moon")

        presets = ttk.Frame(form)
        presets.pack(fill="x", pady=14)
        for label, prompt in (("Forest", "A quiet forest shrine under a bright moon"), ("Neon", "A neon city alley at night"), ("Moon", "A tiny moon camp with a friendly robot")):
            ttk.Button(presets, text=label, command=lambda p=prompt: self._set_prompt(p)).pack(side="left", padx=(0, 6))
        ttk.Button(form, text="Generate pixel art", style="Accent.TButton", command=self._generate_art).pack(fill="x", pady=(4, 0))

        preview = tk.Frame(self.view, bg=self.colors["panel"], padx=18, pady=18, highlightthickness=1, highlightbackground=self.colors["line"])
        preview.grid(row=0, column=1, sticky="nsew", padx=(12, 0))
        preview.rowconfigure(1, weight=1)
        preview.columnconfigure(0, weight=1)
        tk.Label(preview, text="PREVIEW", bg=self.colors["panel"], fg=self.colors["muted"], font=("Segoe UI", 9, "bold")).grid(row=0, column=0, sticky="w", pady=(0, 12))
        self.art_preview = tk.Label(preview, bg="#0d1526", padx=12, pady=12)
        self.art_preview.grid(row=1, column=0, sticky="nsew")
        self.art_caption = tk.Label(preview, text="Original art generated from your prompt", bg=self.colors["panel"], fg=self.colors["muted"], font=("Segoe UI", 9))
        self.art_caption.grid(row=2, column=0, sticky="w", pady=(12, 10))
        self.save_button = ttk.Button(preview, text="Save PNG…", command=self._save_art)
        self.save_button.grid(row=3, column=0, sticky="ew")
        self.current_art = self._make_art("A quiet forest shrine under a bright moon")
        self._display_art(self.current_art)

    def _set_prompt(self, prompt: str) -> None:
        self.prompt_box.delete("1.0", tk.END)
        self.prompt_box.insert("1.0", prompt)
        self._generate_art()

    def _make_art(self, prompt: str) -> Image.Image:
        seed = sum((index + 1) * ord(char) for index, char in enumerate(prompt))
        rng = random.Random(seed)
        text = prompt.lower()
        if "neon" in text or "city" in text:
            sky, ground, building, accent, plant = "#11152f", "#292044", "#6551b8", "#ff5fd2", "#46d8aa"
        elif "moon" in text or "space" in text or "robot" in text:
            sky, ground, building, accent, plant = "#202b4a", "#48536b", "#b8d4f7", "#f5d76e", "#73d6a0"
        else:
            sky, ground, building, accent, plant = "#8ecae6", "#426b4d", "#d9b38c", "#f2c96d", "#69d2a0"
        image = Image.new("RGB", (ART_SIZE, ART_SIZE), sky)
        draw = ImageDraw.Draw(image)
        # Original shapes and palette are generated in code; no third-party assets.
        for _ in range(24):
            x, y = rng.randrange(ART_SIZE), rng.randrange(2, 19)
            if rng.random() > 0.4:
                draw.rectangle((x, y, x + 1, y + 1), fill="#d9e8ff")
        draw.rectangle((0, 22, ART_SIZE, 31), fill=ground)
        draw.rectangle((0, 22, ART_SIZE, 23), fill=plant)
        draw.rectangle((7, 13, 14, 22), fill=building)
        draw.rectangle((18, 11, 26, 22), fill=building)
        draw.rectangle((6, 12, 15, 14), fill=accent)
        draw.rectangle((17, 10, 27, 12), fill=accent)
        draw.rectangle((9, 17, 11, 22), fill="#574b55")
        draw.rectangle((21, 15, 23, 18), fill=accent)
        draw.rectangle((3, 20, 5, 25), fill=plant)
        draw.rectangle((28, 19, 30, 25), fill=plant)
        if "robot" in text:
            draw.rectangle((22, 18, 26, 22), fill="#d7e2ee")
            draw.rectangle((23, 19, 24, 20), fill=accent)
        elif "forest" in text or "tree" in text:
            draw.rectangle((2, 14, 5, 21), fill="#315d49")
            draw.rectangle((1, 12, 6, 16), fill=plant)
            draw.rectangle((27, 13, 30, 21), fill="#315d49")
            draw.rectangle((26, 11, 31, 16), fill=plant)
        else:
            draw.rectangle((2, 17, 6, 22), fill="#44385f")
            draw.rectangle((26, 15, 31, 22), fill="#44385f")
            draw.rectangle((3, 18, 5, 18), fill=accent)
            draw.rectangle((28, 16, 29, 16), fill=accent)
        # A small moon/sun to give the scene a focal point.
        draw.rectangle((24, 3, 28, 7), fill="#fff0ad")
        return image.resize((ART_SIZE * SCALE, ART_SIZE * SCALE), Image.Resampling.NEAREST)

    def _display_art(self, image: Image.Image) -> None:
        self.art_photo = ImageTk.PhotoImage(image)
        self.art_preview.configure(image=self.art_photo)

    def _generate_art(self) -> None:
        prompt = self.prompt_box.get("1.0", "end-1c").strip()
        if not prompt:
            messagebox.showinfo("Add a prompt", "Describe the pixel-art scene you want Juno to create.")
            return
        self.current_art = self._make_art(prompt)
        self._display_art(self.current_art)
        short_prompt = prompt if len(prompt) <= 48 else prompt[:45] + "..."
        self.art_caption.configure(text=f"Generated: {short_prompt}")

    def _save_art(self) -> None:
        destination = filedialog.asksaveasfilename(title="Save Juno pixel art", defaultextension=".png", filetypes=(("PNG image", "*.png"),), initialfile="juno-pixel-art.png")
        if not destination:
            return
        try:
            self.current_art.save(destination, "PNG")
        except OSError as exc:
            messagebox.showerror("Couldn't save image", str(exc))
            return
        messagebox.showinfo("Saved", f"Your pixel art was saved to:\n{destination}")

    def _show_welcome(self) -> None:
        # Welcome content is added when the chat view is first built.
        pass


if __name__ == "__main__":
    JunoApp().mainloop()
