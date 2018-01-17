from django.test import TestCase

from compressor_toolkit.precompilers import SCSSCompiler, ES6Compiler


class SASSES6IntegratinTestCase(TestCase):
    def test_sass_integration(self):
        # This test verifies, if the compiler paths and node packages for
        # SCSS compilation are correctly set up
        self.assertEquals(
            SCSSCompiler(content='p { \n\n\nmargin: 2px+20px; }').input(),
            'p {\n  margin: 22px;\n}\n'
        )

    def test_es6_integration(self):
        # This test verifies, if the compiler paths and node packages for
        # ES6 compilation are correctly set up
        compiled_result = ES6Compiler(content='console.log(3);').input()

        self.assertTrue('function(require,module,exports)' in compiled_result)
        self.assertTrue('console.log(3)' in compiled_result)
