from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline_order_roll_button = InlineKeyboardButton('Заказать ролл', callback_data='Ordered roll')

inline_order_roll_kb = InlineKeyboardMarkup()
inline_order_roll_kb.add(inline_order_roll_button)

inline_order_pizza_button = InlineKeyboardButton('Заказать пиццу', callback_data='Ordered pizza')

inline_order_pizza_kb = InlineKeyboardMarkup()
inline_order_pizza_kb.add(inline_order_pizza_button)

inline_order_burger_button = InlineKeyboardButton('Заказать бургер', callback_data='Ordered burger')


inline_order_burger_kb = InlineKeyboardMarkup()
inline_order_burger_kb.add(inline_order_burger_button)


inline_delete_order_burger_button = InlineKeyboardButton('Отменить заказ бургера', callback_data='delete order burger')
inline_delete_order_burger_kb = InlineKeyboardMarkup()
inline_delete_order_burger_kb.add(inline_delete_order_burger_button)

inline_delete_order_roll_button = InlineKeyboardButton('Отменить заказ роллов', callback_data='delete order roll')
inline_delete_order_roll_kb = InlineKeyboardMarkup()
inline_delete_order_roll_kb.add(inline_delete_order_roll_button)



inline_delete_order_pizza_button = InlineKeyboardButton('Отменить заказ пиццы', callback_data='delete order pizza')
inline_delete_order_pizza_kb = InlineKeyboardMarkup()
inline_delete_order_pizza_kb.add(inline_delete_order_pizza_button)



inline_delete_roll_button_admin = InlineKeyboardButton('Удалить заказ роллов', callback_data='delete order roll admin')
inline_delete_roll_kb_admin = InlineKeyboardMarkup()
inline_delete_roll_kb_admin.add(inline_delete_roll_button_admin)

inline_delete_pizza_button_admin = InlineKeyboardButton('Удалить заказ пиццы', callback_data='delete order pizza admin')
inline_delete_pizza_kb_admin = InlineKeyboardMarkup()
inline_delete_pizza_kb_admin.add(inline_delete_pizza_button_admin)

inline_delete_burger_button_admin = InlineKeyboardButton('Удалить заказ бургеров', callback_data='delete order burger admin')
inline_delete_burger_kb_admin = InlineKeyboardMarkup()
inline_delete_burger_kb_admin.add(inline_delete_burger_button_admin)

