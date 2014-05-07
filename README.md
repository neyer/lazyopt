# lazyopt

  `pip install lazyopt`

## the lazy coder's option parser

  most python scripts accumuluate a bunch of constants. eventually you might like to be able to set values for some of those constants with the command line. you could spend FOREVER writing an argument parser with [argparse](http://docs.python.org/2.7/library/argparse.html) like this:

    # main.py
    import argparse

    IT_WAS_A_CONST = 5
    BUT_NOW_I_WANNA_CHANGE_IT = "damn"
    UGH_I_HATE_THIS = True

    def main():

      parser = argparse.ArgumentParser(description="some stupid script")
      parser.add_argument("--it-was-a-const", default=5,
                         dest='was_const')
      parser.add_argument("--but-now-i-wanna-change-it", default="damn",
                          dest='now_change')
      parser.add_argument("--ugh-i-hate-this", default=True,
                          dest='hate')

      args = parser.parse_args()
      IT_WAS_A_CONST = args.was_const
      BUT_NOW_I_WANNA_CHANGE_IT = args.now_change
      UGH_I_HATE_THIS = args.hate

      # FINALLY 
      do_what_you_came_for() 

    if __name__ == "__main__" : main() 

just so you can run

    python main.py --but-now-i-wanna-change-it 22    


with `lazyopt`, you can just do this!

    # main.py
    import lazyopt

    IT_WAS_A_CONST = 5
    BUT_NOW_I_WANNA_CHANGE_IT = "damn"
    UGH_I_HATE_THIS = True

    def main():

      lazyopt.apply_all() 
      do_what_you_came_for()

    if __name__ == "__main__" : main()

and you can still run

    python  main.py --but-now-i-wanna-change-it 22


## how

`lazyopt` will parse any command in arguments like this:

    --module_name.sub_module.var-name value-here

and apply `value-here` to the variable `var_name` in the module `module_name.sub-module`. if no such variable exists, you'll get a nice `ConfigurationError` to let you know.  note that `lazyopt` converts dashes to underscores for you. if it can't find a name, lazyopt will try to capitalize it for you. 

if you do not specify `module_name` , `lazyopt` will '`value-here` to `var_name` in the module you use to call `apply_all`. most of the time this will be the main script you execute.

argument values are typecast where appropriate: "False", "True" , and "None" take on their keyword cousins. numbers are integers unless a decimal is present; everything else is a string.

if you pass arguments without values, like so:

  --a-flag  --another-flag

those argument names will be assigned the value 'True'

note that `lazyopt` does not currently provide documentation or enforce any rules. it's lazy like that.

## warning

`lazyopt` is best for adding command line configuration to constants in a single script. it can work in more complicated situations, but you'll want to call `lazyopt.apply_all` in the python file you execute from the command line.


## future plans
* add option to create actual arg parser
* use comments as docs, default values for type checking
* keep on keepin' on


## why?

laziness

## who?

mark neyer, gentleman coder

bsd
