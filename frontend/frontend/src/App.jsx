import FileUpload from "./components/FileUpload";
import ChatBox from "./components/ChatBox";

function App() {
  return (
    <div style={{ padding: "20px" }}>
      <h1>📄 PDF RAG Chatbot</h1>
      <FileUpload />
      <hr />
      <ChatBox />
    </div>
  );
}

export default App;
