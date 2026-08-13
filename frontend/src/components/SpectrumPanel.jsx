import React from "react";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  Legend,
  CartesianGrid,
  ResponsiveContainer,
} from "recharts";

// Spectrum needs two overlaid series (raw vs. filtered magnitude), so it
// uses recharts directly rather than the shared single-line SignalChart.
export default function SpectrumPanel({ fftFreqs, fftMagnitudeRaw, fftMagnitudeFiltered, recordName }) {
  if (!fftFreqs || !fftMagnitudeRaw || !fftMagnitudeFiltered) {
    return (
      <div className="chart-card">
        <h3 className="chart-title">Frequency Spectrum</h3>
        <p className="chart-empty">No data yet — select a record.</p>
      </div>
    );
  }

  const data = fftFreqs.map((f, i) => ({
    freq: f,
    raw: fftMagnitudeRaw[i],
    filtered: fftMagnitudeFiltered[i],
  }));

  return (
    <div className="chart-card">
      <h3 className="chart-title">{`Frequency Spectrum for Record ${recordName}`}</h3>
      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={data} margin={{ top: 10, right: 20, left: 0, bottom: 4 }}>
          <CartesianGrid stroke="#e9ecef" strokeDasharray="3 3" />
          <XAxis
            dataKey="freq"
            tick={{ fontSize: 10, fill: "#607d8b" }}
            stroke="#b0bec5"
            label={{ value: "Hz", position: "insideBottom", offset: -2, fontSize: 10, fill: "#607d8b" }}
          />
          <YAxis tick={{ fontSize: 10, fill: "#607d8b" }} stroke="#b0bec5" width={44} />
          <Tooltip contentStyle={{ fontSize: 12 }} />
          <Legend wrapperStyle={{ fontSize: 11 }} />
          <Line type="monotone" dataKey="raw" name="Raw" stroke="#9c27b0" strokeWidth={1.5} dot={false} isAnimationActive={false} />
          <Line type="monotone" dataKey="filtered" name="Filtered" stroke="#6a1b9a" strokeWidth={1.5} dot={false} isAnimationActive={false} />
        </LineChart>
      </ResponsiveContainer>
      <p className="chart-meta">{fftFreqs.length} frequency bins</p>
    </div>
  );
}
