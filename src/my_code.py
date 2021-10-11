imgui_code = """
import dearpygui.dearpygui as dpg

window = dpg.window(label="Example Window")
dpg.add_text("Hello, world")
dpg.add_button(label="Save")
dpg.add_input_text(label="string", default_value="Quick brown fox")
dpg.add_slider_float(label="float", default_value=0.273, max_value=1)

dpg.start_dearpygui()
"""

if __name__ == "__main__":
    import imgui