from pydicom import DataElement


def format_func(format_string, *args):
    return format_string.format(*args)


class Anonymiser:
    FUNCTION_MAP = {
        'format': format_func
    }

    def __init__(self, dicom_data):
        self.dicom_data = dicom_data
        self.variables = {}

    def perform_action(self, action_data):
        if action_data['Action'] == 'Initialization':
            name = action_data['Variable']
            value = action_data['Value']
            value = self.perform_term(value)
            print(f"Setting {name} to {value} for later use")
            self.variables[name] = value

        elif action_data['Action'] == 'Deletion':
            tag = action_data['Lvalue']
            print(f"Removing {tag}")
            del self.dicom_data[tag['dcm_group'], tag['dcm_element']]

        elif action_data['Action'] == 'Assignment':
            tag = action_data['Lvalue']
            value = action_data['RValue']
            value = self.perform_term(value)
            print(f"Assigning {tag} to {value}")
            try:
                self.dicom_data[tag['dcm_group'], tag['dcm_element']].value = value
            except KeyError:
                # Create new data element
                value = DataElement(
                    (tag['dcm_group'], tag['dcm_element']),
                    'ST',
                    value
                )
                self.dicom_data[tag['dcm_group'], tag['dcm_element']] = value

        else:
            print(f'Uknown action: {action_data}')

    def perform_function(self, function_data):
        print(f"Peforming function: {function_data}")
        func = self.FUNCTION_MAP[function_data['FunctionName']]
        args_list = function_data['ArgList']
        # Parse all terms
        args_list = [self.perform_term(x) for x in args_list]
        result = func(*args_list)
        return result

    def perform_term(self, term_data):
        if term_data['Type'] == 'string':
            # Remember to strip the quotes (hence the 1:-1 slice)
            return term_data['TermVal'][1:-1]
        elif term_data['Type'] == 'int':
            return int(term_data['TermVal'])
        elif term_data['Type'] == 'float':
            return float(term_data['TermVal'])
        elif term_data['Type'] == 'DicomTag':
            return self.dicom_data[term_data['dcm_group'], term_data['dcm_element']].value
        elif term_data['Type'] == 'function':
            return self.perform_function(term_data)
        else:
            raise ValueError(f"Encountered unknown term type {term_data['Type']}")