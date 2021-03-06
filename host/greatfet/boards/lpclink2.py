#
# This file is part of GreatFET
#

from ..board import GreatFETBoard
from ..interfaces.gpio import GPIO
from ..interfaces.i2c_bus import I2CBus
from ..interfaces.spi_bus import SPIBus
from ..interfaces.jtag import JTAGChain
from ..programmers.firmware import DeviceFirmwareManager
from ..interfaces.pattern_generator import PatternGenerator
from ..interfaces.sdir import SDIRTransceiver
from ..interfaces.uart import UART
from ..programmers.spi_flash import SPIFlash

class LPClink2(GreatFETBoard):
    """ Class representing the GreatFET varian of the NXP Xplorer base-boards. """

    # Currently, all GreatFET One boards have an ID of zero.
    HANDLED_BOARD_IDS = [3]
    BOARD_NAME = "lpclink2"
#    size_in_bytes = "1048576"
    SUPPORTED_LEDS = 1

#    def __init__(self, **devicidentifiers):
#        """ Initialize a new LPClink2 connection. """

#        super(LPClink2, self).__init__(**device_identifiers)

#        self.onboard_flash = SPIFlash(self, page_size=256, pages=4096, maximum_address=0x100000)

    GPIO_MAPPINGS = {
        #"J1_P1"   : GND,
        #"J2_P2"   : VCC,
        "J1_P3"    : (5, 13),
        "J1_P4"    : (0, 0),
        "J1_P5"    : (5, 14),
        "J1_P6"    : (0, 1),
        "J1_P7"    : (0, 4),
        "J1_P8"    : (2, 9),
        "J1_P9"    : (2, 10),
        "J1_P10"   : (0, 8),
        #"J2_P11"  : CLK0,
        "J1_P12"   : (0, 9),
        "J1_P13"   : (1, 8),
        "J1_P14"   : (2, 11),
        "J1_P15"   : (1, 0),
        "J1_P16"   : (1, 9),
        "J1_P17"   : (1, 2),
        "J1_P18"   : (1, 1),
        "J1_P19"   : (2, 12),
        "J1_P20"   : (1, 3),
        "J1_P21"   : (1, 5),
        "J1_P22"   : (1, 4),
        "J1_P23"   : (2, 14),
        "J1_P24"   : (2, 13),
        "J1_P25"   : (1, 7),
        "J1_P26"   : (1, 6),
        "J1_P27"   : (2, 15),
        "J1_P28"   : (0, 2),
        "J1_P29"   : (2, 7),
        "J1_P30"   : (0, 3),
        "J1_P31"   : (0, 13),
        "J1_P32"   : (0, 12),
        "J1_P33"   : (5, 18),
        "J1_P34"   : (4, 11),
        "J1_P35"   : (5, 0),
        # P36"     : P6_0,
        "J1_P37"   : (0, 15),
        # P38"     : P1_19,
        "J1_P39"   : (0, 11),
        #"J1_P40"   : (0, 10),
        # J2_P1"   : GND,
        # J2_P2"   : VBUS,
        "J2_P3"    : (5, 12),
        "J2_P4"    : (2, 0),
        #"J2_P5"   : ADC0_0,
        "J2_P6"    : (2, 5),
        "J2_P7"    : (2, 4),
        "J2_P8"    : (2, 2),
        "J2_P9"    : (2, 3),
        "J2_P10"   : (2, 6),
        #"J2_P11"  : P4_7,
        #"J2_P12"  : CLK2,
        "J2_P13"   : (5, 7),
        "J2_P14"   : (0, 7),
        "J2_P15"   : (5, 6),
        "J2_P16"   : (3, 15),
        #"J2_P17"  : WAKEUP0,
        "J2_P18"   : (5, 5),
        "J2_P19"   : (5, 4),
        "J2_P20"   : (5, 3),
        #"J2_P21" : PF_4,
        "J2_P22"   : (5, 9),
        "J2_P23"   : (3, 10),
        "J2_P24"   : (5, 8),
        "J2_P25"   : (3, 9),
        #"J2_P26" : P3_0,
        "J2_P27"   : (3, 8),
        #"J2_P28"   : (1, 14),
        "J2_P29"   : (5, 16),
        "J2_P30"   : (5, 10),
        "J2_P31"   : (5, 15),
        #"J2_P32" : P3_3,
        "J2_P33"   : (5, 2),
        "J2_P34"   : (0, 5),
        "J2_P35"   : (5, 1),
        "J2_P36"   : (3, 2),
        #"J2_P37"   : (1, 15),
        #"J2_P38"   : (0, 6),
        #"J2_P39"  : I2C0_SDA,
        #"J2_P40"  : I2C0_SDL,
        #"J7_P1"  : GND,
        "J7_P2"    : (3, 3),
        "J7_P3"    : (3, 4),
        #"J7_P4"   : ADC0_5,
        #"J7_P5"   : ADC0_2,
        "J7_P6"    : (1, 10),
        "J7_P7"    : (1, 12),
        "J7_P8"    : (1, 13),
        #"J7_P9"   : RTC_ALARM,
        #"J7_P10"  : GND,
        #"J7_P11"  : RESET,
        #"J7_P12"  : VBAT,
        "J7_P13"   : (1, 11),
        "J7_P14"   : (0, 14),
        "J7_P15"   : (3, 6),
        "J7_P16"   : (3, 5),
        "J7_P17"   : (3, 1),
        "J7_P18"   : (3, 0),
        #"J7_P19"  : GND,
        #"J7_P20"  : VCC,
    }

    # All of the ADC mappings accessible from the GreatFET headers.
    ADC_MAPPINGS = {
        "J2_P5"  : [(0, 0), (1, 0)],
        "J2_P9"  : [(0, 0), None],
        "J2_P16" : [None, (1, 6)],
        "J7_P4"  : [(0, 5), (1, 5)],
        "J7_P5"  : [(0, 2), (1, 2)],
    }
    # All UART mappings on GreatFET One
    # name, scu port and pin, scu function number
    UART_MAPPINGS = [
    {
        "J1_P33"    : ((9, 5), 7),      # TX
        "J1_P34"    : ((9, 6), 7),      # RX
        "J1_P35"    : ((2, 0), 1),      # TX
        "J2_P35"    : ((2, 1), 1),      # RX
        "J7_P2"     : ((6, 4), 2),      # TX
        "J7_P3"     : ((6, 5), 2)       # RX
    },
    {
        "J1_P25"    : ((1, 14), 1),     # RX
        "J1_P26"    : ((1, 13), 1),     # TX
        "J1_P27"    : ((5, 6), 4),      # TX
        "J2_P28"    : ((3, 4), 4),      # TX
        "J2_P37"    : ((3, 5), 4),      # RX
    },
    {
        "J1_P28"    : ((1, 15), 1),     # TX
        "J1_P30"    : ((1, 16), 1),     # RX
        "J2_P23"    : ((7, 2), 6),      # RX
        "J2_P25"    : ((7, 1), 6)       # TX
    },
    {
        "J2_P8"     : ((4, 2), 6),      # RX
        "J2_P19"    : ((2, 4), 2),      # RX
        "J2_P20"    : ((2, 3), 2)       # TX
    }]


    def initialize_apis(self):
        """ Initialize a new LPClink2 connection. """

        # Set up the core connection.
        super(LPClink2, self).initialize_apis()

        # Create our simple peripherals.
        self._populate_simple_interfaces()

#        self.apis = LegacyAPICollection(self)

        # Create an adapter that behaves like a CommsBackend, so most tools can work with
        # this object propertly.
#        apis_dict = {'firmware': self.apis.firmware}
#        self.comms = type('LegacyCommsAdapter', (), {'apis': apis_dict})()

        # Finally, add a DeviceFirmwareManager object to the given device.
        # This doesn't need anything special, as our LegacyAPICollection presents a
        # fully-API-compatible firmware API.
#        if self.supports_api('firmware'):
#        	self._populate_firmware()
#            self.onboard_flash = DeviceFirmwareManager(self)
#            self.onboard_flash = SPIFlash(self, page_size=256, pages=4096,  maximum_address=1048576)

#    def supports_api(self, class_name):
#        """ Returns true iff the board supports the given API class. """
#        return class_name == "firmware"

        # Initialize the fixed peripherals that come on the board.
        # Populate the per-board GPIO.
        if self.supports_api("gpio"):
            self._populate_gpio()

        if self.supports_api("adc"):
            self._populate_adc()

        if self.supports_api('i2c'):
            self._add_interface('i2c_busses', [ I2CBus(self, 'I2C0') ])
            self._add_interface('i2c', self.i2c_busses[0])

        if self.supports_api('spi') and self.supports_api('gpio'):
            chip_select = self.gpio.get_pin('J1_P37')
            self._add_interface('spi_busses', [ SPIBus(self, chip_select, 'SPI1') ])
            self._add_interface('spi', self.spi_busses[0])

        if self.supports_api('uart'):
            self._add_interface('uart', UART(self))

        if self.supports_api("jtag"):
            try:
                self._add_interface('jtag', JTAGChain(self))
            except:
                pass

        if self.supports_api('sdir'):
            self._add_interface('sdir', SDIRTransceiver(self))

        # As a convenience, if GREATFET_USE_LOWLEVEL is set in the environment,
        # automatically set it up.
        try:
            if os.getenv('GREATFET_USE_LOWLEVEL'):
                self.enable_low_level_access()
        except:
            pass


       # self.onboard_flash = SPIFlash(self, device_id=0x15, pages=16384, maximum_address=0x3FFFFF)
        # Add objects for each of our LEDs.
        self._populate_leds(self.SUPPORTED_LEDS)


