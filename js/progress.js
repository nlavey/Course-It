export function getCompletedTopics(topics) {
    return topics.filter(topic => topic.completed).length;
}

export function getRemainingTopics(topics) {
    return topics.length - getCompletedTopics(topics);
}

export function getProgressPercent(topics) {

    if (topics.length === 0) {
        return 0;
    }

    return (
        getCompletedTopics(topics) /
        topics.length
    ) * 100;
}