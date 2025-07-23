import React, { useRef, useState } from 'react';
import Chart from './Chart';
// tailwindcss 样式，需确保已在项目中配置 tailwind

const parseAIContent = (messages) => {
  // 查找最后一个 AIMessage 并返回 content
  if (!Array.isArray(messages)) return '';
  for (let i = messages.length - 1; i >= 0; i--) {
    const m = messages[i];
    if (typeof m === 'object' && m.__class__ === 'AIMessage' && m.content) {
      return m.content;
    }
    // 兼容字符串格式
    if (typeof m === 'string' && m.startsWith('AIMessage')) {
      const match = m.match(/content='([\s\S]*?)',/);
      if (match) return match[1];
    }
  }
  return '';
};

const ChatSimple = () => {
  const [messages, setMessages] = useState([]); // {role, content}
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const chatRef = useRef();
  const [visualData, setVisualData] = useState({});
  
  const getConfig = (data) => {
    return {
    data,
    angleField: 'value',
    colorField: 'label',
    label: {
      text: 'value',
      position: 'outside',
    },
    legend: {
      color: {
        title: false,
        position: 'right',
        rowPadding: 5,
      },
    },
  };
}

  const sendMessage = async () => {
    if (!input.trim()) return;
    setInput('');
    setLoading(true);
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
      while (!done) {
        const { value, done: doneReading } = await reader.read();
        done = doneReading;
        if (value) {
          const chunk = decoder.decode(value, { stream: true });
          console.log('Received chunk:', chunk);
          const data = JSON.parse(chunk)
          let c = data.content
     
          if(data.tool_calls) {
            c += `\nTool calls: ${data.tool_calls.map(call => `${call.name}(${JSON.stringify(call.args)})`).join(', ')}`
          }
          if(data.type == 'ToolMessage') {
            c = `Tools response: ${c}`
          }
          // const metaData = data.response_metadata;
          // if (metaData?.done) {
          //   setVisualData();
          // }
          let visualContent = null
          try {
            visualContent = JSON.parse(data.content)
          } catch (error) {
            visualContent = null
          }
console.log('Meta datavisualContentvisualContentvisualContent:', visualContent);
          setMessages((msgs) => [...msgs, { role: data.type === 'HumanMessage' ? 'user' : 'ai', content: c,  visualContent }]);
        }
      }
    } catch (err) {
      //
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col h-screen bg-[#ececf1]">
      <div className="flex-1 overflow-y-auto" ref={chatRef}>
        <div className="max-w-2xl mx-auto py-8">
          {messages.length === 0 && (
            <div className="text-gray-400 text-center mt-32">开始你的对话吧~</div>
          )}
          {messages.map((msg, idx) => (
            <div key={idx} className="w-full flex mb-4">
              {msg.role === 'ai' ? (
                <>
                  <img src="https://api.dicebear.com/7.x/bottts/svg?seed=ai" alt="AI" className="w-8 h-8 rounded-full mr-4 mt-1" />
                  <div className="flex-1">
                    {
                      msg.visualContent ? (
                        <pre className="bg-[#007aff] text-white px-5 py-4 rounded-none shadow max-w-2xl block">
                        <Chart msg={msg} />
                        </pre>
                      ) : (
                         <code className="bg-[#007aff] text-white px-5 py-4 rounded-none shadow max-w-2xl block">
                            {msg.content}
                          </code>
                      )
                    }
                  </div>
                </>
              ) : (
                <>
                  <div className="flex-1 flex justify-end">
                   
                   <code className="bg-[#007aff] text-white px-5 py-4 rounded-none shadow max-w-2xl whitespace-pre-line block">
                            {msg.content}
                          </code>
                  </div>
                  <img src="https://api.dicebear.com/7.x/personas/svg?seed=user" alt="User" className="w-8 h-8 rounded-full ml-4 mt-1" />
                </>
              )}
            </div>
          ))}
        </div>
      </div>
      <div className="sticky bottom-0 left-0 w-full bg-[#f7f7f8] border-t z-20">
        <div className="max-w-2xl mx-auto flex items-center py-4 px-2">
          <input
            className="flex-1 border border-gray-300 px-4 py-3 mr-2 focus:outline-none focus:ring-2 focus:ring-blue-400 bg-white shadow-sm text-base rounded-none"
            value={input}
            onChange={e => setInput(e.target.value)}
            onKeyDown={e => { if (e.key === 'Enter' && !loading) sendMessage(); }}
            placeholder="请输入你的问题..."
            disabled={loading}
          />
          <button
            className="bg-[#007aff] hover:bg-blue-600 transition text-white px-6 py-2 shadow disabled:bg-blue-200 text-base rounded-none"
            onClick={sendMessage}
            disabled={loading || !input.trim()}
          >发送</button>
        </div>
      </div>
    </div>
  );
};

export default ChatSimple;
