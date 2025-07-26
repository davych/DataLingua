"use client"

import { useState } from "react"
import { BarChart3, LineChart, PieChart, Download, Share2, Table, Search, User, Settings, LogOut } from "lucide-react"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Textarea } from "@/components/ui/textarea"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"
import { Badge } from "@/components/ui/badge"
import { ChartContainer, ChartTooltip, ChartTooltipContent } from "@/components/ui/chart"
import {
  Bar,
  BarChart,
  Line,
  LineChart as RechartsLineChart,
  Pie,
  PieChart as RechartsPieChart,
  Cell,
  XAxis,
  YAxis,
  CartesianGrid,
} from "recharts"

const sampleData = [
  { month: "Jan", sales: 4000, revenue: 2400 },
  { month: "Feb", sales: 3000, revenue: 1398 },
  { month: "Mar", sales: 2000, revenue: 9800 },
  { month: "Apr", sales: 2780, revenue: 3908 },
  { month: "May", sales: 1890, revenue: 4800 },
  { month: "Jun", sales: 2390, revenue: 3800 },
]

const pieData = [
  { name: "Desktop", value: 400, fill: "#2563eb" },
  { name: "Mobile", value: 300, fill: "#3b82f6" },
  { name: "Tablet", value: 200, fill: "#60a5fa" },
  { name: "Other", value: 100, fill: "#93c5fd" },
]

const chartConfig = {
  sales: {
    label: "Sales",
    color: "#2563eb",
  },
  revenue: {
    label: "Revenue",
    color: "#3b82f6",
  },
}

export default function Dashboard() {
  const [query, setQuery] = useState("")
  const [activeChart, setActiveChart] = useState("")
  const [isLoading, setIsLoading] = useState(false)
  const [hasResults, setHasResults] = useState(false)
  const [data, setData] = useState<any[]>([])
  const [chartTypes, setChartTypes] = useState<any[]>([])

  const handleQuery = async () => {
    if (!query.trim()) return
    setIsLoading(true)
    setHasResults(false)
    try {
      const res = await fetch("http://localhost:8000/query", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: query })
      })
      if (!res.ok) throw new Error("后端接口请求失败")
      const result = await res.json()
      setData(result.data || [])
      setChartTypes(result.chartTypes || [])
      setActiveChart((result.chartTypes && result.chartTypes[0]) || "table")
      setHasResults(true)
    } catch (e) {
      alert("查询失败: " + (e as any).message)
    }
    setIsLoading(false)
  }

  const chartTypeMeta = [
    { id: "bar", label: "Bar Chart", icon: BarChart3 },
    { id: "line", label: "Line Chart", icon: LineChart },
    { id: "pie", label: "Pie Chart", icon: PieChart },
    { id: "table", label: "Table", icon: Table },
  ]

  // 动态获取表头和数值字段
  const getFieldKeys = () => {
    if (!data.length) return []
    return Object.keys(data[0])
  }

  const renderChart = () => {
    if (!data.length) return null
    const keys = getFieldKeys()
    if (keys.length < 2) return null
    switch (activeChart) {
      case "bar":
        return (
          <ChartContainer config={{}} className="h-[400px]">
            <BarChart data={data}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey={keys[0]} />
              <YAxis />
              <ChartTooltip content={<ChartTooltipContent />} />
              <Bar dataKey={keys[1]} fill="#2563eb" radius={4} />
            </BarChart>
          </ChartContainer>
        )
      case "line":
        return (
          <ChartContainer config={{}} className="h-[400px]">
            <RechartsLineChart data={data}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey={keys[0]} />
              <YAxis />
              <ChartTooltip content={<ChartTooltipContent />} />
              <Line type="monotone" dataKey={keys[1]} stroke="#2563eb" strokeWidth={3} />
            </RechartsLineChart>
          </ChartContainer>
        )
      case "pie":
        return (
          <ChartContainer config={{}} className="h-[400px]">
            <RechartsPieChart>
              <Pie
                data={data}
                cx="50%"
                cy="50%"
                outerRadius={120}
                dataKey={keys[1]}
                nameKey={keys[0]}
                label={({ name, percent }) => `${name} ${(percent * 100).toFixed(0)}%`}
              >
                {data.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill="#2563eb" />
                ))}
              </Pie>
              <ChartTooltip content={<ChartTooltipContent />} />
            </RechartsPieChart>
          </ChartContainer>
        )
      case "table":
      default:
        return null
    }
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Top Navigation */}
      <nav className="bg-white border-b border-gray-200 px-4 py-3">
        <div className="max-w-7xl mx-auto flex items-center justify-between">
          <div className="flex items-center space-x-3">
            <div className="w-8 h-8 bg-blue-600 rounded-lg flex items-center justify-center">
              <BarChart3 className="w-5 h-5 text-white" />
            </div>
            <span className="text-xl font-semibold text-gray-900">DataViz AI</span>
          </div>

          <DropdownMenu>
            <DropdownMenuTrigger asChild>
              <Button variant="ghost" className="relative h-10 w-10 rounded-full">
                <Avatar className="h-10 w-10">
                  <AvatarImage src="/placeholder.svg?height=40&width=40" alt="User" />
                  <AvatarFallback>JD</AvatarFallback>
                </Avatar>
              </Button>
            </DropdownMenuTrigger>
            <DropdownMenuContent className="w-56" align="end" forceMount>
              <div className="flex items-center justify-start gap-2 p-2">
                <div className="flex flex-col space-y-1 leading-none">
                  <p className="font-medium">John Doe</p>
                  <p className="w-[200px] truncate text-sm text-muted-foreground">john.doe@company.com</p>
                </div>
              </div>
              <DropdownMenuSeparator />
              <DropdownMenuItem>
                <User className="mr-2 h-4 w-4" />
                <span>Profile</span>
              </DropdownMenuItem>
              <DropdownMenuItem>
                <Settings className="mr-2 h-4 w-4" />
                <span>Settings</span>
              </DropdownMenuItem>
              <DropdownMenuSeparator />
              <DropdownMenuItem>
                <LogOut className="mr-2 h-4 w-4" />
                <span>Log out</span>
              </DropdownMenuItem>
            </DropdownMenuContent>
          </DropdownMenu>
        </div>
      </nav>

      <div className="max-w-7xl mx-auto p-4 space-y-6">
        {/* Main Input Area */}
        <Card className="shadow-sm">
          <CardHeader>
            <CardTitle className="text-2xl font-semibold text-gray-900">Ask your data anything</CardTitle>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="relative">
              <Textarea
                placeholder="Enter your data analysis question... (e.g., 'Show me sales trends by month' or 'Compare revenue across regions')"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                className="min-h-[120px] text-base resize-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                disabled={isLoading}
              />
            </div>
            <div className="flex justify-end">
              <Button
                onClick={handleQuery}
                disabled={!query.trim() || isLoading}
                className="bg-blue-600 hover:bg-blue-700 text-white px-8 py-2 text-base font-medium transition-colors"
              >
                {isLoading ? (
                  <>
                    <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-white mr-2"></div>
                    Analyzing...
                  </>
                ) : (
                  <>
                    <Search className="mr-2 h-4 w-4" />
                    Query
                  </>
                )}
              </Button>
            </div>
          </CardContent>
        </Card>

        {/* Results Area */}
        {hasResults && (
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
            {/* Chart Display Panel */}
            <div className="lg:col-span-2">
              <Card className="shadow-sm">
                <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-4">
                  <CardTitle className="text-lg font-semibold">Sales & Revenue Analysis</CardTitle>
                  <div className="flex items-center space-x-2">
                    <Button variant="outline" size="sm">
                      <Download className="mr-2 h-4 w-4" />
                      Export
                    </Button>
                    <Button variant="outline" size="sm">
                      <Share2 className="mr-2 h-4 w-4" />
                      Share
                    </Button>
                  </div>
                </CardHeader>
                <CardContent>
                  {/* Chart Type Switcher */}
                  <div className="flex items-center space-x-2 mb-6">
                    <span className="text-sm font-medium text-gray-700">Chart Type:</span>
                    {chartTypes.map((type) => {
                      const meta = chartTypeMeta.find((m) => m.id === type) || chartTypeMeta[0]
                      const Icon = meta.icon
                      return (
                        <Button
                          key={type}
                          variant={activeChart === type ? "default" : "outline"}
                          size="sm"
                          onClick={() => setActiveChart(type)}
                          className={`transition-all ${
                            activeChart === type ? "bg-blue-600 hover:bg-blue-700 text-white" : "hover:bg-gray-50"
                          }`}
                        >
                          <Icon className="mr-2 h-4 w-4" />
                          {meta.label}
                        </Button>
                      )
                    })}
                  </div>

                  {/* Chart Display */}
                  <div className="bg-white rounded-lg border p-4">{renderChart()}</div>
                </CardContent>
              </Card>
            </div>

            {/* Data Table and Insights */}
            <div className="space-y-6">
              {/* Key Insights */}
              <Card className="shadow-sm">
                <CardHeader>
                  <CardTitle className="text-lg font-semibold">Key Insights</CardTitle>
                </CardHeader>
                <CardContent className="space-y-3">
                  <div className="flex items-center space-x-2">
                    <Badge variant="secondary" className="bg-green-100 text-green-800">
                      Trend
                    </Badge>
                    <span className="text-sm">Revenue peaked in March</span>
                  </div>
                  <div className="flex items-center space-x-2">
                    <Badge variant="secondary" className="bg-blue-100 text-blue-800">
                      Growth
                    </Badge>
                    <span className="text-sm">15% increase from Q1 to Q2</span>
                  </div>
                  <div className="flex items-center space-x-2">
                    <Badge variant="secondary" className="bg-orange-100 text-orange-800">
                      Alert
                    </Badge>
                    <span className="text-sm">Sales dip in May needs attention</span>
                  </div>
                </CardContent>
              </Card>

              {/* Data Table */}
              <Card className="shadow-sm">
                <CardHeader>
                  <CardTitle className="text-lg font-semibold flex items-center">
                    <Table className="mr-2 h-4 w-4" />
                    Data Table
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="overflow-x-auto">
                    <table className="w-full text-sm">
                      <thead>
                        <tr className="border-b">
                          {getFieldKeys().map((key, idx) => (
                            <th
                              key={key}
                              className={idx === 0 ? "text-left py-2 font-medium text-gray-700" : "text-right py-2 font-medium text-gray-700"}
                            >
                              {key}
                            </th>
                          ))}
                        </tr>
                      </thead>
                      <tbody>
                        {data.length > 0 &&
                          data.map((row, index) => (
                            <tr key={index} className="border-b hover:bg-gray-50 transition-colors">
                              {getFieldKeys().map((key, i) => (
                                <td key={i} className={i === 0 ? "py-2 font-medium" : "text-right py-2"}>{row[key]}</td>
                              ))}
                            </tr>
                          ))}
                      </tbody>
                    </table>
                  </div>
                </CardContent>
              </Card>
            </div>
          </div>
        )}

        {/* Empty State */}
        {!hasResults && !isLoading && (
          <Card className="shadow-sm">
            <CardContent className="text-center py-12">
              <BarChart3 className="mx-auto h-12 w-12 text-gray-400 mb-4" />
              <h3 className="text-lg font-medium text-gray-900 mb-2">Ready to analyze your data</h3>
              <p className="text-gray-600 max-w-md mx-auto">
                Enter a natural language question about your data above to get started. I'll create visualizations and
                insights automatically.
              </p>
            </CardContent>
          </Card>
        )}
      </div>
    </div>
  )
}
