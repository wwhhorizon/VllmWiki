# vllm-project/vllm#28173: [Bug]: Tool use is not supported in Responses API without Harmony None

| 字段 | 值 |
| --- | --- |
| Issue | [#28173](https://github.com/vllm-project/vllm/issues/28173) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Tool use is not supported in Responses API without Harmony None

### Issue 正文摘录

### Your current environment python -m vllm.entrypoints.openai.api_server \ --model Qwen/Qwen3-4B \ --max-model-len 8192 \ --dtype bfloat16 \ --port 23333 --host 0.0.0.0 \ --enable-auto-tool-choice \ --tool-call-parser qwen3_coder vllm version 0.11.0 openai version 2.7.1 client.py client = OpenAI(api_key=openai_api_key, base_url=base_url) resp = client.responses.create( model=model_name, tools=[ { "type": "mcp", "server_label": "1111", "server_url": f"{mcp_url}/mcp/", "require_approval": "never", }, ], tool_choice="auto", input="Roll a few dice!", instructions=""" You are a helpful assistant. You can use the following tools: - mcp: A tool for rolling dice. """, stream=True # input=[{"role": "user", "content": "What's the weather like in Paris today?"}], ) print(resp.output_text) ### 🐛 Describe the bug 1 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: \ --model Qwen/Qwen3-4B \ --max-model-len 8192 \ --dtype bfloat16 \ --port 23333 --host 0.0.0.0 \ --enable-auto-tool-choice \ --tool-call-parser qwen3_coder vllm version 0.11.0 openai version 2.7.1 client.py client = Op...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: environment python -m vllm.entrypoints.openai.api_server \ --model Qwen/Qwen3-4B \ --max-model-len 8192 \ --dtype bfloat16 \ --port 23333 --host 0.0.0.0 \ --enable-auto-tool-choice \ --tool-call-parser qwen3_coder vllm...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: --enable-auto-tool-choice \ --tool-call-parser qwen3_coder vllm version 0.11.0 openai version 2.7.1 client.py client = OpenAI(api_key=openai_api_key, base_url=base_url) resp = client.responses.create( model=model_name,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 1 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ug]: Tool use is not supported in Responses API without Harmony None bug;stale ### Your current environment python -m vllm.entrypoints.openai.api_server \ --model Qwen/Qwen3-4B \ --max-model-len 8192 \ --dtype bfloat16...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
