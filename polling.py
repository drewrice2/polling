######################################################################
#                                                                    #
#                   Basic Python polling object                      #
#                                                                    #
######################################################################

class Poll(object):

    def __init__(self, poll_options):
        '''
        INPUT:  List of voting options

        Initializes the poll.
        Converts the list items to strings. Raises ValueError if no options provided.

        TODO: limit both the number of poll_options, length of option strings
        '''
        self.poll_options = [str(k) for k in poll_options]
        if poll_options:
            self.poll_options = list(self.poll_options)
            self.poll_options_dict = {k:0 for k in self.poll_options}
        else:
            raise ValueError('No voting options provided.')

    def vote(self, selection):
        '''
        INPUT: option to vote for

        Votes for the given selection.
        Type checks the selection, converts to string. Adjusts the values in the options dictionary.
        If the option doesn't exist, fail silently.
        '''
        if type(selection) != str:
            selection = str(selection)
        if selection in self.poll_options:
            self.poll_options_dict[selection] += 1

if __name__ == '__main__':
    poll = Poll(['bap','boop','42','blah-blah-blah'])
    poll.vote('42')
    poll.vote('42')
    print poll.poll_options_dict
