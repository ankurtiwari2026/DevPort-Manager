import React, { useEffect, useState } from 'react';
import axios from 'axios';
import ProjectCard from '../components/ProjectCard';

function ProjectList() {
  const [projects, setProjects] = useState([]);

  const fetchProjects = async () => {
    const res = await axios.get("http://localhost:8000/projects");
    setProjects(res.data);
  };

  const toggleFeatured = async (id, featured) => {
    await axios.patch(`http://localhost:8000/projects/${id}`, { featured });
    fetchProjects();
  };

  const downloadPDF = () => {
    axios.get("http://localhost:8000/pdf");
    alert("PDF generated!");
  };

  useEffect(() => {
    fetchProjects();
  }, []);

  return (
    <div className="container py-5">
      <h1 className="mb-4">My GitHub Projects</h1>
      {projects.map((p) => (
        <ProjectCard key={p.id} project={p} toggleFeatured={toggleFeatured} />
      ))}
      <button onClick={downloadPDF} className="btn btn-primary mt-4">
        Generate PDF of Featured Projects
      </button>
    </div>
  );
}

export default ProjectList;
