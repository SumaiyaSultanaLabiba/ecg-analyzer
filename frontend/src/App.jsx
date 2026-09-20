import { useState } from "react";
import RecordSelector from "./components/RecordSelector";
import RawSignalPanel from "./components/RawSignalPanel";
import FilteredSignalPanel from "./components/FilteredSignalPanel";
import HeartbeatPanel from "./components/HeartbeatPanel";
import SpectrumPanel from "./components/SpectrumPanel";
import ValidationDashboard from "./components/ValidationDashboard";
import HRVPanel from "./components/HRVPanel";
import DiagnosticSummaryPanel from "./components/DiagnosticSummaryPanel";
import SignalChart from "./components/SignalChart";
import { fetchAnalysis, fetchDiagnostics, fetchValidation } from "./api";
import heartIcon from "./assets/logo.jpg";
import "./dashboard.css";





function App() {
  const [recordName, setRecordName] = useState(null);
  const [analysis, setAnalysis] = useState(null);
  const [validation, setValidation] = useState(null);
  const [diagnostics, setDiagnostics] = useState(null);
  const [loading, setLoading] = useState(false);



 async function handleSelect(name) {
  setRecordName(name);
  setLoading(true);
  try {
    const [resultAnalysis, resultValidation, resultDiagnostics] = await Promise.all([
      fetchAnalysis(name),
      fetchValidation(name),
      fetchDiagnostics(name)
    ]);

    setAnalysis(resultAnalysis);
    setValidation(resultValidation);
    setDiagnostics(resultDiagnostics);
  } catch (err) {
    console.error("Error fetching record data:", err);
  }finally{
    setTimeout(() => setLoading(false), 1000);
  }
}


  return (
    <div className="ecg-app">
      <header className="ecg-header">
        <img src={heartIcon} alt="" className="header-icon" />
        <h1>ELECTRO-CARDIOGRAM ANALYZER</h1>
      </header>

      <div className="ecg-main">
        {loading && (
        <div className="global-spinner">
        <div className="loader"></div>
        </div>
      )}

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

          <SignalChart
            title={`Beat type for record ${recordName}`}
            values={analysis?.filtered_signal}
            peakIndices={analysis?.r_peak_indices}
            markerSets={
            diagnostics
            ? [{ indices: diagnostics.abnormal_beat_indices, color: "#13d744", label: "Abnormal beat" }]
            : []
          }
        />

        <HRVPanel diagnostics={diagnostics} record_name={recordName}/>
        <DiagnosticSummaryPanel diagnostics={diagnostics}/>
        </main>

        <ValidationDashboard validation={validation} />

      </div>
    </div>
  );
}

export default App;

