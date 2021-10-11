server_tab_style = '''
ServerDetailsTabWidget {{
    border-top: 0px solid {_border_view};
}}
ServerDetailsTabWidget::pane {{
    border: 1px solid {_border_view};
}}
QTabBar::tab {{
    background-color: #0f2033;
    border: 1px solid {_tab_border_color};
    min-width: 100px;
    min-height: 22px;
    padding: 0px  2px;
    color: rgb(255, 255, 255);
    margin-left: 1px;
    font: 75 12pt "Microsoft YaHei";
}}

QTabBar::tab:selected, QTabBar::tab:hover {{
    background-color: {_tab_selected};
    margin-top: 0px;
}}
QTabBar::tab:!selected {{
    margin-top: 0px;
}}

QListView {{
    border: none;
    color: {_text_color};
    background-color: {_background_color};
}}
QListView::item:hover {{
    outline: none;
    background: none;
    color: white;
}}
QListView::item:selected {{
    background: none;
    color: white;
}}
'''