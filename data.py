CREATE_PAYLOAD = {
    "text": "Hello meme",
    "url": "https://example.com/cat.jpg",
    "tags": ["cat", "funny"],
    "info": {"author": "Nikolay", "likes": 0},
}

INVALID_CREATE = [
    {},
    {"url": "https://example.com/x.jpg", "tags": [], "info": {}},
    {"text": "test 1", "tags": [], "info": {}},
    {"text": "test 2", "url": "https://example.com/1.jpg", "info": {}},
    {"text": "test 3", "url": "https://example.com/2.jpg", "tags": []},
]

UPDATE_PAYLOAD = {
    "text": "Updated text",
    "url": "https://example.com/updated.jpg",
    "tags": ["updated"],
    "info": {"author": "Новый_Nikolay", "likes": 0},
}

INVALID_UPDATE = [
    {"url": "https://example.com/x.jpg", "tags": [], "info": {}},
    {"text": "test 1", "tags": [], "info": {}},
    {"text": "Test 2", "url": "https://example.com/1.jpg", "info": {}},
    {"text": "test 3", "url": "https://example.com/2.jpg", "tags": []},
]
