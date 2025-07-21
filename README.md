# Solar-System 3-D Simulator ★ Processing.py

Real-time 3-D simulation of our Solar System built with **Processing 3 – Python mode**,  
**PeasyCam** free-orbit navigation and a **ControlP5** command panel.

> **Built in 2021, age 16 (Terminale)** – a personal project that taught me both physics and code.

---

## ✨ Highlights

| Area | Features |
|------|----------|
| **Orbital Mechanics** | Newtonian *N-body* integration (configurable `step` & `precision`). |
| **Scalable Rendering** | Log-scaled radii + distance factors so every planet fits on screen; tweak with `+ / -`. |
| **Free Camera** | Full 6-DOF orbit / zoom / roll via **PeasyCam**; adjustable speed (`c` / `w`). |
| **Dual Windows** | **Simulation** viewport **+** **Parameters** panel (POV, toggles, trajectory tools…). |
| **HUD Overlay** | Elapsed time, Δt, precision, FPS, camera coords, instant planet stats. |
| **Trajectories** | Per-planet path tracing with colour coding; instant clear & reference-frame switch. |
| **Focus Mode** | “On-board” view: camera snaps to the selected planet’s centre for an immersive ride. |
| **Extensible Data** | Planet parameters loaded from `bodys_infos.csv` and wrapped in a `Body` class. |

---

## 📸 Screenshots & Tiny Story

| Planet-centric frame (retrograde revealed) | Classical heliocentric frame | Parameters window |
|---|---|---|
| <img alt="Planet-centric view" src="https://github.com/user-attachments/assets/4b26b92d-619f-4d45-988e-2561e5a6033c" width="430"> | <img alt="Heliocentric view" src="https://github.com/user-attachments/assets/f560b850-8c69-4009-8e46-2d982b3bbc98" width="430"> | <img alt="Control panel" src="https://github.com/user-attachments/assets/48ba21c0-222e-47e9-a928-19bb03082271" width="270"> |

*The **Switch Ref** button toggles between a heliocentric view and a planet-centric frame.  
While playing with it I spotted the looping paths of Mars and Venus – my first self-discovery of “retrograde motion”, something I hadn’t yet seen in class.*

---

## 📂 Project Layout

```text
systeme-solaire/
├── SolarSystem.pyde            # main Processing sketch
├── bodys.py                    # Body class + CSV loader
├── bodys_infos.csv             # Planetary data (NASA-derived)
└── README.md
````

---

## ⚙️ Installation

| Requirement        | Version                    |
| ------------------ | -------------------------- |
| **Processing 3.x** | ≥ 3.5.4                    |
| **Python Mode**    | via *Contribution Manager* |
| **Libraries**      | `peasycam`, `controlP5`    |
| **Java**           | JDK 8 or 11                |

```bash
git clone https://github.com/Skyxo/systeme-solaire.git
cd systeme-solaire
# Open SolarSystem.pyde in Processing (Python mode) and press ▶
```

---

## 🎮 Key Controls

| Action              | Key                |
| ------------------- | ------------------ |
| Orbit / pitch / yaw | `z`, `s`, `q`, `d` |
| Roll                | `a`, `e`           |
| Zoom in / out       | `Space`, `Ctrl`    |
| Camera speed ±      | `c`, `w`           |
| Δt ±                | `↑`, `↓`           |
| Precision ±         | `→`, `←`           |
| Planet scale ±      | `+`, `-`           |

All other toggles (HUD, Names, Traj., Lock, Focus, Pause…) live in the **Parameters** window.

---

## 💡 Tips

1. **Select a POV** and tick **Lock** to stay centred on a body.
2. Toggle **Traj.** and press **Switch Ref** to compare heliocentric vs planet-centric orbits.
3. Activate **Focus** for a cockpit-style ride.
4. Adjust `step` and `precision` to balance speed vs accuracy.

---

## 🛣️ Roadmap

* Relativistic corrections.
* High-res textures & ring meshes.
* Moon / asteroid catalogue.
* CSV / OBJ export of trajectories.
* Port to Processing 4 or PyOpenGL.

---

## 📜 Licence & Credits

Code licensed under **MIT**.
Libraries: **PeasyCam** © Jonathan Feinberg, **ControlP5** © Andreas Schlegel.
Planetary data simplified from NASA open datasets.

Made with passion by **Skyxo** – 16 years old, 2021.
