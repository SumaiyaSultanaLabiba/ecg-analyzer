import React from "react";
import {
  ComposedChart,
  Line,
  Scatter,
  XAxis,
  YAxis,
  Tooltip,
  Legend,
  CartesianGrid,
  ResponsiveContainer,
} from "recharts";


export default function SignalChart({
  title,
  values,
  peakIndices,
  markerSets,
  xValues,
  xLabel = "Sample",
  lineColor = "#1565c0",
  height = 300,
  meta,
}) {
  if (!values || values.length === 0) {
    return (
      <div className="chart-card">
        <h3 className="chart-title">{title}</h3>
        <p className="chart-empty">No data yet — select a record.</p>
      </div>
    );
  }

  // Combine the legacy single peakIndices series with any additional
  // markerSets into one uniform list of { indices, color, label }.
  const allMarkerSeries = [
    ...(peakIndices && peakIndices.length > 0
      ? [{ indices: peakIndices, color: "#e63946", label: "Detected beat" }]
      : []),
    ...(markerSets || []),
  ];

  // Precompute one Set per series (once, not per data point).
  const markerIndexSets = allMarkerSeries.map((series) => new Set(series.indices));

  const dataWithMarkers = values.map((y, i) => {
    const point = { x: xValues ? xValues[i] : i, y };
    allMarkerSeries.forEach((series, seriesIdx) => {
      const key = series.label ?? `marker_${seriesIdx}`;
      point[key] = markerIndexSets[seriesIdx].has(i) ? y : null;
    });
    return point;
  });

  return (
    <div className="chart-card">
      <h3 className="chart-title">{title}</h3>
      <ResponsiveContainer width="100%" height={height}>
        <ComposedChart data={dataWithMarkers} margin={{ top: 10, right: 20, left: 0, bottom: 4 }}>
          <CartesianGrid stroke="#e9ecef" strokeDasharray="3 3" />
          <XAxis
            dataKey="x"
            tick={{ fontSize: 10, fill: "#607d8b" }}
            stroke="#b0bec5"
            label={{ value: xLabel, position: "insideBottom", offset: -2, fontSize: 10, fill: "#607d8b" }}
          />
          <YAxis tick={{ fontSize: 10, fill: "#607d8b" }} stroke="#b0bec5" width={44} />
          <Tooltip contentStyle={{ fontSize: 12 }} />
          {allMarkerSeries.length > 1 && <Legend wrapperStyle={{ fontSize: 11 }} />}
          <Line
            type="monotone"
            dataKey="y"
            name={title}
            stroke={lineColor}
            strokeWidth={1.5}
            dot={false}
            isAnimationActive={false}
          />
          {allMarkerSeries.map((series, i) => (
            <Scatter
              key={series.label ?? i}
              dataKey={series.label ?? `marker_${i}`}
              name={series.label}
              fill={series.color}
              r={5}
              isAnimationActive={false}
            />
          ))}
        </ComposedChart>
      </ResponsiveContainer>
      {meta && <p className="chart-meta">{meta}</p>}
    </div>
  );
}
