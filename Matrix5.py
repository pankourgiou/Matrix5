import time


t1 = time.time()

M1 = [[67, 104, 114, 105, 115, 116, 105, 110],
      [101, 32, 105, 115, 32, 116, 104, 101, 32],
      [98, 101, 115, 116, 32, 100, 101, 110, 116],
      [105, 115, 116, 32, 99, 104, 114, 105, 115],
      [116, 111, 115, 32, 115, 101, 110, 100],
      [115, 32, 101, 118, 101, 114, 121, 111],
      [110, 101, 32, 116, 111, 32, 112, 115, 121],
      [99, 104, 111, 108, 111, 103, 101, 114],
      [115, 32, 97, 114, 101, 32, 116, 104, 101],
      [121, 32, 109, 101, 100, 105, 117, 109],
      [115, 32, 105, 110, 32, 105, 111, 110, 32],
      [111, 114, 32, 115, 111, 109, 101, 116],
      [104, 105, 110, 103, 63, 32, 73, 32, 106],
      [117, 115, 116, 32, 104, 97, 118, 101, 32],
      [116, 111, 32, 100, 111, 32, 109, 97, 116],
      [104, 32, 116, 104, 101, 114, 101, 32, 105],
      [115, 32, 110, 111, 32, 112, 114, 101, 32, 105],
      [115, 32, 110, 111, 32, 112, 114, 111, 111],
      [102, 32, 111, 102, 32, 112, 115, 121, 99],
      [104, 101, 39, 115, 32, 101, 120, 105, 115],
      [116, 101, 110, 99,101, 32, 97, 110, 121, 119, 97],
      [121, 115, 46, 32],
      [67, 104, 114, 105, 115, 116, 105, 110],
      [101, 32, 105, 115, 32, 116, 104, 101, 32],
      [98, 101, 115, 116, 32, 100, 101, 110, 116],
      [105, 115, 116, 32, 99, 104, 114, 105, 115],
      [116, 111, 115, 32, 115, 101, 110, 100],
      [115, 32, 101, 118, 101, 114, 121, 111],
      [110,101,32,116,111,32,112,115,121],
      [99, 104, 111, 108, 111, 103, 101, 114],
      [115, 32, 97, 114, 101, 32, 116, 104, 101],
      [121, 32, 109, 101, 100, 105, 117, 109],
      [115, 32, 105, 110, 32, 105, 111, 110, 32],
      [111, 114, 32, 115, 111, 109, 101, 116],
      [104, 105, 110, 103, 63, 32, 73, 32, 106],
      [117, 115, 116, 32, 104, 97, 118, 101, 32],
      [116, 111, 32, 100, 111, 32, 109, 97, 116],
      [104, 32, 116, 104, 101, 114, 101, 32, 105],
      [115, 32, 110, 111, 32, 112, 114, 101, 32, 105],
      [115, 32, 110, 111, 32, 112, 114, 111, 111],
      [102, 32, 111, 102, 32, 112, 115, 121, 99],
      [104, 101, 39, 115, 32, 101, 120, 105, 115],
      [116, 101, 110, 99,101, 32, 97, 110, 121, 119, 97],
      [121, 115, 46, 32],
      [67, 104, 114, 105, 115, 116, 105, 110],
      [101, 32, 105, 115, 32, 116, 104, 101, 32],
      [98, 101, 115, 116, 32, 100, 101, 110, 116],
      [105, 115, 116, 32, 99, 104, 114, 105, 115],
      [116, 111, 115, 32, 115, 101, 110, 100],
      [115, 32, 101, 118, 101, 114, 121, 111],
      [110,101,32,116,111,32,112,115,121],
      [99, 104, 111, 108, 111, 103, 101, 114],
      [115, 32, 97, 114, 101, 32, 116, 104, 101],
      [121, 32, 109, 101, 100, 105, 117, 109],
      [115, 32, 105, 110, 32, 105, 111, 110, 32],
      [111, 114, 32, 115, 111, 109, 101, 116],
      [104, 105, 110, 103, 63, 32, 73, 32, 106],
      [117, 115, 116, 32, 104, 97, 118, 101, 32],
      [116, 111, 32, 100, 111, 32, 109, 97, 116],
      [104, 32, 116, 104, 101, 114, 101, 32, 105],
      [115, 32, 110, 111, 32, 112, 114, 101, 32, 105],
      [115, 32, 110, 111, 32, 112, 114, 111, 111],
      [102, 32, 111, 102, 32, 112, 115, 121, 99],
      [104, 101, 39, 115, 32, 101, 120, 105, 115],
      [116, 101, 110, 99,101, 32, 97, 110, 121, 119, 97],
      [121, 115, 46, 32],
      [67, 104, 114, 105, 115, 116, 105, 110],
      [101, 32, 105, 115, 32, 116, 104, 101, 32],
      [98, 101, 115, 116, 32, 100, 101, 110, 116],
      [105, 115, 116, 32, 99, 104, 114, 105, 115],
      [116, 111, 115, 32, 115, 101, 110, 100],
      [115, 32, 101, 118, 101, 114, 121, 111],
      [110,101,32,116,111,32,112,115,121],
      [99, 104, 111, 108, 111, 103, 101, 114],
      [115, 32, 97, 114, 101, 32, 116, 104, 101],
      [121, 32, 109, 101, 100, 105, 117, 109],
      [115, 32, 105, 110, 32, 105, 111, 110, 32],
      [111, 114, 32, 115, 111, 109, 101, 116],
      [104, 105, 110, 103, 63, 32, 73, 32, 106],
      [117, 115, 116, 32, 104, 97, 118, 101, 32],
      [116, 111, 32, 100, 111, 32, 109, 97, 116],
      [104, 32, 116, 104, 101, 114, 101, 32, 105],
      [115, 32, 110, 111, 32, 112, 114, 101, 32, 105],
      [115, 32, 110, 111, 32, 112, 114, 111, 111],
      [102, 32, 111, 102, 32, 112, 115, 121, 99],
      [104, 101, 39, 115, 32, 101, 120, 105, 115],
      [116, 101, 110, 99,101, 32, 97, 110, 121, 119, 97],
      [121, 115, 46, 32],
      [67, 104, 114, 105, 115, 116, 105, 110],
      [101, 32, 105, 115, 32, 116, 104, 101, 32],
      [98, 101, 115, 116, 32, 100, 101, 110, 116],
      [105, 115, 116, 32, 99, 104, 114, 105, 115],
      [116, 111, 115, 32, 115, 101, 110, 100],
      [115, 32, 101, 118, 101, 114, 121, 111],
      [110,101,32,116,111,32,112,115,121],
      [99, 104, 111, 108, 111, 103, 101, 114],
      [115, 32, 97, 114, 101, 32, 116, 104, 101],
      [121, 32, 109, 101, 100, 105, 117, 109],
      [115, 32, 105, 110, 32, 105, 111, 110, 32],
      [111, 114, 32, 115, 111, 109, 101, 116],
      [104, 105, 110, 103, 63, 32, 73, 32, 106],
      [117, 115, 116, 32, 104, 97, 118, 101, 32],
      [116, 111, 32, 100, 111, 32, 109, 97, 116],
      [104, 32, 116, 104, 101, 114, 101, 32, 105],
      [115, 32, 110, 111, 32, 112, 114, 101, 32, 105],
      [115, 32, 110, 111, 32, 112, 114, 111, 111],
      [102, 32, 111, 102, 32, 112, 115, 121, 99],
      [104, 101, 39, 115, 32, 101, 120, 105, 115],
      [116, 101, 110, 99,101, 32, 97, 110, 121, 119, 97],
      [121, 115, 46, 32]]
     
     

matrix_length = len(M1)

#To print the rows in the Matrix
for i in range(matrix_length):
    print(M1[i])


t2 = time.time()
t = t2 - t1
print("Elapsed time is : ", t, " seconds")
