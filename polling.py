class Poll(object):
    def __init__(self, poll_options):
        '''
        INPUT:  List of voting options

        TODO: limit the number of poll options
        '''
        if poll_options:
            self.poll_options = list(poll_options)
            self.poll_options_dict = {k:0 for k in self.poll_options}

    def vote(self, selection):
        '''
        INPUT: option to vote for

        Adjusts the values in the options dictionary
        '''
        if selection in self.poll_options:
            self.poll_options_dict[selection] += 1

if __name__ == '__main__':
    poll = Poll(['option1','option2','42'])
    poll.vote('42')
    poll.vote('42')
    print poll.poll_options_dict
