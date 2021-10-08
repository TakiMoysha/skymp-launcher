style = '''
ServersTable {{
    outline: none;
    border: 1px solid {border_color};
    border-radius: {radius};
    padding: 5px;
    gridline-color: {transparent};
    color: {color};
    font: {text_font};

}}
ServersTable::item {{
    padding-left: 5px;
    padding-right: 5px;
    border-style: solid;
}}
ServersTable::item:selected {{
    background-color: {selection_color};
}}

HorizontalHeader {{
}}
HorizontalHeader::section:selected {{
    color: ffffff;
}}
HorizontalHeader::section:horizontal {{
    border: none;
	background-color: {header_background};
	padding: 4px;
}}
HorizontalHeader::section::horizontal:first {{
    border-top-left-radius: 8px;
}}
HorizontalHeader::section::horizontal:last {{
    border-top-right-radius: 8px;
}}
'''

'''
/* ///////////////////////////////ScrollBars///////////////////////////////// */
QScrollBar:horizontal {{
    border: none;
    background: #FFF;
    height: 8px;
    margin: 0px 21px 0 21px;
	border-radius: 0px;
}}
QScrollBar::handle:horizontal {{
    background: #00ABE8;
    min-width: 25px;
	border-radius: 4px
}}
QScrollBar::add-line:horizontal {{
    border: none;
    background: #333123;
    width: 20px;
	border-top-right-radius: 4px;
    border-bottom-right-radius: 4px;
    subcontrol-position: right;
    subcontrol-origin: margin;
}}
QScrollBar::sub-line:horizontal {{
    border: none;
    background: #333123;
    width: 20px;
	border-top-left-radius: 4px;
    border-bottom-left-radius: 4px;
    subcontrol-position: left;
    subcontrol-origin: margin;
}}
QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal
{{
     background: none;
}}
QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
{{
     background: none;
}}
QScrollBar:vertical {{
	border: none;
    background: #FFF;
    width: 8px;
    margin: 21px 0 21px 0;
	border-radius: 0px;
}}
QScrollBar::handle:vertical {{
	background: #00ABE8;
    min-height: 25px;
	border-radius: 4px
}}
QScrollBar::add-line:vertical {{
     border: none;
    background: #333123;
     height: 20px;
	border-bottom-left-radius: 4px;
    border-bottom-right-radius: 4px;
     subcontrol-position: bottom;
     subcontrol-origin: margin;
}}
QScrollBar::sub-line:vertical {{
	border: none;
    background: #333123;
     height: 20px;
	border-top-left-radius: 4px;
    border-top-right-radius: 4px;
     subcontrol-position: top;
     subcontrol-origin: margin;
}}
QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {{
     background: none;
}}
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {{
     background: none;
}}
'''

'''
QHeaderView::section{{
	background-color: rgb(33, 37, 43);
	max-width: 30px;
	border: 1px solid rgb(44, 49, 58);
	border-style: none;
    border-bottom: 1px solid rgb(44, 49, 60);
    border-right: 1px solid rgb(44, 49, 60);
}}
'''