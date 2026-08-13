import { useState } from "react";
import RecordSelector from "./components/RecordSelector";
import RawSignalPanel from "./components/RawSignalPanel";
import FilteredSignalPanel from "./components/FilteredSignalPanel";
import HeartbeatPanel from "./components/HeartbeatPanel";
import SpectrumPanel from "./components/SpectrumPanel";
import ValidationDashboard from "./components/ValidationDashboard";
import { fetchAnalysis, fetchValidation } from "./api";
import heartIcon from "./assets/logo.jpg";
import "./dashboard.css";





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
    <div className="ecg-app">
      <header className="ecg-header">
        <img src={heartIcon} alt="" className="header-icon" />
        <h1>ELECTRO-CARDIOGRAM ANALYZER</h1>
      </header>

      <div className="ecg-main">
        <RecordSelector onSelect={handleSelect} />

        <main className="ecg-plots">
          <RawSignalPanel 
          rawSignal={analysis?.raw_signal} 
          recordName={recordName}
          />
          <FilteredSignalPanel 
          filteredSignal={analysis?.filtered_signal} 
          recordName={recordName}
          />
          <HeartbeatPanel
            filteredSignal={analysis?.filtered_signal}
            rPeakIndices={analysis?.r_peak_indices}
            heartRateBpm={analysis?.heart_rate_bpm}
            recordName={recordName}
          />
          <SpectrumPanel
            fftFreqs={analysis?.fft_freqs}
            fftMagnitudeRaw={analysis?.fft_magnitude_raw}
            fftMagnitudeFiltered={analysis?.fft_magnitude_filtered}
            recordName={recordName}
          />
        </main>

        <ValidationDashboard validation={validation} />
      </div>
    </div>
  );
}

export default App;

