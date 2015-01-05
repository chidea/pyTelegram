from enum import Enum
class MtpCoreEnum(Enum):
  # core types
  mtpc_int = 0xa8509bda
  mtpc_long = 0x22076cba
  mtpc_int128 = 0x4bb5362b
  mtpc_int256 = 0x929c32f
  mtpc_double = 0x2210c154
  mtpc_string = 0xb5286e24

  mtpc_boolTrue = 0x997275b5
  mtpc_boolFalse = 0xbc799737
  mtpc_vector = 0x1cb5c415
  mtpc_error = 0xc4b9f9bb
  mtpc_null = 0x56730bcc

  # layers
  mtpc_invokeWithLayer1 = 0x53835315
  mtpc_invokeWithLayer2 = 0x289dd1f6
  mtpc_invokeWithLayer3 = 0xb7475268
  mtpc_invokeWithLayer4 = 0xdea0d430
  mtpc_invokeWithLayer5 = 0x417a57ae
  mtpc_invokeWithLayer6 = 0x3a64d54d
  mtpc_invokeWithLayer7 = 0xa5be56d3
  mtpc_invokeWithLayer8 = 0xe9abd9fd
  mtpc_invokeWithLayer9 = 0x76715a63
  mtpc_invokeWithLayer10 = 0x39620c41
  mtpc_invokeWithLayer11 = 0xa6b88fdf
  mtpc_invokeWithLayer12 = 0xdda60d3c
  mtpc_invokeWithLayer13 = 0x427c8ea2
  mtpc_invokeWithLayer14 = 0x2b9b08fa
  mtpc_invokeWithLayer15 = 0xb4418b64
  mtpc_invokeWithLayer16 = 0xcf5f0987
  mtpc_invokeWithLayer17 = 0x50858a19
  mtpc_invokeWithLayer18 = 0x1c900537

  mtpc_invokeWithLayer   = 0xda9b0d0d # after 18 layer

  # manually parsed
  mtpc_rpc_result = 0xf35c6d01
  mtpc_msg_container = 0x73f1f8dc
  #	mtpc_msg_copy = 0xe06046b2
  mtpc_gzip_packed = 0x3072cfa1

class MtpLayerEnum(Enum):


class MptData():
  v = None
  cnt = 1
  def __init__(self):
    pass
  def incr(self):
    self.cnt+=1
    return self
  def decr(self):
    self.cnt-=1
    return self.cnt == 0
  def needSplit(self):
    return self.cnt > 1
  def clone(self):
    pass
class MtpDataOwner():
  data = None
  def __init__(self, data=None):
    if type(data) is MtpDataOwner:
      self.data = data.data.incr()
    else:
      self.data = data
  def split(self):
    if self.data and self.data.needSplit():
      self.data = self.data.clone()