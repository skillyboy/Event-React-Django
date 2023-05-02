const path = require("path")
const css = require("mini-css-extract-plugin")

module.exports = {
    mode: "production",
    entry: path.join(__dirname, "src", "index.tsx"),
    output: {
        path: path.join(__dirname, "static"),
        filename: "React+django.js"
    },
    module: {
        rules: [
            {
                test: /\.(tsx|ts)$/,
                include: path.join(__dirname, "src"),
                use: [
                    'babel-loader',
                    'ts-loader'
                ]
            },
            {
                test: /\.(css|scss)$/,
                use: [
                    css.loader,
                    "css-loader",
                    "postcss-loader",
                    "sass-loader",
                ]
            }
        ]
    },
    resolve: {
        extensions: [".tsx", ".ts", ".js"],
    },
    plugins: [
        new css({
            filename: "React+django.css"
        })
    ]
}