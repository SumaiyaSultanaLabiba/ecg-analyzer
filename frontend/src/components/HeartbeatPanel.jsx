import React from "react";
import SignalChart from "./SignalChart";

export default function HeartbeatPanel({ filteredSignal, rPeakIndices, heartRateBpm,recordName }) {
  const meta =
    filteredSignal && rPeakIndices && heartRateBpm != null
      ? `${rPeakIndices.length} beats detected · ${heartRateBpm.toFixed(1)} BPM`
      : null;

  return (
    <SignalChart
      title={recordName?`Detected Heartbeats for Record ${recordName}`:`Detected Heartbeats`}
      values={filteredSignal}
      peakIndices={rPeakIndices}
      lineColor="#2e7d32"
      meta={meta}
    />
  );
}
