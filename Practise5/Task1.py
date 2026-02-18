import sys

import pandas as pd
import matplotlib.ticker as mticker

from PyQt5.QtWidgets import (
    QApplication, QWidget, QRadioButton, QCheckBox,
    QVBoxLayout, QGroupBox, QGridLayout, QHBoxLayout
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

CSV_FILE = "demo21_2023.csv"

class StatisticApp(QWidget):
    def __init__(self):
        super().__init__()
        self.data = None
        self.load_data()
        self.initUI()

    def load_data(self):
        try:
            self.data = pd.read_csv(
                CSV_FILE,
                header=None,
                names=["Год", "Рождаемость", "Смертность", "Тип"]
            )
            self.data["Год"] = pd.to_numeric(self.data["Год"], errors='coerce')
            self.data["Рождаемость"] = pd.to_numeric(self.data["Рождаемость"], errors='coerce')
            self.data["Смертность"] = pd.to_numeric(self.data["Смертность"], errors='coerce')
        except Exception as e:
            print(f"Ошибка загрузки {CSV_FILE}: {e}")
            self.data = pd.DataFrame(columns=["Год", "Рождаемость", "Смертность", "Тип"])

    def initUI(self):
        self.setWindowTitle("Рождаемость / Смертность")
        self.resize(1100, 650)

        control_layout = QVBoxLayout()
        control_layout.setSpacing(10)
        control_layout.setContentsMargins(8, 8, 8, 8)

        pop_group = QGroupBox("Население")
        pop_layout = QVBoxLayout()
        self.radio_all = QRadioButton("Все")
        self.radio_urban = QRadioButton("Городское")
        self.radio_rural = QRadioButton("Сельское")
        self.radio_urban.setChecked(True)
        for rb in [self.radio_all, self.radio_urban, self.radio_rural]:
            pop_layout.addWidget(rb)
        pop_group.setLayout(pop_layout)

        years_group = QGroupBox("Годы")
        years_layout = QGridLayout()
        years_layout.setSpacing(4)
        years = sorted(set(list(range(1950, 2000, 10)) + [1995, 2000] + list(range(2001, 2016))))
        self.year_checks = {}
        row = col = 0
        for year in years:
            cb = QCheckBox(str(year))
            cb.setChecked(True)
            years_layout.addWidget(cb, row, col)
            self.year_checks[year] = cb
            col += 1
            if col == 2:
                col = 0
                row += 1
        years_group.setLayout(years_layout)

        control_layout.addWidget(pop_group)
        control_layout.addWidget(years_group)
        control_layout.addStretch()

        control_widget = QWidget()
        control_widget.setLayout(control_layout)

        self.figure = Figure(figsize=(9, 5))
        self.canvas = FigureCanvas(self.figure)

        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(control_widget, stretch=1)
        main_layout.addWidget(self.canvas, stretch=5)
        self.setLayout(main_layout)

        self.radio_all.toggled.connect(self.plot_graph)
        self.radio_urban.toggled.connect(self.plot_graph)
        self.radio_rural.toggled.connect(self.plot_graph)

        for cb in self.year_checks.values():
            cb.stateChanged.connect(self.plot_graph)

        self.plot_graph()

    def plot_graph(self):
        if self.data is None or self.data.empty:
            return

        pop_type = "Все" if self.radio_all.isChecked() else \
                   "Городское" if self.radio_urban.isChecked() else "Сельское"
        years = [y for y, cb in self.year_checks.items() if cb.isChecked()]
        if not years:
            return

        df = self.data[self.data["Год"].isin(years)].copy()
        if pop_type == "Все":
            df = df.groupby("Год")[["Рождаемость", "Смертность"]].sum().reset_index()
        else:
            df = df[df["Тип"] == pop_type]

        if df.empty:
            self.figure.clear()
            self.canvas.draw()
            return

        df = df.sort_values("Год")

        self.figure.clear()
        ax = self.figure.add_subplot()

        ax.plot(df["Год"], df["Рождаемость"], 'o-', label="Рождаемость", linewidth=2, markersize=5)
        ax.plot(df["Год"], df["Смертность"], 's-', label="Смертность", linewidth=2, markersize=5)

        ax.set_xlabel("Год")
        ax.set_ylabel("Человек")

        def format_func(value, tick_number):
            return f"{int(value):,}".replace(",", " ")

        ax.yaxis.set_major_formatter(mticker.FuncFormatter(format_func))
        ax.yaxis.set_major_locator(mticker.MaxNLocator(integer=True, steps=[1, 2, 5, 10]))

        ax.legend()
        ax.grid(True, linestyle='--', alpha=0.6)
        ax.tick_params(axis='x', rotation=45)

        self.canvas.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = StatisticApp()
    window.show()
    sys.exit(app.exec_())