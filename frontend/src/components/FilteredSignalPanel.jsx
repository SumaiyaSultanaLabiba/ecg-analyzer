
import React, { useEffect, useState } from 'react';


export default function FilteredSignalPanel({ filteredSignal }) {
  if (!filteredSignal) return <p>No data yet — select a record.</p>;

  return (
    <div>
      <h3>Filtered Signal</h3>
      {/* TODO: replace with <LineChart data={filteredSignal} /> */}
      <p>{filteredSignal.length} samples (chart goes here)</p>
    </div>
  );
}
