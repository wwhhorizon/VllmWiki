# vllm-project/vllm#21756: [Bug]: tool call parameters doesn't respect schema for parameters when Streaming=True and tool_choice="auto"

| 字段 | 值 |
| --- | --- |
| Issue | [#21756](https://github.com/vllm-project/vllm/issues/21756) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: tool call parameters doesn't respect schema for parameters when Streaming=True and tool_choice="auto"

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hello. I have started qwen3 coder with following parameters: ``` localhost/vllm/vllm-openai:v0.10.0-coder-toolparser \ --model Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8 \ --disable-log-requests \ --enable-auto-tool-choice --tool-call-parser qwen3_coder \ --tensor-parallel-size 8 \ --enable-prompt-tokens-details \ --enable-expert-parallel ``` Used following client test program ``` from openai import OpenAI from openai.lib.streaming.chat import ChatCompletionStreamState import json client = OpenAI(base_url="http://10.150.255.221:8000/v1", api_key="dummy") tools = [{ "type": "function", "function": { "name": "get_weather", "description": "Get the current weather in a given location", "parameters": { "type": "object", "properties": { "location": {"type": "string", "description": "City and state, e.g., 'San Francisco, CA'"}, "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}, "random": {"type": "number", "description": "A random number to be able to distinguish between requests"} }, "required": ["location", "unit", "random"] } } }, {"type": "function", "function": { "name": "get_water_leve", "description": "Get the current wa...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: ur current environment ### 🐛 Describe the bug Hello. I have started qwen3 coder with following parameters: ``` localhost/vllm/vllm-openai:v0.10.0-coder-toolparser \ --model Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8 \ --di...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: ect schema for parameters when Streaming=True and tool_choice="auto" bug;stale ### Your current environment ### 🐛 Describe the bug Hello. I have started qwen3 coder with following parameters: ``` localhost/vllm/vllm-ope...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: -expert-parallel ``` Used following client test program ``` from openai import OpenAI from openai.lib.streaming.chat import ChatCompletionStreamState import json client = OpenAI(base_url="http://10.150.255.221:8000/v1",...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: :v0.10.0-coder-toolparser \ --model Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8 \ --disable-log-requests \ --enable-auto-tool-choice --tool-call-parser qwen3_coder \ --tensor-parallel-size 8 \ --enable-prompt-tokens-details...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: notebooks (.ipynb files), use the NotebookRead instead\\n- You have the capability to call multiple tools in a single response. It is always better to speculatively read multiple files as a batch that are potentially us...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
