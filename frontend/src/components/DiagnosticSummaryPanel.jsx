import React from "react";



export default function DiagnosticSummaryPanel({ diagnostics}) {
  if (!diagnostics) {
    return (
      <div className="chart-card">
        <h3 className="chart-title">Diagnostic Summary</h3>
        <p className="chart-empty">No data yet — select a record.</p>
      </div>
    );
  }

  const { status, notes, rhythm_classification, abnormal_beat_indices } = diagnostics;
  const isAbnormal = status === "abnormal";

  const flagList = [
    { key: "tachycardia", label: "Tachycardia (HR > 100 bpm)" },
    { key: "bradycardia", label: "Bradycardia (HR < 60 bpm)" },
    { key: "irregular_rhythm", label: "Irregular rhythm (high HRV)" },
    { key: "abnormal_beats_detected", label: "Abnormal beat shape detected" },
  ];

  return (
    <section className="diagnostic-summary-panel">
      <h2 className="panel-heading">Diagnostic Summary</h2>

      <div className={`status-badge ${isAbnormal ? "status-abnormal" : "status-normal"}`}>
        {isAbnormal ? "⚠ Abnormal pattern flagged" : "✓ Normal pattern"}
      </div>

      <ul className="rhythm-flags">
        {flagList.map((flag) => {
          const active = rhythm_classification[flag.key];
          return (
            <li key={flag.key} className={active ? "flag-active" : "flag-inactive"}>
              <span className="flag-dot" />
              {flag.label}
            </li>
          );
        })}
      </ul>

      {abnormal_beat_indices.length > 0 && (
        <div className="abnormal-beats-list">
          <strong>{abnormal_beat_indices.length} abnormal beat(s) flagged</strong>
          <p className="chart-meta">Sample indices: {abnormal_beat_indices.join(", ")}</p>
        </div>
      )}

      <p className="notes-text">{notes}</p>
      <p className="disclaimer-text">
        Rule-based pattern flagging for educational purposes only — not a clinical
        diagnostic tool.
      </p>
    </section>
  );
}