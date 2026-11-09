"""Tests for camera capability and nodedef selection."""

from utils.camera_caps import (
    NODEDEF_AI,
    NODEDEF_AI_AUDIO,
    NODEDEF_DETECT,
    NODEDEF_DOORBELL,
    camera_is_doorbell,
    camera_nodedef_for,
    camera_supports_smart_type,
)


def test_basic_detect_camera():
    cam = {
        'featureFlags': {
            'smartDetectTypes': ['person', 'vehicle'],
        },
    }
    assert camera_nodedef_for(cam) == NODEDEF_DETECT


def test_ai_camera_with_face():
    cam = {
        'featureFlags': {
            'smartDetectTypes': ['person', 'face'],
        },
    }
    assert camera_nodedef_for(cam) == NODEDEF_AI


def test_ai_audio_camera():
    cam = {
        'featureFlags': {
            'smartDetectTypes': ['person'],
            'smartDetectAudioTypes': ['smoke'],
        },
    }
    assert camera_nodedef_for(cam) == NODEDEF_AI_AUDIO


def test_doorbell_camera():
    cam = {
        'featureFlags': {
            'isDoorbell': True,
            'smartDetectTypes': ['person'],
        },
    }
    assert camera_nodedef_for(cam) == NODEDEF_DOORBELL


def test_g6_pro_entry_public_api_payload():
    """G6 Entry on public API: no isDoorbell, hasPackageCamera + G6 Entry type."""
    cam = {
        'name': 'Jenkins G6 Pro Entry',
        'type': 'UVC G6 Pro Entry',
        'hasPackageCamera': True,
        'featureFlags': {
            'smartDetectTypes': [
                'person', 'vehicle', 'animal', 'package', 'face', 'licensePlate',
            ],
            'smartDetectAudioTypes': ['alrmSmoke', 'alrmSiren'],
        },
    }
    assert camera_is_doorbell(cam)
    assert camera_nodedef_for(cam) == NODEDEF_DOORBELL


def test_g4_doorbell_lite_by_type_only():
    cam = {
        'type': 'UVC G4 Doorbell Lite',
        'featureFlags': {'smartDetectTypes': ['person']},
    }
    assert camera_is_doorbell(cam)
    assert camera_nodedef_for(cam) == NODEDEF_DOORBELL


def test_doorbell_supports_ring_not_in_smart_detect_types():
    """Ring is an event type, not listed in featureFlags.smartDetectTypes."""
    cam = {
        'type': 'UVC G6 Pro Entry',
        'hasPackageCamera': True,
        'featureFlags': {'smartDetectTypes': ['person', 'face']},
    }
    assert camera_supports_smart_type(cam, 'ring')
    assert camera_supports_smart_type(cam, 'person')


def test_supports_line_crossing():
    cam = {'featureFlags': {'hasLineCrossing': True}}
    assert camera_supports_smart_type(cam, 'line')
    assert camera_nodedef_for(cam) == NODEDEF_AI


def test_line_events_allowed_when_public_api_omits_flag():
    """Public Integration API strips hasLineCrossing from featureFlags."""
    cam = {
        'featureFlags': {
            'smartDetectTypes': ['person', 'face'],
        },
    }
    assert camera_supports_smart_type(cam, 'line')
    assert camera_supports_smart_type(cam, 'person')
