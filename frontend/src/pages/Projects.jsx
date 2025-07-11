import React, { useEffect, useState } from 'react';
import { Container } from 'react-bootstrap';
import ProjectCard from '../components/ProjectCard';
import API from '../services/api';

const Projects = () => {
  const [projects, setProjects] = useState([]);

  useEffect(() => {
    const fetchProjects = async () => {
      const res = await API.get('/projects');
      setProjects(res.data);
    };
    fetchProjects();
  }, []);

  return (
    <Container>
      <h2>Your GitHub Projects</h2>
      {projects.map((project) => (
        <ProjectCard key={project.id} project={project} />
      ))}
    </Container>
  );
};

export default Projects;