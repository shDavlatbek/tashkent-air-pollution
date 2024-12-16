def clean_data(data: list[dict], key_map: dict, value_map: dict) -> list[dict]:
    """
    Cleans and transforms the data by replacing keys and specific values.

    Args:
        data (list[dict]): The data to be cleaned.
        key_map (dict): A mapping of old key names to new key names.
        value_map (dict): A mapping of old values to new values for specific keys.

    Returns:
        list[dict]: The cleaned data.
    """
    cleaned_data = []

    for record in data:
        cleaned_record = {}
        for key, value in record.items():
            # Replace keys using key_map
            new_key = key_map.get(key, key)

            # Replace values for specific keys using value_map
            if new_key in value_map and value in value_map[new_key]:
                value = value_map[new_key][value]

            cleaned_record[new_key] = value
        cleaned_data.append(cleaned_record)

    return cleaned_data