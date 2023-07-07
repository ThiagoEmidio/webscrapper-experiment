def show_click(driver, element, x_offset, y_offset, tooltip_text="here"):
    # Get the coordinates of the element's center
    element_x = element.location['x'] + element.size['width'] / 2
    element_y = element.location['y'] + element.size['height'] / 2

    # Calculate the absolute coordinates based on the element's center and offsets
    x = int(element_x + x_offset)
    y = int(element_y + y_offset)

    # Create a tooltip element dynamically using JavaScript
    driver.execute_script('''
        var tooltip = document.createElement('div');
        tooltip.className = 'tooltip';
        tooltip.textContent = arguments[0];
        tooltip.style.position = 'absolute';
        tooltip.style.top = arguments[1] + 'px';
        tooltip.style.left = arguments[2] + 'px';
        document.body.appendChild(tooltip);
    ''', tooltip_text, y, x)
    