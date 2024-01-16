import BottleSensors as bs
from threading import Thread
import checkChange as cc
import bottlesSold as bb
import dataSend as ds


def main() -> None:
    """main function."""
    try:
        bs.setup_GPIO()
        print("Sensor setup complete")

        print("press CTRL+C to exit")
        bb.soldPrint()
        t1 = Thread(target=cc.check)
        t2 = Thread(target=bb.main)
        t3 = Thread(target=ds.iothub_messaging)
        t1.start()
        t2.start()
        t3.start()

        
    except KeyboardInterrupt:
        bs.GPIO.cleanup()

main()