import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import Whiteboard from "./pages/Whiteboard";

function App() {
  return (
    <BrowserRouter>
      <nav style={{ padding: "10px", backgroundColor: "#f0f0f0" }}>
        <Link to="/" style={{ marginRight: "10px" }}>Главная</Link>
        <Link to="/whiteboard">Доска</Link>
      </nav>
      <Routes>
        <Route path="/" element={<h1>Добро пожаловать в LINGWARD!</h1>} />
        <Route path="/whiteboard" element={<Whiteboard />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;