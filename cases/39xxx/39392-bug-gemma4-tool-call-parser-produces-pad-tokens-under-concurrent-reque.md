# vllm-project/vllm#39392: [Bug]: Gemma4 tool-call-parser produces <pad> tokens under concurrent requests

| 字段 | 值 |
| --- | --- |
| Issue | [#39392](https://github.com/vllm-project/vllm/issues/39392) |
| 状态 | open |
| 标签 | bug |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Gemma4 tool-call-parser produces <pad> tokens under concurrent requests

### Issue 正文摘录

### Your current environment - vLLM Docker image: vllm/vllm-openai:gemma4 - GPU: 8× NVIDIA GeForce RTX 4090 (24GB each) - OS: Ubuntu 24.04 LTS - Model: google/gemma-4-31B-it - tensor-parallel-size: 8 - max-model-len: 196608 ### 🐛 Describe the bug ## Bug Description When multiple requests with tool calling are sent **concurrently** to vLLM using `--tool-call-parser gemma4`, some requests produce outputs filled entirely with ` ` tokens (e.g., 4096 ` ` tokens). The same requests succeed 100% of the time when sent **sequentially**. ## Reproduction Steps ### 1. Define tools and system prompt ```python from openai import OpenAI import concurrent.futures client = OpenAI(base_url="http://localhost:8000/v1", api_key="your-api-key") tools = [ { "type": "function", "function": { "name": "regex_scan", "description": "Scan text for sensitive patterns like IP addresses, passwords, API keys.", "parameters": { "type": "object", "properties": { "scope": {"type": "string", "default": "all"} }, } } } ] system_prompt = "You are a security reviewer. Analyze the given text and call tools to check for sensitive information, then output a JSON report." # Use any long-ish content (10K+ characters) content...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Gemma4 tool-call-parser produces <pad> tokens under concurrent requests bug ### Your current environment - vLLM Docker image: vllm/vllm-openai:gemma4 - GPU: 8× NVIDIA GeForce RTX 4090 (24GB each) - OS: Ubuntu 24....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: okens under concurrent requests bug ### Your current environment - vLLM Docker image: vllm/vllm-openai:gemma4 - GPU: 8× NVIDIA GeForce RTX 4090 (24GB each) - OS: Ubuntu 24.04 LTS - Model: google/gemma-4-31B-it - tensor-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: t - vLLM Docker image: vllm/vllm-openai:gemma4 - GPU: 8× NVIDIA GeForce RTX 4090 (24GB each) - OS: Ubuntu 24.04 LTS - Model: google/gemma-4-31B-it - tensor-parallel-size: 8 - max-model-len: 196608 ### 🐛 Describe the bug...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: g-ish content (10K+ characters) content = "..." ``` ### 2. Sequential test — 5/5 pass ```python for i in range(5): resp = client.chat.completions.create( model="gemma4-31b", messages=[ {"role": "system", "content": syst...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: h={reason}") ``` **Result: 2/5 produce ` ` output.** ``` #4: pad=False, len=217, finish=stop #2: pad=False, len=204, finish=stop #0: pad=False, len=209, finish=stop #1: pad=True, len=20480, finish=no_tools ← filled enti...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
