class LiftController:
    def __init__(self):
        self.lift_called = [[False,False] for _ in range(5)]
    def supervisor_call(self,floor):
        for i_floor in range(len(self.lift_called)):
            for i_direction in range(len(self.lift_called[i_floor])):
                if i_floor == floor:
                    self.lift_called[i_floor][i_direction] = True
                else:
                    self.lift_called[i_floor][i_direction] = False
    