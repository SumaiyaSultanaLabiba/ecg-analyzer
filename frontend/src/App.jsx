import { useState } from "react";
import RecordSelector from "./components/RecordSelector";
import RawSignalPanel from "./components/RawSignalPanel";
import FilteredSignalPanel from "./components/FilteredSignalPanel";
import HeartbeatPanel from "./components/HeartbeatPanel";
import SpectrumPanel from "./components/SpectrumPanel";
import ValidationDashboard from "./components/ValidationDashboard";
import { fetchAnalysis } from "./api";



function App() {
  const [recordName, setRecordName] = useState(null);
  const [analysis, setAnalysis] = useState(null);

  async function handleSelect(name) {
    setRecordName(name);
    try {
      const result = await fetchAnalysis(name);
      setAnalysis(result);
    } catch (err) {
      console.error(err);
    }
  }

  return (
    <div style={{ padding: "1rem" }}>
      <h1>ECG Signal Analyzer</h1>
      <RecordSelector onSelect={handleSelect} />

      <RawSignalPanel rawSignal={analysis?.raw_signal} />
      <FilteredSignalPanel filteredSignal={analysis?.filtered_signal} />
      <HeartbeatPanel
        filteredSignal={analysis?.filtered_signal}
        rPeakIndices={analysis?.r_peak_indices}
        heartRateBpm={analysis?.heart_rate_bpm}
      />
      <SpectrumPanel
        fftFreqs={analysis?.fft_freqs}
        fftMagnitudeRaw={analysis?.fft_magnitude_raw}
        fftMagnitudeFiltered={analysis?.fft_magnitude_filtered}
      />
      {recordName && <ValidationDashboard recordName={recordName} />}
    </div>
  );
}

export default App;

