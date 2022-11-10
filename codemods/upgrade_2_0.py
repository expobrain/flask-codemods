import libcst as cst
from libcst import matchers
from libcst.codemod import VisitorBasedCodemodCommand


class DotInBlueprintNameCommand(VisitorBasedCodemodCommand):

    DESCRIPTION = "Replace the dot (.) in blueprint names with an underscore (_)."

    matcher = matchers.OneOf(
        matchers.Call(func=matchers.Name(value="Blueprint")),
        matchers.Call(
            func=matchers.Attribute(
                value=matchers.Name(value="flask"), attr=matchers.Name(value="Blueprint")
            )
        ),
    )

    def leave_Call(self, original_node: cst.Call, updated_node: cst.Call) -> cst.Call:
        if matchers.matches(updated_node, self.matcher):
            arg: cst.Arg = updated_node.args[0]
            arg_value = arg.value

            if not isinstance(arg_value, cst.SimpleString):
                raise RuntimeError("Blueprint name not a string.")

            blueprint_name = arg_value.value
            blueprint_name = blueprint_name.replace(".", "_")

            updated_args = list(updated_node.args)
            updated_args[0] = cst.Arg(cst.SimpleString(blueprint_name))

            return updated_node.with_changes(args=updated_args)

        return updated_node
