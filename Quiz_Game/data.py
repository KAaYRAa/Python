import requests
parameter = {
  'amount':10,
  'type':"boolean"}
response= requests.get("https://opentdb.com/api.php",params=parameter)
response.raise_for_status()
data=response.json()
question_data= data["results"]
"""question_data = [
{
  "response_code": 0,
  "results": [
    {
      "type": "boolean",
      "difficulty": "easy",
      "category": "Mythology",
      "question": "In the Greek Mythology, the Gorgon can turn those who behold her to stone.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "type": "boolean",
      "difficulty": "medium",
      "category": "Mythology",
      "question": "The Japanese god Izanagi successfully returned his wife Izanami from the Underworld.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "type": "boolean",
      "difficulty": "medium",
      "category": "Mythology",
      "question": "In Greek mythology, Hera is the goddess of harvest.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "type": "boolean",
      "difficulty": "hard",
      "category": "Mythology",
      "question": "Janus was the Roman god of doorways and passageways.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "type": "boolean",
      "difficulty": "easy",
      "category": "Mythology",
      "question": "According to Greek Mythology, Zeus can control lightning.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "type": "boolean",
      "difficulty": "easy",
      "category": "Mythology",
      "question": "A wyvern is the same as a dragon.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "type": "boolean",
      "difficulty": "hard",
      "category": "Mythology",
      "question": "Ska&eth;i is the Norse Goddess of skiing, mountains, winter and bowhunting.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "type": "boolean",
      "difficulty": "medium",
      "category": "Mythology",
      "question": "According to Norse mythology, Loki is a mother.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    },
    {
      "type": "boolean",
      "difficulty": "easy",
      "category": "Mythology",
      "question": "In the Greek Mythology, the god of war is called Mars.",
      "correct_answer": "False",
      "incorrect_answers": [
        "True"
      ]
    },
    {
      "type": "boolean",
      "difficulty": "hard",
      "category": "Mythology",
      "question": "Rannamaari was a sea demon that haunted the people of the Maldives and had to be appeased monthly with the sacrifice of a virgin girl.",
      "correct_answer": "True",
      "incorrect_answers": [
        "False"
      ]
    }
  ]
}
]"""