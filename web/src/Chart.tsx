import React from 'react';
import { Pie } from '@ant-design/charts';
const Chart: React.FC = ({ msg }) => {
    console.log('msg', msg);
    const data = msg.visualContent?.visualization?.data || [];
    const config = {
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
  }
    return <div className='bg-white'><Pie {...config} /></div>;
};

export default Chart;