import matplotlib.pyplot as plt  # Funcion para graficar

def plot_df(
    df,
    x,
    y,
    title="",
    xlabel="Fecha",
    ylabel="Numero de Pasajeros",
    colores="",
    dpi=100,
):
    plt.figure(figsize=(15, 4), dpi=dpi)
    plt.plot(x, y, color=colores)
    plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
    plt.show()


def plot_ts2(
    df,
    x,
    y,
    title="",
    xlabel="Fecha",
    ylabel="Numero de Pasajeros",
    colores="",
    dpi=100,
    MA=6,
):
    ma = y.rolling(MA).mean()
    std_ma = y.rolling(MA).std()
    plt.figure(figsize=(15, 4), dpi=dpi)
    plt.plot(x, ma + std_ma, color="cyan")
    plt.plot(x, ma - std_ma, color="cyan")
    plt.fill_between(
        x, y1=ma + std_ma, y2=ma - std_ma, alpha=0.3, linewidth=2, color="cyan"
    )
    plt.plot(x, ma, color="red", label="Media Movil")
    plt.plot(x, y, color=colores, label="Original")
    plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
    plt.legend(loc="best")
    plt.show()
