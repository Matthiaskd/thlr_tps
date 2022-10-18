from thlr_automata import *

B=ENFA([0, 1, 2, 3], [0], [2], ["a", "b"], ((0, "a", 1), (0, "b", 2), (3, "a", 2), (2, "b", 2)))

#[Q3]

def get_accessible_states(automaton, origin):
    res=[]
    A=automaton.alphabet
    temp=[]
    for e in A:
        temp=automaton.get_successors(origin, e)
        while(len(temp)!=0):
             res.append(temp.pop())
    return set(res)


#/[Q3]

#[Q4]
def is_accessible(automaton, state):
    alll=automaton.all_states
    for i in alll:
        temp=get_accessible_states(B, i)
        for i in temp:
            if (i==state):
                return True
    return False
#/[Q4]


#[Q5]
def is_co_accessible(automaton, state):
    comp1=automaton.final_states
    comp2=get_accessible_states(automaton, state)

    for i in comp1:
        for j in comp2:
            if (i==j):
                return True
    return False
#/[Q5]

#[Q6]
def is_useful(automaton, state):
    return is_accessible(automaton, state) and is_co_accessible(automaton, state)
#/[Q6]

#[Q7]
def prune(automaton):
    alll=automaton.all_states
    unuseful=[]
    for e in alll:
        if (not is_useful(automaton, e) ):
            unuseful.append(e)
            print(e, is_useful(automaton, e))
    for e in unuseful:
        automaton.remove_state(e)
#/[Q7]
B.export("avant")
prune(B)
B.export("export")
