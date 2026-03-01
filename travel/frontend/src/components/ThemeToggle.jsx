import React from 'react';

export default function ThemeToggle({ theme, toggleTheme }) {
    return (
        <button
            onClick={toggleTheme}
            className="theme-toggle glass-card hover-lift"
            aria-label="Toggle Theme"
        >
            {theme === 'dark' ? '☀️ Light Mode' : '🌙 Dark Mode'}
        </button>
    );
}
