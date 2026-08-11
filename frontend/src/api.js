import axios from "axios";


export const api = axios.create({
    baseURL : "http://localhost:8000"
});


export async function fetchRecordList() {
  const res = await api.get(`/records`)
  return ["record1", "record2", "record3"]; 
}


export async function fetchAnalysis(recordName) {
  const res = await api.get(`/analyze/${recordName}`);
  return {
    raw_signal: [0, 0, 0, 0],
    filtered_signal: [0, 0, 0, 0],
    r_peak_indices: [0],
    heart_rate_bpm: 0,
    fft_freqs: [0, 1, 2],
    fft_magnitude_raw: [0, 0, 0],
    fft_magnitude_filtered: [0, 0, 0],
  };
}


export async function fetchValidation(recordName) {
  const res = await api.get(`/validate/${recordName}`);
  return { status: "ok", record: recordName };
}


