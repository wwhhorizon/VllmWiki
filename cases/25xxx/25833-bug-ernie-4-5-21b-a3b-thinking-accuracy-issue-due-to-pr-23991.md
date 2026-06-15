# vllm-project/vllm#25833: [Bug]: ERNIE-4.5-21B-A3B-Thinking accuracy issue due to PR 23991

| 字段 | 值 |
| --- | --- |
| Issue | [#25833](https://github.com/vllm-project/vllm/issues/25833) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: ERNIE-4.5-21B-A3B-Thinking accuracy issue due to PR 23991

### Issue 正文摘录

### Your current environment H800 GPU ### 🐛 Describe the bug start server ``` vllm serve baidu/ERNIE-4.5-21B-A3B-Thinking \ --served-model-name ERNIE-4.5-21B-A3B-Thinking \ --port 8508 \ --max-model-len 32768 \ --reasoning-parser deepseek_r1 ``` test script ```python from openai import OpenAI import argparse # Set OpenAI's API key and API base to use vLLM's API server. # 解析命令行参数 parser = argparse.ArgumentParser(description="Run OpenAI client with custom API base.") parser.add_argument( "--api-base", type=str, default="http://127.0.0.1:8508/v1", help="OpenAI API base URL (e.g. http://127.0.0.1:8508/v1)" ) args = parser.parse_args() openai_api_key = "EMPTY" openai_api_base = args.api_base client = OpenAI( api_key=openai_api_key, base_url=openai_api_base, ) tools = [ { "type": "function", "function": { "strict": True, "name": "get_current_temperature", "description": "Get current temperature at a location.", "parameters": { "type": "object", "properties": { "location": { "type": "string", "description": 'The location to get the temperature for, in the format "City, State, Country".', }, "unit": { "type": "string", "enum": ["celsius", "fahrenheit"], "description": 'The unit to return...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: \ --reasoning-parser deepseek_r1 ``` test script ```python from openai import OpenAI import argparse # Set OpenAI's API key and API base to use vLLM's API server. # 解析命令行参数 parser = argparse.ArgumentParser(description="...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: start server ``` vllm serve baidu/ERNIE-4.5-21B-A3B-Thinking \ --served-model-name ERNIE-4.5-21B-A3B-Thinking \ --port 8508 \ --max-model-len 32768 \ --reasoning-parser deepseek_r1 ``` test script ```python from openai...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: ERNIE-4.5-21B-A3B-Thinking accuracy issue due to PR 23991 bug ### Your current environment H800 GPU ### 🐛 Describe the bug start server ``` vllm serve baidu/ERNIE-4.5-21B-A3B-Thinking \ --served-model-name ERNIE-...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: ERNIE-4.5-21B-A3B-Thinking accuracy issue due to PR 23991 bug ### Your current environment H800 GPU ### 🐛 Describe the bug start server ``` vllm serve baidu/ERNIE-4.5-21B-A3B-Thinking \ --served-model-name ERNIE-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
