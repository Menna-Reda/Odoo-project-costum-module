# Project Custom

This Odoo module extends the standard Project and HR applications to provide enhanced project tracking, technical metadata, collaborator management, and reporting.

---

## Features

- **Project Enhancements:**  
  - Track Odoo version, type, GitHub repository name & URL, and hosting details for each project.
  - Add a "Collaborators" tab to projects, allowing you to manage employee collaborators and their active/inactive status.

- **Employee Enhancements:**  
  - Add a "GitHub Account" field to employee records (visible in tree, form, and kanban views).
  - Add a "Project Collaborations" tab to employee records, listing all projects where the employee is a collaborator, with status toggling.
  - Prevent archiving employees who are still active collaborators in any project.

- **Collaborator Management:**  
  - Dedicated menu for managing all project collaborators.
  - Toggle collaborator status directly from the list view.

- **Project Report:**  
  - Print a PDF report from the project form, including all technical and collaboration details.

- **API Endpoint:**  
  - `/api/employees_with_active_projects/` (GET, HTTP Basic Auth): Returns a JSON list of employees and their active projects.

---

## Installation

1. Copy the `project_custom` folder into your Odoo `custom_addons` directory.
2. Update the Odoo app list (Apps > Update Apps List).
3. Search for **Project Custom** in the Apps menu and install it.

**Dependencies:**  
- Odoo 17  
- Apps: Project, HR

---

## Usage

- **Projects:**  
  - Open any project. Fill in Odoo, GitHub, and hosting details.
  - Use the "Collaborators" tab to add/remove employees and set their status.

- **Employees:**  
  - Open any employee. The "GitHub Account" field is available.
  - The "Project Collaborations" tab lists all related projects and allows status toggling.
  - Attempting to archive an employee who is still active in a project will raise a warning.

- **Collaborators:**  
  - Use the "Collaborators" menu under Project to manage all project collaborators.

- **Project Report:**  
  - Print the project report from the project form to get a PDF with all details.

- **API:**  
  - Make a GET request to `/api/employees_with_active_projects/` using HTTP Basic Auth.
  - Returns a JSON list of employees and their active projects.

---

## Testing

- **Manual:**  
  - Add projects, set technical details, add collaborators, and test status toggling.
  - Try to archive an employee who is still active in a project (should fail).
  - Print the project report and verify all fields.
  - Use Postman/curl to test the API endpoint.

- **API Example:**  
  ```
  GET http://localhost:8069/api/employees_with_active_projects/
  ```
  Use HTTP Basic Auth with a user who has access to HR and Project.

---

## Author

Developed by Menna Reda

---