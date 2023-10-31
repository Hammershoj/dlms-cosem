import pprint

from dlms_cosem.cosem import Obis
from dlms_cosem.hdlc import frames
from dlms_cosem.protocol import xdlms
from dlms_cosem.time import datetime_from_bytes
from dlms_cosem.utils import parse_as_dlms_data

# 3-phase
hdlc_data_hex = (
"7ea02a410883130413e6e7000f40000000000101020309060100010700ff0600001d3a02020f00161b16f97e"
)

hdlc_data_hex = "7EA0E22B2113239AE6E7000F000000000C07E6011801123A32FF80000002190A0E4B616D73747275705F563030303109060101000005FF0A103537303635363733323635393034303709060101600101FF0A1236383431313338424E32343531303130393009060101010700FF060000033A09060101020700FF060000000009060101030700FF060000006809060101040700FF06000000B0090601011F0700FF06000000ED09060101330700FF060000005909060101470700FF060000004B09060101200700FF1200E809060101340700FF1200E909060101480700FF1200EC84467E"

ui = frames.UnnumberedInformationFrame.from_bytes(bytes.fromhex(hdlc_data_hex))
dn = xdlms.DataNotification.from_bytes(
    ui.payload[3:]
)  # The first 3 bytes should be ignored.
result = parse_as_dlms_data(dn.body)
# pprint.pprint(result)
# First is date
# date_row = result.pop(0)
# clock_obis = Obis.from_bytes(date_row[0])
# clock, stats = datetime_from_bytes(date_row[1])
# print(f"Clock object: {clock_obis.to_string()}, datetime={clock}")

# rest is data
for item in result:
    try:
        obis = Obis.from_bytes(item)
        print(obis)
    except Exception:
        print(item)

clock, status = datetime_from_bytes(b"5706567326590407")
print(clock)
