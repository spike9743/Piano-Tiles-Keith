import easygui
from resources import *

from objects import Tile
import gensound
import random

def createTile(win,noteValue,beat,song,measures=None,keyboard=None): #this method is important because it advanctes the beat of the tile
    global tile_height
    #print("In create tile %f" % (Tile.tile_height))
    #print("---")
    #print(beat)
    if measures is not None and keyboard is not None:
        if beat[0] < len(measures) and beat[1]+1 < len(measures[beat[0]].chords):
            note_val = measures[beat[0]].chords[beat[1]+1][0]
            if len(measures[beat[0]].chords[beat[1]+1]) == 1: 
                #print("IN!!! notevalue %f" % (note_val))
                height = note_val * Tile.tile_height
                horizontalPos = random.randint(0,3)
                x = horizontalPos * TILE_WIDTH
                y = -height
                tile = Tile(x,y,height,horizontalPos,beat,get_random_color(),win)
                tile.color = SCREEN_COLOR
                tile.rest = True
                tile.ignore = True
                Tile.next_chord(song)
                return tile
            else:
                #print("IN THE OTHER ONE note value %f" % (note_val))
                height = note_val * Tile.tile_height
                horizontalPos = random.randint(0,3)
                x = horizontalPos * TILE_WIDTH
                y = -height
                Tile.next_chord(song)
                return Tile(x,y,height,horizontalPos,beat,get_random_color(),win)
    #print("IN THE OTHER OTHER ONE note value %f" % (noteValue))
    height = noteValue * Tile.tile_height
    horizontalPos = random.randint(0,3)
    x = horizontalPos * TILE_WIDTH
    y = -height
    Tile.next_chord(song)
    return Tile(x,y,height,horizontalPos,beat,get_random_color(),win)

def produceSound(song,current_chord):
    last_index = len(song.measures[current_chord[0]].chords[current_chord[1]+1])
    chord = song.measures[current_chord[0]].chords[current_chord[1]+1][1:last_index] #we add 1 to current_chord()[1] (which represents the current chord in the current measure) becauase the first value in the array for a measure is a string representing which measure the user is currently at and we dont want that
    duration_in_beats =  song.measures[current_chord[0]].chords[current_chord[1]+1][0] #the 0th index of a chord represents the duration of the chord in beats
    duration_in_seconds = (1 / song.beats_per_second) * duration_in_beats
    duration_in_ms = float(duration_in_seconds * 1000)
    #print("chord %s" % (chord))
    #print("duration in beats %f" % (duration_in_beats))
    sound = gensound.Sawtooth(0,0)
    for note in chord:
        if note:
            sound += gensound.Sawtooth(note,duration_in_ms)
    if len(chord) > 0:
        if chord[0]:
            sound.play(max_amplitude = .1)


def get_tile_speed(bpm,tile_height):
    seconds_in_one_beat = (1/bpm) * 60
    pixel_per_frame = (Tile.tile_height) * (1/FPS) * (1/seconds_in_one_beat)
    return pixel_per_frame

def get_random_color():
    return RAINBOW[random.randint(0,len(RAINBOW)-1)]

def open_JSON_dir():
    return easygui.fileopenbox(msg="Please select a JSON file",default='C:\\Users\\keith\\coding-projects\\Python\\MIDI_To_Piano_Tiles_JSON\\songs\\*.json')

def update_text_on_text_display(text_display,text):
    text_display.text = pygame.font.Font(None,100).render(text,True,BLACK)



def placeholder():
    pass

