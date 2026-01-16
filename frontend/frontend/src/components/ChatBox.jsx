import { useState } from "react";
import { askQuestion } from "../api";

function ChatBox() {
  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const sendQuestion = async () => {
    if (!question) return;

    setMessages([...messages, { role: "User", text: question }]);
    setLoading(true);

    const res = await askQuestion(question);

    setMessages((prev) => [
      ...prev,
      { role: "AI", text: res.answer },
    ]);

    setQuestion("");
    setLoading(false);
  };

  return (
    <div>
      <h3>Ask Question</h3>

      <div style={{ minHeight: "150px" }}>
        {messages.map((msg, i) => (
          <p key={i}>
            <b>{msg.role}:</b> {msg.text}
          </p>
        ))}
        {loading && <p>Thinking...</p>}
      </div>

      <input
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Ask from document..."
      />
      <button onClick={sendQuestion}>Ask</button>
    </div>
  );
}

export default ChatBox;
