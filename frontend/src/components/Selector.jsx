export default function Selector({ label, id, value, onChange, options }) {
  return (
    <div className="form-field">
      <label htmlFor={id}>{label}</label>
      <div className="custom-select">
        <select id={id} value={value} onChange={e => onChange(e.target.value)}>
          {options.map(opt => (
            <option key={opt.value ?? opt} value={opt.value ?? opt}>
              {opt.label ?? opt}
            </option>
          ))}
        </select>
        <span className="select-arrow">▾</span>
      </div>
    </div>
  )
}
