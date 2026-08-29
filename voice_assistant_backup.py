import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
import pyttsx3
import sounddevice as sd
import scipy.io.wavfile as wav
import subprocess
import webbrowser
import datetime
import threading


# ================= COLORS =================

BG = "#0B1020"
SIDEBAR = "#11182B"
CARD = "#17213A"
ACCENT = "#00D9FF"
GREEN = "#35E58B"
RED = "#FF4D6D"
WHITE = "#F5F7FF"
MUTED = "#8994AA"


class VoiceAssistant:

    def __init__(self, root):

        self.root = root
        self.root.title("Smart Voice Assistant")
        self.root.geometry("1100x700")
        self.root.configure(bg=BG)

        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()

        self.history = []

        self.build_gui()

    # ================= GUI =================

    def build_gui(self):

        # ---------- SIDEBAR ----------

        sidebar = tk.Frame(
            self.root,
            bg=SIDEBAR,
            width=220
        )
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)

        tk.Label(
            sidebar,
            text="◉",
            font=("Segoe UI", 38, "bold"),
            fg=ACCENT,
            bg=SIDEBAR
        ).pack(pady=(35, 0))

        tk.Label(
            sidebar,
            text="SMART",
            font=("Segoe UI", 16, "bold"),
            fg=WHITE,
            bg=SIDEBAR
        ).pack()

        tk.Label(
            sidebar,
            text="VOICE ASSISTANT",
            font=("Segoe UI", 9, "bold"),
            fg=ACCENT,
            bg=SIDEBAR
        ).pack(pady=(0, 40))

        self.menu_button(sidebar, "⌂  Dashboard", self.show_dashboard)
        self.menu_button(sidebar, "🎙  Voice Control", self.listen)
        self.menu_button(sidebar, "📜  History", self.show_history)
        self.menu_button(sidebar, "📝  Notes", self.show_notes)

        tk.Label(
            sidebar,
            text="●  SYSTEM ONLINE",
            font=("Segoe UI", 9, "bold"),
            fg=GREEN,
            bg=SIDEBAR
        ).pack(side="bottom", pady=25)

        # ---------- MAIN ----------

        self.main = tk.Frame(
            self.root,
            bg=BG
        )
        self.main.pack(
            side="left",
            fill="both",
            expand=True
        )

        self.show_dashboard()

    # ================= MENU =================

    def menu_button(self, parent, text, command):

        button = tk.Button(
            parent,
            text=text,
            font=("Segoe UI", 10, "bold"),
            bg=SIDEBAR,
            fg="#AAB4C8",
            activebackground="#1D2B49",
            activeforeground=WHITE,
            relief="flat",
            bd=0,
            anchor="w",
            padx=25,
            pady=14,
            cursor="hand2",
            command=command
        )

        button.pack(
            fill="x",
            padx=10,
            pady=3
        )

    # ================= CLEAR MAIN =================

    def clear_main(self):

        for widget in self.main.winfo_children():
            widget.destroy()

    # ================= DASHBOARD =================

    def show_dashboard(self):

        self.clear_main()

        # ================= HEADER =================

        header = tk.Frame(
            self.main,
            bg=BG
        )
        header.pack(
            fill="x",
            padx=35,
            pady=(28, 15)
        )

        tk.Label(
            header,
            text="Good Evening 👋",
            font=("Segoe UI", 12),
            fg=ACCENT,
            bg=BG
        ).pack(anchor="w")

        tk.Label(
            header,
            text="Voice Command Center",
            font=("Segoe UI", 28, "bold"),
            fg=WHITE,
            bg=BG
        ).pack(anchor="w")

        tk.Label(
            header,
            text="Your smart desktop assistant is ready to help",
            font=("Segoe UI", 10),
            fg=MUTED,
            bg=BG
        ).pack(anchor="w", pady=(4, 0))

        # ================= STATS =================

        stats = tk.Frame(
            self.main,
            bg=BG
        )
        stats.pack(
            fill="x",
            padx=35,
            pady=10
        )

        self.card(
            stats,
            "TOTAL COMMANDS",
            str(len(self.history)),
            ACCENT
        )

        self.card(
            stats,
            "SYSTEM STATUS",
            "ONLINE",
            GREEN
        )

        self.card(
            stats,
            "VOICE MODE",
            "ACTIVE",
            "#A56CFF"
        )

        # ================= MAIN CONTROL =================

        control = tk.Frame(
            self.main,
            bg=CARD
        )
        control.pack(
            fill="both",
            expand=True,
            padx=35,
            pady=20
        )

        tk.Label(
            control,
            text="VOICE CONTROL",
            font=("Segoe UI", 11, "bold"),
            fg=ACCENT,
            bg=CARD
        ).pack(pady=(25, 5))

        tk.Label(
            control,
            text="Speak a command and let your assistant handle it",
            font=("Segoe UI", 10),
            fg=MUTED,
            bg=CARD
        ).pack()

        # ================= MICROPHONE =================

        self.mic = tk.Button(
            control,
            text="🎙",
            font=("Segoe UI Emoji", 38),
            bg=RED,
            fg=WHITE,
            activebackground=ACCENT,
            activeforeground=WHITE,
            relief="flat",
            bd=0,
            width=5,
            height=2,
            cursor="hand2",
            command=self.listen
        )

        self.mic.pack(pady=20)

        self.status = tk.Label(
            control,
            text="READY TO LISTEN",
            font=("Segoe UI", 11, "bold"),
            fg=GREEN,
            bg=CARD
        )
        self.status.pack()

        # ================= RESULT =================

        result_frame = tk.Frame(
            control,
            bg="#10192D"
        )
        result_frame.pack(
            fill="x",
            padx=45,
            pady=20
        )

        self.result = tk.Label(
            result_frame,
            text="Press the microphone and speak a command.",
            font=("Segoe UI", 11),
            fg=WHITE,
            bg="#10192D",
            wraplength=650,
            pady=15
        )
        self.result.pack()

        # ================= QUICK ACTIONS =================

        quick_title = tk.Label(
            self.main,
            text="QUICK ACTIONS",
            font=("Segoe UI", 10, "bold"),
            fg=WHITE,
            bg=BG
        )
        quick_title.pack(
            anchor="w",
            padx=35,
            pady=(0, 8)
        )

        quick = tk.Frame(
            self.main,
            bg=BG
        )
        quick.pack(
            fill="x",
            padx=35,
            pady=(0, 20)
        )

        self.quick_button(
            quick,
            "🕐  TIME",
            "time"
        )

        self.quick_button(
            quick,
            "📅  DATE",
            "date"
        )

        self.quick_button(
            quick,
            "🧮  CALCULATOR",
            "calculator"
        )

        self.quick_button(
            quick,
            "▶  YOUTUBE",
            "youtube"
        )

        self.quick_button(
            quick,
            "📝  NOTEPAD",
            "notepad"
        )

        # ---------- TOP CARDS ----------

        cards = tk.Frame(
            self.main,
            bg=BG
        )
        cards.pack(
            fill="x",
            padx=35
        )

        self.card(cards, "COMMANDS", str(len(self.history)), ACCENT)
        self.card(cards, "STATUS", "READY", GREEN)
        self.card(cards, "VOICE", "ACTIVE", "#A56CFF")

        # ---------- CENTER ----------

        center = tk.Frame(
            self.main,
            bg=CARD
        )
        center.pack(
            fill="both",
            expand=True,
            padx=35,
            pady=25
        )

        tk.Label(
            center,
            text="VOICE CONTROL",
            font=("Segoe UI", 11, "bold"),
            fg=ACCENT,
            bg=CARD
        ).pack(pady=(30, 5))

        tk.Label(
            center,
            text="Press the microphone and speak",
            font=("Segoe UI", 10),
            fg=MUTED,
            bg=CARD
        ).pack()

        self.mic = tk.Button(
            center,
            text="🎙",
            font=("Segoe UI Emoji", 40),
            bg=RED,
            fg="white",
            activebackground=ACCENT,
            relief="flat",
            bd=0,
            width=5,
            height=2,
            cursor="hand2",
            command=self.listen
        )

        self.mic.pack(pady=25)

        self.status = tk.Label(
            center,
            text="READY",
            font=("Segoe UI", 11, "bold"),
            fg=GREEN,
            bg=CARD
        )
        self.status.pack()

        # ---------- RESULT ----------

        result_frame = tk.Frame(
            center,
            bg="#10192D"
        )
        result_frame.pack(
            fill="x",
            padx=40,
            pady=25
        )

        self.result = tk.Label(
            result_frame,
            text="Your assistant is ready.",
            font=("Segoe UI", 11),
            fg=WHITE,
            bg="#10192D",
            wraplength=600,
            pady=15
        )
        self.result.pack()

        # ---------- QUICK BUTTONS ----------

        quick = tk.Frame(
            self.main,
            bg=BG
        )
        quick.pack(
            fill="x",
            padx=35,
            pady=(0, 25)
        )

        tk.Label(
            quick,
            text="QUICK ACTIONS",
            font=("Segoe UI", 10, "bold"),
            fg=WHITE,
            bg=BG
        ).pack(anchor="w", pady=(0, 10))

        self.quick_button(
            quick,
            "🕐 TIME",
            "time"
        )

        self.quick_button(
            quick,
            "📅 DATE",
            "date"
        )

        self.quick_button(
            quick,
            "🧮 CALCULATOR",
            "calculator"
        )

        self.quick_button(
            quick,
            "▶ YOUTUBE",
            "youtube"
        )

        self.quick_button(
            quick,
            "📝 NOTEPAD",
            "notepad"
        )

    # ================= CARD =================

    def card(self, parent, title, value, color):

        frame = tk.Frame(
            parent,
            bg=CARD,
            height=80
        )
        frame.pack(
            side="left",
            fill="both",
            expand=True,
            padx=5
        )
        frame.pack_propagate(False)

        tk.Label(
            frame,
            text=title,
            font=("Segoe UI", 8, "bold"),
            fg=MUTED,
            bg=CARD
        ).pack(
            anchor="w",
            padx=15,
            pady=(12, 0)
        )

        tk.Label(
            frame,
            text=value,
            font=("Segoe UI", 17, "bold"),
            fg=color,
            bg=CARD
        ).pack(
            anchor="w",
            padx=15
        )

    # ================= QUICK BUTTON =================

    def quick_button(self, parent, text, command):

        tk.Button(
            parent,
            text=text,
            font=("Segoe UI", 9, "bold"),
            bg=CARD,
            fg=WHITE,
            activebackground="#243454",
            activeforeground=WHITE,
            relief="flat",
            bd=0,
            padx=15,
            pady=10,
            cursor="hand2",
            command=lambda: self.process(command)
        ).pack(
            side="left",
            padx=(0, 8)
        )

    def recognize(self):
        filename = "voice_command.wav"

        try:
            self.root.after(
                0,
                lambda: self.result.config(
                    text="Listening... Speak now."
                )
            )

            samplerate = 16000
            duration = 6

            recording = sd.rec(
                int(duration * samplerate),
                samplerate=samplerate,
                channels=1,
                dtype="int16"
            )

            sd.wait()

            wav.write(
                filename,
                samplerate,
                recording
            )

            with sr.AudioFile(filename) as source:
                audio = self.recognizer.record(source)

            text = self.recognizer.recognize_google(
                audio
            ).lower()

            self.root.after(
                0,
                lambda: self.process(text)
            )

        except sr.UnknownValueError:

                self.error(
                    "Sorry, I could not understand you."
                )

        except sr.RequestError:

                self.error(
                    "Speech recognition service is unavailable."
                )

        except Exception as e:

                print("MICROPHONE ERROR:", e)

                self.error(
                    "Microphone error. Check your microphone."
            )

    # ================= VOICE =================

    def listen(self):

        self.status.config(
            text="LISTENING...",
            fg=RED
        )

        self.mic.config(bg=ACCENT)

        threading.Thread(
            target=self.recognize,
            daemon=True
        ).start()

        

    # ================= COMMAND PROCESSING =================

    def process(self, command):

        command = command.lower().strip()

        self.status.config(
            text="PROCESSING...",
            fg="#FFB84D"
        )

        self.result.config(
            text="You said: " + command
        )

        response = ""

        if "time" in command:

            time = datetime.datetime.now().strftime(
                "%I:%M %p"
            )

            response = f"Current time is {time}"

        elif "date" in command:

            date = datetime.date.today().strftime(
                "%d %B %Y"
            )

            response = f"Today's date is {date}"

        elif "calculator" in command:

            try:
                subprocess.Popen("calc.exe")
                response = "Opening Calculator."

            except:
                response = "Could not open Calculator."

        elif "notepad" in command:

            try:
                subprocess.Popen("notepad.exe")
                response = "Opening Notepad."

            except:
                response = "Could not open Notepad."

        elif "youtube" in command:

            webbrowser.open(
                "https://www.youtube.com"
            )

            response = "Opening YouTube."

        elif "google" in command or "search" in command:

            query = command

            for word in [
                "search for",
                "search",
                "google"
            ]:

                query = query.replace(
                    word,
                    ""
                )

            query = query.strip()

            if query:

                webbrowser.open(
                    "https://www.google.com/search?q="
                    + query.replace(" ", "+")
                )

                response = f"Searching Google for {query}."

            else:

                response = "Please tell me what to search."

        elif "hello" in command or "hi" in command:

            response = "Hello! How can I help you?"

        elif "exit" in command or "close" in command:

            response = "Goodbye!"

            self.speak(response)

            self.root.after(
                1000,
                self.root.destroy
            )

        else:

            response = (
                "Sorry, I don't understand that command."
            )

        self.result.config(
            text=response
        )

        self.add_history(
            command,
            response
        )

        self.speak(response)

        self.status.config(
            text="READY",
            fg=GREEN
        )

        self.mic.config(
            bg=RED
        )

    # ================= SPEAK =================

    def speak(self, text):

        threading.Thread(
            target=lambda: self._speak(text),
            daemon=True
        ).start()

    def _speak(self, text):

        try:

            self.engine.say(text)
            self.engine.runAndWait()

        except:
            pass

    # ================= HISTORY =================

    def add_history(self, command, response):

        self.history.append(
            f"{command}  →  {response}"
        )

    def show_history(self):

        self.clear_main()

        tk.Label(
            self.main,
            text="Command History",
            font=("Segoe UI", 25, "bold"),
            fg=WHITE,
            bg=BG
        ).pack(
            anchor="w",
            padx=35,
            pady=(35, 20)
        )

        box = tk.Listbox(
            self.main,
            font=("Segoe UI", 10),
            bg=CARD,
            fg=WHITE,
            selectbackground="#263B61",
            relief="flat"
        )

        box.pack(
            fill="both",
            expand=True,
            padx=35,
            pady=(0, 35)
        )

        if not self.history:

            box.insert(
                tk.END,
                "No commands yet."
            )

        else:

            for item in self.history:

                box.insert(
                    tk.END,
                    item
                )

    # ================= NOTES =================

    def show_notes(self):

        self.clear_main()

        tk.Label(
            self.main,
            text="My Notes",
            font=("Segoe UI", 25, "bold"),
            fg=WHITE,
            bg=BG
        ).pack(
            anchor="w",
            padx=35,
            pady=(35, 20)
        )

        tk.Label(
            self.main,
            text="Type a note below:",
            font=("Segoe UI", 10),
            fg=MUTED,
            bg=BG
        ).pack(
            anchor="w",
            padx=35
        )

        entry = tk.Entry(
            self.main,
            font=("Segoe UI", 12),
            bg=CARD,
            fg=WHITE,
            insertbackground=WHITE,
            relief="flat"
        )

        entry.pack(
            fill="x",
            padx=35,
            pady=15,
            ipady=12
        )

        def save():

            text = entry.get().strip()

            if text:

                with open(
                    "assistant_notes.txt",
                    "a",
                    encoding="utf-8"
                ) as file:

                    file.write(
                        text + "\n"
                    )

                entry.delete(0, tk.END)

                messagebox.showinfo(
                    "Notes",
                    "Note saved successfully!"
                )

        tk.Button(
            self.main,
            text="SAVE NOTE",
            font=("Segoe UI", 10, "bold"),
            bg=ACCENT,
            fg="#06101A",
            relief="flat",
            bd=0,
            padx=20,
            pady=10,
            cursor="hand2",
            command=save
        ).pack(
            anchor="w",
            padx=35
        )

    # ================= ERROR =================

    def error(self, message):

        self.root.after(
            0,
            lambda: self.result.config(
                text=message
            )
        )

        self.root.after(
            0,
            lambda: self.status.config(
                text="READY",
                fg=GREEN
            )
        )

        self.root.after(
            0,
            lambda: self.mic.config(
                bg=RED
            )
        )


# ================= START =================

if __name__ == "__main__":

    root = tk.Tk()

    app = VoiceAssistant(root)

    root.mainloop()