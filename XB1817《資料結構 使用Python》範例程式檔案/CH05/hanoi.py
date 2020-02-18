def hanoi(num, start = 'A柱', relay = 'B柱', target = 'C柱'):
   if num > 0:
      hanoi(num - 1, start, target, relay)
      print('移動圓盤{:}，從 {:} --> {:} '.format(
            num, start, target))
      hanoi(num - 1, relay, start, target)

print(hanoi(4))
