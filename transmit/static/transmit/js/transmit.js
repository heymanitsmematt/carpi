$(document).ready(function(){
    console.log('ready');
    play = new Player();
    play.sing();
    
    //handle autoplay changes
    $('#autoPlay').click(function(){
        play.autoPlay();
    });
});

function Player(){
    self = this;

    //grab player for easier reference later
    self.player = $('#player');

    //manage playing and changing songs
    self.sing = function() {
        $('.song').click(function() {
            if (this.id != self.player.data('currentlyPlayingID')) { 
                self.player.attr('src','/transmit/play/'+this.id)
                    .data('currentlyPlayingID', this.id);
                self.player[0].play();
            };
        });
    };

    //tuple of song id's for playback and other stuff
    self.songIDs = function() {
        ids = [];
        $('.song').each(function(){
            ids.push(this.id);
        });
        return ids;
    };

    self.autoPlay = function() {
        if ($('#autoPlay')[0].checked) {
            self.player.on('ended', function() {
                newSong = Math.floor(Math.random() * self.songIDs().length);
                self.player.attr('src','/transmit/play/'+newSong)
                    .data('currentPlayingID', newSong);
                self.player[0].play();
            });
        };
    };
};
