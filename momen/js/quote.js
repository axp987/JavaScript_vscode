const quotes = [
    {
        quote: "Tis better to have loved and lost, than never to have loved at all",
        author: "Alfred, Lord Tennyson",
    },
    {
        quote: "There is always some madness in love. But there is also always some reason in madness.",
        author: "Friedrich Nietzsche",
    },
    {
        quote: "Love, free as air at sight of human ties, Spreads his light wings, and in a moment flies.",
        author: "Alexander Pope",
    },
];

const quote = document.querySelector("#quote span:first-child");
const author = document.querySelector("#quote span:last-child");

const todayQuotes = quotes[Math.floor(Math.random() * quotes.length)];

quote.innerText = `${todayQuotes.quote}`;
author.innerText = `${todayQuotes.author}`;