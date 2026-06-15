# vllm-project/vllm#13139: [Bug]:  vllm 0.7.2 call server wrong

| 字段 | 值 |
| --- | --- |
| Issue | [#13139](https://github.com/vllm-project/vllm/issues/13139) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:  vllm 0.7.2 call server wrong

### Issue 正文摘录

### Your current environment vllm 0.7.2 torch 2.5.1 openai 1.61.1 ### 🐛 Describe the bug CUDA_VISIBLE_DEVICES=3,4,5 vllm serve ./DeepSeek-R1-Distill-Qwen-7B --host 0.0.0.0 --port 8000 then run code in vllm/examples []( import argparse import gradio as gr from openai import OpenAI # Argument parser setup parser = argparse.ArgumentParser( description='Chatbot Interface with Customizable Parameters') parser.add_argument('--model-url', type=str, default='http://localhost:8000/v1', help='Model URL') parser.add_argument('-m', '--model', type=str, required=True, help='Model name for the chatbot') parser.add_argument('--temp', type=float, default=0.8, help='Temperature for text generation') parser.add_argument('--stop-token-ids', type=str, default='', help='Comma-separated stop token IDs') parser.add_argument("--host", type=str, default=None) parser.add_argument("--port", type=int, default=8001) # Parse the arguments args = parser.parse_args() # Set OpenAI's API key and API base to use vLLM's API server. openai_api_key = "EMPTY" openai_api_base = args.model_url # Create an OpenAI client to interact with the API server client = OpenAI( api_key=openai_api_key, base_url=openai_api_base, ) de...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: the bug CUDA_VISIBLE_DEVICES=3,4,5 vllm serve ./DeepSeek-R1-Distill-Qwen-7B --host 0.0.0.0 --port 8000 then run code in vllm/examples []( import argparse
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: vllm 0.7.2 call server wrong bug;stale ### Your current environment vllm 0.7.2 torch 2.5.1 openai 1.61.1 ### 🐛 Describe the bug CUDA_VISIBLE_DEVICES=3,4,5 vllm serve ./DeepSeek-R1-Distill-Qwen-7B --host 0.0.0.0 -...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: import argparse import gradio as gr
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: onment vllm 0.7.2 torch 2.5.1 openai 1.61.1 ### 🐛 Describe the bug CUDA_VISIBLE_DEVICES=3,4,5 vllm serve ./DeepSeek-R1-Distill-Qwen-7B --host 0.0.0.0 --port 8000 then run code in vllm/examples []( import a
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ] if args.stop_token_ids else [] })

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
