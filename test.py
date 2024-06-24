@router.message(StateFilter(None), Command("food"))
async def cmd_food(message: Message, state: FSMContext):
    await message.answer(
        text="Выберите блюдо:",
        reply_markup=make_row_keyboard(available_food_names)
    )
    # Устанавливаем пользователю состояние "выбирает название"
    await state.set_state(OrderFood.choosing_food_name)