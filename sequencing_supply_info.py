"""Following information is map cost for the sequencing waste stream at Adaptive.
One kit is used per run, regardless of cycle count for kit.
This is for waste generated from NexSeq (current state).
Adaptive will potentially transition to NovaSeq"""

sequencing_waste_supplies = {'15_gal_poly_empty_$': 66,
                             '15_gal_poly_disposal_$': 348.18,
                             'seq_waste_volume_per_run_ml': 1480.45,  #avg taken from 150 and 300 cycle kit waste volumes provided by Barb Z
                             'sequencing_drum_volume_in_ml': 56781.2,
                            }


def sequencing_life_cycle_cost():
    total_cost = sequencing_waste_supplies['15_gal_poly_empty_$'] + sequencing_waste_supplies['15_gal_poly_disposal_$']
    return total_cost


sequencing_waste_supplies['sequencing_drum_life_cycle_cost'] = sequencing_life_cycle_cost()


def runs_per_sequencing_drum():
    runs_per_drum = sequencing_waste_supplies['sequencing_drum_volume_in_ml'] / sequencing_waste_supplies['seq_waste_volume_per_run_ml']
    return round(runs_per_drum)  #rounding runs per drum is necessary to make sense


sequencing_waste_supplies['runs_per_sequencing_drum'] = runs_per_sequencing_drum()


def cost_per_run():
    run_cost = sequencing_waste_supplies['sequencing_drum_life_cycle_cost'] / sequencing_waste_supplies['runs_per_sequencing_drum']
    return round(run_cost)


print(f'Total cost of sequencing drum (supply cost + disposal cost): ${sequencing_life_cycle_cost()}')
print(f'Nova Seq runs per sequencing waste drum: {runs_per_sequencing_drum()}')
print(f'Disposal cost of Nova Seq run: ${cost_per_run()}')

