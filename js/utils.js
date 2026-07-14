export function generateId() {
    return crypto.randomUUID();
}

export function formatPercent(value) {
    return `${Math.round(value)}%`;
}