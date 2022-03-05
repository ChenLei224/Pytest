"""Test the Task data type."""

from collections import namedtuple

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)

def test_asdict():
    """_asdict() should return a dictionary."""
    t_task = Task('do something', 'lei', True, 30)
    t_dict = t_task._asdict()
    expected = {'summary': 'do something',
                'owner': 'lei',
                'done': True,
                'id': 30}
    assert t_dict == expected

def test_replace():
    """replace() should change passed in fields."""
    t_before = Task('finish book', 'lei', False)
    t_after = t_before._replace(id=10, done=True)
    t_expected = Task('finish book', 'lei', True, 10)
    assert t_after == t_expected
