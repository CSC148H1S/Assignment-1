import unittest
import pytest
import grouper
from typing import List, Set, FrozenSet


class TestGroup:
    def test__len__(self, group) -> None:
        assert len(group) > 0

    def test__contains__(self, group) -> None:
        assert len(group) > 1

    def test__str__(self, s) -> None:
        assert type(s) == str

    def test_get_members(self, members) -> None:
        assert len(members) > 1


class TestGrouping:
    def test__len__(self, grouping):
        assert len(grouping) > 1

    def test__str__(self, grouping) -> None:
        assert type(grouping) == str

    def test_add_groups(self) -> None:
        group = grouper.Group()
        grouping = grouper.Grouping()
        if len(group) == 0:
            assert group not in grouping

    def test_get_groups(self, group, grouping) -> None:
        for group in grouping:
            assert group in grouping


if __name__ == '__main__':
    pytest.main(['example_tests.py'])



