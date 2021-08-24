style = '''
ServersTable {{
    border-style: solid;
    border-width: 1px;
    border-color: {border_color};
    border-radius: {radius};
    background-color: {bg_color};
    padding: 5px;
    color: {color};
}}
ServersTable::item {{
    border-color: none;
    padding-left: 5px;
    padding-right: 5px;
}}
ServersTable::item:selected {{
    background-color: {selection_color};
}}

/* ////////TOP BAR////////// */
QTableWidget QTableCornerButton::section {{
    border: none;
	background-color: {selection_color};
	padding: 3px;
    border-top-left-radius: {radius}px;
}}
QHeaderView::section:horizontal {{
    border: none;
	background-color: {selection_color};
	padding: 3px;
}}
QHeaderView::section:vertical {{
    border: none;
	background-color: {selection_color};
	padding-left: 5px;
    padding-right: 5px;
    border-bottom: 1px solid {selection_color};
    margin-bottom: 1px;
}}
'''