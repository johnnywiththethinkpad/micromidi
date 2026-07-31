#micro:midi

An open-source, embedded Digital Audio Workstation (DAW) and loop sequencer built for the **micro:bit v2** using Microsoft MakeCode.
##Control Layout

The system utilizes the on-board micro:bit physical inputs to navigate the interface and manage the audio sequencer state:

* **Button B**: Moves the visual cursor along the **X-axis** (horizontal grid navigation).
* **Button A**: Moves the visual cursor along the **Y-axis** (vertical grid navigation).
* **Touch Logo**: **Places a note** at the current cursor coordinates.
* **Button A + B (Combined)**: **Wipes all notes** clean from the memory grid to start a fresh track.

##Development 
1. [x] Core grid environment configuration & XY cursor movement coordinates.
2. [ ] Note variable mapping and dynamic audio frequency routing.
3. [ ] Memory List Array storage allocation for active step sequencing.
4. [ ] Background clock sync for looped loop playback based on custom BPM variables.
