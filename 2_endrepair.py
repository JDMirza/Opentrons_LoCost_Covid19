from opentrons import protocol_api

# metadata
metadata = {'protocolName': 'LoCost Protocol, Part 2 of 4','author': 'JM','description': 'End Repair', 'apiLevel': '2.10'}

# protocol
def run(protocol: protocol_api.ProtocolContext):

    # labware
    endrepair = protocol.load_labware('nest_96_wellplate_2ml_deep', '6', 'End repair')
    dilution = protocol.load_labware('nest_96_wellplate_2ml_deep', '5', 'dilution')
    tube = protocol.load_labware('opentrons_24_aluminumblock_nest_1.5ml_snapcap', '3', 'Run Tube')
    tiprack = protocol.load_labware('opentrons_96_filtertiprack_200ul', '7', '200 tips')
    wastetiprack =protocol.load_labware('opentrons_96_filtertiprack_200ul', '10', '200 waste')
    smalltiprack = protocol.load_labware('opentrons_96_filtertiprack_20ul', '1', '20 tips')
    wastesmalltiprack = protocol.load_labware('opentrons_96_filtertiprack_20ul', '11', '20 waste')
    
    # pipettes
    left = protocol.load_instrument('p300_multi_gen2', 'left', tip_racks=[tiprack])
    right = protocol.load_instrument('p20_multi_gen2', 'right', tip_racks=[smalltiprack])

    # commands
    # transfers endrepair mastermix to well plate
    left.pick_up_tip(tiprack['H1'])
    wells = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1' , 'G1' , 'H1']
    for well in wells:
        left.aspirate(95, tube['A1'])
        left.dispense(95, endrepair[well])
    left.drop_tip(tiprack['H1'])

    left.pick_up_tip(tiprack['A1'])
    left.aspirate(5, endrepair['A1'])
    left.distribute(6.7, endrepair['A1'], endrepair.columns()[1:12], disposal_volume=0, new_tip='never')
    left.drop_tip(wastetiprack['A1'])
    
    # transfer diluted amplicon to well plate for endrepair
    wells = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12']
    for well in wells:
        right.pick_up_tip(smalltiprack[well])
        right.aspirate(3.3, dilution[well])
        right.dispense(5, endrepair[well])
        right.speed.aspirate = 20
        right.speed.dispense = 20
        right.mix(4,8)
        right.speed.aspirate = 10
        right.speed.dispense = 10        
        right.drop_tip(wastesmalltiprack[well])