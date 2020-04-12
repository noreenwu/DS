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

    def user_in_group(self, user):
        if user in self.users:
            return True

        # check subgroups
        for g in self.groups:
            print("checking subgroup {}".format(g))
            return g.user_in_group(user)

        return False

    def __repr__(self):
        groups = ""
        for g in self.groups:
            groups = groups + " {}".format(g)

        users = ""
        for u in self.users:
            users = users + " {}".format(u)


        str = "name: {}\n".format(self.name)

        if groups != "":
            str += "groups: {}\n".format(groups)

        if users != "":
            str += "users: {}".format(users)

        return (str)


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    print("look for {} in {}\n".format(user, group))

    return group.user_in_group(user)


parent_group = Group("parentgroup")
child_group = Group("childgroup")
parent_group.add_group(child_group)

child_user = "childuser"
child_group.add_user(child_user)

print(is_user_in_group("childuser", parent_group))

sub_child_group = Group("subchildgroup")
child_group.add_group(sub_child_group)

sub_child_user = "subchilduser"
sub_child_group.add_user(sub_child_user)

print(is_user_in_group("subchilduser", parent_group))
