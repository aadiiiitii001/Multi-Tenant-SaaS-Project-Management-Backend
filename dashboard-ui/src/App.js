import { useEffect, useState } from "react";

function App() {
  const [status, setStatus] = useState("Loading...");
  const [stats, setStats] = useState({
    tenants: 0,
    users: 0,
    projects: 0,
  });

  useEffect(() => {
    // Backend status
    fetch("https://multi-tenant-saas-project-management-kim3.onrender.com")
      .then((res) => res.json())
      .then((data) => setStatus(data.status))
      .catch(() => setStatus("Error"));

    // Dummy stats (we will replace with real API later)
    setStats({
      tenants: 5,
      users: 25,
      projects: 12,
    });
  }, []);

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1>🚀 SaaS Dashboard</h1>

      {/* Status */}
      <div style={{
        marginTop: "20px",
        padding: "15px",
        background: "#f0f0f0",
        borderRadius: "10px",
        width: "250px"
      }}>
        <h3>Server Status</h3>
        <p>{status}</p>
      </div>

      {/* Cards */}
      <div style={{
        display: "flex",
        gap: "20px",
        marginTop: "30px"
      }}>
        <div style={cardStyle}>
          <h3>Tenants</h3>
          <p>{stats.tenants}</p>
        </div>

        <div style={cardStyle}>
          <h3>Users</h3>
          <p>{stats.users}</p>
        </div>

        <div style={cardStyle}>
          <h3>Projects</h3>
          <p>{stats.projects}</p>
        </div>
      </div>
    </div>
  );
}

const cardStyle = {
  padding: "20px",
  borderRadius: "10px",
  background: "#e3f2fd",
  width: "150px",
  textAlign: "center",
  fontSize: "18px",
};

export default App;
