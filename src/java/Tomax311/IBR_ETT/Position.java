package Tomax311.IBR_ETT;

public class Position {

    //checkpoint detctor for minecraft on the y axis
    static boolean CPTrackerY (int CPx,int CPy1,int CPy2,int POSx1,int POSy1,int POSx2,int POSy2) {
        int r = (CPx - POSx1) / (POSx2 - POSx1);
        int post = (POSy2 - POSy1) * r + POSy1;

        if (CPy1 <= post && CPy2 >=post) {
            return true;
        }
		else{
            return false;
        }
    }

    //checkpoint detctor for minecraft on the x axis
    static boolean CPTrackerX (int CPy,int CPx1,int CPx2,int POSx1,int POSy1,int POSx2,int POSy2) {
        int r = (CPy - POSy1) / (POSy2 - POSy1);
        int post = (POSx2 - POSx1) * r + POSx1;

        if (CPx1 <= post && CPx2 >=post) {
            return true;
        }
		else{
        return false;
		}
    }

    //This function is to choose witch way the checpoint is (use "X"/"Y")
    //CP variable example CP = [the lonely coord,the first coord,the second coord]
    static boolean CP(direction,CP,PlayerPos1,PlayerPos2):

    POSx1 = int(PlayerPos1[1])
    POSy1 = int(PlayerPos1[2])
    POSx2 = int(PlayerPos2[1])
    POSy2 = int(PlayerPos2[2])

	if direction == "X" :

    CPy = CP[0]
    CPx1 = CP[1]
    CPx2 = CP[2]

            return CPTrackerX(CPy, CPx1, CPx2, POSx1, POSy1, POSx2, POSy2)

	else:
    CPx = CP[0]
    CPy1 = CP[1]
    CPy2 = CP[2]

            return CPTrackerY(CPx, CPy1, CPy2, POSx1, POSy1, POSx2, POSy2)

}
