import { Line } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Tooltip,
  Legend,
} from 'chart.js';

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Tooltip, Legend);

interface HistoryItem {
  date: string;
  portfolio_value: number;
  long_exposure: number;
  short_exposure: number;
}

interface PortfolioChartProps {
  history: HistoryItem[];
}

export function PortfolioChart({ history }: PortfolioChartProps) {
  if (!history || history.length === 0) {
    return <div className="text-muted-foreground">No metrics available</div>;
  }

  const labels = history.map(h => h.date);

  const data = {
    labels,
    datasets: [
      {
        label: 'Portfolio Value',
        data: history.map(h => h.portfolio_value),
        borderColor: 'rgb(75, 192, 192)',
        backgroundColor: 'rgba(75, 192, 192, 0.4)',
      },
      {
        label: 'Long Exposure',
        data: history.map(h => h.long_exposure),
        borderColor: 'rgb(54, 162, 235)',
        backgroundColor: 'rgba(54, 162, 235, 0.4)',
      },
      {
        label: 'Short Exposure',
        data: history.map(h => h.short_exposure),
        borderColor: 'rgb(255, 99, 132)',
        backgroundColor: 'rgba(255, 99, 132, 0.4)',
      },
    ],
  };

  const options = {
    responsive: true,
    maintainAspectRatio: false,
  } as const;

  return (
    <div className="w-full h-72">
      <Line options={options} data={data} />
    </div>
  );
}
