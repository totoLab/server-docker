import json
import argparse
import os

def load_config(config_file):
    try:
        with open(config_file, "r") as f:
            config = json.load(f)
        return config
    except FileNotFoundError:
        print(f"Error: The file '{config_file}' was not found.")
        exit(1)
    except json.JSONDecodeError:
        print(f"Error: The file '{config_file}' is not a valid JSON file.")
        exit(1)

def save_config(config_files, config):
    with open(config_files["config_file"], "w") as f:
        json.dump(config, f, indent=4)

    subdomains_names = [item["name"] for item in get_configured_subdomains(config)]
    for save_location in config_files["alternative_save_location"]:
        with open(save_location, "w") as f:
            json.dump(subdomains_names, f)

def get_configured_subdomains(config):
    return config["cloudflare"][0]["subdomains"]

def list_subdomains(config):
    subdomains_names = [item["name"] for item in get_configured_subdomains(config)]
    if not subdomains_names:
        print("No subdomains configured.")
    for i, name in enumerate(subdomains_names):
        print(f"{i + 1}. {name}")
    return subdomains_names

def add_subdomain(config):
    configured_subdomains = get_configured_subdomains(config)
    subdomains_names = [item["name"] for item in configured_subdomains]
    new_subdomain = input("Enter the new subdomain name: ")
    if new_subdomain in subdomains_names:
        print(f"Subdomain '{new_subdomain}' already exists.")
    else:
        configured_subdomains.append({"name": new_subdomain, "proxied": True})
        print(f"Subdomain '{new_subdomain}' added.")

def remove_subdomain(config):
    subdomains_names = list_subdomains(config)
    if not subdomains_names:
        return
    try:
        choice = int(input("Enter the number of the subdomain to remove: "))
        if 1 <= choice <= len(subdomains_names):
            removed_subdomain = get_configured_subdomains(config).pop(choice - 1)
            print(f"Subdomain '{removed_subdomain['name']}' removed.")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    parser = argparse.ArgumentParser(description="Manage Cloudflare subdomains in a config file.")
    parser.add_argument("config_file", help="Path to the config file")

    args = parser.parse_args()

    config = load_config(args.config_file)
    save_locations = {
        "config_file": args.config_file,
        "alternative_save_location": [os.path.expanduser("~/sites/antolab.xyz/html/data.json")]
    }

    while True:
        print("\nCurrent subdomains:")
        list_subdomains(config)
        print("\nOptions:")
        print("1. Add subdomain")
        print("2. Remove subdomain")
        print("3. Force save")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            add_subdomain(config)
            save_config(save_locations, config)
        elif choice == '2':
            remove_subdomain(config)
            save_config(save_locations, config)
        elif choice == '3':
            save_config(save_locations, config)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
