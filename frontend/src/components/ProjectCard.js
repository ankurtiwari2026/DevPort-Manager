import React from 'react';

function ProjectCard({ project, toggleFeatured }) {
  return (
    <div className="mb-3 card">
      <div className="card-body">
        <h5 className="card-title">{project.name}</h5>
        <p className="card-text">{project.description || "No description"}</p>
        <p className="card-text">
          <small className="text-muted">
            Language: {project.language} | ⭐ Stars: {project.stars}
          </small>
        </p>
        <button
          className={`btn ${project.featured ? 'btn-success' : 'btn-secondary'}`}
          onClick={() => toggleFeatured(project.id, !project.featured)}
        >
          {project.featured ? "Unmark Featured" : "Mark as Featured"}
        </button>
      </div>
    </div>
  );
}

export default ProjectCard;
