// episode = {
//     title: "Inside",
//     duration: 87,
//     hasBeenWatched: true,
//     manage: {
//         foo: "Bar",
//         gen: "Too"
//     }
//     }
//     console.log(episode.title);
//     console.log(episode["manage"]["foo"])
//     episode["title"] = "What";

//     console.log(episode["title"]);

class Episode {
    constructor(title, duration, hasBeenWatched) {
    this.title = title;
    this.duration = duration;
    this.hasBeenWatched = hasBeenWatched;
    }
    }
    let firstMovie = new Episode('Inside', 87, true);
    console.log(firstMovie)