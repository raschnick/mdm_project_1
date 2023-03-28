const jsConfetti = new JSConfetti()

if (document.getElementById("result-text").innerHTML === "No Spam") {
    jsConfetti.addConfetti({
        emojis: ['✅', '🦄', '😊'],
        emojiSize: 100,
        confettiNumber: 30,
    })
} else {
    jsConfetti.addConfetti({
        emojis: ['⚠️', '⛔', '☢️'],
        emojiSize: 100,
        confettiNumber: 30,
    })
}


