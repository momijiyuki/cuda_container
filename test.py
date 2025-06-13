import matplotlib.pyplot as plt
import numpy as np
import torch


def main() -> None:
    print(f"device: {'cuda' if torch.cuda.is_available() else 'cpu'}")
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)
    plt.plot(x, y)
    plt.show()


if __name__ == "__main__":
    main()
