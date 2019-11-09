<template>
    <div id="overlay"><h1 id="overlay-text">*Girls Are Preparing . . .*</h1></div>
</template>

<script>


export default {
    name: 'LoadingOverlay'
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    #overlay {
        position: fixed; /* Sit on top of the page content */
        width: 100%; /* Full width (cover the whole page) */
        height: 100%; /* Full height (cover the whole page) */
        display: none;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: rgba(0,0,0,0.5); /* Black background with opacity */
        z-index: 2; /* Specify a stack order in case you're using a different order for other elements */
        cursor: pointer; /* Add a pointer on hover */
    }

    #overlay-text {
        position: absolute;
        top: 50%;
        left: 50%;
        font-size: 10em;
        margin-top: -1em;
        margin-left: -5em;
        color: pink;
    }
</style>
