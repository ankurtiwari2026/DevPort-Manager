import React from 'react';
import { Card, Button } from 'react-bootstrap';

const ProjectCard = ({ project }) => {
  return (
    <Card className="mb-3">
      <Card.Body>
        <Card.Title>{project.name}</Card.Title>
        <Card.Text>{project.description}</Card.Text>
        <Button variant="primary" href={project.html_url} target="_blank">
          View on GitHub
        </Button>
      </Card.Body>
    </Card>
  );
};

export default ProjectCard;