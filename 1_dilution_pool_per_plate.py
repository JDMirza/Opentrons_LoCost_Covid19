from opentrons import protocol_api
# metadata
metadata = {'protocolName': 'LoCost Protocol, Part 1 of 4','author': 'JM','description': 'Amplicon Dilution',
    'apiLevel': '2.10'}
def run(protocol: protocol_api.ProtocolContext):
    # Run this protocol if Pool 1 and Pool 2 are on separate plates plate
    # labware and pipettes
    dil = protocol.load_labware('usascientific_96_wellplate_2.4ml_deep', '6', 'Dilution')
    pool_1 = protocol.load_labware('nest_96_wellplate_2ml_deep', '5', 'Pool 1')
    pool_2 = protocol.load_labware('nest_96_wellplate_2ml_deep', '9', 'Pool 2')
    trough = protocol.load_labware('agilent_1_reservoir_290ml', '3', 'trough')
    tiprack = protocol.load_labware('opentrons_96_filtertiprack_200ul', '7', '200 tips')
    wastetiprack =protocol.load_labware('opentrons_96_filtertiprack_200ul', '10', '200 waste')
    smalltiprack = protocol.load_labware('opentrons_96_filtertiprack_20ul', '1' , '20 tips')
    wastesmalltiprack = protocol.load_labware('opentrons_96_filtertiprack_20ul', '11', '20 waste')
    left = protocol.load_instrument('p300_multi_gen2', 'left', tip_racks=[tiprack])
    right = protocol.load_instrument('p20_multi_gen2', 'right', tip_racks=[smalltiprack])

    # commands
    # Transfer water from trough to wells without removing tips
    left.pick_up_tip(tiprack['A1'])
    left.distribute(45, trough['A1'], dil.rows()[0], disposal_volume=0, new_tip='never')
    left.drop_tip(wastetiprack['A1'])

    # Transfer DNA amplicons from primer pool 1 and primer pool 2 into dilution plate
    wells = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12']
    for well in wells:
        right.pick_up_tip(smalltiprack[well])
        right.aspirate(2.5, pool_1[well])
        right.dispense(4, dil[well])
        right.aspirate(2.5, pool_2[well])
        right.dispense(4, dil[well])
        right.drop_tip(wastesmalltiprack[well])    
    
    # If running 48 samples delete 'A7'-'A12'