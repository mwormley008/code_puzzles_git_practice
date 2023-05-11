# further git practice
# after merge
def leo(oscar):
    oscar_dict = {
        88:'Leo finally won the oscar! Leo is happy',
        87:'When will you give Leo an Oscar?',
        86:'Not even for Wolf of wallstreet?!'
    }
    if oscar >= 89:
        return "Leo got one already!"
    elif oscar < 86:
        return "When will you give Leo an Oscar?"
    else:
        return oscar_dict[oscar]