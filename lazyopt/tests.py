import lazyopt
import unittest


class LazyoptTest(unittest.TestCase):

  def test_cast_value(self):
    "Ensure that string values are cast to the appropriate types."

    test_pairs = {
        "foo" : "foo",
        "1" : 1,
         "0" : 0,
        "1.5" : 1.5,
        "0.0.1" : "0.0.1",
        "False" : False,
        "None" :  None,
        "True" : True
    }

    for k, v in test_pairs.items():
      self.assertEqual(lazyopt.cast_value_str(k),v)

  def test_get_argv_bindings(self):
    "Test that argv strings are properly parsed."
    args = ["--bool-flag", 
            "--foo-int", "5",
            "--bar-float", "4.5",
            "ignore-me",
            "ignore-me-too",
            "--baz-str", "b.b.b",
            "--non-str", "None",
            "--is-false", "False",
            "--end-flag"]


    bindings = lazyopt.get_argv_bindings(args)

    self.assertEqual(bindings["bool-flag"], True)
    self.assertEqual(bindings["foo-int"], 5)
    self.assertEqual(bindings["bar-float"], 4.5)
    self.assertEqual(bindings["baz-str"], "b.b.b")
    self.assertEqual(bindings["non-str"], None)
    self.assertEqual(bindings["is-false"], False)
    self.assertEqual(bindings["end-flag"], True)

    # now try a duplicate config
    args = [ "--double-flag", "--double-flag" ]

    with self.assertRaises(lazyopt.ConfigurationError):
      lazyopt.get_argv_bindings(args)


  def test_get_module_and_var_name(self):

    tests = [
      ["foo.bar", "foo", "bar"],
      ["foo.bar.baz", "foo.bar", "baz"],
      ["foo.bar-baz.bat", "foo.bar_baz", "bat"],
      ["foo-bar.baz-bat", "foo_bar", "baz_bat"],
    ]
    for pair in tests:
        res = lazyopt.get_module_and_var_name(pair[0])
        self.assertEqual(res[0], pair[1])
        self.assertEqual(res[1], pair[2])


  def test_apply_binding(self):
    "Make sure bindings can be applied to a module"

    lazyopt.apply_binding("lazyopt.fake_module","VAL_IS_2", 3)
    lazyopt.apply_binding("lazyopt.fake_module","VAL_IS_FOO", "bar")

    self.assertEqual(lazyopt.fake_module.VAL_IS_2, 3)
    self.assertEqual(lazyopt.fake_module.VAL_IS_FOO, "bar")


    with self.assertRaises(lazyopt.ConfigurationError):
      lazyopt.apply_binding("lazyopt.fake_module","PANTS_MAN", "totenhosen")

  def test_get_caller_module(self):

    
    def spurious_function():
      return lazyopt.get_caller_module().__name__
    
    module_name = spurious_function()
    self.assertEqual(module_name, 'lazyopt.tests')





