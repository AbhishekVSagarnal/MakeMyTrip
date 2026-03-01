const STEPS = [
    { emoji: '🏨', label: 'Hotels' },
    { emoji: '🏛️', label: 'Attractions' },
    { emoji: '🍽️', label: 'Restaurants' },
    { emoji: '✨', label: 'AI Itinerary' },
];

export default function ProgressStepper({ currentStep }) {
    return (
        <div className="progress-stepper">
            {STEPS.map((step, idx) => {
                const status = idx < currentStep ? 'completed' : idx === currentStep ? 'active' : '';
                return (
                    <div key={idx} style={{ display: 'flex', alignItems: 'center' }}>
                        {idx > 0 && <div className={`step-line ${idx <= currentStep ? 'active' : ''}`} />}
                        <div className={`step ${status}`}>
                            <div className="step-dot">
                                {status === 'completed' ? '✓' : step.emoji}
                            </div>
                            <span className="step-label">{step.label}</span>
                        </div>
                    </div>
                );
            })}
        </div>
    );
}
