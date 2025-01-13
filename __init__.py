def log_message(message):
    print(f"[LOG] {message}")

def load_config(config_file):
    import json
    with open(config_file, 'r') as file:
        return json.load(file)

def save_config(config, config_file):
    import json
    with open(config_file, 'w') as file:
        json.dump(config, file, indent=4)