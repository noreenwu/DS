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
            print("   checking subgroup {}:\n".format(g.name))

            # return g.user_in_group(user)
            if g.user_in_group(user):
                # print(" {} is returning True".format(g.name))
                return True
            # else:
            #     print(" {} is  False, so keep going!".format(g.name))

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
            str += "users: {}\n\n".format(users)

        return (str)


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    print("Look for {} in {}\n".format(user, group.name))

    result = group.user_in_group(user)
    print("Is the user {} in group {}?  {}\n".format(user, group.name, result))
    return result


# create a tree of groups and subgroups:
#  Parent Group contains Child Group A and Child Group B
#  Child Group A contains Child Group AA and Child Group AB
#  Child Group B contains Child Group BA and Child Group BB

#  User P is in the Parent Group
#  User B is in Child Group B
#  User BA is in Child Group BA

parent_group = Group("Parent Group")
user_p = "User P"
parent_group.add_user(user_p)

is_user_in_group(user_p, parent_group)          # True: user is in Parent Group

child_group_a = Group("Child Group A")
parent_group.add_group(child_group_a)

child_group_b = Group("Child Group B")
parent_group.add_group(child_group_b)

child_group_aa = Group("Child Group AA")
child_group_ab = Group("Child Group AB")

child_group_a.add_group(child_group_aa)
child_group_a.add_group(child_group_ab)

child_group_ba = Group("Child Group BA")
child_group_bb = Group("Child Group BB")

child_group_b.add_group(child_group_ba)
child_group_b.add_group(child_group_bb)

child_user_b = "childuserb"
child_group_b.add_user(child_user_b)

is_user_in_group(child_user_b, parent_group)   # True: user is found in Child Group B under Parent Group
is_user_in_group(child_user_b, child_group_b)  # True: user is found in Child Group B
is_user_in_group(child_user_b, child_group_a)  # False: user is not in Child Group A

child_user_ba = "childuserba"
child_group_ba.add_user(child_user_ba)

is_user_in_group(child_user_ba, parent_group)  # True: user is found in Child Group BA under Child Group B under Parent Group

is_user_in_group(child_user_ba, child_group_a) # False: user is NOT found in Child Group A (the user is in B)


