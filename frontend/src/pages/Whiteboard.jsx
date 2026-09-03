import React from "react";
import { Excalidraw } from "@excalidraw/excalidraw";
import "@excalidraw/excalidraw/index.css";

export default function Whiteboard() {
  return (
    <div style={{ height: "100vh", width: "100%" }}>
      <Excalidraw langCode="ru-RU" />
    </div>
  );
}