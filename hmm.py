import hmm as hmm

def vitrebi():
    # Define the model
    model = hmm.Model()

    # Define the states
    model.add_state('Healthy')
    model.add_state('Fever')

    # Define the observations
    model.add_observation('normal')
    model.add_observation('cold')
    model.add_observation('dizzy')

    # Define the start probabilities
    model.set_start_probability('Healthy', 0.6)
    model.set_start_probability('Fever', 0.4)

    # Define the transition probabilities
    model.set_transition_probability('Healthy', 'Healthy', 0.7)
    model.set_transition_probability('Healthy', 'Fever', 0.3)
    model.set_transition_probability('Fever', 'Healthy', 0.4)
    model.set_transition_probability('Fever', 'Fever', 0.6)

    # Define the emission probabilities
    model.set_emission_probability('Healthy', 'normal', 0.5)
    model.set_emission_probability('Healthy', 'cold', 0.4)
    model.set_emission_probability('Healthy', 'dizzy', 0.1)
    model.set_emission_probability('Fever', 'normal', 0.1)
    model.set_emission_probability('Fever', 'cold', 0.3)
    model.set_emission_probability('Fever', 'dizzy', 0.6)

    # Run the Viterbi algorithm
    result = model.viterbi(['normal', 'cold', 'dizzy'])
    print(result)

def baum_welch():
    # Define the model
    model = hmm.Model()

    # Define the states
    model.add_state('Healthy')
    model.add_state('Fever')

    # Define the observations
    model.add_observation('normal')
    model.add_observation('cold')
    model.add_observation('dizzy')

    # Define the start probabilities
    model.set_start_probability('Healthy', 0.6)
    model.set_start_probability('Fever', 0.4)

    # Define the transition probabilities
    model.set_transition_probability('Healthy', 'Healthy', 0.7)
    model.set_transition_probability('Healthy', 'Fever', 0.3)
    model.set_transition_probability('Fever', 'Healthy', 0.4)
    model.set_transition_probability('Fever', 'Fever', 0.6)

    # Define the emission probabilities
    model.set_emission_probability('Healthy', 'normal', 0.5)
    model.set_emission_probability('Healthy', 'cold', 0.4)
    model.set_emission_probability('Healthy', 'dizzy', 0.1)
    model.set_emission_probability('Fever', 'normal', 0.1)
    model.set_emission_probability('Fever', 'cold', 0.3)
    model.set_emission_probability('Fever', 'dizzy', 0.6)

    # Run the Baum-Welch algorithm
    model.baum_welch(['normal', 'cold', 'dizzy'], 10)
    print(model)