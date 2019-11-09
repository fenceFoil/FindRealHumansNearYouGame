export const REST_BASE = 'http://44.224.175.124'

export const OVERLAY_CONTROL = {
    ON: function() {
        document.getElementById("overlay").style.display = "block";
    },

    OFF: function() {
        document.getElementById("overlay").style.display = "none";
    }
}

export const HUD_CONTROL = {
    ON: function() {
        document.getElementById("hud").style.display = "block";
    },

    OFF: function() {
        document.getElementById("hud").style.display = "none";
    }
}