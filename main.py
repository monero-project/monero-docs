def define_env(env):
    """
    This is the hook for the variables, macros and filters.
    """

    @env.macro
    def multiply(arg1, arg2):
        "Multiply 2 numbers"
        return arg1 * arg2
