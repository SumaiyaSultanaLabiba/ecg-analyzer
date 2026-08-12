
import React, { useEffect, useState } from 'react';


export default function SpectrumPanel({ fftFreqs, fftMagnitudeRaw, fftMagnitudeFiltered }) {
  if (!fftFreqs || !fftMagnitudeRaw || !fftMagnitudeFiltered)
  {
    return <p>No data yet — select a record.</p>;
  }

  return (
    <div>
      <h3>Frequency Spectrum</h3>
      {/* TODO: two <LineChart> side by side, x = fftFreqs,
          y = fftMagnitudeRaw and fftMagnitudeFiltered respectively */}
      <p>{fftFreqs.length} frequency bins (chart goes here)</p>
    </div>
  );
}
