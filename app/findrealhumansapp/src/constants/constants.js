export const REST_BASE = 'http://44.224.175.124'

export const OVERLAY_CONTROL = {
    ON: function() {
        document.getElementById("overlay").classList.add("fade-enter-active")
    },

    OFF: function() {
        document.getElementById("hud").classList.remove("fade-enter-active")
    }
}

export const HUD_CONTROL = {
    ON: function() {
        let hud = document.getElementById("hud");
        hud.classList.add("fade-enter-active");
    },

    OFF: function() {
        document.getElementById("hud").classList.remove("fade-enter-active")
    }
}