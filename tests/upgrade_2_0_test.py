from libcst.codemod import CodemodTest

from codemods.upgrade_2_0 import DotInBlueprintNameCommand


class DotInBlueprintNameCommandTests(CodemodTest):

    TRANSFORM = DotInBlueprintNameCommand

    def test_change_dot_in_blueprint_name(self) -> None:
        before = "Blueprint('foo.bar')"
        after = "Blueprint('foo_bar')"

        self.assertCodemod(before, after)

    def test_change_dot_in_blueprint_name_module_call(self) -> None:
        before = "flask.Blueprint('foo.bar')"
        after = "flask.Blueprint('foo_bar')"

        self.assertCodemod(before, after)

    def test_do_not_change_dot_in_blueprint_name_if_missing(self) -> None:
        before = "Blueprint('foo_bar')"
        after = "Blueprint('foo_bar')"

        self.assertCodemod(before, after)

    def test_do_not_change_dot_in_blueprint_name_if_missing_2(self) -> None:
        before = "Blueprint('foobar')"
        after = "Blueprint('foobar')"

        self.assertCodemod(before, after)
