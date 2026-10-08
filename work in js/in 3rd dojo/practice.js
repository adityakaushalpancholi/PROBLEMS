/*
 * Module 2 Practice Assessment — Task Tracker data utilities
 * ------------------------------------------------------------------
 * Implement the 10 functions below. Each one is checked by a Jasmine
 * spec in tests/FunctionsTest.js (10 specs x 2 marks = 20).
 *
 * A "task" is a plain object shaped like:
 *   { title: "Buy milk", status: "todo", done: false, priority: "high" }
 *
 * Rules:
 *   - Do NOT rename the functions and do NOT change their parameters.
 *   - Do NOT edit index.html, main.css, or tests/FunctionsTest.js.
 *   - Keep each function pure: return a value, do not print or mutate
 *     the inputs unless the task explicitly says to.
 * ------------------------------------------------------------------
 */

// 1. greet(name) -> a greeting built with a TEMPLATE LITERAL.
//    greet("Aisha") must return exactly:  "Hi, Aisha! Welcome back."
function greet(name) {
    // parameter
    //    greet("Aisha") must return exactly:  "Hi, Aisha! Welcome back."
    // TODO: use a template literal (backticks) to build the string
    return `Hi, ${ name }! Welcome back.`;
}

greet("Aisha");

// 2. isPassing(score) -> true if score is 40 or more, else false.
function isPassing(score) {
    // TODO: use a comparison operator
    if (score >= 40) {
        return true;
    } else {
        return false;
    }
}

// 3. sumScores(scores) -> the sum of all numbers in the array.
//    sumScores([]) must return 0.
function sumScores(scores) {
    // TODO: add up the array (a loop OR reduce)
    let sum = 0;
    for (let i = 0; i < scores.length; i++) {
        sum += scores[i];
    }
    return sum;
}

// 4. highScores(scores, min) -> a NEW array with only the scores
//    strictly greater than min.  highScores([10,50,90], 40) -> [50,90]
function highScores(scores, min) {
    // TODO: filter the array
    let ans = scores.filter((item) => item > min);
    // console.log(ans)
    return ans;
}

// 5. titles(tasks) -> an array of every task's .title, in order.
function titles(tasks) {
    // TODO: map each task object to its title
    let ans = tasks.map((item) => item.title);
    return ans;
}

// 6. countByStatus(tasks, status) -> how many tasks have that .status.
function countByStatus(tasks, status) {
    // TODO: count the matches
    // console.log(status,tasks)
    let ans = tasks.filter((item) => item.status == status);
    // console.log(ans)
    return ans.length;
}

// 7. toggleDone(task) -> a NEW task object identical to the input but
//    with .done flipped. The ORIGINAL object must not be changed.
function toggleDone(task) {
    let ans = { ...task, done: !task.done };

    return ans;
    // TODO: copy the object (spread) and flip done
}

// 8. longestTitle(tasks) -> the single .title string with the most
//    characters. Assume at least one task; ties may return either.
function longestTitle(tasks) {
    // TODO: compare title lengths
    // console.log(tasks)
    let max = 0;
    let str = "";
    for (let i = 0; i < tasks.length; i++) {
        if (tasks[i].title.length > max) {
            max = tasks[i].title.length;
            str = tasks[i].title
        }
    }
    return str;
}

// 9. averageScore(scores) -> the average of the numbers.
//    averageScore([]) must return 0 (do not divide by zero).
function averageScore(scores) {
    // TODO: guard the empty case, then average
    if (scores.length == 0) {
        return 0;
    }
    let sum = 0;
    for (let i = 0; i < scores.length; i++) {
        sum += scores[i];
    }
    return sum / scores.length;
}

// 10. formatTask(task) -> a display line built with a TEMPLATE LITERAL:
//     done tasks start with "[x] ", not-done with "[ ] ", then the
//     title, then " (priority)".
//     { title:"Ship", done:true, priority:"low" } -> "[x] Ship (low)"
function formatTask(task) {
    // TODO: choose the box with a conditional, build with a template literal
    if (task.done == true) {
        return `[x] ${ task.title } (${ task.priority })`;
    }
    else {
        return [] ${ task.title } (${ task.priority })

    }
}