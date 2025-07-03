import { useNodeContext } from '@/contexts/node-context';
import { PortfolioChart } from '@/components/charts/PortfolioChart';

interface OutputTabProps {
  className?: string;
}

export function OutputTab({ className }: OutputTabProps) {
  const { outputNodeData } = useNodeContext();
  const history = outputNodeData?.portfolio_history || [];

  return (
    <div className={className}>
      <div className="h-full bg-background/50 rounded-md p-3 text-sm overflow-auto">
        {history.length > 0 ? (
          <PortfolioChart history={history} />
        ) : (
          <div className="text-muted-foreground">No output to display</div>
        )}
      </div>
    </div>
  );
}
