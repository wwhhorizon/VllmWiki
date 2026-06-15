# vllm-project/vllm#17481: [Bug]: Tool calling and JSON schema guided generation not working properly on Qwen2.5-72B-AWQ with vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#17481](https://github.com/vllm-project/vllm/issues/17481) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization;sampling_logits |
| 子分类 | kernel_eff |
| Operator 关键词 | quantization |
| 症状 | crash |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Tool calling and JSON schema guided generation not working properly on Qwen2.5-72B-AWQ with vLLM

### Issue 正文摘录

### Your current environment I use the vllm/vllm-openai:v0.8.5 image with 2*A100 40G ### 🐛 Describe the bug ## Environment: • Model: Qwen2.5-72B-Instruct-GPTQ-AWQ • Hardware: 2x A100 40G • vLLM version: v0.8.5 Launch Command: ```bash vllm serve \ --model /data/share/models/Qwen2.5-72B-Instruct-AWQ \ --host 0.0.0.0 \ --port 30000 \ --tensor-parallel-size 2 \ --trust-remote-code \ --served-model-name Qwen2.5-72B-Instruct-GPTQ-AWQ \ --gpu-memory-utilization 0.92 \ --max-model-len 8000 \ --enable-auto-tool-choice \ --tool-call-parser hermes ``` ⸻ ## 🧪 Test 1: Tool Calling with tool_choice="auto" fails to trigger I attempted to use OpenAI-style function calling with a simple get_weather tool and tool_choice="auto". However, the model ignored the tool and responded with a regular message like: "Sure, I can help with that. Do you prefer the temperature in Celsius or Fahrenheit?" Only when I forced the tool via: ```bash tool_choice={"type": "function", "function": {"name": "get_weather"}} ``` did I receive the correct tool_calls structure, e.g.: ```json { "tool_calls": [ { "function": { "name": "get_weather", "arguments": "{\"location\": \"San Francisco, CA\", \"unit\": \"fahrenheit\"}" }...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: • Model: Qwen2.5-72B-Instruct-GPTQ-AWQ • Hardware: 2x A100 40G • vLLM version: v0.8.5 Launch Command: ```bash vllm serve \ --model /data/share/models/Qwen2.5-72B-Instruct-AWQ \ --host 0.0.0.0 \ --port 30000 \ --tensor-p...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Your current environment I use the vllm/vllm-openai:v0.8.5 image with 2*A100 40G ### 🐛 Describe the bug ## Environment: • Model: Qwen2.5-72B-Instruct-GPTQ-AWQ • Hardware: 2x A100 40G • vLLM version: v0.8.5 Launch Comman...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: : Tool calling and JSON schema guided generation not working properly on Qwen2.5-72B-AWQ with vLLM bug;stale ### Your current environment I use the vllm/vllm-openai:v0.8.5 image with 2*A100 40G ### 🐛 Describe the bug ##...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: guided generation not working properly on Qwen2.5-72B-AWQ with vLLM bug;stale ### Your current environment I use the vllm/vllm-openai:v0.8.5 image with 2*A100 40G ### 🐛 Describe the bug ## Environment: • Model: Qwen2.5-...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: d questions. performance distributed_parallel;frontend_api;model_support;quantization;sampling_logits quantization crash Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
