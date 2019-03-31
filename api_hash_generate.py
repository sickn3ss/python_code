# I honestly can't even remember if I coded this or if I got it from somewhere else. 
# If this is your code just let me know and I'll credit you and add a link to the original code posting. 

from sys import path
import os, time, sys

def ror( dword, bits ):
  return ( dword >> bits | dword << ( 32 - bits ) ) & 0xFFFFFFFF
 
def unicode( string, uppercase=True ):
  result = "";
  if uppercase:
    string = string.upper()
  for c in string:
    result += c + "\x00"
  return result
 
def hash( module, function, bits=13, print_hash=True ):
  module_hash = 0
  function_hash = 0
  for c in unicode( module + "\x00" ):
    module_hash  = ror( module_hash, bits )
    module_hash += ord( c )
  for c in str( function + "\x00" ):
    function_hash  = ror( function_hash, bits )
    function_hash += ord( c )
  h = module_hash + function_hash & 0xFFFFFFFF
  if print_hash:
    print "[+] 0x%08X = %s!%s" % ( h, module.lower(), function )
  return h

def main( argv=None ):
  if not argv:
    argv = sys.argv
  try:
    if len( argv ) == 1:
      print "Usage: hash.py [<module.dll> <function>]"
    else:
      print "[+] Ran on %s\n" % (  time.asctime( time.localtime() ) )
      hash( argv[1], argv[2] )
  except Exception, e:
    print "[-] ", e

if __name__ == "__main__":
  main()