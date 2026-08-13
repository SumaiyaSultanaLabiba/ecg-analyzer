import React from "react";
import SignalChart from "./SignalChart";

export default function FilteredSignalPanel({ filteredSignal, recordName }) {
  return (
    <SignalChart
      title={recordName?`Filtered Signal ${recordName}`:`Filtered Signal`}
      values={filteredSignal}
      lineColor="#0d47a1"
      meta={filteredSignal ? `${filteredSignal.length} samples` : null}
    />
  );
}
