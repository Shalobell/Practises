import matplotlib.pyplot as plt
import numpy as np


def calculate_break_even(fixed_costs, variable_costs_per_unit, price_per_unit):
    if price_per_unit <= variable_costs_per_unit:
        return None
    return fixed_costs / (price_per_unit - variable_costs_per_unit)


def plot_break_even(fixed_costs, variable_costs_per_unit, price_per_unit, planned_volume, ax):
    break_even = calculate_break_even(fixed_costs, variable_costs_per_unit, price_per_unit)
    if break_even is None:
        return None

    max_volume = max(planned_volume * 1.2, break_even * 2.5, 300)
    volumes = np.linspace(0, max_volume, 200)

    total_revenue = price_per_unit * volumes
    fixed_costs_line = np.full_like(volumes, fixed_costs)
    variable_costs = variable_costs_per_unit * volumes
    total_costs = fixed_costs + variable_costs

    ax.plot(volumes, total_revenue, label='Валовый доход (TR)', color='blue', linewidth=2)
    ax.plot(volumes, fixed_costs_line, label='Постоянные издержки (FC)', color='orange', linewidth=2)
    ax.plot(volumes, variable_costs, label='Переменные издержки (VC)', color='green', linewidth=2)
    ax.plot(volumes, total_costs, label='Валовые издержки (TC)', color='red', linewidth=3)

    break_even_revenue = price_per_unit * break_even
    ax.plot(break_even, break_even_revenue, 'ko', markersize=10, label='Точка безубыточности', zorder=5)
    ax.axvline(x=break_even, color='black', linestyle='--', linewidth=1.5, alpha=0.7)
    ax.axhline(y=break_even_revenue, color='black', linestyle='--', linewidth=1.5, alpha=0.7)

    annotation_text = f'Точка безубыточности\nBEP = FC / (P - AVC)\n({break_even:.0f}, {int(break_even_revenue)})'
    ax.annotate(annotation_text,
                xy=(break_even, break_even_revenue),
                xytext=(break_even * 1.25, break_even_revenue * 1.15),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5, connectionstyle='arc3,rad=0.1'),
                fontsize=9,
                bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor='black', alpha=0.9),
                ha='left', va='bottom')

    ax.set_xlabel('Шт.', fontsize=11)
    ax.set_ylabel('Руб.', fontsize=11)
    ax.set_title(f'График безубыточности при цене = {price_per_unit:.2f} р.', fontsize=12, fontweight='bold')
    ax.grid(True, alpha=0.3, linestyle=':')
    ax.legend(loc='upper left', fontsize=9)
    ax.set_xlim(0, max_volume)
    ax.set_ylim(0, max(total_revenue[-1], total_costs[-1]) * 1.15)
    ax.ticklabel_format(style='plain', axis='y', useOffset=False)
    ax.xaxis.set_major_locator(plt.MaxNLocator(10))
    ax.yaxis.set_major_locator(plt.MaxNLocator(8))

    return break_even


fixed_costs_1 = 55000
variable_costs_1 = 250
price_1 = 450
planned_volume_1 = 300

fixed_costs_2 = 35000
variable_costs_2 = 150
price_2 = 300
planned_volume_2 = 200

break_even_1 = calculate_break_even(fixed_costs_1, variable_costs_1, price_1)
break_even_2 = calculate_break_even(fixed_costs_2, variable_costs_2, price_2)

print(f"Сценарий 1: ТБ = {break_even_1:.1f} шт., Цена = {price_1} руб.")
print(f"Сценарий 2: ТБ = {break_even_2:.1f} шт., Цена = {price_2} руб.")

fig, axes = plt.subplots(1, 2, figsize=(16, 6))
plot_break_even(fixed_costs_1, variable_costs_1, price_1, planned_volume_1, axes[0])
plot_break_even(fixed_costs_2, variable_costs_2, price_2, planned_volume_2, axes[1])

plt.tight_layout()
plt.savefig('break_even_comparison.png', dpi=300, bbox_inches='tight')
plt.show()