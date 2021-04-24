class SearchSpotify extends React.Component {
    constructor(props) {
        super(props);
        this.state = {items: [], text: ''};
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    render() {
        return React.createElement(
            "div",
            null,
            React.createElement(
                "h3",
                null,
                "Spotify Search"
            ),

            React.createElement(
                "form",
                {onSubmit: this.handleSubmit},
                React.createElement("input", {
                    onChange: this.handleChange,
                    value: this.state.text
                }),
                React.createElement(
                    "button",
                    {type: "submit"},
                    "Search"
                )
            ),
            React.createElement(TracksList, {items: this.state.items}),
        );
    }

    handleChange(e) {
        this.setState({text: e.target.value.toLowerCase()});
    }

    handleSubmit(e) {
        e.preventDefault();
        fetch(`/api/tracks/${this.state.text}`).then(resp => resp.json()).then(tracks => {
            this.setState(state => ({
                items: tracks,
                text: ''
            }));
        })

        if (this.state.text.length === 0) {
            return;
        }
    }
}

class TracksList extends React.Component {
    render() {
        return React.createElement(
            "table",
            null,
            React.createElement(
                "tbody",
                null,
                React.createElement("tr", null,
                    React.createElement(
                        "th",
                        null,
                        "Artist"
                    ),
                    React.createElement(
                        "th",
                        null,
                        "Track"
                    ),
                    React.createElement(
                        "th",
                        null,
                        "Album Image"
                    ),
                    React.createElement(
                        "th",
                        null,
                        "Preview"
                    ),
                ),
                this.props.items.map(item => React.createElement(
                    "tr",
                    {key: `${item.artist}${item.track}`},
                    React.createElement(
                        "td",
                        null,
                        item.artist
                    ),
                    React.createElement(
                        "td",
                        null,
                        item.track
                    ),
                    React.createElement(
                        "td",
                        null,
                        React.createElement(
                            "img",
                            {src: item.album_image_url}
                        )
                    ),
                    React.createElement(
                        "td",
                        null,
                        React.createElement(
                            "a",
                            {href: item.preview_url, target: "_blank"}
                            , "Play It"
                        )
                    ),
                    )
                )
            )
        );
    }
}

ReactDOM.render(React.createElement(SearchSpotify, null), document.getElementById('spotify-search'));