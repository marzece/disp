import ctypes
from ctypes import c_uint, c_uint32, c_uint16

TAGSIZE = 8
BUFFER_SIZE = 130000

records = \
{
'MAST_RECORD':    0x4d415354,  # 'MAST'
'RHDR_RECORD':    0x52484452,  # 'RHDR'  (as written to ZDAB file)
'RUN_RECORD' :    0x52554E20,  # 'RUN '  (as dispatched and sent by SHaRC)
'TRIG_RECORD':    0x54524947,  # 'TRIG'
'EPED_RECORD':    0x45504544,  # 'EPED'
'VTHR_RECORD':    0x56544852,  # 'VTHR'
'CAST_RECORD':    0x43415354,  # 'CAST'
'CLST_RECORD':    0x434C5354,  # 'CLST' - obsolete
'CAAC_RECORD':    0x43414143,  # 'CAAC'
'CLAC_RECORD':    0x434C4143,  # 'CLAC' - obsolete
'SOSA_RECORD':    0x534F5341,  # 'SOSA'
'SOSG_RECORD':    0x534F5347,  # 'SOSG'
'SOSL_RECORD':    0x534F534C,  # 'SOSL'
'SOSR_RECORD':    0x534F5352,  # 'SOSR'
'TASK_RECORD':    0x5441534B,  # 'TASK'
'ZDAB_RECORD':    0x5a444142,  # 'ZDAB'  (as written to ZDAB file)
'PMT_RECORD' :    0x504d5420,  # 'PMT '  (as dispatched and sent by SHaRC)
'CRON_RECORD':    0x43524F4E,  # 'CRON'
'VRLY_RECORD':    0x56524C59,  # 'VRLY'
'MSEI_RECORD':    0x4D534549,  # 'MSEI'
}

class GenericRecordHeader(ctypes.BigEndianStructure):
    _fields_ = [('RecordID',      ctypes.c_uint32),
                ('RecordLength',  ctypes.c_uint32),
                ('RecordVersion', ctypes.c_uint32)]

#   Master Trigger Card data 
class MTCReadoutData(ctypes.BigEndianStructure):
    _fields_ = [ #   word 0 
                ('Bc10_1',            c_uint32,  32),
                #   word 1 
                ('Bc50_1',            c_uint32,  11),
                ('Bc10_2',            c_uint32,  21),
                #   word 2 
                ('Bc50_2',            c_uint32,  32),
                #   word 3 
                ('Owln',              c_uint,    1), #   MSB 
                ('ESum_Hi',           c_uint,    1),
                ('ESum_Lo',           c_uint,    1),
                ('Nhit_20_LB',        c_uint,    1),
                ('Nhit_20',           c_uint,    1),
                ('Nhit_100_Hi',       c_uint,    1),
                ('Nhit_100_Med',      c_uint,    1),
                ('Nhit_100_Lo',       c_uint,    1),
                ('BcGT',              c_uint32,  24), #   LSB 
                #   word 4 
                ('Diff_1',            c_uint,    3),
                ('Peak',              c_uint,    10),
                ('Miss_Trig',         c_uint,    1),
                ('Soft_GT',           c_uint,    1),
                ('NCD_Mux',           c_uint,    1),
                ('Special_Raw',       c_uint,    1),
                ('Ext_8',             c_uint,    1),
                ('NCD_Shaper',        c_uint,    1),
                ('Ext_6',             c_uint,    1),
                ('Ext_5',             c_uint,    1),
                ('Ext_4',             c_uint,    1),
                ('Ext_3',             c_uint,    1),
                ('Hydrophone',        c_uint,    1),
                ('Ext_Async',         c_uint,    1),
                ('Sync',              c_uint,    1),
                ('Pong',              c_uint,    1),
                ('Pedestal',          c_uint,    1),
                ('Prescale',          c_uint,    1),
                ('Pulse_GT',          c_uint,    1),
                ('Owle_Hi',           c_uint,    1),
                ('Owle_Lo',           c_uint,    1),
                #  word 5 
                ('Unused3',           c_uint,    1),
                ('Unused2',           c_uint,    1),
                ('Unused1',           c_uint,    1),
                ('FIFOsAllFull',      c_uint,    1),
                ('FIFOsNotAllFull',   c_uint,    1),
                ('FIFOsNotAllEmpty',  c_uint,    1),
                ('SynClr24_wo_TC24',  c_uint,    1),
                ('SynClr24',          c_uint,    1),
                ('SynClr16_wo_TC16',  c_uint,    1),
                ('SynClr16',          c_uint,    1),
                ('TestMem2',          c_uint,    1),
                ('TestMem1',          c_uint,    1),
                ('Test10',            c_uint,    1),
                ('Test50',            c_uint,    1),
                ('TestGT',            c_uint,    1),
                ('Int',               c_uint,    10),
                ('Diff_2',            c_uint,    7)]

class PmtEventRecord(ctypes.BigEndianStructure):
    _fields_ = [('PmtEventRecord',  c_uint16),
                ('DataType',        c_uint16),
                ('RunNumber',       c_uint32),
                ('EvNumber',        c_uint32),
                ('DaqStatus',       c_uint16),
                ('NPmtHit',         c_uint16),
                ('CalPckType',      c_uint32), # used to store sub-run number
                ('TriggerCardData', MTCReadoutData)]

