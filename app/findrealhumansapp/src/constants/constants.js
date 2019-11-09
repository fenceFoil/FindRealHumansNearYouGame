export const REST_BASE = 'http://44.224.175.124'

export const OVERLAY_CONTROL = {
    ON: function() {
        document.getElementById("overlay").style.display = "block";
    },

    off: function() {
        document.getElementById("overlay").style.display = "none";
    }
}