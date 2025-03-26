import vlc
from stations import stations


class radio:
    def __init__(self):
        """Instantiates object with a list of known stations
        and creates VLC media player instance
        """
        radio_stations = stations()
        self._station_names = []

        # Reads all available station names in
        for key in radio_stations.get:
            self._station_names.append(key)

        self._stations = radio_stations.get  # Reads in all station details
        self._target = ''
        self._station = ''
        self._volume = 50

        self._vlc_instance = vlc.Instance('-q')
        self._vlc_player = self._vlc_instance.media_player_new()

    @property
    def tune(self):
        print('a')
        """Prepares for tune to new station and stops current playback
        """
        self._station = ''
        self.stop

    @property
    def play(self):
        """Resumes live playback on a paused connection at current time
        """
        self._vlc_player.play()

    @property
    def pause(self):
        """Pauses connection playback, but doesn't preserve timestamp
        e.g will resume live, not when paused
        """
        self._vlc_player.pause()

    @property
    def stop(self):
        """Completely stops playback and streaming of data
        """
        print('Stopping playback')
        self._vlc_player.stop()

    @property
    def connect(self):
        """Connects to radio stream URL and starts playback
        """
        media = self._vlc_instance.media_new(self._target)
        self._vlc_player.set_media(media)
        self._vlc_player.play()

    @property
    def get_volume(self):
        return self._volume

    @property
    def available_stations(self):
        """Lists available stations
        """
        num = 1
        for s in self._station_names:
            print('   ' + str(num) + '. ' + s)
            num += 1

    def set_volume(self, value: int):
        """Sets playback volume

        Args:
            value: audio level (0-100%)
        """
        if value > 100:
            value = 100
        elif value < 0:
            value = 0

        self._volume = value

        self._vlc_player.audio_set_volume(value)
        self.connect
        return ('Radio volume set to: ' + str(value) + '%')

    @property
    def fine_tune(self):
        """Allows for manual selection of playback URL
        """
        print('Current playback via: ' + self._stat_type)
        print('\nAvailable connections for ' + self._station + ' are:')

        pos = 0
        while pos < len(self._stations[self._station]):
            self._stat_type, self._target = self._stations[self._station][pos]
            print('   ' + str(pos+1) + '. ' + self._stat_type)
            pos += 1

        opt = 0
        while (opt < 1) or (opt > pos):
            opt = int(input('\nSelection: '))

        self._stat_type, self._target = self._stations[self._station][opt-1]

        print()
        self.stop
        self.connect

        print('\nNow playing ' + self._station +
              ', via ' + self._stat_type)

    @property
    def attempt_connect(self):
        """Attempts to connect to radio station via known URL's

        Raises:
            ConnectionError: Raised if current URL doesn't give working playback (based on user response)
        """
        pos = 0
        # Sets no. of connection methods
        max = len(self._stations[self._station])

        while pos < max:
            try:
                # Sets station type and target URL based off name and pos
                self._stat_type, self._target = self._stations[self._station][pos]

                print('Attempting to stream ' +
                      self._station + ', via ' + self._stat_type)

                self.connect

                # Queries user to check if playing
                playing = input('Is it playing? (yes/no): ')

                if playing.lower() not in ['yes', 'y']:
                    print()
                    self.stop
                    raise ConnectionError
                else:
                    break

            except ConnectionError:
                pos += 1
                if pos < max:
                    print('Re-attempting to connect via other URL: \n')
                else:
                    # If all known URL's don't work
                    print('\nAll connections exhausted, radio station unavailable')

        if playing.lower() in ['yes', 'y']:
            print('\nNow playing ' + self._station +
                  ', via ' + self._stat_type)

    @property
    def interface(self):
        """Command based interface for radio control

        Returns:
            Boolean: True if radio should be tuned again
        """
        # Initialises volume to 50
        self.set_volume(self._volume)

        self.attempt_connect
        try:
            command = ''
            commands = ['tune', 'fine tune',
                        'stop', 'resume', 'volume', 'exit']

            while command.lower() != 'exit':
                command = ''

                print('\nOptions:')
                for c in commands:
                    print('• ' + c)

                while command.lower() not in commands:
                    command = input('\nCommand: ')

                if command == 'stop':
                    self.pause
                elif command == 'resume':
                    self.play
                elif command == 'volume':
                    print('\nCurrent volume: ' + str(self.get_volume) + '%')
                    inp = int(input('Please enter volume (0-100): '))
                    print('\n' + self.set_volume(inp))
                elif command == 'tune':
                    print("\nTerminating radio stream\n")
                    self.stop
                    print()
                    self._station = ''
                    return True
                elif command == 'fine tune':
                    print()
                    self.fine_tune

            print("\nTerminating radio stream")
            self.stop
            return False

        except KeyboardInterrupt:
            print("\nTerminating radio stream")
            self.stop

    def main(self):
        """Shell interface that allows for selection of radio station via tune until the user chooses to exit
        """
        run = True
        while run:
            print('Available stations: ')
            self.available_stations

            while (self._station not in self._station_names):
                if self._station.isnumeric():
                    self._station = int(self._station)

                    if (self._station <= len(self._station_names)) and self._station > 0:
                        self._station = self._station_names[self._station-1]
                        break

                self._station = input('Please enter the station to play: ')
            print()

            run = self.interface


radio_instance = radio()
radio_instance.main()
