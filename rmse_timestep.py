import os
import matplotlib.pyplot as plt
import numpy as np

def plot_overlay_rmse_b(
    npz_paths,
    labels=None,
    step_min=None,
    step_max=None,
    save=False,
    fname="overlay_rmse.png"
):
    if labels is None:
        labels = [os.path.basename(p).replace(".npz", "") for p in npz_paths]

    colors = ["tab:pink", "tab:blue", "tab:orange", "tab:green", "tab:red"]

    plt.figure(figsize=(12, 3.2))

    for i, (path, lab) in enumerate(zip(npz_paths, labels)):
        d = np.load(path)

        step = d["step"].astype(int)
        rmse_b = d["rmse_b"].astype(float)

        mask = np.ones_like(step, dtype=bool)
        if step_min is not None:
            mask &= (step >= step_min)
        if step_max is not None:
            mask &= (step <= step_max)

        plt.plot(
            step[mask],
            rmse_b[mask],
            label=lab,
            linewidth=1.2,
            color=colors[i % len(colors)]
        )

    plt.xlabel("Time steps")
    plt.ylabel("RMSE")
    plt.grid(True, alpha=0.3)
    plt.legend(loc="upper right")
    plt.tight_layout()

    if save:
        plt.savefig(fname, dpi=400, bbox_inches="tight")
        print(f"[Saved] {fname}")

    plt.show()


# =========================
# settings
# =========================
num = 2    # CASE number

paths = [
    f"./CASE{num}_LETKF_Ne50_rmse_b.npz",
    f"./CASE{num}_GETKF_Ne50_rmse_b.npz",
    f"./CASE{num}_MLETKF_noR_Ne50_rmse_b.npz",
    f"./CASE{num}_MLETKF_R_Ne50_rmse_b.npz",
    f"./CASE{num}_MLETKF_Z_Ne50_rmse_b.npz",
]

labels = [
    "LETKF",
    "GETKF",
    "MLETKF-noR",
    "MLETKF-R",
    "MLETKF-Z"
]

# =========================
# plot
# =========================
plot_overlay_rmse_b(
    npz_paths=paths,
    labels=labels,
    step_min=3000,
    step_max=4000,
    save=True,
    fname=f"CASE{num}_overlay_rmse_3000_4000.png"
)