# Reference Analysis & Implementation Notes (`3.mp4`)

## Reference Video Analysis (`3.mp4`)
- **Source**: Downloaded directly from the attached reference link (`202x360`, `30 fps`, `duration: 49.784s`).
- **Tools Run**:
  - `npx hyperframes measure cuts /tmp/ref_3.mp4` (30 fps exact cut points).
  - `ffmpeg` dense `10 fps` frame extraction across World 3B (`22.8s–31.8s`, 90 frames) and World 4 (`31.2s–43.2s`, 120 frames) tiled into contact sheets for side-by-side comparison.

---

## World 3B: Manuscript / Blueprint Scene (`23.08s – 31.46s`)

### Exact Measured Cuts & Motion (`3.mp4`)
1. **Shot 3B-1 (`23.08s – 25.48s`) — Graph-Paper Reveal & 5-App In-Place Swap**:
   - **Cut/Entry**: `23.367s` (frame `701`) wipes from dark 3D apps onto off-white gray blueprint paper (`#eceef1`, fine dual-level grid, subtle `rotateX`).
   - **Camera**: Gentle push-in (`1.04 -> 1.08`, `sine.inOut`) as center app tile swaps in place.
   - **Measured Swap Timings** (matching `measure cuts` frames `701, 717, 725, 733`):
     - `23.367s -> 23.62s`: HungerStation
     - `23.62s -> 23.90s`: Google Maps
     - `23.90s -> 24.167s`: Salla
     - `24.167s -> 24.433s`: Absher
     - `24.433s -> 25.48s`: Tamara (anchors in place)
   - **Sticky Note**: Tilted yellow sticky note (`"التطبيقات بشكل عام"`) with dark outline, soft shadow, top highlight sheen, 2 semi-transparent corner tape strips, and deterministic 3D wind oscillation (`rotationX`, `rotationY`, `skewX`) + corner tape flutter.

2. **Shot 3B-2 (`25.48s – 28.14s`) — Pan Up-Right to Apple Pay & Crimson Red X**:
   - **Framing**: Diagonal pan up-right (`x: -5550, y: 490`, `power2.inOut`) keeps Tamara visible in the bottom-left quadrant while centering Apple Pay right-of-center inside a hand-drawn double-stroke circle.
   - **Accent**: Crimson Red Brush `X` (`#dc2626`) slashes over Apple Pay (`26.38s -> 26.86s`, `power3.out`), accompanied by `#w3b-guard-badge` (`"بدون تفاصيل سرية!"`, `mix-blend-mode: multiply`).

3. **Shot 3B-3 (`28.14s – 29.26s`) — Return Pan to Tamara + Waiter Sticky Note**:
   - **Camera**: Pull-back pan down-left (`scale 1.14 -> 0.92`, `power2.inOut`) re-centering Tamara and revealing `"نرجع للنادل!"` yellow sticky note with wind oscillation.

4. **Shot 3B-4 (`29.26s – 31.46s`) — Pan Up-Right to Flork Waiter + Emerald Checkmark**:
   - **Measured Cuts**: `29.733s` (frame `892`), `30.433s` (frame `913`), `31.267s` (frame `938` -> dissolve into World 4).
   - **Motion**: Red `X` fades (`29.55s`), Flork Waiter with burger enters from left (`29.38s`), Flork Card enters from right (`29.62s`), crisp green checkmark `✓` with white halo draws cleanly (`29.88s`).

---

## World 4: Tabby 3D GLB Phone & Spatial Stage (`31.46s – 42.88s`)
- **Phone Entrance (`31.46s -> 32.22s`)**: Side-profile 3D rotation (`rotY: -1.48 -> -0.32`) matching `3.mp4` (`31.5s–32.0s`), surrounded by blurred depth-layered Noon, Amazon, Purple stripe, Salla, and shopping-bag badges.
- **Macro Dive (`34.18s -> 35.95s`, cut at `34.233s`)**: Smooth camera dive onto the mint `tabby` button (`pressAmt` + ripple at `34.50s`).
- **Tabby Emblem & Processing Flow (`36.00s -> 41.20s`)**:
  - `36.80s -> 38.80s`: Clean centered glowing Mint Tabby tile (`w4-tabby-tile`) hold after phone slides off left.
  - `38.80s -> 39.75s`: Spinning green cycle arrows (`معالجة الطلب`).
  - `39.75s -> 41.15s`: Branching curves stroke out into 4 stacked perforated installment tickets (`دفعة ١..٤`).
- **Finale (`41.22s -> 42.88s`)**: Whip pan back to upright 3D iPhone with `"تم الدفع بنجاح ✓"`, 6 bursting green checkmarks, and celebrating Flork.

---

## Remaining Minor Intentional Differences from `3.mp4`
- **4px Black Tile Borders & Guard Callout**: Kept `4px solid #09090b` rounded-square app borders, inner sheen gradients, and `"بدون تفاصيل سرية!"` shield annotation per explicit user specification.
- **GLB iPhone Screen UI**: Custom crisp Arabic e-commerce checkout (`"لابتوب كويس (أتوقع)"`, `"٤٠٠٠ ر.س"`) mapped onto real Draco GLB mesh `xXDHkMplTIDAXLN` (`RoomEnvironment` PMREM studio lighting).
