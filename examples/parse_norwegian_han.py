from dlms_cosem.cosem import Obis
from dlms_cosem.hdlc import frames
from dlms_cosem.protocol import xdlms
from dlms_cosem.time import datetime_from_bytes
from dlms_cosem.utils import parse_as_dlms_data

# 3-phase
hdlc_data_hex = (
"7ea02a410883130413e6e7000f40000000000101020309060100010700ff0600001d3a02020f00161b16f97e"
)

ui = frames.UnnumberedInformationFrame.from_bytes(bytes.fromhex(hdlc_data_hex))
dn = xdlms.DataNotification.from_bytes(
    ui.payload[3:]
)  # The first 3 bytes should be ignored.
result = parse_as_dlms_data(dn.body)

# First is date
date_row = result.pop(0)
clock_obis = Obis.from_bytes(date_row[0])
clock, stats = datetime_from_bytes(date_row[1])
print(f"Clock object: {clock_obis.to_string()}, datetime={clock}")

# rest is data
for item in result:
    obis = Obis.from_bytes(item[0])
    value = item[1]
    print(f"{obis.to_string()}={value}")
