class MatesWidget():
    """
    An enumerated class to represent all possible widget types within the BBM ecosystem

    Attributes
    ----------
    MATES_LED - int
        - corresponds to LED widget

    MATES_RULER_GAUGE - int
        - corresponds to Ruler Gauge widget

    MATES_ANGULAR_METER - int
        - corresponds to Angular Meter widget

    MATES_GAUGE_A - int
        - corresponds to Gauge A widget

    MATES_GAUGE_B - int
        - corresponds to Gauge B widget

    MATES_LED_DIGITS - int
        - corresponds to LED Digits widget

    MATES_LABELS - int
        - corresponds to Label widget

    MATES_BUTTON_A - int
        - corresponds to Button A widget

    MATES_SWITCH_A - int
        - corresponds to Switch A widget

    MATES_SLIDER_B - int
        - corresponds to Slider B widget

    MATES_KNOB - int
        - corresponds to Knob widget

    MATES_MEDIA_LED - int
        - corresponds to Media LED widget

    MATES_MEDIA_COLOR_LED - int
        - corresponds to Color LED widget

    MATES_GAUGE_C - int
        - corresponds to Gauge C widget

    MATES_GAUGE_D - int
        - corresponds to Gauge D widget

    MATES_GAUGE_E - int
        - corresponds to Gauge E widget

    MATES_GAUGE_F - int
        - corresponds to Gauge F widget

    MATES_MEDIA_GAUGE_A - int
        - corresponds to Media Gauge A widget

    MATES_MEDIA_GAUGE_B - int
        - corresponds to Media Gauge B widget

    MATES_MEDIA_GAUGE_C - int
        - corresponds to Media Gauge C widget

    MATES_MEDIA_GAUGE_D - int
        - corresponds to Media Gauge D widget

    MATES_MEDIA_THERMOMETER - int
        - corresponds to Media Thermometer widget

    MATES_LED_SPECTRUM - int
        - corresponds to LED Spectrum widget

    MATES_MEDIA_SPECTRUM - int
        - corresponds to Media Spectrum widget

    MATES_SCOPE - int
        - corresponds to Scope widget

    MATES_SYMBOLS - int
        - corresponds to Symbols widget

    MATES_ROTARY_GAUGE - int
        - corresponds to Rotary Gauge widget

    MATES_BUTTON_B - int
        - corresponds to Button B widget

    MATES_SWITCH_B - int
        - corresponds to Switch B widget

    MATES_MEDIA_BUTTON - int
        - corresponds to Media Button widget

    MATES_SLIDER_A - int
        - corresponds to Slider A widget

    MATES_SLIDER_C - int
        - corresponds to Slider C widget

    MATES_SLIDER_D - int
        - corresponds to Slider D widget

    MATES_SLIDER_E - int
        - corresponds to Slider E widget

    MATES_SLIDER_F - int
        - corresponds to Slider F widget

    MATES_MEDIA_SLIDER - int
        - corresponds to Media Slider widget

    MATES_MEDIA_ROTARY - int
        - corresponds to Media Rotary widget

    MATES_SLIDE_SHOW - int
        - corresponds to Slideshow widget

    MATES_ANIMATION - int
        - corresponds to Animation widget

    MATES_FANCY_LED_A - int
        - corresponds to Fancy LED A widget

    MATES_FANCY_LED_B - int
        - corresponds to Fancy LED B widget

    MATES_FANCY_BUTTON_A - int
        - corresponds to Fancy Button A widget

    MATES_FANCY_BUTTON_B - int
        - corresponds to Fancy Button B widget

    """
    MATES_LED = 0
    MATES_RULER_GAUGE = 1
    MATES_ANGULAR_METER = 2
    MATES_GAUGE_A = 3
    MATES_GAUGE_B = 4
    MATES_LED_DIGITS = 5
    MATES_LABELS = 6
    MATES_BUTTON_A = 32
    MATES_SWITCH_A = 33
    MATES_SLIDER_B = 34
    MATES_KNOB = 35
    MATES_MEDIA_LED = 64
    MATES_MEDIA_COLOR_LED = 65
    MATES_GAUGE_C = 66
    MATES_GAUGE_D = 67
    MATES_GAUGE_E = 68
    MATES_GAUGE_F = 69
    MATES_MEDIA_GAUGE_A = 70
    MATES_MEDIA_GAUGE_B = 71
    MATES_MEDIA_GAUGE_C = 72
    MATES_MEDIA_GAUGE_D = 73
    MATES_MEDIA_THERMOMETER = 74
    MATES_LED_SPECTRUM = 75
    MATES_MEDIA_SPECTRUM = 76
    MATES_SCOPE = 77
    MATES_SYMBOLS = 78
    MATES_ROTARY_GAUGE = 79
    MATES_BUTTON_B = 96
    MATES_SWITCH_B = 97
    MATES_MEDIA_BUTTON = 98
    MATES_SLIDER_A = 99
    MATES_SLIDER_C = 100
    MATES_SLIDER_D = 101
    MATES_SLIDER_E = 102
    MATES_SLIDER_F = 103
    MATES_MEDIA_SLIDER = 104
    MATES_MEDIA_ROTARY = 105
    MATES_SLIDE_SHOW = 128
    MATES_ANIMATION = 129
    MATES_FANCY_LED_A = 130
    MATES_FANCY_LED_B = 131
    MATES_FANCY_BUTTON_A = 160
    MATES_FANCY_BUTTON_B = 161


class MatesParamsLed():
    MATES_LED_BEZEL_COLOR_A = 4
    MATES_LED_BEZEL_COLOR_B = 5
    MATES_LED_LED_COLOR_ON = 7
    MATES_LED_LED_COLOR_OFF = 8
    MATES_LED_SHINE_COLOR = 6

class MatesParamRulerGauge():
    MATES_RULER_GAUGE_BACKGROUND_COLOR = 11
    MATES_RULER_GAUGE_PARTITION_1_COLOR = 12
    MATES_RULER_GAUGE_PARTITION_2_COLOR = 13
    MATES_RULER_GAUGE_PARTITION_3_COLOR = 14
    MATES_RULER_GAUGE_TICK_COLOR = 15

class MatesParamAngularMeter():
    MATES_ANGULAR_METER_BACKGROUND_COLOR = 11
    MATES_ANGULAR_METER_SCALE_SECTION_1_COLOR = 12
    MATES_ANGULAR_METER_SCALE_SECTION_2_COLOR = 13
    MATES_ANGULAR_METER_SCALE_SECTION_3_COLOR = 14
    MATES_ANGULAR_METER_TICK_COLOR = 9
    MATES_ANGULAR_METER_LABEL_COLOR = 18
    MATES_ANGULAR_METER_NEEDLE_COLOR = 43
    MATES_ANGULAR_METER_NEEDLE_PIN_COLOR = 45
    MATES_ANGULAR_METER_NEEDLE_PIN_DOT_COLOR = 47
    MATES_ANGULAR_METER_CAPTION_COLOR = 23

class MatesParamGaugeA():
    MATES_GAUGE_A_BASE_COLOR = 9
    MATES_GAUGE_A_PARTITION_1_INACTIVE_COLOR = 10
    MATES_GAUGE_A_PARTITION_1_ACTIVE_COLOR = 11
    MATES_GAUGE_A_PARTITION_2_INACTIVE_COLOR = 12
    MATES_GAUGE_A_PARTITION_2_ACTIVE_COLOR = 13
    MATES_GAUGE_A_PARTITION_3_INACTIVE_COLOR = 14
    MATES_GAUGE_A_PARTITION_3_ACTIVE_COLOR = 15

class MatesParamGaugeB():
    MATES_GAUGE_B_BACKGROUND_COLOR = 7
    MATES_GAUGE_B_TRACK_FILL_COLOR_A = 9
    MATES_GAUGE_B_TRACK_FILL_COLOR_B = 8
    MATES_GAUGE_B_MAJOR_TICK_COLOR = 15
    MATES_GAUGE_B_MINOR_TICK_COLOR = 15
    MATES_GAUGE_B_FONT_COLOR = 17

class MatesParamLedDigits():
    MATES_LED_DIGITS_SEGMENT_COLOR_ON = 8
    MATES_LED_DIGITS_SEGMENT_COLOR_OFF = 9

class MatesParamLabels():
    MATES_LABELS_FOREGROUND_COLOR = 5
    MATES_LABELS_BACKGROUND_COLOR = 6

class MatesParamButtonA():
    MATES_BUTTON_A_BASE_COLOR_A = 3
    MATES_BUTTON_A_BASE_COLOR_B = 4
    MATES_BUTTON_A_RING_COLOR_OFF = 6
    MATES_BUTTON_A_RING_COLOR_ON = 7
    MATES_BUTTON_A_BUTTON_COLOR_A = 8
    MATES_BUTTON_A_BUTTON_COLOR_B = 9
    MATES_BUTTON_A_FACE_COLOR = 12
    MATES_BUTTON_A_CAPTION_COLOR_OFF = 14
    MATES_BUTTON_A_CAPTION_COLOR_ON = 15
    MATES_BUTTON_A_DOT_COLOR_A = 14
    MATES_BUTTON_A_DOT_COLOR_B = 15

class MatesParamSwitchA():
    MATES_SWITCH_A_BEVEL_MAIN_COLOR = 5
    MATES_SWITCH_A_BEVEL_SHADOW_COLOR = 6
    MATES_SWITCH_A_TRACK_COLOR_ON = 9
    MATES_SWITCH_A_TRACK_COLOR_OFF = 10
    MATES_SWITCH_A_LABEL_COLOR_ON = 15
    MATES_SWITCH_A_LABEL_COLOR_OFF = 16

class MatesParamSliderB():
    MATES_SLIDER_B_BACKGROUND_COLOR = 7
    MATES_SLIDER_B_TRACK_FILL_COLOR_A = 9
    MATES_SLIDER_B_TRACK_FILL_COLOR_B = 8
    MATES_SLIDER_B_MAJOR_TICK_COLOR = 15
    MATES_SLIDER_B_MINOR_TICK_COLOR = 17
    MATES_SLIDER_B_FONT_COLOR = 19
    MATES_SLIDER_B_KNOB_OUTLINE_COLOR_A = 20
    MATES_SLIDER_B_KNOB_OUTLINE_COLOR_B = 21
    MATES_SLIDER_B_KNOB_FACE_COLOR_A = 23
    MATES_SLIDER_B_KNOB_FACE_COLOR_B = 24

class MatesParamKnob():
    MATES_KNOB_BACKGROUND_COLOR = 11
    MATES_KNOB_KNOB_COLOR = 12
    MATES_KNOB_BEVEL_COLOR_LEFT = 15
    MATES_KNOB_BEVEL_COLOR_RIGHT = 14
    MATES_KNOB_PARTITION_1_INACTIVE_COLOR = 18
    MATES_KNOB_PARTITION_1_ACTIVE_COLOR = 21
    MATES_KNOB_PARTITION_2_INACTIVE_COLOR = 19
    MATES_KNOB_PARTITION_2_ACTIVE_COLOR = 22
    MATES_KNOB_PARTITION_3_INACTIVE_COLOR = 20
    MATES_KNOB_PARTITION_3_ACTIVE_COLOR = 23
    MATES_KNOB_LABEL_COLOR = 30
    MATES_KNOB_CAPTION_COLOR = 36
    MATES_KNOB_POINTER_COLOR = 27

class MatesParamMediaLed():
    MATES_MEDIA_LED_BACKGROUND_COLOR = 8
    MATES_MEDIA_LED_BEVEL_COLOR = 6
    MATES_MEDIA_LED_FACE_COLOR = 7
    MATES_MEDIA_LED_LED_COLOR_ON = 10
    MATES_MEDIA_LED_LED_COLOR_OFF = 9
    MATES_MEDIA_LED_SYMBOL_COLOR = 12

class MatesParamMediaColorLed():
    MATES_MEDIA_COLOR_LED_OUTER_COLOR = 4
    MATES_MEDIA_COLOR_LED_INNER_COLOR = 5

class MatesParamGaugeC():
    MATES_GAUGE_C_BACKGROUND_COLOR = 7
    MATES_GAUGE_C_TRACK_FILL_COLOR_A = 10
    MATES_GAUGE_C_TRACK_FILL_COLOR_B = 9
    MATES_GAUGE_C_TICK_COLOR = 11
    MATES_GAUGE_C_FONT_COLOR = 13

class MatesParamGaugeD():
    MATES_GAUGE_D_BACKGROUND_COLOR = 7
    MATES_GAUGE_D_TRACK_FILL_COLOR_A = 10
    MATES_GAUGE_D_TRACK_FILL_COLOR_B = 9
    MATES_GAUGE_D_TICK_COLOR = 11
    MATES_GAUGE_D_FONT_COLOR = 13

class MatesParamGaugeE():
    MATES_GAUGE_E_BEVEL_COLOR = 7
    MATES_GAUGE_E_TRACK_FILL_COLOR_A = 6
    MATES_GAUGE_E_TRACK_FILL_COLOR_B = 8

class MatesParamGaugeF():
    MATES_GAUGE_F_OUTER_BEVEL_COLOR_A = 6
    MATES_GAUGE_F_OUTER_BEVEL_COLOR_B = 7
    MATES_GAUGE_F_INNER_BEVEL_COLOR_A = 9
    MATES_GAUGE_F_INNER_BEVEL_COLOR_B = 10
    MATES_GAUGE_F_TRACK_FILL_COLOR_A = 13
    MATES_GAUGE_F_TRACK_FILL_COLOR_B = 12

class MatesParamMediaGaugeA():
    MATES_MEDIA_GAUGE_A_BACKGROUND_COLOR = 10
    MATES_MEDIA_GAUGE_A_SCALE_BEVEL_COLOR = 9
    MATES_MEDIA_GAUGE_A_SCALE_BOTTOM_LEFT_FILL_COLOR = 7
    MATES_MEDIA_GAUGE_A_SCALE_TOP_RIGHT_FILL_COLOR = 8

class MatesParamMediaGaugeB():
    MATES_MEDIA_GAUGE_B_NEEDLE_COLOR = 12
    MATES_MEDIA_GAUGE_B_OUTER_BEZEL_COLOR = 4
    MATES_MEDIA_GAUGE_B_INNER_BEZEL_COLOR = 5
    MATES_MEDIA_GAUGE_B_DIAL_COLOR = 6
    MATES_MEDIA_GAUGE_B_SCALE_LOW_COLOR = 13
    MATES_MEDIA_GAUGE_B_SCALE_MEDIUM_COLOR = 14
    MATES_MEDIA_GAUGE_B_SCALE_HIGH_COLOR = 15
    MATES_MEDIA_GAUGE_B_TICK_COLOR = 7
    MATES_MEDIA_GAUGE_B_FONT_COLOR = 8

class MatesParamMediaGaugeC():
    MATES_MEDIA_GAUGE_C_ON_COLOR = 4
    MATES_MEDIA_GAUGE_C_OFF_COLOR = 5

class MatesParamMediaGaugeD():
    MATES_MEDIA_GAUGE_D_ACTIVE_START_COLOR = 4
    MATES_MEDIA_GAUGE_D_ACTIVE_END_COLOR = 5
    MATES_MEDIA_GAUGE_D_INACTIVE_COLOR = 6

class MatesParamMediaThermometer():
    MATES_MEDIA_THERMOMETER_BASE_COLOR = 6
    MATES_MEDIA_THERMOMETER_BULB_COLOR = 7
    MATES_MEDIA_THERMOMETER_FONT_COLOR = 9
    MATES_MEDIA_THERMOMETER_SCALE_TICK_COLOR = 8

class MatesParamLedSpectrum():
    MATES_LED_SPECTRUM_BASE_COLOR = 11
    MATES_LED_SPECTRUM_PARTITION_1_INACTIVE_COLOR = 12
    MATES_LED_SPECTRUM_PARTITION_1_ACTIVE_COLOR = 13
    MATES_LED_SPECTRUM_PARTITION_2_INACTIVE_COLOR = 14
    MATES_LED_SPECTRUM_PARTITION_2_ACTIVE_COLOR = 15
    MATES_LED_SPECTRUM_PARTITION_3_INACTIVE_COLOR = 16
    MATES_LED_SPECTRUM_PARTITION_3_ACTIVE_COLOR = 17

class MatesParamMediaSpectrum():
    MATES_MEDIA_SPECTRUM_ACTIVE_START_COLOR = 6
    MATES_MEDIA_SPECTRUM_ACTIVE_END_COLOR = 7
    MATES_MEDIA_SPECTRUM_INACTIVE_COLOR = 8

class MatesParamButtonB():
    MATES_BUTTON_B_BEVEL_COLOR_A = 5
    MATES_BUTTON_B_BEVEL_COLOR_B = 6
    MATES_BUTTON_B_FACE_ON_COLOR = 9
    MATES_BUTTON_B_FACE_OFF_COLOR_A = 10
    MATES_BUTTON_B_FACE_OFF_COLOR_B = 11
    MATES_BUTTON_B_TEXT_ON_COLOR = 17
    MATES_BUTTON_B_TEXT_OFF_COLOR = 18
    MATES_BUTTON_B_SHINE_COLOR = 13

class MatesParamSwitchB():
    MATES_SWITCH_B_BEVEL_MAIN_COLOR = 5
    MATES_SWITCH_B_BEVEL_SHADOW_COLOR = 10
    MATES_SWITCH_B_LABEL_COLOR_ON = 15
    MATES_SWITCH_B_LABEL_COLOR_OFF = 16

class MatesParamMediaButton():
    MATES_MEDIA_BUTTON_BACKGROUND_COLOR = 8
    MATES_MEDIA_BUTTON_BEVEL_COLOR = 6
    MATES_MEDIA_BUTTON_FACE_COLOR = 7
    MATES_MEDIA_BUTTON_LED_COLOR_ON = 10
    MATES_MEDIA_BUTTON_LED_COLOR_OFF = 9
    MATES_MEDIA_BUTTON_SYMBOL_COLOR = 12

class MatesParamSliderA():
    MATES_SLIDER_A_BACKGROUND_COLOR = 7
    MATES_SLIDER_A_BORDER_COLOR = 8
    MATES_SLIDER_A_LED_OUTLINE_COLOR_A = 15
    MATES_SLIDER_A_LED_OUTLINE_COLOR_B = 16
    MATES_SLIDER_A_LED_ACTIVE_COLOR = 21
    MATES_SLIDER_A_LED_INACTIVE_COLOR_A = 17
    MATES_SLIDER_A_LED_INACTIVE_COLOR_B = 18
    MATES_SLIDER_A_TRACK_OUTLINE_COLOR_A = 9
    MATES_SLIDER_A_TRACK_OUTLINE_COLOR_B = 10
    MATES_SLIDER_A_TRACK_FILL_COLOR_A = 11
    MATES_SLIDER_A_TRACK_FILL_COLOR_B = 12
    MATES_SLIDER_A_KNOB_COLOR_A = 22
    MATES_SLIDER_A_KNOB_COLOR_B = 23
    MATES_SLIDER_A_FONT_COLOR = 26

class MatesParamSliderC():
    MATES_SLIDER_C_BACKGROUND_COLOR = 7
    MATES_SLIDER_C_KNOB_COLOR = 8
    MATES_SLIDER_C_TRACK_FILL_COLOR_A = 10
    MATES_SLIDER_C_TRACK_FILL_COLOR_B = 9
    MATES_SLIDER_C_TICK_COLOR = 11
    MATES_SLIDER_C_FONT_COLOR = 13

class MatesParamSliderD():
    MATES_SLIDER_D_BACKGROUND_COLOR = 7
    MATES_SLIDER_D_KNOB_COLOR = 8
    MATES_SLIDER_D_TRACK_FILL_COLOR_A = 10
    MATES_SLIDER_D_TRACK_FILL_COLOR_B = 9
    MATES_SLIDER_D_TICK_COLOR = 11
    MATES_SLIDER_D_FONT_COLOR = 13

class MatesParamSliderE():
    MATES_SLIDER_E_BEVEL_COLOR = 7
    MATES_SLIDER_E_TRACK_FILL_COLOR_A = 6
    MATES_SLIDER_E_TRACK_FILL_COLOR_B = 8
    MATES_SLIDER_E_KNOB_COLOR = 9

class MatesParamSliderF():
    MATES_SLIDER_F_OUTER_BEVEL_COLOR_A = 6
    MATES_SLIDER_F_OUTER_BEVEL_COLOR_B = 7
    MATES_SLIDER_F_INNER_BEVEL_COLOR_A = 9
    MATES_SLIDER_F_INNER_BEVEL_COLOR_B = 10
    MATES_SLIDER_F_TRACK_FILL_COLOR_A = 13
    MATES_SLIDER_F_TRACK_FILL_COLOR_B = 12
    MATES_SLIDER_F_KNOB_OUTLINE_COLOR_A = 14
    MATES_SLIDER_F_KNOB_OUTLINE_COLOR_B = 15
    MATES_SLIDER_F_KNOB_FACE_COLOR_A = 17
    MATES_SLIDER_F_KNOB_FACE_COLOR_B = 18
    MATES_SLIDER_F_KNOB_DOT_COLOR = 20

class MatesParamMediaSlider():
    MATES_MEDIA_SLIDER_BACKGROUND_COLOR = 10
    MATES_MEDIA_SLIDER_SCALE_BEVEL_COLOR = 9
    MATES_MEDIA_SLIDER_SCALE_BOTTOM_LEFT_FILL_COLOR = 7
    MATES_MEDIA_SLIDER_SCALE_TOP_RIGHT_FILL_COLOR = 8
    MATES_MEDIA_SLIDER_KNOB_BEVEL_COLOR = 6
    MATES_MEDIA_SLIDER_KNOB_CENTER_COLOR = 5

class MatesParamMediaRotary():
    MATES_MEDIA_ROTARY_OUTER_EDGE_COLOR = 5
    MATES_MEDIA_ROTARY_OUTER_RADIUS_COLOR = 6
    MATES_MEDIA_ROTARY_INNER_EDGE_COLOR = 7
    MATES_MEDIA_ROTARY_INNER_RADIUS_COLOR = 8
    MATES_MEDIA_ROTARY_INDICATOR_OUTER_COLOR = 9
    MATES_MEDIA_ROTARY_INDICATOR_INNER_COLOR = 10


def getWidgetId(widget_type: MatesWidget, widget_index: int) -> int:
    """
    Helper function to obtain the ID of a widget based on its index and type.

    Args:

        widget_type: MatesWidget
            the type of the target widget.

        widget_index: int
            the index of the target widget.

    Returns:

        Widget ID from type and index
    """
    return (widget_type << 8) | widget_index