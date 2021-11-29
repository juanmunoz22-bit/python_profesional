def make_division_by(n):
    '''
        This closure return a function that returns the division of an x number by n
    '''
    def denominator(x):
        return x/n

    return denominator

def run():
    division_by_6 = make_division_by(6)
    print(division_by_6(24))

if __name__ == '__main__':
    run()