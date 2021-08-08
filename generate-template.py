from jinja2 import Template


data = '''
{% raw %}
# ------------------------------- Problem Description ----------------------------
#
#
# ---------------------------------------------------------------------------------



# ------------------------------ Brute Force Solution ------------------------------
#
#
#
# Time Complexity :
#
# Space Complexity
# ----------------------------------------------------------------------------------


def function_name_slow():
    pass



# ----------------------------- Effiecient Solution --------------------------------
#
#
#
# Time Complexity:
#
# Space Complexity:
#------------------------------------------------------------------------------------

def function_name_efficient():
    pass



# Driver Code

def main():
    pass



main()
{% endraw %}
'''

tm = Template(data)

with open("file.py", "w") as f:
    msg = tm.render()
    f.write(msg)