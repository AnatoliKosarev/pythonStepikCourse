def var_in_namespace(namespace, query_var):
    if namespace in namespace_dict and query_var in namespace_dict[namespace]['vars']:
        return True
    else:
        return False


req_count = input('Enter number of requests: ')

if req_count and req_count.isdigit():
    int_req_count = int(req_count)
    namespace_dict = {'global': {'parent': None, 'vars': []}}
    for _ in range(int_req_count):
        request = input('Enter your request: ')
        request_parsed = request.split()
        command = request_parsed[0].lower()
        namespace_name = request_parsed[1].lower()
        if command == 'create':
            parent_name = request_parsed[2].lower()
            if namespace_name not in namespace_dict:
                namespace_dict[namespace_name] = {'parent': parent_name, 'vars': []}
            else:
                print('Such namespace already exists.')
                continue
        elif command == 'add':
            var_name = request_parsed[2].lower()
            if namespace_name in namespace_dict:
                namespace_dict[namespace_name]['vars'].append(var_name)
            else:
                print('Such namespace doesn\'t exist.')
                continue
        elif command == 'get':
            var_name = request_parsed[2].lower()
            while True:
                if var_in_namespace(namespace_name, var_name):
                    print(namespace_name)
                    break
                namespace_name = namespace_dict[namespace_name].get('parent', False)
                if not namespace_name:
                    print('None')
                    break
        else:
            print('Command is invalid')
            break
