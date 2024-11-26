from pydbml._classes.table_group import TableGroup
from pydbml.classes import Table
from pydbml.renderer.dbml.default import render_table_group


def test_render_table_group(table1: Table, table2: Table, table3: Table) -> None:
    tg = TableGroup(
        name="mygroup", items=[table1, table2, table3], comment="My comment"
    )
    expected = (
        "// My comment\n"
        "TableGroup \"mygroup\" {\n"
        '    "products"\n'
        '    "products"\n'
        '    "orders"\n'
        "}"
    )
    assert render_table_group(tg) == expected

def test_render_table_group_when_name_with_dash(table1: Table, table2: Table, table3: Table) -> None:
    tg = TableGroup(
        name="mygroup-1", items=[table1, table2, table3], comment="My comment"
    )
    expected = (
        "// My comment\n"
        "TableGroup \"mygroup-1\" {\n"
        '    "products"\n'
        '    "products"\n'
        '    "orders"\n'
        "}"
    )
    assert render_table_group(tg) == expected

