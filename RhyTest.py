#Rhythm Tester

import time

def Rhythm_Tester():

    def Playing():
             
        speed = 0
        rounds = 0
        
        print('\nWelcome to Rhythm Tester')
        print('This program will test your rhythm - how consistent are YOU!')
        
        while True: 
            try:
                speed = int(input('Choose rhythm speed (1, 2 or 3): '))
                if speed != 3 and speed != 2 and speed != 1:
                    raise SpeedError
                else:
                    while True:
                        try:
                            rounds = int(input('Choose number of rounds (5 to 50): '))
                            if rounds < 5 or rounds > 50:
                                raise RoundsError
                            else:
                                print(f'\nOkay, this test will last {rounds} rounds and you are aiming  for a {speed} second rhythm.')
                                return speed,rounds
                        except Exception:
                            print('Invalid choice. Enter a number from 5 to 50.')
            except Exception:
                print('Invalid choice. Enter 1, 2 or 3.')
                

    def Results(speed,rounds):

        input('Press Enter to begin!')
        StartingTime = time.time()
        AllResponse = []
        
        for i in range(1,rounds+1):
            
            input(f'\nRound {i} of {rounds}')
            currentTime = time.time() 
            Response = currentTime - StartingTime
            AllResponse.append(Response)
            print(f'{Response:.2f}s - {(rate_rhythm(speed,Response))} ')
            StartingTime = currentTime

        input('\n\nTest Complete!  Press Enter to see your results.')
        print('\nResults:')
        print(f' Fastest Response: {min(AllResponse):.2f}s ({(rate_rhythm(speed,min(AllResponse)))})')
        print(f' Average Response: {(sum(AllResponse) / rounds):.2f}s ({(rate_rhythm(speed,(sum(AllResponse) / rounds)))})')
        print(f' Slowest Response: {max(AllResponse):.2f}s ({(rate_rhythm(speed,max(AllResponse)))})')

        print(f'\n Round  Response  Difference\n -----  --------  ----------')

        speedstr = ['1.00','2.00','3,00']
        
        for i in range(1,rounds+1):            
            if str(abs(round(AllResponse[i-1],2))) + '0' in speedstr:
                stat = 'Spot on!.'            
            elif AllResponse[i-1]-speed > 0:
                stat = 'late.'
            else:
                stat = 'early.'
                
            print(f' {i:<2}     {AllResponse[i-1]:.2f}s     {abs(AllResponse[i-1]-speed):.2f}s {stat}')

       
    def rate_rhythm(target_time,actual_time):
        
        Difference = (abs((actual_time - target_time) / target_time) * 100)
        speedstr = f'{str(target_time) + '.' + '0' + '0'}'
        SpotOn = f"{actual_time:.2f}"
        
        if len(SpotOn) > 4:
            return 'Miss!'
        if int(SpotOn[0]) == int(speedstr[0]) and int(SpotOn[2]) == int(speedstr[2]) and int(SpotOn[3]) == int(speedstr[3]):
            return 'Spot on!'
        elif Difference <= 8:        
            return 'Great!'
        elif Difference <= 16:
            return 'Okay!' 
        else:
            return 'Miss!'

    def Continue():
        
        print('\n')
        while True:
            try:
                yn = str(input('Would you like to play again (y or n) : ')).strip().lower()
                if yn != 'y' and yn != 'n':
                    print('Invalid choice.')
                else:
                    return yn
            except Exception:
                pass


    #Main Program
            
    while True:
        
        speed,rounds = Playing()
        Results(speed,rounds)
        if Continue() == 'y':
            pass
        else:
            print('End of program.')
            break


Rhythm_Tester()
