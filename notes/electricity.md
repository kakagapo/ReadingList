# Notes on electricity and power grid

## 3 main parts of power grid

- Generation
- Transmision
- Distribution

## Notes

- North American Power grid uses 120 V (+/- 5%) for homes
- At large power plants electricity is produced at lower voltage of around 10-30 kilovolts (kV).
- Then voltage is increase to much higher voltage(to reduce losses along the way but making it dangerous) using transformers to send along transmission lines.
- Before power is distributed to houses the high voltage has to stepped down by transformers in the substations.
- Substations have lots of things that are supervised and operated remotely (using SCADA systems) and it is periodically inspected by people.

## Substations

### Types of substations

- Step-up
- High Voltage
- Step-down
- Distribution
- Distribution Transformer
- Converter
- Switching

## Things inside a substation

- Tranformers
- `Instrument transformers` are use to provide power for various system monitoring devices in a substation
- Regualtors are used to smaller adjustments to the current leaving the substation
- Bushings used to create a safe distance between energized lines and the grounded metal housings
- Large concerete walls fire barriers
- Grid of grounding rods buried below the surface

### Transformers

- Two coils - as voltage in one coil(primary) changes it creates a magenetic field which in turn couples with the other coil(secondary) inducing a voltage in the other coil. The voltage in the other coil is determined by the number of turns/loops in it versus the number of turns/loops in the primary.
- To prevent arcing the internals of a transformer is filled with a dielectric material(non-conductive) or is vaccum sealed (for lower voltages). Non-conductive oil or dense gas is used as the dielectric material in lots of transformers.

## Commmon types of faults

- Short-circuit to ground - low resitance path from a line to the ground and results in an overload. Can happen if a tree falls on a power line. Preveted by using a simple fuse.
- Overload - demand becomes so high that the system can't handle it in which case you shed load i.e. do a rolling backout or something like that.

## Circuit breakers vs fuses

- Fuse burns out at a certain current threshold, one time use.
- Circuit breakers - has the same problem as a transformers w.r.t arcing and requires the same protections like 

## Fundamentals

- Current leaves the source and returns to the source
- Bonding - connection of non-current-carrying conductive elements like enclosures and structures
- Grounding - attachment of bonded systems to the earth

## Glossary

- SCADA - Supervisory control and data acquisition, a control system architecture

## References

- [United States Electricity Industry Primer](https://www.energy.gov/sites/prod/files/2015/12/f28/united-states-electricity-industry-primer.pdf)
- [Wiki - North American power transmission grid](https://en.wikipedia.org/wiki/North_American_power_transmission_grid)
