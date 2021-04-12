#!/usr/bin/env python

"""Tests for `powerline_pulseaudio_volume` package."""

from powerline_pulseaudio_volume import powerline_pulseaudio_volume


def test_current_volume():
    powerline_pulseaudio_volume.current_volume(None)
