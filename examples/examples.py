import matplotlib.pyplot as plt
from usyd_colors import get_palette

def create_bar_plot():
    primary_palette = get_palette('primary')

    categories = ['A', 'B', 'C', 'D', 'E']
    values = [5, 7, 3, 8, 4]

    # Create bar plot with custom colors from the palette
    plt.figure(figsize=(8, 6))
    plt.bar(categories, values, color=primary_palette.hex_colors())
    plt.title('Bar Plot with USYD Primary Palette', fontsize=16)
    plt.ylabel('Values', fontsize=12)
    plt.savefig('examples/bar_plot_primary.png')

# Using matplotlib
def create_heatmap():
    import matplotlib.pyplot as plt
    import numpy as np
    from usyd_colors import get_palette, PaletteName

    heatmap_palette = get_palette(PaletteName.HEATMAP)
    data = np.random.rand(10, 10)

    # Create heatmap with the heatmap palette
    plt.figure(figsize=(8, 6))
    plt.imshow(data, cmap=heatmap_palette.matplotlib_colormap(), aspect='auto')
    plt.title('Heatmap with USYD Heatmap Palette', fontsize=16)
    plt.colorbar()
    plt.savefig('examples/heatmap_heatmap.png')

if __name__ == '__main__':
    create_bar_plot()
    create_heatmap()