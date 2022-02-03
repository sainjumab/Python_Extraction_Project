import json
import glob
import re


# Load Json Files
def load_text_file(f):    
    with open(f, 'r') as file:
        json_map = json.load(file)
        return json_map

# Function to clean data
def data_clean(text):
    try:
        strip_po = [i.strip() for i in text.split('\n')]
        remove_space = [i for i in strip_po if i not in [' ', '']]
        remove_space_between = [i.split('  ') for i in remove_space]
        cleaned_data = list()
        count = 0
        for i in remove_space_between:
            cleaned_data.append([])
            for j in i:
                if j not in ['']:
                    cleaned_data[count].append(j.strip())
            count += 1
        
        return cleaned_data

    except Exception as e:
        print("kvt data clean exception")
        print(e)
        return None


# Get text between lines
def get_lines_between(origtmp, str1, str2):
    start_index = 0
    stop_index = 0
    for ele_nos, ele in enumerate(origtmp):
        for stchar in ele:
            if str1 in stchar.lower():
                start_index = ele_nos

            if str2 in stchar.lower():
                stop_index = ele_nos
                return origtmp[start_index:stop_index+1]
    return([])


def get_carrier_name(carrier_info):
    carr_info = get_lines_between(carrier_info, "carrier:","carrier:")
    #print(carr_info)
    if len(carr_info) == 0:
        return 'Carrier name not found'
    if len(carr_info[0]) > 2:
        return carr_info[0][1]
    else:
        return carr_info[0][-1]


def get_mc_number(mc_info):
    m_info = get_lines_between(mc_info, "mc#","mc#")
    # print(m_info)
    if len(m_info) == 0:
        return 'MC not found'
    if len(m_info[0]) > 2:
        return m_info[0][1]
    else:
        return m_info[0][-1]
    
def get_attention(attention_info):    
    att_info = get_lines_between(attention_info, "attention:","attention:")
    # print(att_info)
    if len(att_info) == 0:
        return 'Attention not found'
    if len(att_info[0]) > 2:
        return att_info[0][1]
    else:
        return att_info[0][-1]


def get_equipment(equipment_info):
    equ_info = get_lines_between(equipment_info, "equipment:","equipment:")
    # print(equ_info)
    if len(equ_info) == 0:
        return 'Equipment not found'
    if len(equ_info[0]) > 2:
        return equ_info[0][1]
    else:
        return equ_info[0][-1]
    pass

def get_carrier_phone(carr_phone_info):
    phone_info = get_lines_between(carr_phone_info, "phone:","phone:")
    # print(phone_info)
    if len(phone_info) == 0:
        return 'Phone not found'
    if len(phone_info[0]) > 2:
        return phone_info[0][1]
    else:
        return phone_info[0][-1]


def get_pro_number():
    pass

# Extract  Information
def kvt_extract(text_data):
    carrier_information = {} 
    cleaned_data = data_clean(text_data)

    # Get carrier info    
    carrier_info = get_carrier_name(cleaned_data)
    mc_number = get_mc_number(cleaned_data)
    attention = get_attention(cleaned_data)
    equipment = get_equipment(cleaned_data)
    carrier_phone = get_carrier_phone(cleaned_data)
    
    
    carrier_information["Carrier"] = carrier_info
    carrier_information["MC#"] = mc_number
    carrier_information["Attention"] = attention
    carrier_information["Equipment"] = equipment
    carrier_information["Phone"] = carrier_phone
    
    return carrier_information

extracted_info = []

# Main
for file_path in glob.glob('C:/Users/mabin/Desktop/gc apply/Generation-Student/Documents/TEXT Files/*.json'):
    #print(file_path)
    text_map = load_text_file(file_path)
    text = "\n\n\n".join(text_map['text'].values())
    
    
    # print(text)
    details = kvt_extract(text)
    extracted_info.append(details)
for items in extracted_info:
    print(items)
