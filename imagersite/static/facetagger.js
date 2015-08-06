var FaceTagger =
    {
        init: function(options)
        {
            FaceTagger.options = options;
            $(document).on("click", ".facelabel", FaceTagger.changeName);
        },
        make: function(face)
        {
            // make box -- ideally we'd use a proper JavaScript templating solution, like Mustache
            var tagger = $("<div class='facelabel'><div class='border'></div><div class='name'></div></div>");
            tagger.attr("id", "facelabel-" + face.id);
            tagger.attr("data-id", face.id);
            tagger.find(".name").html(face.name);
            // set coords
            tagger.css("left", face.x * FaceTagger.options.newWidth / FaceTagger.options.originalWidth);
            tagger.css("top", face.y * FaceTagger.options.newHeight / FaceTagger.options.originalHeight);
            tagger.find(".border").css("width", face.width * FaceTagger.options.newWidth / FaceTagger.options.originalWidth);
            tagger.find(".border").css("height", face.height * FaceTagger.options.newHeight / FaceTagger.options.originalHeight);
            // add it!
            $(FaceTagger.options.container).append(tagger);
        },
        changeName: function(e)
        {
            var face = $(e.toElement).parent();
            var name = face.find(".name").text();
            swal({
                title: "Name That Face",
                type: "input",
                animation: "slide-from-top",
                inputPlaceholder: "Name goes here",
                inputValue: name
                }, function(inputValue) {
                    FaceTagger.saveName(face, inputValue);
            });
        },
        saveName: function(face, name)
        {
            var id = face.attr("data-id");
            face.find(".name").html(name);
            $.ajax({
                type: "POST",
                url: FaceTagger.options.labelUrl,
                data: {id: id, name: name, csrfmiddlewaretoken: FaceTagger.options.csrf},
                success: function(result) {
                    console.log("Saved.");
                }
        });
    }
}