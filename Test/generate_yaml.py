import yaml

data = {
    'train': 'Dataset_with_validation/images/train',
    'val': 'Dataset_with_validation/images/val',
    'test': 'Dataset_with_validation/images/test',
    'nc': 3,  
    'names': ['l_fully_ripened', 'l_half_ripened', 'l_green']  
}

with open('dataset.yaml', 'w') as yaml_file:
    yaml.dump(data, yaml_file, default_flow_style=False)