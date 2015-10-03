
#include "musicplayer.h" // for Player, used in Fader::wait()
#include "PyThreading.hpp" // used in Fader::wait()

#include <assert.h>
#include "Fader.hpp"



Fader::Fader() {
	cur = limit = 0;
	inc = 0;
}

#define FADE_TIME 50 // in ms

void Fader::change(int8_t _inc, int Samplerate, bool reset) {
	uint16_t newLimit = Samplerate * FADE_TIME / 1000;
	reset = reset && finished();
	uint16_t oldLimit = limit.exchange(newLimit);
	reset = reset || oldLimit != newLimit;
	inc = _inc;
	if(reset) {
		if(_inc >= 0) cur = 0;
		else cur = newLimit;
	}
}

void Fader::finish() {
	if(inc < 0) cur = 0;
	else cur = limit.load();
}

void Fader::wait(PlayerObject* player) {
	// We expect to have the PlayerObject lock here.
	while(!finished()) {
		PyScopedUnlock(player->lock);
		usleep(10000);
	}
}

