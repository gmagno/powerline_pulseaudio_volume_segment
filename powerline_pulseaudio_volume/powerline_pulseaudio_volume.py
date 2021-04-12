"""Main module."""

import pulsectl


def current_volume(pl, format="墳 {0:2.0f}%"):
    with pulsectl.Pulse("volume") as pulse:
        sinks = pulse.sink_list()
        s = sinks[0]  # catch exception
        vol = pulse.volume_get_all_chans(s)  # normalized volume: [0.0 - 1.0]
        vol_pct = round(vol * 100)
        # pulse.volume_set_all_chans(s, 0.20)

    return [
        {
            "contents": format.format(vol_pct),
            "gradient_level": vol_pct,
            "highlight_groups": [
                "pulse_audio_volume_gradient",
                "pulse_audio_volume",
            ],
            "divider_highlight_group": "background:divider",
        }
    ]


def main():
    print(current_volume(None))


if __name__ == "__main__":
    main()
