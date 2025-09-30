import os
import csv
import datetime
import tkinter as tk
from tkinter import ttk, messagebox

# Optional but recommended: charts
import pandas as pd
import matplotlib
matplotlib.use("TkAgg")  # use TkAgg backend
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ---------------------- Config ----------------------
APP_TITLE = "Personal Wellbeing Dashboard"
CSV_PATH = "wellbeing_log.csv"
CSV_HEADERS = ["date", "mood", "sleep_hours", "weather", "note"]

MOOD_OPTIONS = ["Happy", "Calm", "Excited", "Tired", "Stressed", "Sad"]
WEATHER_OPTIONS = ["Sunny", "Cloudy", "Rainy", "Snowy", "Extreme Hot", "Extreme Cold"]

# map mood to numeric score for charts
MOOD_SCORES = {
    "Happy": 5,
    "Excited": 5,
    "Calm": 4,
    "Tired": 3,
    "Stressed": 2,
    "Sad": 1,
}

QUOTES = [
    "Keep going; future-you will be grateful.",
    "Progress over perfection.",
    "Small steps add up.",
    "Be gentle with yourself."
]

# ---------------------- Data helpers ----------------------
def ensure_csv(path=CSV_PATH):
    if not os.path.exists(path):
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(CSV_HEADERS)

def append_row(row, path=CSV_PATH):
    with open(path, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(row)

def load_df(path=CSV_PATH):
    if not os.path.exists(path):
        return pd.DataFrame(columns=CSV_HEADERS)
    try:
        df = pd.read_csv(path)
        # normalize columns if needed
        missing = [c for c in CSV_HEADERS if c not in df.columns]
        for m in missing:
            df[m] = ""  # add empty
        return df[CSV_HEADERS]
    except Exception:
        # corrupted or empty—return blank
        return pd.DataFrame(columns=CSV_HEADERS)

# ---------------------- App ----------------------
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(APP_TITLE)
        self.geometry("880x620")
        self.configure(bg="#f7e1f0")  # soft pink background

        ensure_csv()

        # Notebook tabs
        notebook = ttk.Notebook(self)
        notebook.pack(expand=True, fill="both", padx=8, pady=8)

        # Tabs
        self.entry_frame = tk.Frame(notebook, bg="#f7e1f0")
        self.dashboard_frame = tk.Frame(notebook, bg="#ffffff")

        notebook.add(self.entry_frame, text="Log Entry")
        notebook.add(self.dashboard_frame, text="Dashboard")

        self.build_entry_tab(self.entry_frame)
        self.build_dashboard_tab(self.dashboard_frame)

    # -------- Entry Tab --------
    def build_entry_tab(self, frame):
        # Title
        tk.Label(frame, text="Daily Check-In", font=("Arial", 20, "bold"),
                 bg="#f7e1f0").pack(pady=(16, 6))

        # Date (auto)
        today_str = datetime.date.today().strftime("%B %d, %Y")
        tk.Label(frame, text=today_str, font=("Arial", 11), bg="#f7e1f0").pack()

        # Form container
        form = tk.Frame(frame, bg="#f7e1f0")
        form.pack(pady=16)

        # Mood
        tk.Label(form, text="Mood", bg="#f7e1f0").grid(row=0, column=0, sticky="e", padx=6, pady=6)
        self.mood_var = tk.StringVar()
        ttk.Combobox(form, textvariable=self.mood_var, values=MOOD_OPTIONS, state="readonly", width=28)\
            .grid(row=0, column=1, padx=6, pady=6)

        # Sleep hours
        tk.Label(form, text="Sleep (hours)", bg="#f7e1f0").grid(row=1, column=0, sticky="e", padx=6, pady=6)
        self.sleep_var = tk.StringVar()
        tk.Entry(form, textvariable=self.sleep_var, width=30).grid(row=1, column=1, padx=6, pady=6)

        # Weather
        tk.Label(form, text="Weather", bg="#f7e1f0").grid(row=2, column=0, sticky="e", padx=6, pady=6)
        self.weather_var = tk.StringVar()
        ttk.Combobox(form, textvariable=self.weather_var, values=WEATHER_OPTIONS, state="readonly", width=28)\
            .grid(row=2, column=1, padx=6, pady=6)

        # Note
        tk.Label(form, text="Note (optional)", bg="#f7e1f0").grid(row=3, column=0, sticky="ne", padx=6, pady=6)
        self.note_txt = tk.Text(form, width=40, height=6)
        self.note_txt.grid(row=3, column=1, padx=6, pady=6)

        # Quote
        import random
        self.quote_lbl = tk.Label(frame, text=random.choice(QUOTES),
                                  wraplength=600, justify="center",
                                  bg="#f7e1f0", fg="#444", font=("Arial", 10, "italic"))
        self.quote_lbl.pack(pady=8)

        # Buttons
        btns = tk.Frame(frame, bg="#f7e1f0")
        btns.pack(pady=8)
        tk.Button(btns, text="Save Entry", command=self.save_entry,
                  bg="white", fg="#b30068", font=("Arial", 12, "bold"), width=14)\
            .grid(row=0, column=0, padx=6)
        tk.Button(btns, text="Clear", command=self.clear_form,
                  bg="white", fg="#666", font=("Arial", 11), width=10)\
            .grid(row=0, column=1, padx=6)

        # Status
        self.status_lbl = tk.Label(frame, text="", bg="#f7e1f0", fg="#333")
        self.status_lbl.pack(pady=(4, 0))

    def save_entry(self):
        date = datetime.date.today().isoformat()
        mood = self.mood_var.get().strip()
        sleep = self.sleep_var.get().strip()
        weather = self.weather_var.get().strip()
        note = self.note_txt.get("1.0", "end").strip()

        # validation
        if not mood:
            messagebox.showerror("Missing info", "Please select a mood.")
            return
        if sleep and not self._is_number(sleep):
            messagebox.showerror("Invalid input", "Sleep hours must be a number (e.g., 7.5).")
            return

        append_row([date, mood, sleep, weather, note])
        self.status_lbl.config(text="Entry saved.")
        self.clear_form()
        self.refresh_dashboard()

    def clear_form(self):
        self.mood_var.set("")
        self.sleep_var.set("")
        self.weather_var.set("")
        self.note_txt.delete("1.0", "end")

    def _is_number(self, s):
        try:
            float(s)
            return True
        except Exception:
            return False

    # -------- Dashboard Tab --------
    def build_dashboard_tab(self, frame):
        # container for charts
        self.charts_container = tk.Frame(frame, bg="#ffffff")
        self.charts_container.pack(expand=True, fill="both", padx=10, pady=10)

        # add a refresh button
        controls = tk.Frame(frame, bg="#ffffff")
        controls.pack(fill="x", padx=10)
        tk.Button(controls, text="Refresh", command=self.refresh_dashboard,
                  bg="#f2f2f2").pack(side="right", padx=4, pady=4)

        self.refresh_dashboard()

    def refresh_dashboard(self):
        # Clear previous charts
        for w in self.charts_container.winfo_children():
            w.destroy()

        df = load_df()
        if df.empty:
            tk.Label(self.charts_container, text="No data yet. Save an entry to see charts.",
                     bg="#ffffff", fg="#555").pack(pady=20)
            return

        # parse/prepare
        df = df.copy()
        # map mood score
        df["mood_score"] = df["mood"].map(MOOD_SCORES).fillna(0)
        # coerce sleep to float
        def to_float(x):
            try:
                return float(x)
            except Exception:
                return None
        df["sleep_hours"] = df["sleep_hours"].apply(to_float)
        # date for x-axis
        df["date"] = pd.to_datetime(df["date"], errors="coerce")

        # ---- Chart 1: Mood over Time ----
        fig1 = Figure(figsize=(5.6, 2.8), dpi=100)
        ax1 = fig1.add_subplot(111)
        # sort by date
        d1 = df.dropna(subset=["date"]).sort_values("date")
        if not d1.empty:
            ax1.plot(d1["date"], d1["mood_score"], marker="o")
            ax1.set_title("Mood Over Time")
            ax1.set_ylabel("Mood Score (1–5)")
            ax1.set_xlabel("Date")
            ax1.grid(True, alpha=0.3)
        else:
            ax1.text(0.5, 0.5, "No dated entries", ha="center", va="center")

        canvas1 = FigureCanvasTkAgg(fig1, master=self.charts_container)
        canvas1.draw()
        canvas1.get_tk_widget().pack(fill="x", padx=6, pady=6)

        # ---- Chart 2: Sleep vs Mood ----
        fig2 = Figure(figsize=(5.6, 2.8), dpi=100)
        ax2 = fig2.add_subplot(111)
        d2 = df.dropna(subset=["sleep_hours", "mood_score"])
        if not d2.empty:
            ax2.scatter(d2["sleep_hours"], d2["mood_score"])
            ax2.set_title("Sleep vs Mood")
            ax2.set_xlabel("Sleep Hours")
            ax2.set_ylabel("Mood Score (1–5)")
            ax2.grid(True, alpha=0.3)
        else:
            ax2.text(0.5, 0.5, "Need sleep & mood data", ha="center", va="center")

        canvas2 = FigureCanvasTkAgg(fig2, master=self.charts_container)
        canvas2.draw()
        canvas2.get_tk_widget().pack(fill="x", padx=6, pady=6)

# ---------------------- Run ----------------------
if __name__ == "__main__":
    app = App()
    app.mainloop()