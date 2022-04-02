#The following files (which are all shell) scripts perform the following tasks

0-iam_betty === Switches from current user to the user "betty"

1-who_am_i === Prints effective username of current user

2-groups === Prints all groups the current user is part of

3-new_owner === Changes the owner of a file named "Hello: to the owner "betty'

4-empty === Create an empty file with the name "hello"

5-execute === ADDS execution permission to the owner of the file "hello"

6-multiple_permissions === ADDS execution permission to owner and group of the file "hello" and read permission to others

7-everybody === ADDS execution permission to owner, group and other users without use of commas

8-James_Bond === Givs no permission to the owner and group of the file "hello" but gives all permissions to other users

9-Jon_Doe === Gives permissions -rwxr-x-wx to file "hello"

10-mirror-permission === Copies the permission of one file to another

12-directory_permissions === Creates a directory called my_dir/ with permissions 751 in the working directory.

100-change_group === Changes the group owner to "school" for the file "hello".

14-change_owner_and_group === Changes the owner to "vincent" and the group owner to "staff" for all the files and directories in the working directory.

101-symbolic_link_permissions === Changes the owner and the group owner of '_hello' to 'vincent' and 'staff' respectively.

102-if_only === Changes the owner of the file "hello" to "betty" only if it is owned by the user guillaume.

103-Star_Wars === Plays Star Wars IV episode in the terminal
