import sys

linha = 0
ipt_file = sys.argv[1]
opt_file = sys.argv[2]

output = open(opt_file, "w")


def bin_to_dec(b):
  return int(b, 2)


def dec_to_hex(n):
  result = hex(n)
  result = result[2:]
  if (len(result) < 2):
    return "0" + result
  return result


def endereco_to_hex(str):
  r = ""
  if (str[0] == "0" and str[1] == "b"):
    r = hex(bin_to_dec(str[2:]))[2:]
  elif (str[0] == "0" and str[1] == "x"):
    r = str[2:]
  else:
    r= hex(int(str))[2:]
  if(len(r) < 2):
    r = "0" + r
  return r

dict_inst_4 = {
    "add": "1000",
    "shr": "1001",
    "shl": "1010",
    "not": "1011",
    "and": "1100",
    "or": "1101",
    "xor": "1110",
    "cmp": "1111",
    "ld": "0000",
    "st": "0001"
}

dict_inst_io= {
  "in": "01110",
  "out": "01111",
  "data": "0",
  "addr": "1"
}

dict_inst_6 = {"data": "001000", "jmpr": "001100"}

dict_inst_8 = {
    "jmp": "01000000",
    "clf": "01100000",
    "jc": "01011000",
    "ja": "01010100",
    "je": "01010010",
    "jz": "01010001",
    "jca": "01011100",
    "jce": "01011010",
    "jcz": "01011001",
    "jae": "01010110",
    "jaz": "01010101",
    "jez": "01010011",
    "jcae": "01011110",
    "jcaz": "01011101",
    "jcez": "01011011",
    "jaez": "01010111",
    "jcaez": "01011111",
}

dict_reg = {"r0": "00", "r1": "01", "r2": "10", "r3": "11"}

with open(ipt_file, "r") as input:
  output.write("v3.0 hex words adressed" + "\n")
  acc = 0
  for line in input:
    if (line.strip() != ""):
      inst_bin = ""
      inst_hex = ""
      registrador = ""
      endereco = ""

      lp = line.split(",")
      lista_palavras = []
      for s in lp:
        sv = s.split()
        lista_palavras.extend(sv)
      
      for i in range(len(lista_palavras)):
        lista_palavras[i] = lista_palavras[i].lower()

      print("linha: "+  " ".join(lista_palavras))
      print("instrucao: " + lista_palavras[0])
      
      if (lista_palavras[0] == "data"):
        inst_bin = dict_inst_6["data"] + dict_reg[lista_palavras[1]]
        inst_hex = hex(bin_to_dec(inst_bin))[2:]
        endereco = lista_palavras[2]
        endereco = endereco_to_hex(endereco)
        print("cod: " + dict_inst_6["data"])
        print("reg: " + lista_palavras[1])
        print("cod: " + dict_reg[lista_palavras[1]])
        print("ender: " + endereco)

      elif (lista_palavras[0] == "jmpr"):
        inst_bin = dict_inst_6["jmpr"] + dict_reg[lista_palavras[1]]
        inst_hex = hex(bin_to_dec(inst_bin))[2:]
        print("cod: " + dict_inst_6["jmpr"])
        print("reg " + lista_palavras[1])
        print("cod: " + dict_reg[lista_palavras[1]])

      elif (lista_palavras[0] == "jmp"):
        inst_bin = dict_inst_8["jmp"]
        inst_hex = hex(bin_to_dec(inst_bin))[2:]
        endereco = lista_palavras[1]
        endereco = endereco_to_hex(endereco)
        print("cod: " + dict_inst_8["jmp"])
        print("ender: " + endereco)

      elif (lista_palavras[0] == "clf"):
        inst_bin = dict_inst_8["clf"]
        inst_hex = hex(bin_to_dec(inst_bin))[2:]
        print("cod: " + dict_inst_8["clf"])

      elif (lista_palavras[0] in dict_inst_8):
        inst_bin = dict_inst_8[lista_palavras[0]]
        inst_hex = hex(bin_to_dec(inst_bin))[2:]
        endereco = lista_palavras[1]
        endereco = endereco_to_hex(endereco)
        print("cod: " + dict_inst_8[lista_palavras[0]])
        print("ender: " + endereco)

      elif (lista_palavras[0] in dict_inst_4):
        inst_bin = dict_inst_4[lista_palavras[0]] + dict_reg[lista_palavras[1]] + dict_reg[lista_palavras[2]]
        inst_hex = hex(bin_to_dec(inst_bin))[2:]
        print("cod: " + dict_inst_4[lista_palavras[0]])
        print("regA " + lista_palavras[1])
        print("cod: " + dict_reg[lista_palavras[1]])
        print("regB " + lista_palavras[2])
        print("cod: " + dict_reg[lista_palavras[2]])

      elif(lista_palavras[0] in dict_inst_io): #ver essa questao do endereco, se vai precisar passar para decimal
        inst_bin = dict_inst_io[lista_palavras[0]] + dict_inst_io[lista_palavras[1]] + dict_reg[lista_palavras[2]]
        inst_hex = hex(bin_to_dec(inst_bin))[2:] #7
        print("cod: " + dict_inst_io[lista_palavras[0]] + dict_inst_io[lista_palavras[1]])
        print("regB " + lista_palavras[2])
        print("cod: " + dict_reg[lista_palavras[2]])
        
        
      elif(lista_palavras[0] == "halt"):
        inst_bin = dict_inst_8["jmp"] #falta complentar essa parte ver se tá certinha também em decimal ou hexa
        inst_hex = hex(bin_to_dec(inst_bin))[2:]
        endereco = str(acc).zfill(2)
        print("cod do instrucao: " + dict_inst_8["jmp"])

      elif(lista_palavras[0] == "swap"):
        ra = dict_reg[lista_palavras[1]]
        rb = dict_reg[lista_palavras[2]]
        inst_bin = dict_inst_4["xor"] + ra + rb
        inst_hex = hex(bin_to_dec(inst_bin))[2:]
        output.write(dec_to_hex(acc) + ": " + inst_hex + "\n")
        acc = acc +1
        inst_bin = dict_inst_4["xor"] + rb + ra
        inst_hex = hex(bin_to_dec(inst_bin))[2:]
        output.write(dec_to_hex(acc) + ": " + inst_hex + "\n")
        acc = acc+1
        inst_bin = dict_inst_4["xor"] + ra + rb
        inst_hex = hex(bin_to_dec(inst_bin))[2:]
        
        print("cod: " + dict_inst_4["xor"])
        print("regA " + lista_palavras[1])
        print("cod: " + dict_reg[lista_palavras[1]])
        print("regB " + lista_palavras[2])
        print("cod: " + dict_reg[lista_palavras[2]])
        
        
      if (len(inst_hex) < 2):
        inst_hex = "0" + inst_hex

      lochex = dec_to_hex(acc)
      output.write(lochex + ": " + inst_hex + "\n")
      acc = acc + 1
      

      if (endereco != ""):
        lochex = dec_to_hex(acc)
        output.write(lochex + ": " + endereco + "\n")
        acc = acc + 1

      print("instrucao hex: " + inst_hex)
      print("instrucao bin: " + inst_bin)
      print("\n")