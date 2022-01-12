from opentrons import protocol_api
# metadata
metadata = {'protocolName': 'LoCost Protocol, Part 4 of 4','author': 'JM','description': 'Pooling',
    'apiLevel': '2.10'}
def run(protocol: protocol_api.ProtocolContext):

    # labware and pipettes
    code = protocol.load_labware('nest_96_wellplate_2ml_deep', '6', 'code')
    tube = protocol.load_labware('opentrons_24_aluminumblock_nest_1.5ml_snapcap', '3', 'Run Tube')
    tiprack = protocol.load_labware('opentrons_96_filtertiprack_200ul', '4', '200 tips')
    wastetiprack =protocol.load_labware('opentrons_96_filtertiprack_200ul', '10', 'waste tips')
    left = protocol.load_instrument('p300_multi_gen2', 'left', tip_racks=[tiprack])
    
    # commands
    # pool samples into column 1 of well plate
    
    left.pick_up_tip(tiprack['A1'])
    wells = ['A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', ]
    for well in wells:
        left.aspirate(12, code[well])
    left.dispense(150, code['A1'])
    left.blow_out()
    left.drop_tip(wastetiprack['A1'])

    # transfer samples from column 1 into eppendorf tube
    left.pick_up_tip(tiprack['H2'])
    pools = ['A1','B1','C1','D1','E1','F1','G1','H1']
    for pool in pools:
       left.aspirate(140, code[pool])
       left.dispense(150, tube['A1'])
       left.blow_out()
    left.drop_tip(wastetiprack['H2'])