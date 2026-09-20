import React from "react";
import SignalChart from "./SignalChart";

/**
 * Displays HRV (Heart Rate Variability) analysis:
 * - a metrics table (time-domain + frequency-domain)
 * - the R-R interval tachogram (irregular beat-to-beat variation over time)
 * - the LF/HF power spectrum (frequency-domain view of that variability)
 *
 * Reuses the existing SignalChart component, unmodified in its basic usage —
 * these two charts just need line data, no peak markers.
 */
export default function HRVPanel({ diagnostics }) {
  if (!diagnostics) {
    return (
      <div className="chart-card">
        <h3 className="chart-title">Heart Rate Variability</h3>
        <p className="chart-empty">No data yet — select a record.</p>
      </div>
    );
  }

  const { hrv_metrics, rr_times, rr_intervals, psd_freqs, psd_values } = diagnostics;

  const metricRows = [
    { label: "SDNN", value: hrv_metrics.sdnn_ms.toFixed(1), unit: "ms" },
    { label: "RMSSD", value: hrv_metrics.rmssd_ms.toFixed(1), unit: "ms" },
    { label: "pNN50", value: hrv_metrics.pnn50_percent.toFixed(1), unit: "%" },
    { label: "LF Power", value: hrv_metrics.lf_power.toExponential(2), unit: "" },
    { label: "HF Power", value: hrv_metrics.hf_power.toExponential(2), unit: "" },
    { label: "LF/HF Ratio", value: hrv_metrics.lf_hf_ratio.toFixed(2), unit: "" },
  ];

  return (
    <section className="hrv-panel">
      <h2 className="panel-heading">Heart Rate Variability</h2>

      <table className="metrics-table">
        <thead>
          <tr>
            <th>Metric</th>
            <th>Value</th>
          </tr>
        </thead>
        <tbody>
          {metricRows.map((row) => (
            <tr key={row.label}>
              <td>{row.label}</td>
              <td>
                {row.value} {row.unit}
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      <SignalChart
        title="R-R Interval Tachogram"
        values={rr_intervals}
        xValues={rr_times}
        xLabel="Time (s)"
        lineColor="#7b2cbf"
        meta="Beat-to-beat interval variation, resampled onto a uniform time grid."
      />

      <SignalChart
        title="R-R Power Spectrum (LF/HF)"
        values={psd_values}
        xValues={psd_freqs}
        xLabel="Frequency (Hz)"
        lineColor="#2a9d8f"
        meta="LF band: 0.04–0.15 Hz · HF band: 0.15–0.4 Hz"
      />
    </section>
  );
}