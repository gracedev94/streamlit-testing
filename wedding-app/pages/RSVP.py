import streamlit as st
import pandas as pd




columns = ["GuestID", "PartyID", "GuestName", "RSVP"]
data = [["001","001","Jane O'Halloran","Cordially Accepted"],
        ["002","002","David O'Halloran","No Response"],
        ["003","003","Marc O'Halloran","No Response"],
        ["004","003","Neve Carey","No Response"],
        ["005","001","Huw","No Response"],
        ["006","002","Olga","No Response"],
        ["007","004","Magi Farrand","No Response"],
        ["008","005","Lucy Wilkinson","No Response"],
        ["009","005","Ben Rogan","No Response"]]
guests = pd.DataFrame(columns = columns, data = data)

st.text_input("Enter a name from your party:", key="name")
name = st.session_state.name
if name:
    partyid = guests.where(guests['GuestName']==name)['PartyID'][0]
    responses = guests[guests['PartyID']==partyid]['RSVP']
    party_and_responses = guests[guests['PartyID']==partyid][['GuestName','RSVP']]
    responses_list = responses.to_list()
    num_of_responses = len(responses_list)
    no_responses = [x for x in responses_list if x == 'No Response']
    num_of_no_responses = len(no_responses)
    if num_of_responses > num_of_no_responses:
        st.write('One or more people in your party have already submitted a response:')
        party_and_responses
        st.write('If you want to overwrite one or more responses, or you want to provide a response for someone in your party who does not already have a response, click Continue. \n If you want to keep these responses, click Abandon.')
        left,right = st.columns(2)
        with left:
            if st.button('Continue'):
                party = guests[guests['PartyID']==partyid]['GuestName']
                party_list = party.to_list()
                st.write('Select which guests in your party you would like to RSVP for:')
                guests_to_rsvp_for = []
                for guest in party_list:
                    if st.checkbox(guest):
                        guests_to_rsvp_for.append(guest)
                    
                st.write('You are RSVPing for: ' + str(guests_to_rsvp_for))

                if 'next' not in st.session_state:
                    st.session_state['next'] = False
                next = st.button('Next',type='primary')
                
                if next:
                    st.session_state['next'] = True
                if st.session_state['next']:
                    responses = {}
                    for guest in guests_to_rsvp_for:
                        response = st.radio(
                            guest,
                            ('Cordially Accept', 'Regretfully Decline'),key=guest
                        )
                        responses[guest] = response
                        
                    if st.button('Submit',type='primary'):
                        st.write('You have submitted the following RSVPs:')
                        for guest in guests_to_rsvp_for:
                            guests.loc[guests['GuestName']==guest,'RSVP'] = responses[guest]
                            st.write(guest + ': ' + responses[guest])
                        st.write('Thank you for RSVPing!')
                        guests[guests['GuestName'].isin(guests_to_rsvp_for)]
                        st.session_state['next'] = False

            with right:
                if st.button('Abandon'):
                    st.write('You have abandoned your RSVPs. No changes have been made.')
    else:
        party = guests[guests['PartyID']==partyid]['GuestName']
        party_list = party.to_list()
        st.write('Select which guests in your party you would like to RSVP for:')
        guests_to_rsvp_for = []
        for guest in party_list:
            if st.checkbox(guest):
                guests_to_rsvp_for.append(guest)
            
        st.write('You are RSVPing for: ' + str(guests_to_rsvp_for))

        if 'next' not in st.session_state:
            st.session_state['next'] = False
        next = st.button('Next',type='primary')
        
        if next:
            st.session_state['next'] = True
        if st.session_state['next']:
            responses = {}
            for guest in guests_to_rsvp_for:
                response = st.radio(
                    guest,
                    ('Cordially Accept', 'Regretfully Decline'),key=guest
                )
                responses[guest] = response
                
            if st.button('Submit',type='primary'):
                st.write('You have submitted the following RSVPs:')
                for guest in guests_to_rsvp_for:
                    guests.loc[guests['GuestName']==guest,'RSVP'] = responses[guest]
                    st.write(guest + ': ' + responses[guest])
                st.write('Thank you for RSVPing!')
                guests[guests['GuestName'].isin(guests_to_rsvp_for)],
                st.session_state['next'] = False

                




                

            


# Path: wedding-app/pages/RSVP.py