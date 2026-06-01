def define_env(env):
    """
    This is the hook for the variables, macros and filters.
    """

    @env.macro
    def multiply(arg1, arg2):
        "Multiply 2 numbers"
        return arg1 * arg2

    @env.macro
    def i18n_str(key_path):
        # https://mkdocs-macros-plugin.readthedocs.io/en/latest/macros/
        lang = env.conf['theme']['language']
        # conf is for mkdocs.yml , use variables
        result = env.variables[lang]
        # print(f"lang: {lang}, string file contents: {result}")

        # the for loop will set translations
        # result = result.notices returns the list
        # result = result.outdatedTranslation skips over notices and returns the value
        for key in key_path.split('.'):
            result = result[key]
        if result is None:
            # fallback to english
            lang = "en"
            result = env.variables[lang]
            for key in key_path.split('.'):
                result = result[key]
        return result
