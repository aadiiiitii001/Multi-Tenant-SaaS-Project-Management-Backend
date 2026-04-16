import { useEffect, useState } from "react";
import API from "../api/api";

export default function Dashboard() {
  const [organizations, setOrganizations] = useState([]);
  const [projects, setProjects] = useState([]);
  const [selectedOrg, setSelectedOrg] = useState(null);

  useEffect(() => {
    fetchOrganizations();
  }, []);

  const fetchOrganizations = async () => {
    const res = await API.get("/organizations/");
    setOrganizations(res.data);
    if (res.data.length > 0) {
      setSelectedOrg(res.data[0].id);
      fetchProjects(res.data[0].id);
    }
  };

  const fetchProjects = async (orgId) => {
    const res = await API.get(`/projects/?organization_id=${orgId}`);
    setProjects(res.data);
  };

  const handleOrgChange = (e) => {
    const orgId = e.target.value;
    setSelectedOrg(orgId);
    fetchProjects(orgId);
  };

  return (
    <div style={{ padding: 40 }}>
      <h2>Dashboard</h2>

      {/* Organization Switcher */}
      <select onChange={handleOrgChange} value={selectedOrg}>
        {organizations.map((org) => (
          <option key={org.id} value={org.id}>
            {org.name}
          </option>
        ))}
      </select>

      <h3>Projects</h3>
      <ul>
        {projects.map((p) => (
          <li key={p.id}>{p.name}</li>
        ))}
      </ul>
    </div>
  );
}
