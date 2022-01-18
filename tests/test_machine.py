import unittest

class MachineTest(unittest.TestCase):
    def test_agent_can_refull_A(self):
        racks = [Rack("A", "biscuit au choco",100)]
        machine = Machine(racks)
        
        #Machine refilled with 10 biscuits "A"
        machine.refill("A",10)
        
        self.asssertEqual(machine.racks["A"].quantity,10)