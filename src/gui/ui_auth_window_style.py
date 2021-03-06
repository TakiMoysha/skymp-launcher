combo_box_style = '''
QComboBox {{
    subcontrol-origin: padding;
    subcontrol-position: top right;

    border: 1px solid {border_color};
    border-radius: 8px;
    padding: 1px 18px 1px 3px;
    font: 12pt 'Segoe UI';
    background-color: {background_color};
    color: {text_color};
}}

QComboBox:open {{
    padding-top: 3px;
    padding-left: 4px;
}}

QComboBox::drop-down {{
    subcontrol-origin: padding;
    subcontrol-position: right;
    width: 30px;

    border-left-width: 1px;
    border-left-color: {border_color};
    border-left-style: solid;
}}

QComboBox::down-arrow {{
    image: url({arrow_path});
    width: 14px;
    height: 14px;
}}

QComboBox::down-arrow:on {{
    width: 12px;
    height: 12px;
}}

QListView {{
    border: 1px solid {border_color};
    border-radius: 8px;
    background-color: {background_color};
    color: {text_color};
}}
'''

line_edit_style = '''
QLineEdit {{
    border-radius: 8px;
    border: 1px solid {border_color};
    color: {text_color};
    background-color: {background_color};
    font: 12px "Segoe UI";
    padding: 2px;
}}
'''

check_box_style ='''
'''

push_button_style = '''
'''