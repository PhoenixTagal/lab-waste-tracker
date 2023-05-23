"""Following information is map cost for the sequencing waste stream at Adaptive.
One kit is used per run, regardless of cycle count for kit.
This is for waste generated from NexSeq (current state).
Adaptive will potentially transition to NovaSeq"""

sequencing_waste_supplies = {'15_gal_poly_empty_$': 66,
                             '15_gal_poly_disposal_$': 348.18,
                             'next_seq_waste_volume_per_run_ml': 1480.45,  #avg taken from 150 and 300 cycle kit waste volumes provided by Barb Z
                             'nova_seq_waste_volume_per_run_ml': 18800, #from s4 300 cycle dual side
                             'sequencing_drum_volume_in_ml': 56781.2,
                             'samples_analyzed_per_year': 0,
                             'clonoseq_samples_analyzed_per_nextseq_run': 24, #provided by illumina rep
                             'clonoseq_samples_analyzed_per_novaseq_run': 576, #provided by illumina rep
                             'total_clonoseq_samples_analyzed_in_2022': 55480 #sum of ID and MRD year end totals
                            }


def sequencing_life_cycle_cost():
    total_cost = sequencing_waste_supplies['15_gal_poly_empty_$'] + sequencing_waste_supplies['15_gal_poly_disposal_$']
    return total_cost

sequencing_waste_supplies['sequencing_drum_life_cycle_cost'] = sequencing_life_cycle_cost()


def next_seq_runs_per_sequencing_drum():
    runs_per_drum = sequencing_waste_supplies['sequencing_drum_volume_in_ml'] / sequencing_waste_supplies['next_seq_waste_volume_per_run_ml']
    return round(runs_per_drum)  #rounding runs per drum is necessary to make sense

sequencing_waste_supplies['next_seq_runs_per_sequencing_drum'] = next_seq_runs_per_sequencing_drum()


def cost_per_next_seq_run():
    run_cost = sequencing_waste_supplies['sequencing_drum_life_cycle_cost'] / sequencing_waste_supplies['next_seq_runs_per_sequencing_drum']
    return round(run_cost)


def nova_seq_runs_per_sequencing_drum():
    nova_runs_per_drum = sequencing_waste_supplies['sequencing_drum_volume_in_ml'] / sequencing_waste_supplies['nova_seq_waste_volume_per_run_ml']
    return round(nova_runs_per_drum)

sequencing_waste_supplies['nova_seq_runs_per_sequencing_drum'] = nova_seq_runs_per_sequencing_drum()


def cost_per_nova_seq_run():
    nova_run_cost = sequencing_waste_supplies['sequencing_drum_life_cycle_cost'] / sequencing_waste_supplies['nova_seq_runs_per_sequencing_drum']
    return round(nova_run_cost)


"""The following functions are used to calculate disposal cost based on number of colonoseq samples analyzed in 2022"""


def next_seq_annual_cost():
    total_next_seq_runs = sequencing_waste_supplies['total_clonoseq_samples_analyzed_in_2022'] / sequencing_waste_supplies['clonoseq_samples_analyzed_per_nextseq_run']
    next_seq_annual_disposal_cost = total_next_seq_runs * cost_per_next_seq_run()
    return round(next_seq_annual_disposal_cost)



def nova_seq_annual_cost():
    total_nova_seq_runs = sequencing_waste_supplies['total_clonoseq_samples_analyzed_in_2022'] / sequencing_waste_supplies['clonoseq_samples_analyzed_per_novaseq_run']
    nova_seq_annual_disposal_cost = total_nova_seq_runs * cost_per_nova_seq_run()
    return round(nova_seq_annual_disposal_cost)


print(f'Total cost of sequencing drum (supply cost + disposal cost): ${sequencing_life_cycle_cost()}')
print('')
print(f'Next Seq runs per sequencing waste drum: {next_seq_runs_per_sequencing_drum()}')
print(f'Disposal cost of one Next Seq run: ${cost_per_next_seq_run()}')
print('')
print(f'Nova Seq runs per sequencing waste drum: {nova_seq_runs_per_sequencing_drum()}')
print(f'Disposal cost of one Nova Seq run: ${cost_per_nova_seq_run()}')
print('')
print('')
print(f'Next Seq Annual Disposal Spend: ${next_seq_annual_cost()}')
print(f'Nova Seq Annual Disposal Spend: ${nova_seq_annual_cost()}')
print(f'Annual Savings gained by using Nova Seq: ${next_seq_annual_cost() - nova_seq_annual_cost()}')

