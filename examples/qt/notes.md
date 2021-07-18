## QT Examples
A registry of self contained PyQt examples.

## Some QT Stuff
- All QT apps require one (exactly) one instance of QApplication 
- app.exec() will run the app until the user closes it 
- Everything in a PyQt app is a widget, some widgets are:
    - Button
    - Label
    - Window
    - Dialog
    - Progress bar, etc.
- Widgets are often nested, like in HTML
    - Window -> Button -> Label is an example 
- Layouts exist
    - QVBoxLayout used to stack widgets vertically
    - There are other layout 
- Changing the overall app/widget styling 
    - No reason for us to use anything other than the default windows widgets
    - Other options include windows vista, and fusion 
- Changing the theme (Dark mode??)
    - Can use QPalette and app.setPalette(...)
    - Can define the style individually for each widget in a palette and then apply it
    - We can have a dark palette and a light palette
- Stylesheets
    - Can also use a Qt equivalent of css
    - Can be used to apply margins, positions and other things to widgets
    - I probably will not use them tbh

## Signals and Slots
Signals are a mechanism to let you react to events such as the user clicking a button. An example of a signal for a button is "clicked". We create a slot for signal, and pass it a function. In python, this is pretty straightforward and we can use any function (not too sure about member functions and binding and whatnot though)

## Resources
Documentation
- Python: https://www.riverbankcomputing.com/static/Docs/PyQt5/index.html
- C++: https://doc.qt.io/qt.html

Articles
- https://build-system.fman.io/pyqt5-tutorial
