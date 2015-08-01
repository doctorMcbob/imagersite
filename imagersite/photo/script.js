<script type="text/javescript">
    FaceTagger.init({
        container: "#photo-container",
        labelUrl: "{{photo.id}}/faces",
        csfr: "{{csrf_token}}",
        originalWidth: {{photo.image.width}},
        originalHeight: {{photo.image.height}},
        newWidth: $("#photo-container img").width(),
        newHeight: $("#photo-container img").height(),
    });

//optical character reg
    {% for f in faces %}

        var face = {
            id: {{{f.id}}}
            name: "{{f.name}}"
        }
        
</script>