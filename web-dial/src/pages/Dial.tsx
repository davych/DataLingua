import React, { useState, useRef, useEffect } from 'react';
import { Input, Button, Typography, Avatar, List, } from 'antd';
import { SendOutlined, PlusOutlined, MessageOutlined } from '@ant-design/icons';
import http from '../http';
import { AiMessage } from '../components/AiMessage';
const { Text } = Typography;

interface Message {
  id: string;
  content: string;
  isUser: boolean;
  timestamp: Date;
}

interface ChatSession {
  id: string;
  title: string;
  lastMessage: string;
  timestamp: string;
}

const ChatInterface: React.FC = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const [chatSessions, setChatSessions] = useState<ChatSession[]>([
    {
      id: '1',
      title: '新的对话',
      lastMessage: '',
      timestamp: '3 小时前'
    }
  ]);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSendMessage = async () => {
    if (!inputValue.trim()) return;

    const userMessage: Message = {
      id: Date.now().toString(),
      content: inputValue,
      isUser: true,
      timestamp: new Date()
    };

    const nextMessages = [...messages, userMessage];
    setMessages(nextMessages);
    setInputValue('');
    setIsLoading(true);

    // 只收集human消息内容组成query数组
    const queryArr = nextMessages.filter(m => m.isUser).map(m => m.content);
    // conversation_id可用当前会话id或自定义
    const conversation_id = '1';
    try {
      const res = await http.post('/qa', {
        conversation_id,
        query: queryArr
      });
      // AI回复
      const aiContent = JSON.stringify(res.data);
      setMessages(prev => [...prev, {
        id: Date.now().toString() + '-ai',
        content: aiContent,
        isUser: false,
        timestamp: new Date()
      }]);
    } catch (error) {
      setMessages(prev => [...prev, {
        id: Date.now().toString() + '-ai',
        content: 'AI接口请求失败',
        isUser: false,
        timestamp: new Date()
      }]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSendMessage();
    }
  };

  const handleNewChat = () => {
    setMessages([]);
    
    // 添加新的对话会话
    const newSession: ChatSession = {
      id: Date.now().toString(),
      title: '新的对话',
      lastMessage: 'gpt-4-1-mini',
      timestamp: '刚刚'
    };
    setChatSessions(prev => [newSession, ...prev]);
  };

  return (
    <div className="flex h-screen bg-gray-900">
      {/* 左侧边栏 */}
      <div className="w-80 bg-gray-800 border-r border-gray-700 flex flex-col">
        {/* 头部 */}
        <div className="p-4 border-b border-gray-700">
          <div className="flex items-center gap-3 mb-4">
            <Avatar 
              size={32} 
              className="!bg-blue-500 flex items-center justify-center"
            >
              <MessageOutlined className="!text-white" />
            </Avatar>
            <div>
              <Text className="!text-white font-medium block">Visual Dial</Text>
              <Text className="!text-gray-400 text-sm">Talk with your data</Text>
            </div>
          </div>
          
          <Button
            type="primary"
            icon={<PlusOutlined />}
            block
            className="!bg-blue-600 !border-blue-600 !hover:bg-blue-700 !hover:border-blue-700"
            onClick={handleNewChat}
          >
            新的对话
          </Button>
        </div>

        {/* 对话列表 */}
        <div className="flex-1 overflow-y-auto">
          <List
            dataSource={chatSessions}
            renderItem={(session) => (
              <List.Item className={`!px-4 !py-3 hover:bg-gray-700 cursor-pointer border-l-2 ${
                session.id === '1' ? 'border-blue-500 bg-gray-700' : 'border-transparent'
              }`}>
                <div className="w-full">
                  <Text className="!text-white font-medium block mb-1">
                    {session.title}
                  </Text>
                  <div className="flex justify-between items-center">
                    <Text className="!text-gray-400 text-sm">
                      {session.lastMessage}
                    </Text>
                    <Text className="!text-gray-500 text-xs">
                      {session.timestamp}
                    </Text>
                  </div>
                </div>
              </List.Item>
            )}
          />
        </div>

      </div>

      {/* 右侧主聊天区域 */}
      <div className="flex-1 flex flex-col">
        {/* 聊天头部 */}
        <div className="bg-gray-800 border-b border-gray-700 p-4">
          <Text className="!text-white text-lg font-medium">模型选择</Text>
        </div>

        {/* 消息区域 */}
        <div className="flex-1 overflow-y-auto p-4 bg-gray-900">
          <div className="max-w-4xl mx-auto space-y-4">
            {messages.map((message) => (
              message.isUser ? (
                <div
                  key={message.id}
                  className="flex gap-3 justify-end"
                >
                  <div className="max-w-2xl px-4 py-3 rounded-lg !bg-blue-600 !text-white ml-12">
                    <Text className="!text-white">{message.content}</Text>
                  </div>
                  <Avatar 
                    size={32} 
                    className="!bg-green-500 flex items-center justify-center flex-shrink-0"
                  >
                    U
                  </Avatar>
                </div>
              ) : (
                <AiMessage key={message.id} content={message.content} />
              )
            ))}
            
            {isLoading && (
              <div className="flex gap-3 justify-start">
                <Avatar 
                  size={32} 
                  className="bg-blue-500 flex items-center justify-center flex-shrink-0"
                >
                  <MessageOutlined className="text-white" />
                </Avatar>
                <div className="bg-gray-700 text-gray-100 px-4 py-3 rounded-lg mr-12">
                  <div className="flex space-x-1">
                    <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce"></div>
                    <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '0.1s' }}></div>
                    <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '0.2s' }}></div>
                  </div>
                </div>
              </div>
            )}
            <div ref={messagesEndRef} />
          </div>
        </div>

        {/* 输入区域 */}
        <div className="bg-gray-800 border-t border-gray-700 p-4">
          <div className="max-w-4xl mx-auto">
            <div className="relative">
              <Input.TextArea
                value={inputValue}
                onChange={(e) => setInputValue(e.target.value)}
                onKeyUp={handleKeyPress}
                placeholder="询问问题"
                // className="resize-none pr-12"
                autoSize={{ minRows: 2, maxRows: 4 }}
              />
              
              <div className="absolute right-2 bottom-2 flex items-center gap-2">
                <Button
                  type="primary"
                  size="small"
                  shape="circle"
                  onClick={handleSendMessage}
                  disabled={!inputValue.trim() || isLoading}
                >
                  <SendOutlined />
                </Button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ChatInterface;