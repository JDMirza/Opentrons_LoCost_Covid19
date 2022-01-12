from opentrons import protocol_api

# metadata
metadata = {'protocolName': 'LoCost Protocol, Part 3 of 4','author': 'JM','description': 'Barcoding Protocol',
    'apiLevel': '2.10'}

def run(protocol: protocol_api.ProtocolContext):

    # labware
    nativebarcodes = protocol.load_labware('nest_96_wellplate_2ml_deep', '2', 'Coding Kit')
    barcoding = protocol.load_labware('nest_96_wellplate_2ml_deep', '6', 'Barcode Plate')
    endrepair = protocol.load_labware('corning_96_wellplate_360ul_flat', '5', 'End Repair Plate')
    tube = protocol.load_labware('opentrons_24_aluminumblock_nest_1.5ml_snapcap', '3', 'Run Tube')
    smalltiprack = protocol.load_labware('opentrons_96_filtertiprack_20ul', '1', '20 tips')
    wastesmalltiprack = protocol.load_labware('opentrons_96_filtertiprack_20ul', '11', '20 waste')
    tiprack = protocol.load_labware('opentrons_96_filtertiprack_200ul', '7', '200 tips')
    wastetiprack =protocol.load_labware('opentrons_96_filtertiprack_200ul', '10', '200 waste')
    
    # pipettes
    left = protocol.load_instrument('p300_multi_gen2', 'left', tip_racks=[tiprack])
    right = protocol.load_instrument('p20_multi_gen2', 'right', tip_racks=[smalltiprack])

    # commands
    # transfer ligase master mix to well plate
    left.pick_up_tip(tiprack['H1'])
    wells = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1' , 'G1' , 'H1']
    for well in wells:
        left.aspirate(105, tube['A1'])
        left.dispense(105, barcoding[well])
    left.drop_tip(tiprack['H1'])

    left.pick_up_tip(tiprack['A1'])
    left.aspirate(5, barcoding['A1'])
    left.distribute(8, barcoding['A1'], barcoding.columns()[1:12], disposal_volume=0, new_tip='never')
    left.drop_tip(wastetiprack['A1'])
    
    # transfer barcode aliquots to well plate
    wells = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12']

    for well in wells:
        right.pick_up_tip(smalltiprack[well])
        right.aspirate(1.5, nativebarcodes[well])
        right.dispense(3, barcoding[well])
        right.drop_tip(wastesmalltiprack[well])

    protocol.pause("Change the tip boxes on 1 and 11 for new ones")

    # transfer endrepair aliquot into well plate
    for well in wells:
        right.pick_up_tip(smalltiprack[well])
        right.aspirate(1, endrepair[well])
        right.dispense(1.5, barcoding[well])
        right.speed.aspirate = 20
        right.speed.dispense = 20
        right.mix(4,8)
        right.speed.aspirate = 5
        right.speed.dispense = 5        
        right.drop_tip(wastesmalltiprack[well])