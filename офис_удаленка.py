def calculate_hourly_payment():
    total_salary = float(input("Введите общую зарплату за месяц (в рублях): "))
    work_type = input("Вы работаете удалённо или в офисе? (введите 'удалёнка' или 'офис'): ").strip().lower()

    # Приводим к единому варианту написания
    if work_type in ('удалёнка', 'удаленка'):
        work_type = 'удалёнка'
    elif work_type in ('офис',):
        work_type = 'офис'
    else:
        print("Некорректный тип работы. Введите 'удалёнка' или 'офис'.")
        return

    # Среднее количество рабочих дней в месяце
    average_working_days = 21.8
    
    # Часы работы в день
    remote_hours_per_day = 8
    office_hours_per_day = 8 + 2  # 8 рабочих часов + 2 часа на дорогу
    
    # Почасовая ставка на удалёнке
    remote_total_hours = average_working_days * remote_hours_per_day
    remote_hourly_payment = total_salary / remote_total_hours
    
    if work_type == 'удалёнка':
        print(f"\nВ среднем месяце {average_working_days:.1f} рабочих дней.")
        print(f"Ваша оплата за один час работы на удалёнке: {remote_hourly_payment:.2f} руб.")
    
    elif work_type == 'офис':
        # Почасовая ставка в офисе без учёта дороги
        office_total_hours = average_working_days * office_hours_per_day
        office_hourly_payment = total_salary / office_total_hours
        
        # Считаем необходимую доплату для одинаковой почасовой ставки
        required_salary = remote_hourly_payment * office_total_hours
        extra_payment = required_salary - total_salary
        
        print(f"\nВ среднем месяце {average_working_days:.1f} рабочих дней.")
        print(f"Ваша фактическая оплата за один час работы в офисе (учитывая дорогу): {office_hourly_payment:.2f} руб.")
        print(f"Чтобы ваша почасовая ставка была такой же, как на удалёнке, зарплата должна быть: {required_salary:.2f} руб.")
        print(f"Разница, которую должны доплатить за дополнительные часы: {extra_payment:.2f} руб.")

# Запуск программы
calculate_hourly_payment()
