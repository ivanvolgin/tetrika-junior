def appearance(intervals: dict[str, list[int]]) -> int:
    # Преобразуем входные данные в интервалы
    lesson = _to_intervals(intervals['lesson'])[0]
    pupil = _to_intervals(intervals['pupil'])
    tutor = _to_intervals(intervals['tutor'])

    # Находим все пересечения ученика и преподавателя в рамках урока
    common = _find_common_intervals(pupil, tutor, lesson)

    # Объединяем пересекающиеся интервалы, чтобы не учитывать общее время дважды
    merged = _merge_intervals(common)

    # Считаем итоговую длительность
    return _sum_durations(merged)


def _to_intervals(flat: list[int]) -> list[tuple[int, int]]:
    """Преобразует плоский список в список пар (start, end)"""
    return list(zip(flat[::2], flat[1::2]))


def _intersections(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int] | None:
    """Возвращает пересечение двух интервалов, если оно существует"""
    start = max(a[0], b[0])
    end = min(a[1], b[1])
    return (start, end) if start < end else None


def _merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Объединяет пересекающиеся интервалы в непересекающиеся"""
    if not intervals:
        return []

    intervals.sort()  # сортируем по началу интервала
    result = [intervals[0]]

    for curr in intervals[1:]:
        last = result[-1]
        if curr[0] <= last[1]:
            # если есть пересечение — объединяем
            result[-1] = (last[0], max(last[1], curr[1]))
        else:
            result.append(curr)

    return result


def _find_common_intervals(
        pupil: list[tuple[int, int]],
        tutor: list[tuple[int, int]],
        lesson: tuple[int, int]
) -> list[tuple[int, int]]:
    """
    Ищет пересечения между интервалами ученика и преподавателя,
    а затем пересекает результат с интервалом урока
    """
    i = j = 0
    result = []

    while i < len(pupil) and j < len(tutor):
        p = pupil[i]
        t = tutor[j]

        # Пересечение ученик ∩ преподаватель
        pair = _intersections(p, t)
        if pair:
            # Пересекаем с интервалом урока
            triple = _intersections(pair, lesson)
            if triple:
                result.append(triple)

        # Сдвигаем указатель на интервал, который раньше закончился
        if p[1] < t[1]:
            i += 1
        else:
            j += 1

    return result


def _sum_durations(intervals: list[tuple[int, int]]) -> int:
    """Считает суммарную длительность всех интервалов"""
    return sum(end - start for start, end in intervals)
