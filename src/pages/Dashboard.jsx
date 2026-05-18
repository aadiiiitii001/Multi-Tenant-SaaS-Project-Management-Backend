import { useEffect, useState } from "react";
import API from "../api/api";
import Navbar from "../components/Navbar";
import OrgSwitcher from "../components/OrgSwitcher";

export default function Dashboard() {
  const [organizations, setOrganizations] = useState([]);
  const [projects, setProjects] = useState([]);
  const [selectedOrg, setSelectedOrg] = useState(null);

  useEffect(() => {
    fetchOrganizations();
  }, []);

  const fetchOrganizations = async () => {
    try {
      const res = await API.get("/organizations/");
      setOrganizations(res.data);

      if (res.data.length > 0) {
        setSelectedOrg(res.data[0].id);
        fetchProjects(res.data[0].id);
      }
    } catch (err) {
      console.error(err);
    }
  };

  const fetchProjects = async (orgId) => {
    try {
      const res = await API.get(`/projects/?organization_id=${orgId}`);
      setProjects(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  const selectedOrgName =
    organizations.find((o) => o.id == selectedOrg)?.name;

  return (
    <div>
      <Navbar selectedOrgName={selectedOrgName} />

      <div style={{ padding: "30px" }}>
        <h2>Dashboard</h2>

        <OrgSwitcher
          organizations={organizations}
          selectedOrg={selectedOrg}
          onChange={(orgId) => {
            setSelectedOrg(orgId);
            fetchProjects(orgId);
          }}
        />

        <h3>Projects</h3>

        {projects.length === 0 ? (
          <p>No projects found</p>
        ) : (
          <ul>
            {projects.map((p) => (
              <li key={p.id}>{p.name}</li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
}
