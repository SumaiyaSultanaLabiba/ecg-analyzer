import React from "react";
import {
  ComposedChart,
  Line,
  Scatter,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  ResponsiveContainer,
} from "recharts";

/**
 * Shared line chart for signal panels. Plots `values` (array of numbers)
 * against sample index, and optionally overlays red dots at `peakIndices`.
 */
export default function SignalChart({
  title,
  values,
  peakIndices,
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

  //dataWithPeaks array,oi point e peak thakle peak property set korbo,nahole null
  const peakSet = new Set(peakIndices || []);
  const dataWithPeaks = values.map((y, i) => ({
    x: xValues ? xValues[i] : i,
    y,
    peak: peakSet.has(i) ? y : null,  
  }));

  return (
    <div className="chart-card">
      <h3 className="chart-title">{title}</h3>
      <ResponsiveContainer width="100%" height={height}>
        <ComposedChart data={dataWithPeaks} margin={{ top: 10, right: 20, left: 0, bottom: 4 }}>
          <CartesianGrid stroke="#e9ecef" strokeDasharray="3 3" />
          <XAxis
            dataKey="x"
            tick={{ fontSize: 10, fill: "#607d8b" }}
            stroke="#b0bec5"
            label={{ value: xLabel, position: "insideBottom", offset: -2, fontSize: 10, fill: "#607d8b" }}
          />
          <YAxis tick={{ fontSize: 10, fill: "#607d8b" }} stroke="#b0bec5" width={44} />
          <Tooltip contentStyle={{ fontSize: 12 }} />
          <Line
            type="monotone"
            dataKey="y"
            stroke={lineColor}
            strokeWidth={1.5}
            dot={false}
            isAnimationActive={false}
          />
          {peakIndices && peakIndices.length > 0 && (
            <Scatter 
              dataKey="peak"
              fill="#e63946" 
              r={5}
              isAnimationActive={false} 
            />
          )}
        </ComposedChart>
      </ResponsiveContainer>
      {meta && <p className="chart-meta">{meta}</p>}
    </div>
  );
}
