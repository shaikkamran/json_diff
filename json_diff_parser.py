import json


class JsonParser:
    def __init__(self, filename):

        """JsonDiff object used for parsing complex json structures containg lists ,dictionaries 
		   
		    usage -

		    obj=JsonDiff(dict)
			obj.parse_json() ->Traverses recursively the json in a dfs fashion and stores the result in obj.nodes.
			obj.nodes -> This prints all the leaf nodes extracted..
			obj.get_leaf_res(stack) -> prints the output of the leaf by parsing through the required dc given the keys in stack.
		"""

        self.filename = filename

        self.dc = self.read_json_file()

        self.nodes = []

        self.parse_json()

    def read_json_file(self):

        try:

            with open(self.filename, "r") as f:

                return json.loads(f.read())

        except Exception as e:

            print(f"Error in reading json file bad format {e}")

    def get_leaf_res(self, stack):

        """returns value of leaf node and returns False if the object (x) is not a dictionary or list"""

        dc = self.dc

        if stack:
            try:

                x = dc[stack[0]]
                for i in stack[1:]:
                    x = x[i]

                return x, isinstance(x, (dict, list))
            except Exception as e:
                print(e, "\n---------------\nAssertion Error\n---------------\ne,stack")
        return None, True

    def dfs_for_json(self, no, stack=[]):

        """  dfs_for_json a function of json_diff this recursively parses all the leaf nodes of json by depth first search traversal and gives the list of all the
		childs """

        if isinstance(no, (dict)):

            for new_json in no:

                # if new_json not in stack:

                stack.append(new_json)

                self.dfs_for_json(no[new_json], stack)

        elif isinstance(no, (list)):

            for i, values in enumerate(no):

                # if values not in stack:

                stack.append(i)
                self.dfs_for_json(values, stack)

        if stack:

            result_values = self.get_leaf_res(stack)
            if result_values[1] == False:

                self.nodes.append(stack[:])

            stack.pop()

    def parse_json(self):

        """Call dfs_for_json"""

        self.nodes = []
        self.dfs_for_json(self.dc)


# b=JsonDiff(resp1)
# a.parse_json()
# # b.parse_json()
# print(help(a))
# a.Dfs_for_json()
# print(a.nodes)

# file_old='config.json'
# file_new='config_kamran.json'


# def get_differences_keywise(json_obj_old,json_obj_new):

# 	def get_keynodes(obj):

# 		return set(['->'.join(str(i) for i in node) for node in obj.nodes if node])


# 	old_key_nodes=get_keynodes(json_obj_old)
# 	new_key_nodes=get_keynodes(json_obj_new)
# 	# print(old_key_nodes)


# 	for key in new_key_nodes-old_key_nodes:

# 		print(f'Key "{key}" not present in the file  "{json_obj_old.filename}" ')


# def get_difference_in_the_common_keys(json_obj_old,json_obj_new):

# 	print(f'\nFound Difference from {json_obj_new.filename}\n')
# 	for node in json_obj_new.nodes:

# 		try:

# 			node_new,_=json_obj_new.get_leaf_res(node)
# 			if node not in json_obj_old.nodes:

# 				print(f'{node} not present in file {json_obj_old.filename}')

# 				continue


# 			node_old,_=json_obj_old.get_leaf_res(node)

# 			# print(node_new,node_old)

# 			if node_old!=node_new:

# 				print(f'{node} {node_new} != {node_old} ')

# 		except Exception as e:

# 			# print(e)
# 			pass


# # old_file=JsonDiff('config.json')
# # new_file=JsonDiff('config_kamran.json')


# # print('\n\n Key_value Differences\n\n----------------------\n\n')

# get_difference_in_the_common_keys(JsonDiff(file_old),JsonDiff(file_new))


# get_difference_in_the_common_keys(b,a)

# print('\n\n Json Key Differences\n\n----------------------\n\n')


# get_differences_keywise(b,a)

# get_differences_keywise(a,b)
