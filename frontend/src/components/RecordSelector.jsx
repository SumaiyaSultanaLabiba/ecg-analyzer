import React, { useEffect, useState } from "react";
import { fetchRecordList } from "../api";

export default function RecordSelector({ onSelect }) {
  const [records, setRecords] = useState([]);
  const [selected, setSelected] = useState("");

  useEffect(() => {
    fetchRecordList().then((res) => setRecords(res.records)).catch(console.error);
  }, []);

  function handleChange(e) {
    const value = e.target.value;
    setSelected(value);
    onSelect(value);
  }

  return (
    <div className="ecg-sidebar">
      <div className="sidebar-header">
        <span className="pulse-dot" />
        <h2>ECG Records</h2>
      </div>

      <div className="sidebar-body">
        <div>
          <label className="control-label" htmlFor="record-select">
            Select ECG Record
            <span className="control-sub">MIT-BIH Arrhythmia Database</span>
          </label>

          <div className="select-wrap">
            <select
              id="record-select"
              className="control-select"
              onChange={handleChange}
              value={selected}
            >
              <option value="" disabled>
                Choose a record
              </option>
              {records.map((r) => (
                <option key={r} value={r}>
                  Record {r}
                </option>
              ))}
            </select>
          </div>
        </div>

        {selected ? (
          <div className="selection-chip">
            <span className="dot" />
            Now viewing Record {selected}
          </div>
        ) : (
          <div className="selection-chip empty">
            <span className="dot" />
            No record selected
          </div>
        )}
      </div>
    </div>
  );
}
