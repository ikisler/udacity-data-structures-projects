from collections import deque

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    # Validate inputs
    if user == "" or user is None or group is None or not isinstance(group, Group):
        return False

    queue = deque()
    queue.appendleft(group)

    while len(queue) > 0:
        current_group = queue.pop()

        if user in current_group.get_users():
            return True
        elif len(current_group.get_groups()) != 0:
            for subgroup in current_group.get_groups():
                # If it's an empty group with no users or subgroups, don't bother with it
                if len(subgroup.get_users()) != 0 or len(subgroup.get_groups()) !=0:
                    queue.appendleft(subgroup)
    return False

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child.add_user("sub_child_user")
sub_child.add_user("sub_child_user_2")

child.add_group(sub_child)
parent.add_group(child)
parent.add_user("parent_user")

# Check if we can find a valid user multiple levels down
print(is_user_in_group("sub_child_user", parent))
# Returns True

# Check if we can find a valid user at the parent level
print(is_user_in_group("parent_user", parent))
# Returns True

# Check when there is a valid user and only one level of groups
print(is_user_in_group("sub_child_user", sub_child))
# Returns True

# Check for non-existant user
print(is_user_in_group("user does not exist", parent))
# Returns False

# Check when user is blank string
print(is_user_in_group("", parent))
# Returns False

# Check when user is None
print(is_user_in_group(None, parent))
# Returns False

