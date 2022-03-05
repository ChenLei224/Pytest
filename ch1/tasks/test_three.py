"""Test the task data type."""
from collections import namedtuple
Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)
# 你可以使用__new__.__defaults__创建默认的Task对象，不必指定所有属性，测试用例test_defaults()中演示了默认值的校验

def test_defaults():
    """Using no parameters should invoke defaults."""
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2

def test_member_access():
    """Check .field functionality of namedtuple"""
    t = Task('buy milk', 'lei')
    assert t.summary == 'buy milk'
    assert t.owner == 'lei'
    assert (t.done, t.id) == (False, None)

# 测试用例test_member_access()演示了如何利用属性名（而不是索引）来访问对象成员，这也是选用namedtuple的一个原因
