import { useState } from "react";
import RecordSelector from "./components/RecordSelector";
import RawSignalPanel from "./components/RawSignalPanel";
import FilteredSignalPanel from "./components/FilteredSignalPanel";
import HeartbeatPanel from "./components/HeartbeatPanel";
import SpectrumPanel from "./components/SpectrumPanel";
import ValidationDashboard from "./components/ValidationDashboard";
import { fetchAnalysis, fetchValidation } from "./api";



function App() {
  const [recordName, setRecordName] = useState(null);
  const [analysis, setAnalysis] = useState(null);
  const [validation, setValidation] = useState(null);


  async function handleSelect(name) {
    setRecordName(name);
    try {
      const resultAnalysis = await fetchAnalysis(name);
      setAnalysis(resultAnalysis);
      const resultValidation = await fetchValidation(name);
      setValidation(resultValidation);
    } catch (err) {
      console.error(err);
    }
  }


  return (
    <div>
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
      <ValidationDashboard validation={validation} />
    </div>
  );
}

export default App;

