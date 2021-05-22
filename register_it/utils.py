# -*- coding: utf-8 -*-
# @Time    : 2021/5/22
# @Author  : Lart Pang
# @GitHub  : https://github.com/lartpang


def formatter_for_dict(info_dict: dict, headers: list, name_length=20, obj_str_length=60):
    assert len(headers) == 2
    table_cfg = dict(
        name=dict(max_length=name_length, mode="left"),
        obj=dict(max_length=obj_str_length, mode="left"),
    )

    table_rows = [item2str(headers[0], **table_cfg["name"]) + "|" + item2str(headers[1], **table_cfg["obj"])]
    for name, obj in info_dict.items():
        table_rows.append((item2str(name, **table_cfg["name"]) + "|" + item2str(str(obj), **table_cfg["obj"])))

    dividing_line = "\n" + "-" * len(table_rows[0]) + "\n"
    return dividing_line.join(table_rows)


def item2str(string: str, max_length: int, padding_char: str = " ", mode: str = "left"):
    assert isinstance(max_length, int), f"{max_length} must be `int`"

    real_length = len(string)
    if real_length <= max_length:
        padding_length = max_length - real_length
        if mode == "left":
            clipped_string = string + f"{padding_char}" * padding_length
        elif mode == "center":
            left_padding_str = f"{padding_char}" * (padding_length // 2)
            right_padding_str = f"{padding_char}" * (padding_length - padding_length // 2)
            clipped_string = left_padding_str + string + right_padding_str
        elif mode == "right":
            clipped_string = f"{padding_char}" * padding_length + string
        else:
            raise NotImplementedError
    else:
        clipped_string = string[:max_length]

    return clipped_string
