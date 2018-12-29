from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json
import os

from PyInquirer import style_from_dict, Token, prompt, Separator
from pprint import pprint
from pyfiglet import Figlet

style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})

text = Figlet(font='lean')
pprint(text.renderText('Tulu'))

questions = [
    {
        'type': 'checkbox',
        'message': 'Select Function',
        'name': 'function',
        'choices': [
            Separator('= The Git ='),
            {
                'name': 'add',
            },
            {
                'name': 'commit',

            },
            {
                'name': 'push',
            },
            {
                'name': 'pull',
            }
        ],
        'validate': lambda answer: 'You must choose at least one config.' \
            if len(answer) == 0 else True
    }
]
answers = prompt(questions, style=style)
config = answers['function']

def luffy(spell):
    os.system(spell)

def cody():
    pprint("commit message: ")
    message = input()
    if message != 'q':
        spell = 'git commit -m '+ f'"{message}"'
        luffy(spell)

def ada():
    spell = 'git add .'
    luffy(spell)

def pupper():
    pprint("repo name")
    repo = input()
    if repo != 'q':
        spell = 'git push ' + f'"{repo}"' + ' master'
        luffy(spell)

def kyle():
    repo = input()
    spell = 'git pull ' + repo + ' master'
    luffy(spell)

if 'add' in config:
    ada()
if 'commit' in config:
    cody()
if 'push' in config:
    pupper()
if 'pull' in config:
    kyle()
    

#os.system("git status")