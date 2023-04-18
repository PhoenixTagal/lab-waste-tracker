"""Following information is used to calculate cost saving within the hazardous waste program. Commits from
4/3/2023 are from Clean Earth pricing"""


etoh_waste_supplies = {'18_gal_container_empty_$': 44.230,
                       '18_gal_container_full_$': 384.91,
                       '18_gal_total_$': 429.14,
                       '5_gal_carboy_empty_$': 18,
                       '5_gal_carboy_full_$': 92.970,
                       '5_gal_carboy_total_$': 110.97,
                       '33_gal_biohazard_box_empty_$': 0,
                       '33_gal_biohazard_box_full_$': 30,
                       'etoh_in_18_gal_container_cost_$': 11,
                       'trays_per_18_gal_container': 50,
                       'weight_of_empty_18_gal_container_lbs': 5.5,
                       'weight_of_etoh_in_empty_18_gal_container_lbs': 3.85,
                       'weight_attributed_to_trays_in_18_gal_container': 0,
                       'biowaste_box_max_waste_lbs': 50,
                       'avg_full_biohaz_box_lbs': 19,
                       'avg_full_18-gal-container_lbs': 18,
                       'yearly_etoh_lbs': 9968,
                       'average_full_18-gal-container_shipped_per_year': 554
                       }


def weight_break_down_18_gal_container():
    """Calculates the weight breakdown of the current 18 gal waste containers generated by KingFisher Extraction. Data
    is used to map cost to a new management practice."""
    weight_of_trays = etoh_waste_supplies['avg_full_18-gal-container_lbs'] - (etoh_waste_supplies['weight_of_empty_18_gal_container_lbs'] + etoh_waste_supplies['weight_of_etoh_in_empty_18_gal_container_lbs'])
    return f'Weight of trays: {weight_of_trays} lbs'


def kingfisher_plates_to_biohaz_box(lp_container):
    """Function used to convert volume of waste generated from LP containers to biohaz boxes, will also calculate the associated
    costs and cost reduction percent."""
    biohaz_box_amount = lp_container * 0.5
    lp_cost = lp_container * etoh_waste_supplies['18_gal_total_$']
    biohaz_cost = biohaz_box_amount * etoh_waste_supplies['33_gal_biohazard_box_full_$']
    etoh_cost = etoh_waste_supplies['etoh_in_18_gal_container_cost_$'] * lp_container
    cost_saving = lp_cost - (biohaz_cost + etoh_cost)
    proposed_cost = biohaz_cost + etoh_cost
    cost_reduction_percent = 100 - ((proposed_cost / lp_cost) * 100)
    etoh_amount = lp_container * 2
    return f'Current Loose Pack EtOH cost: ${lp_cost} \nNew Process Cost: ${proposed_cost} \nBiohazard box amount: {biohaz_box_amount} \nBiohazard box cost: ${biohaz_cost} \nEtOH Volume: {etoh_amount}L \nEtOH Cost (shipped under EtOH Solution Waste Stream): ${etoh_cost} \nCost savings: ${cost_saving} \nCost Reduction: {cost_reduction_percent}%'


print(weight_break_down_18_gal_container())
print('LP EtOH Containers shipped in 2022: 444')
print(f'1 LP Container ($429.214) ~ 0.5 Biohaz Box($15) + 2L liquid EtOH ($11)')
print()
print('Cost Break Down:')
print(kingfisher_plates_to_biohaz_box(lp_container=444))