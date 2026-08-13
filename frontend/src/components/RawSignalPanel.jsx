import React from "react";
import SignalChart from "./SignalChart";

export default function RawSignalPanel({ rawSignal, recordName }) {
  return (
    <SignalChart
      title={recordName?`Raw Signal for Record ${recordName}`:`Raw Signal`}
      values={rawSignal}
      lineColor="#1a73e8"
      meta={rawSignal ? `${rawSignal.length} samples loaded` : null}
    />
  );
}
