def recursive_search(src: dict, value: str, deep: int = -1, parent: str = None):
    if isinstance(src, dict):
        for k, v in src.items():
            recursive_search(v, value, deep=deep + 1, parent=k)
    elif isinstance(src, list):
        for l in src:
            recursive_search(l, value, deep=deep, parent=parent)
    else:
        if src == value:
            print(f"{value} is found! Deep={deep}, Parent={parent}")
            return


source_dict = {
    "key1": {
        "key2": {
            "key3": [
                "John",
                {
                    "key4": "Bob",
                    "key5": "Alex",
                    "key6": {
                        "key7": [
                            {
                                "key7": "Jessica",
                                "key8": {
                                    "key9": [
                                        "Alex"
                                    ]
                                }
                            }
                        ]
                    }
                }
            ]
        }
    },
    "key4": "Kate"
}

recursive_search(source_dict, 'Alex')
