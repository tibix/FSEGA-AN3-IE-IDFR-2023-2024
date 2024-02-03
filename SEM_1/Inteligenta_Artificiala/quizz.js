document.addEventListener('DOMContentLoaded', () => {
    const startButton = document.getElementById('start-btn');
    const nextButton = document.getElementById('next-btn');
    const questionContainerElement = document.getElementById('question-container');
    const questionElement = document.getElementById('question');
    const answerButtonsElement = document.getElementById('answer-buttons');
    const resultsElement = document.getElementById('results');
    const quizInfoElement = document.getElementById('quiz-info');

    let shuffledQuestions, currentQuestionIndex;
    let score = 0, totalQuestions;
    let responses = []; // Pentru a stoca răspunsurile greșite

    startButton.addEventListener('click', startGame);
    nextButton.addEventListener('click', nextQuestion);

    function startGame() {
        startButton.style.display = 'none';
        questionContainerElement.style.display = 'block';
        fetch('AI-Grile1.json') // Asigurați-vă că calea este corectă
            .then(response => response.json())
            .then(data => {
                console.log(data);
                shuffledQuestions = data.questions.sort(() => Math.random() - .5);
                totalQuestions = shuffledQuestions.length;
                currentQuestionIndex = 0;
                score = 0;
                responses = []; // Resetăm răspunsurile greșite
                questionContainerElement.style.display = 'block';
                setNextQuestion();
            })
            .catch(error => {
                console.error("Error loading the quiz questions: ", error);
            });
    }

    function setNextQuestion() {
        resetState();
        showQuestion(shuffledQuestions[currentQuestionIndex]);
    }

    function showQuestion(question) {
        quizInfoElement.textContent = `Întrebare ${currentQuestionIndex + 1} / ${totalQuestions}`;
        quizInfoElement.style.display = 'block';
        questionElement.innerText = question.question;
        answerButtonsElement.innerHTML = ''; // Asigură-te că zona de răspunsuri este golită inițial
    
        question.options.forEach((option, index) => {
            const key = Object.keys(option)[0];
            const value = option[key];
    
            const radioInput = document.createElement('input');
            radioInput.type = 'radio';
            radioInput.id = key;
            radioInput.name = 'options';
            radioInput.value = key;
    
            const label = document.createElement('label');
            label.htmlFor = key;
            label.textContent = value;
            label.style.marginLeft = '5px';
    
            // Crează un container pentru fiecare set de input radio și label, folosind Bootstrap pentru a le afișa pe linii separate
            const container = document.createElement('div');
            container.classList.add('form-check', 'mb-2'); // 'mb-2' adaugă un spațiu mic între opțiuni
    
            container.appendChild(radioInput);
            container.appendChild(label);
            answerButtonsElement.appendChild(container);
            radioInput.addEventListener('change', () => handleAnswer(radioInput.value, question.answer));
        });
        nextButton.style.display = 'none'; // Ascunde butonul până când un răspuns este selectat
    }
    

    function handleAnswer(selected, correct) {
        const isCorrect = selected === correct;
        if (isCorrect) {
            score++;
        } else {
            responses.push({
                question: questionElement.innerText,
                givenAnswer: document.querySelector(`label[for="${selected}"]`).textContent,
                correctAnswer: document.querySelector(`label[for="${correct}"]`).textContent
            });
        }
        showNextButton();
    }

    function showNextButton() {
        nextButton.style.display = 'block';
    }

    function nextQuestion() {
        if (currentQuestionIndex < shuffledQuestions.length - 1) {
            currentQuestionIndex++;
            setNextQuestion();
        } else {
            showResults();
        }
    }

    function showResults() {
        questionContainerElement.style.display = 'none';
        nextButton.style.display = 'none';
        quizInfoElement.style.display = 'none';
        finalScore = score * (9 / totalQuestions);
        finalFinalSore = finalScore.toFixed(2)
        let resultsHTML = `<h3>Quiz finalizat! Scorul tău este: ${score} / ${totalQuestions} (${finalScore} / 9)</h3>`;
        if (responses.length > 0) {
            resultsHTML += '<h4>Ai răspuns greșit la următoarele întrebări:</h4>';
            responses.forEach((response, index) => {
                resultsHTML += `<p>${index + 1}. ${response.question}<br>Răspunsul tău: ${response.givenAnswer}<br>Răspuns corect: ${response.correctAnswer}</p>`;
            });
        }
    
        // Adaugă butonul de "Reia Quiz-ul" la sfârșitul rezultatelor
        resultsHTML += '<button id="restart-btn" class="btn btn-primary mt-3">Reia Quiz-ul</button>';
        
        resultsElement.innerHTML = resultsHTML;
        resultsElement.style.display = 'block';
    
        // Adaugă event listener pentru butonul de restart pentru a reîncărca pagina
        document.getElementById('restart-btn').addEventListener('click', () => window.location.reload());
    }
    

    function resetState() {
        while (answerButtonsElement.firstChild) {
            answerButtonsElement.removeChild(answerButtonsElement.firstChild);
        }
        nextButton.style.display = 'none';
    }
});
