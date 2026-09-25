import axios from "axios";


export const api = axios.create({
    baseURL : "https://ecg-analyzer-3urd.onrender.com/"
});


export async function fetchRecordList() {
  const res = await api.get(`/records`)
  return res.data; 
}


export async function fetchAnalysis(recordName) {
  const res = await api.get(`/analyze/${recordName}`);
  return res.data;
}


export async function fetchValidation(recordName) {
  const res = await api.get(`/validate/${recordName}`);
  return res.data;
}


export async function fetchDiagnostics(recordName) {
  const res = await api.get(`/diagnose/${recordName}`);
  return res.data;
}
