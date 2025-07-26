# Copilot Instructions for lgjs/web

## Project Overview
This is a React + Vite project with a minimal setup, using HMR and ESLint. The codebase includes both JavaScript and TypeScript files. Visualization is handled via `@ant-design/charts` (see `src/Chart.tsx`).

## Key Components & Structure
- `src/`: Main source directory
  - `App.jsx`: Main application entry point
  - `main.jsx`: Vite/React bootstrap
  - `Chart.tsx`: Pie chart visualization using Ant Design Charts
  - `ChatPro.jsx`, `ChatSimple.jsx`: Chat-related components
  - `App.css`: Global styles
  - `assets/`: Static assets (SVGs, etc.)
- `public/`: Static files for Vite
- `index.html`: Vite entry HTML
- `vite.config.js`: Vite configuration
- `eslint.config.js`: ESLint rules

## Developer Workflows
- **Start Dev Server:**
  ```sh
  npm run dev
  ```
- **Build for Production:**
  ```sh
  npm run build
  ```
- **Preview Production Build:**
  ```sh
  npm run preview
  ```
- **Lint:**
  ```sh
  npm run lint
  ```

## Patterns & Conventions
- React components use functional style and hooks.
- TypeScript is used for some components (e.g., `Chart.tsx`).
- Data for charts is passed via props, e.g., `msg.visualContent?.visualization?.data` in `Chart.tsx`.
- CSS is imported directly in components.
- Ant Design Charts are configured via a `config` object and rendered inside a styled div.

## External Dependencies
- `@ant-design/charts`: For chart visualizations
- `react`, `react-dom`: Core UI
- `vite`: Build tool
- ESLint: Linting

## Integration Points
- Chart data flows from parent components to `Chart.tsx` via the `msg` prop.
- Static assets are stored in `src/assets/` and `public/`.

## Example: Chart Component Usage
```jsx
<Chart msg={...} />
```
- Expects `msg.visualContent.visualization.data` to be an array of objects with `label` and `value` fields.

## Recommendations for AI Agents
- Follow the existing component and prop patterns.
- Use Vite commands for builds and previews.
- Reference `Chart.tsx` for chart integration patterns.
- Place new assets in `src/assets/` or `public/` as appropriate.
- Use TypeScript for new components if type safety is required.

---
If any section is unclear or missing, please provide feedback to improve these instructions.
