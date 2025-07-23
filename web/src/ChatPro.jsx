import React, { useRef, useState, useEffect } from 'react';

// 大气PC端风格，左右分栏，顶部品牌，聊天区大气卡片，输入区悬浮，tailwindcss
const parseAIContent = (messages) => {
  if (!Array.isArray(messages)) return '';
  for (let i = messages.length - 1; i >= 0; i--) {
    const m = messages[i];
    if (typeof m === 'object' && m.__class__ === 'AIMessage' && m.content) {
      return m.content;
    }
    if (typeof m === 'string' && m.startsWith('AIMessage')) {
      const match = m.match(/content='([\s\S]*?)',/);
      if (match) return match[1];
    }
  }
  return '';
};

const ChatPro = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const chatRef = useRef();

  useEffect(() => {
    if (chatRef.current) {
      chatRef.current.scrollTop = chatRef.current.scrollHeight;
    }
  }, [messages]);

  const sendMessage = async () => {
    if (!input.trim()) return;
    const userMsg = { role: 'user', content: input };
    setMessages((msgs) => [...msgs, userMsg]);
    setInput('');
    setLoading(true);
    let aiMsg = { role: 'ai', content: '' };
    setMessages((msgs) => [...msgs, aiMsg]);
    try {
      const response = await fetch('http://0.0.0.0:8000/query/stream', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question: input }),
      });
      if (!response.body) throw new Error('No stream body');
      const reader = response.body.getReader();
      const decoder = new TextDecoder('utf-8');
      let done = false;
      let fullContent = '';
      while (!done) {
        const { value, done: doneReading } = await reader.read();
        done = doneReading;
        if (value) {
          const chunk = decoder.decode(value, { stream: true });
          const lines = chunk.split(/\r?\n/).filter(Boolean);
          for (const line of lines) {
            try {
              const data = JSON.parse(line.replace(/'/g, '"'));
              const aiContent = parseAIContent(data.messages);
              if (aiContent !== undefined) {
                fullContent = aiContent;
                aiMsg = { role: 'ai', content: fullContent };
                setMessages((msgs) => {
                  const copy = [...msgs];
                  copy[copy.length - 1] = aiMsg;
                  return copy;
                });
              }
            } catch {
              // ignore parse error for non-JSON lines
            }
          }
        }
      }
    } catch (err) {
      aiMsg = { role: 'ai', content: '出错了: ' + err.message };
      setMessages((msgs) => {
        const copy = [...msgs];
        copy[copy.length - 1] = aiMsg;
        return copy;
      });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex h-screen bg-gradient-to-br from-gray-100 to-blue-50">
      {/* 侧边栏 */}
      <aside className="hidden md:flex flex-col w-72 bg-white border-r shadow-lg p-6">
        <div className="flex items-center mb-8">
          <img src="/vite.svg" alt="logo" className="w-10 h-10 mr-3" />
          <span className="text-2xl font-bold text-blue-700 tracking-wide">AI Copilot</span>
        </div>
        <div className="flex-1 flex flex-col gap-4">
          <div className="text-gray-500 text-sm">历史会话</div>
          <div className="flex flex-col gap-2">
            <button className="text-left px-3 py-2 rounded hover:bg-blue-50 transition">今天：SQL 问答</button>
            <button className="text-left px-3 py-2 rounded hover:bg-blue-50 transition">昨天：数据分析</button>
          </div>
        </div>
        <div className="mt-8 text-xs text-gray-400">© 2025 Copilot</div>
      </aside>
      {/* 主内容区 */}
      <main className="flex-1 flex flex-col h-full">
        {/* 顶部栏 */}
        <header className="h-16 flex items-center px-8 bg-white border-b shadow-sm">
          <span className="text-xl font-semibold text-gray-800">AI Copilot 聊天</span>
        </header>
        {/* 聊天内容区 */}
        <div className="flex-1 overflow-y-auto px-2 md:px-0" ref={chatRef}>
          <div className="max-w-3xl mx-auto py-8 flex flex-col gap-6">
            {messages.length === 0 && (
              <div className="text-gray-400 text-center mt-32">开始你的对话吧~</div>
            )}
            {messages.map((msg, idx) => (
              <div key={idx} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
                {msg.role === 'ai' && (
                  <img src="https://api.dicebear.com/7.x/bottts/svg?seed=ai" alt="AI" className="w-10 h-10 rounded-full mr-4 shadow" />
                )}
                <div className={`rounded-2xl px-6 py-4 max-w-[60%] text-base shadow-lg whitespace-pre-line ${msg.role === 'user' ? 'bg-blue-600 text-white rounded-br-none' : 'bg-white text-gray-900 border border-gray-200 rounded-bl-none'}`}>
                  {msg.content}
                </div>
                {msg.role === 'user' && (
                  <img src="https://api.dicebear.com/7.x/personas/svg?seed=user" alt="User" className="w-10 h-10 rounded-full ml-4 shadow" />
                )}
              </div>
            ))}
          </div>
        </div>
        {/* 输入区 */}
        <div className="sticky bottom-0 left-0 w-full bg-white/90 border-t z-20 shadow-lg">
          <div className="max-w-3xl mx-auto flex items-center py-6 px-4 gap-4">
            <input
              className="flex-1 border border-gray-300 rounded-full px-5 py-3 focus:outline-none focus:ring-2 focus:ring-blue-400 bg-gray-50 shadow text-base"
              value={input}
              onChange={e => setInput(e.target.value)}
              onKeyDown={e => { if (e.key === 'Enter' && !loading) sendMessage(); }}
              placeholder="请输入你的问题..."
              disabled={loading}
            />
            <button
              className="bg-blue-600 hover:bg-blue-700 transition text-white px-8 py-3 rounded-full shadow disabled:bg-blue-200 text-base font-semibold"
              onClick={sendMessage}
              disabled={loading || !input.trim()}
            >发送</button>
          </div>
        </div>
      </main>
    </div>
  );
};

export default ChatPro;
