import React, { useEffect, useState } from 'react';
import { Line } from 'react-chartjs-2';
import 'chartjs-adapter-date-fns';

const App = () => {
  const [weatherData, setWeatherData] = useState([]);

  useEffect(() => {
    fetch('/api/weather')
      .then(response => response.json())
      .then(data => setWeatherData(data));
  }, []);

  const data = {
    labels: weatherData.map(item => item.name),
    datasets: [
      {
        label: 'Temperature',
        data: weatherData.map(item => item.temp),
        borderColor: 'rgba(75,192,192,1)',
        backgroundColor: 'rgba(75,192,192,0.2)',
      },
      {
        label: 'Humidity',
        data: weatherData.map(item => item.humidity),
        borderColor: 'rgba(153,102,255,1)',
        backgroundColor: 'rgba(153,102,255,0.2)',
      },
    ],
  };

  return (
    <div>
      <h2>Weather Dashboard</h2>
      <Line data={data} />
    </div>
  );
};

export default App;