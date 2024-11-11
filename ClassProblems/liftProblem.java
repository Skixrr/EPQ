public class LiftController {
    private boolean[][] liftCalled;

    public LiftController() {
        liftCalled = new boolean[5][2];
        for (int i = 0; i < 5; i++) {
            liftCalled[i][0] = false;
            liftCalled[i][1] = false;
        }
    }

    public void supervisorCall(int floor) {
        for (int iFloor = 0; iFloor < liftCalled.length; iFloor++) {
            for (int iDirection = 0; iDirection < liftCalled[iFloor].length; iDirection++) {
                if (iFloor == floor) {
                    liftCalled[iFloor][iDirection] = true;
                } else {
                    liftCalled[iFloor][iDirection] = false;
                }
            }
        }
    }
}
