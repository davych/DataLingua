import React, { useCallback } from "react";
import { Typography, Avatar, Table, Card } from "antd";
import { MessageOutlined } from "@ant-design/icons";

export const AiMessage: React.FC<{ content: string }> = ({ content }) => {
  const uiRender = useCallback(() => {
    let parsedContent;
    try {
      parsedContent = JSON.parse(content);
    } catch {
      return content;
    }
    if (parsedContent?.follow_up) {
      return parsedContent.follow_up;
    }
    const result = parsedContent?.result;
    if (Array.isArray(result) && result.length > 0 && typeof result[0] === 'object') {
      const columns = Object.keys(result[0]).map((key) => ({
        title: key,
        dataIndex: key,
        key,
      }));
      const dataSource = result.map((row, idx) => ({ key: idx, ...row }));
      return (
        <Card >
          <Table
            columns={columns}
            dataSource={dataSource}
            pagination={false}
            bordered
          />
        </Card>
      );
    }
    if (typeof result === 'string') {
      return result;
    }
    return result ? JSON.stringify(result) : '';
  }, [content]);

  return (
    <div className="flex gap-3 justify-start">
      <Avatar
        size={32}
        className="!bg-blue-500 flex items-center justify-center flex-shrink-0"
      >
        <MessageOutlined className="!text-white" />
      </Avatar>
      <div className="bg-gray-700 !text-gray-100 px-4 py-3 rounded-lg mr-12">
        <Typography.Text className="!text-gray-100">{uiRender()}</Typography.Text>
      </div>
    </div>
  );
};
