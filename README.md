#micro:midi

An open-source, embedded Digital Audio Workstation (DAW) and loop sequencer built for the **micro:bit v2** using Microsoft MakeCode.
##Control Layout

The system utilizes the on-board micro:bit physical inputs to navigate the interface and manage the audio sequencer state:

* **Button B**: Moves the visual cursor along the **X-axis** (horizontal grid navigation).
* **Button A**: Moves the visual cursor along the **Y-axis** (vertical grid navigation).
* **Touch Logo**: **Places a note** at the current cursor coordinates.
* **Shake**: Plays the Notes
* **A+B**: Changes Playing Mode (MIDIMODE) (BITMODE)
For the microbit to actually speak to MIDI devices use hairless midi at: https://projectgus.github.io/hairless-midiserial/ and to further use other DAWs you must use https://www.tobias-erichsen.de/software/loopmidi.html

(WARNING) Midimode is very dependent on the cable you use and your setup it can skip notes or not play them at all due to the 64MHz ARM CPU inside the microbit V2
