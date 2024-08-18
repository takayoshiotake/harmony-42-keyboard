# Harmony 42

[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]
[![KiCad][kicad-shield]][kicad]
[![Vial][vial-shield]][vial]

A 42-key keyboard.

![](gallery/001.jpg)

- Switch: TTC Frozen V2
- Keycap: StarryPoem + HIBI Artisan

## Concept

![](layout/concept.svg)

## Layout

v0.1.0

![](layout/keyboard-layout.png)

- width: 14u
- depth: <6u

Made with Python script: 📁 [editor](layout/editor)

- 📄 [locations.csv](layout/locations.csv)
- 📄 [keyboard-layout.rawdata.json](layout/keyboard-layout.rawdata.json)

## Schematic and PCB

![schematic svg](assets/pcb_schematic.svg)

![pcb png](assets/pcb_t.png)

![pcb png](assets/pcb_b.png)

![schematic svg](assets/mcu_schematic.svg)

![pcb png](assets/mcu_t.png)

KiCad files:

- 📄 [harmony-42-pcb.kicad_sch](electronics/harmony-42-pcb/harmony-42-pcb.kicad_sch) (v1.0.0)
- 📄 [harmony-42-pcb.kicad_pcb](electronics/harmony-42-pcb/harmony-42-pcb.kicad_pcb) (v1.0.0)
- 📄 [mcu-16-pcb.kicad_sch](electronics/mcu-16-pcb/mcu-16-pcb.kicad_sch) (v1.0.0)
- 📄 [mcu-16-pcb.kicad_pcb](electronics/mcu-16-pcb/mcu-16-pcb.kicad_pcb) (v1.0.0)

## Mechanics

![topview svg](assets/case_plate.png)

Files:

- 📄 [harmony-42-case-topview.svg](mechanics/harmony-42-case-topview.svg)
    - 📄 [1.5mm PMMA plate for 遊舎工房 レーザー加工サービス](mechanics/harmony-42-plate_Laser_A4_template_inkscape.svg)
        - アクリル クリア 1.5mm A4
    - 📄 [2mm PORON gasket for 遊舎工房 レーザー加工サービス](mechanics/harmony-42-gasket_Poron%20laserCut%20Template%202022-10-20_OUTLINED.svg)
        - フォーム 2mm 297x190接着シート付き
- 📄 [harmony-42-case.FCStd](mechanics/harmony-42-case.FCStd)
    - 📄 [harmony-42-case-Top.step](mechanics/harmony-42-case-Top.step)
    - 📄 [harmony-42-case-Bottom.step](mechanics/harmony-42-case-Bottom.step)

## Firmware

### Vial

- Built UF2
    - 📄 [takayoshiotake_harmony_42_vial_20240726.uf2](vial-bin/takayoshiotake_harmony_42_vial_20240726.uf2)

See [vial-porting](vial-porting) for more details.

## License

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/license-CC%20BY--SA%204.0-lightgrey.svg

[kicad]: https://www.kicad.org/
[kicad-shield]: https://img.shields.io/badge/KiCad-314CB0.svg

[vial]: https://get.vial.today/
[vial-shield]: https://img.shields.io/badge/Vial-03045E.svg
