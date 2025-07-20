# LangGraph DB Assistant 🤖

A local offline database intelligent assistant based on LangGraph and Ollama, powered by DeepSeek-R1:32B model for robust data querying and management capabilities.

## ✨ Features

- 🏠 **Fully Local** - Runs on Ollama, no internet required, protecting data privacy
- 🧠 **Intelligent Reasoning** - Uses ReAct (Reasoning and Acting) pattern for clear logic
- 🛠️ **Tool-Driven** - Interacts with database through dedicated tools, ensuring data accuracy
- 🎬 **Movie Database** - Built-in movie database example with multiple query methods
- 🚀 **High Performance** - DeepSeek-R1:32B model delivers excellent performance with fast and accurate responses

## Example
Question

<img width="388" height="69" alt="image" src="https://github.com/user-attachments/assets/c246a53d-46e3-4798-87c1-e25a5473d2f2" />

Observation

<img width="986" height="169" alt="image" src="https://github.com/user-attachments/assets/ae60c64b-b8b7-4e89-acd3-75995a4e3a2f" />

Result

<img width="539" height="367" alt="image" src="https://github.com/user-attachments/assets/647fda79-c3e8-43ae-b0c2-83374797755d" />


## 🎯 Core Features

### Database Query Tools

1. **Get All Movies** (`get_all_movies`)
   - Returns complete movie list from the database
   - Perfect for browsing and overview scenarios

2. **Search by Title** (`search_movies_by_title`)
   - Supports fuzzy matching and partial title search
   - Intelligently handles typos and case sensitivity

3. **Search by Genre** (`search_movies_by_genre`)
   - Find movies by type/genre
   - Supports Action, Comedy, Drama, Horror and many other genres

## 🚀 Quick Start

### Requirements

- Node.js 18+
- Ollama (with DeepSeek-R1:32B model installed)

### Installation

```bash
# Clone the project
git clone https://github.com/davych/langgraph-db-js.git
cd langgraph-db-js

# Install dependencies
npm install

# Ensure Ollama service is running
ollama serve

# Pull DeepSeek-R1 model (if not already installed)
ollama pull deepseek-r1:32b
```

### Running

```bash
# Start the assistant
npm start
```

## 💬 Usage Examples

### Get All Movies
```
User: "Show me all movies"
Assistant: Uses get_all_movies tool to query database and returns complete movie list
```

### Search Specific Movie
```
User: "Do you have Inception?"
Assistant: Uses search_movies_by_title tool to search for "Inception"
```

### Find by Genre
```
User: "Recommend some action movies"
Assistant: Uses search_movies_by_genre tool to find "action" genre movies
```

## 🏗️ Architecture Design

```
User Input → LangGraph Agent → ReAct Reasoning → Tool Invocation → Database Query → Result Return
```

### Core Components

- **LangGraph**: Workflow orchestration and state management
- **Ollama**: Local large language model service
- **DeepSeek-R1:32B**: Powerful open-source model with strong reasoning capabilities
- **ReAct Pattern**: Think-Act-Observe intelligent reasoning pattern

## 🛠️ Tech Stack

- **Framework**: LangChain.js / LangGraph
- **Model**: DeepSeek-R1:32B (via Ollama)
- **Runtime**: Node.js
- **Database**: Extensible support for multiple databases
- **Tool System**: DynamicTool dynamic tool invocation

## 🎯 Why Choose This Solution?

### Local Advantages
- ✅ Complete data privacy control
- ✅ No network dependency, stable and reliable
- ✅ No API call costs
- ✅ Fast response times

### DeepSeek-R1:32B Advantages
- 🧠 Powerful reasoning capabilities
- 🎯 Excellent instruction following
- 🔧 High accuracy in tool usage
- 💡 Supports complex multi-step reasoning

### ReAct Pattern Advantages
- 🤔 Transparent thinking process
- 🎯 Clear decision logic
- 🛠️ Precise tool usage
- 🔄 Multi-turn interaction support (coming soon)

## 📄 License

MIT License

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

If you encounter any issues or have questions, please open an issue on GitHub.
