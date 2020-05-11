from enum import Enum, unique
from textwrap import dedent

from pathvalidate import replace_symbol


class Header:
    FILEPATH = "filepath"
    TESTFUNC = "function"


class ColorPoicy:
    AUTO = "auto"
    TEXT = "text"
    NEVER = "never"
    LIST = (AUTO, TEXT, NEVER)


class ZerosRender:
    NUMBER = "number"
    EMPTY = "empty"
    LIST = (NUMBER, EMPTY)


class FGColor:
    SUCCESS = "light_green"
    ERROR = "light_red"
    SKIP = "light_yellow"
    GRAYOUT = "light_black"


class BGColor:
    EVEN_ROW = "#202020"
    ODD_ROW = "black"


class Default:
    COLOR = ColorPoicy.AUTO
    MARGIN = 1
    ZEROS = ZerosRender.NUMBER


@unique
class Option(Enum):
    MD_REPORT = ("md-report", "create markdown report.")
    MD_REPORT_VERBOSE = (
        "md-report-verbose",
        dedent(
            """\
            verbosity level for pytest-md-report. if not set, using verbosity level of pytest.
            defaults to 0.
        """
        ),
    )
    MD_REPORT_COLOR = (
        "md-report-color",
        dedent(
            """\
            auto: display colored (text and background) reports by using ANSI escape codes.
            text: display colored (text) reports by using ANSI escape codes.
            never: display report without color.
            defaults to '{default}'.
            """
        ).format(default=Default.COLOR),
    )
    MD_REPORT_MARGIN = (
        "md-report-margin",
        dedent(
            """\
            margin size for each cells.
            defaults to {default}.
            """
        ).format(default=Default.MARGIN),
    )
    MD_REPORT_ZEROS = (
        "md-report-zeros",
        dedent(
            """\
            rendering method for results of zero values.
            number: render as a digit number (0).
            empty: not rendering.
            defaults to {default}.
            """
        ).format(default=Default.ZEROS),
    )

    @property
    def cmdoption_str(self) -> str:
        return "--" + replace_symbol(self.__name, "-").lower()

    @property
    def envvar_str(self) -> str:
        return "PYTEST_" + replace_symbol(self.__name, "_").upper()

    @property
    def inioption_str(self) -> str:
        return replace_symbol(self.__name, "_").lower()

    @property
    def help_msg(self) -> str:
        return self.__help_msg

    def __init__(self, name: str, help_msg: str) -> None:
        self.__name = name.strip()
        self.__help_msg = help_msg


class HelpMsg:
    EXTRA_MSG_TEMPLATE = " you can also specify the value with {} environment variable."
