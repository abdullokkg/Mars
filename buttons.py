from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

asosiy_menu = ReplyKeyboardMarkup(
    keyboard=[
       [
          KeyboardButton(text="Ozbek tili🇺🇿"),
          KeyboardButton(text="Русский язык🇷🇺"),
       ]
    ],
    resize_keyboard=True
)
menuMain = ReplyKeyboardMarkup(
    keyboard=[
       [
          KeyboardButton(text="Ma'lumotlar📄"),
       ],
       [
          KeyboardButton(text="Xodimlar xaqida Malumot👨‍💻"),
       ],
       [
          KeyboardButton(text="Nima yordam bera olaman😇"),
       ],
       [
          KeyboardButton(text="Savollar📝"),
          KeyboardButton(text="Tilni ozgartirish🇷🇺")
       ]
    ],
    resize_keyboard=True
)

menuBack = ReplyKeyboardMarkup(
    keyboard=[
        [
           KeyboardButton(text="Ortga↩️")
        ]
    ],
    resize_keyboard=True
)

menuMene = ReplyKeyboardMarkup(
    keyboard=[
         [
           KeyboardButton(text="Bo'lim mudiri🤵🏼‍♀️"),
           KeyboardButton(text="Shifokor👩🏼‍⚕️")
         ],
         [
           KeyboardButton(text="Psixolog👱🏼"),
           KeyboardButton(text="Ijtimoiy xodim🤝")
         ],
         [
           KeyboardButton(text="Ortga↩️")
         ]
        ],
    resize_keyboard=True
)

menuKoz = ReplyKeyboardMarkup(
    keyboard=[
         [
           KeyboardButton(text="Pul yordami💸")
         ],
         [
           KeyboardButton(text="O'yinchoq🧸"),
           KeyboardButton(text="Koʻngili(волонтёр) boʻlmoqchiman")
         ],
         [
           KeyboardButton(text="Oziq-ovqat🍕"),
           KeyboardButton(text="Boshqa🤔")
         ],
         [
           KeyboardButton(text="Ortga↩️")
         ]
    ],
    resize_keyboard=True
)

menuizi = ReplyKeyboardMarkup(
    keyboard=[
        [
           KeyboardButton(text="Payme💵"),
           KeyboardButton(text="Click💵")
        ],
        [
           KeyboardButton(text="Ortga↩️")
        ]
    ],
    resize_keyboard=True
)