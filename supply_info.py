"""Following information is used to calculate cost saving within the hazardous waste program. Commits from
4/3/2023 are from Clean Earth pricing"""


etoh_waste_supplies = {'18_gal_container_empty': 44.230,
                       '18_gal_container_full': 389,
                       '18_gal_total': 433.23,
                       '5_gal_carboy_empty': 18,
                       '5_gal_carboy_full': 92.970,
                       '5_gal_carboy_total': 110.97,
                       '33_gal_biohazard_box_empty': 0,
                       '33_gal_biohazard_box_full': 30
                       }


def kingfisher_plates_to_biohaz_box(lp_container):
    """Function used to convert volume of waste generated from LP containers to biohaz boxes, will also calculate the associated
    costs and cost reduction percent."""
    biohaz_box_amount = lp_container * 2
    lp_cost = lp_container * etoh_waste_supplies['18_gal_total']
    biohaz_cost = biohaz_box_amount * etoh_waste_supplies['33_gal_biohazard_box_full']
    cost_saving = lp_cost - biohaz_cost
    cost_reduction_percent = 100 - ((biohaz_cost / lp_cost) * 100)
    return f'Loose Pack EtOH cost: ${lp_cost} \nBiohazard box amount: {biohaz_box_amount} \nBiohazard box cost: ${biohaz_cost} \nCost savings: ${cost_saving} \nCost Reduction: {cost_reduction_percent}%'


print(kingfisher_plates_to_biohaz_box(lp_container=1))