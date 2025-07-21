# Solar-System 3-D Simulator ★ Processing.py

Interactive, real-time 3-D simulation of our Solar System written in **Processing 3 – Python mode**  
with **PeasyCam** free-orbit navigation and a **ControlP5** control panel.

> **Project history**: built in **2021**, when I was **16 y.o. (Terminale, final year of French high-school)** as a personal physics & coding challenge.

---

## ✨ Highlights

| Area | Features |
|------|----------|
| **Orbital Mechanics** | Newtonian N-body integration (configurable `step` & `precision`). |
| **Scalable Rendering** | Log-scaled radii & distance factors (`facteur`, `facteur_dessin`) so every planet fits in frame. |
| **Free Camera** | Full 6-DOF orbit / zoom / roll via **PeasyCam**; adjustable speed (`c`/`w`). |
| **Dual Windows** | **Simulation** viewport + **Parameters** panel (POV selection, toggles, trajectory controls…). |
| **HUD** | Live overlay: elapsed time, step, precision, FPS, camera coords & current POV infos. |
| **Trajectories** | Per-planet path tracing with colour coding; clear or switch reference frame on the fly. |
| **Focus Mode** | Sit “on board” the chosen planet (camera distance → 0) for immersive flight. |
| **Extensible Data** | Planet parameters imported from `bodys_infos.csv` and wrapped in the `Body` class (mass, colour, radius, tilt, etc.). |

---

## 📸 Screenshots

![Plan view with trajectories](docs/captures/screenshot_orbits_01.png)

![Clean circular view](docs/captures/screenshot_orbits_02.png)

![Control panel window](docs/captures/screenshot_params.png)

*(All captures generated on Windows 10, Processing 3.5.4)*

---

## Project Layout

```text
solar-system/
├── SolarSystem.pyde              # main Processing sketch
├── bodys.py                      # Body class + CSV loader
├── bodys_infos.csv               # planetary data
├── docs/
│   └── captures/                 # screenshots (png)
└── README.md
````

---

## Installation

| Requirement        | Version                                            |
| ------------------ | -------------------------------------------------- |
| **Processing 3.x** | ≥ 3.5.4                                            |
| **Python Mode**    | via *Contribution Manager*                         |
| **Libraries**      | `peasycam`, `controlP5` (install from *Libraries*) |
| **Java**           | JDK 8 or 11                                        |

```bash
git clone https://github.com/Skyxo/systeme-solaire.git
cd systeme-solaire

# open SolarSystem.pyde in Processing, switch to Python mode and press ▶
```

---

## Controls

| Action                        | Key                   |
| ----------------------------- | --------------------- |
| Orbit camera (pitch / yaw)    | `z` / `s` / `q` / `d` |
| Roll camera                   | `a` / `e`             |
| Zoom in / out                 | `Space` / `Ctrl`      |
| Camera speed ±                | `c` / `w`             |
| Increase / decrease Δt        | `↑` / `↓`             |
| Increase / decrease precision | `→` / `←`             |
| Planet scale ±                | `+` / `-`             |

All other toggles (HUD, names, trajectories, lock, focus, pause…) live in the **Parameters** window.

---

## Quick Tips

1. **Pick a POV** in the Parameters window to centre on any planet; tick **Lock** to stay locked.
2. Enable **Traj.** to trace selected orbits; switch **Ref** to render in a planet-centred frame.
3. Turn on **Focus** for a cockpit-style view on the active body.
4. Adapt `step` and `precision` for the accuracy / speed trade-off you need.

---

## To Do

* Relativistic corrections & tidal forces
* High-res textures / ring meshes
* Moon & minor-body catalogue
* CSV / OBJ export of trajectories
* Port to Processing 4 or PyOpenGL

---

## Licence & Credits

Code released under the **MIT Licence**.
Third-party libraries:

* **PeasyCam** © Jonathan Feinberg
* **ControlP5** © Andreas Schlegel

Planetary data simplified from NASA open datasets.

Made with passion by **Skyxo** (age 16), 2021.
