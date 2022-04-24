from asyncio.windows_events import NULL

import PySimpleGUI as sg
import sql as cn


def Search_Window():
    layout_Search = [
        [sg.Text("?איזה זוג נעליים תרצה למצוא", size=(25, 2), font=('Arial', 15))],
        [sg.Input(size=(10, 4)), sg.Text(':מספר דגם*', font=('Arial', 12))],
        [sg.Listbox([36, 36.5, 37, 37.5, 38, 38.5, 39, 39.5, 40, 40.5, 41, 41.5,
                     42, 42.5, 43, 43.5, 44, 44.5, 45, 45.5, 46, 46.5, 47, 47.5, 48],
                    size=(7, 7)), sg.Text(':מידה', font=('Arial', 12))],
        [sg.Listbox(["אדום", "שחור", "לבן", "ירוק", "אפור", "חום", "כחול", "צבעוני"],
                    size=(10, 4)), sg.Text(':צבע', font=('Arial', 12))],
        [sg.Button(button_text="אישור", size=(6, 2), pad=(10, 20), button_color="green"),
         sg.Button(button_text="ביטול", size=(6, 2), pad=(10, 20), button_color="red")]
    ]

    SearchWindow = sg.Window("חיפוש", layout_Search, element_justification='center', margins=(100, 50))

    while True:
        event_Search, values_Search = SearchWindow.read()
        if event_Search in (sg.WIN_CLOSED, 'ביטול'):
            break
        # if the user did not input any model
        elif values_Search[0] == "":
            layout_error = [
                [sg.Text("שגיאה! חובה להזין מספר דגם", size=(20, 2), text_color="black", font=('Arial', 14))],
                [sg.Button(button_text="אישור", size=(5, 1), pad=(10, 20), button_color="grey")]]
            ErrorWindow = sg.Window("!שגיאה", layout_error, element_justification='center', margins=(50, 25))
            while True:
                event_error, values_error = ErrorWindow.read()
                if event_error in (sg.WIN_CLOSED, "אישור"):
                    break
            ErrorWindow.close()
        elif event_Search == "אישור":
            cn.search_sql(values_Search[0], values_Search[1], values_Search[2])
    SearchWindow.close()


def Add_Window():
    layout_Add = [
        [sg.Text("?איזה זוג נעליים תרצה להוסיף למלאי", size=(25, 2), font=('Arial', 15))],
        [sg.Input(size=(10, 4), key="MODEL"), sg.Text(':מספר דגם*', font=('Arial', 12))],
        [sg.Listbox(["אדום", "שחור", "לבן", "ירוק", "אפור", "חום", "כחול", "צבעוני"],
                    size=(10, 4), key="COLOR"), sg.Text(':צבע*', font=('Arial', 12))],
        [sg.Listbox([1, 2], size=(10, 4), key="FLOOR"), sg.Text(':קומה*', font=('Arial', 12))],
        [sg.Listbox(["חורף", "קיץ", "סתיו", "אביב"],
                    size=(10, 4), key="SEASON"), sg.Text(':עונה', font=('Arial', 12))],
        [sg.Button(button_text="אישור", size=(6, 2), pad=(10, 20), button_color="green"),
         sg.Button(button_text="ביטול", size=(6, 2), pad=(10, 20), button_color="red")]
    ]

    AddWindow = sg.Window("הוספה", layout_Add, element_justification='center', margins=(100, 50))

    while True:
        event_Add, values_Add = AddWindow.read()
        if event_Add in (sg.WIN_CLOSED, 'ביטול'):
            break

        # if the user did not input model/size/floor -- ERROR WINDOW
        elif values_Add['MODEL'] == "" or values_Add['COLOR'] == [] or values_Add['FLOOR'] == []:
            layout_Error = [[sg.Text("שגיאה! פרטים חסרים", size=(20, 2), text_color="black", font=('Arial', 15))],
                            [sg.Button(button_text="אישור", size=(5, 1), pad=(10, 20), button_color="grey")]]
            ErrorWindow = sg.Window("!שגיאה", layout_Error, element_justification='center', margins=(50, 25))
            while True:
                event_Error, values_Error = ErrorWindow.read()
                if event_Error in (sg.WIN_CLOSED, "אישור"):
                    break
            ErrorWindow.close()
        elif event_Add == "אישור":
            if values_Add['SEASON'] == []:
                values_Add['SEASON'].append(NULL)
            cn.Add_sql(values_Add['MODEL'], values_Add['COLOR'][0], values_Add['FLOOR'][0], values_Add['SEASON'][0])
    AddWindow.close()


layout = [[sg.Button("חיפוש", size=(12, 3)), sg.Button("רכישה", size=(12, 3))],
          [sg.Button("הוספה", size=(12, 3)), sg.Button("עדכון", size=(12, 3))],
          [sg.Button("קופה יומית", size=(26, 2), button_color="green")]]

# Create the window (Home page)
window = sg.Window("San diego Shoes", layout, margins=(250, 150))

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == sg.WIN_CLOSED:
        break
    elif event == "חיפוש":
        Search_Window()
    elif event == "הוספה":
        Add_Window()

window.close()
