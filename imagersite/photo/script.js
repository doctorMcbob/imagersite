<script type="text/javescript">
    FaceTagger.init({
        container: "#photo-container",
        labelUrl: "{{photo.id}}/faces",
        csfr: "{{csrf_token}}",
        originalWidth: {{photo.image.width}},
        originalHeight: {{photo.image.height}},
        newWidth: $("#photo-container img").width(),
        



        pass
    });

//optical character reg

</script>