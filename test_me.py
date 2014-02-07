import lazyopt
import lazyopt.fake_module
import test_me


ANOTHER_CONST = "boring-default"
A_GUY = False

def main():
  "Print out values for all the constants. Just for testing."

  lazyopt.apply_all()

  print "lazyopt.fake_module.VAL_IS_2", lazyopt.fake_module.VAL_IS_2
  print "lazyopt.fake_module.VAL_IS_FOO", lazyopt.fake_module.VAL_IS_FOO
  print "test_me.ANOTHER_CONST", test_me.ANOTHER_CONST
  print "test_me.A_GUY", test_me.A_GUY

if __name__ == "__main__" : main()
