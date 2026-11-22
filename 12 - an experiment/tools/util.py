from psychopy import core, gui

def getID():
    info = {'Participant ID': ''}
    dlg = gui.DlgFromDict(dictionary=info, title='Orientation experiment')
    if dlg.OK:
        return info['Participant ID']
    else:
        core.quit()
