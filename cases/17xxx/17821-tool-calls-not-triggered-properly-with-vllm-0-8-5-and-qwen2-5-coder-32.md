# vllm-project/vllm#17821: Tool calls not triggered properly with vLLM 0.8.5 and Qwen2.5-Coder-32B-Instruct-GPTQ-Int4

| 字段 | 值 |
| --- | --- |
| Issue | [#17821](https://github.com/vllm-project/vllm/issues/17821) |
| 状态 | closed |
| 标签 | bug;stale;tool-calling |
| 评论 | 24; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Tool calls not triggered properly with vLLM 0.8.5 and Qwen2.5-Coder-32B-Instruct-GPTQ-Int4

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi team, I am running `vllm` version 0.8.5 with the following launch command: ``` vllm serve Qwen/Qwen2.5-Coder-32B-Instruct-GPTQ-Int4 \ --quantization gptq \ --download-dir /models \ --tensor-parallel-size 4 \ --enable-auto-tool-choice \ --tool-call-parser hermes ``` I am trying to test function calling (tool calling) with the model (`Qwen/Qwen2.5-Coder-32B-Instruct-GPTQ-Int4`), sending the following request body (for example, via Postman): ```json { "model": "Qwen/Qwen2.5-Coder-32B-Instruct-GPTQ-Int4", "messages": [ { "role": "system", "content": "you are helpful ai" }, { "role": "user", "content": "what is the weather in seoul?" } ], "stream": false, "tool_choice": "auto", "tools": [ { "type": "function", "function": { "name": "get_weather", "description": "Get the current weather in a given location", "parameters": { "type": "object", "properties": { "location": { "type": "string", "description": "City and state, e.g., 'San Francisco, CA'" }, "unit": { "type": "string", "enum": [ "celsius", "fahrenheit" ] } }, "required": [ "location", "unit" ] } } } ] } ``` However, I'm seeing the following issue: Instead of getting an actua...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: t environment ### 🐛 Describe the bug Hi team, I am running `vllm` version 0.8.5 with the following launch command: ``` vllm serve Qwen/Qwen2.5-Coder-32B-Instruct-GPTQ-Int4 \ --quantization gptq \ --download-dir /models...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: t triggered properly with vLLM 0.8.5 and Qwen2.5-Coder-32B-Instruct-GPTQ-Int4 bug;stale;tool-calling ### Your current environment ### 🐛 Describe the bug Hi team, I am running `vllm` version 0.8.5 with the following laun...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ed properly with vLLM 0.8.5 and Qwen2.5-Coder-32B-Instruct-GPTQ-Int4 bug;stale;tool-calling ### Your current environment ### 🐛 Describe the bug Hi team, I am running `vllm` version 0.8.5 with the following launch comman...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: e`. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Tool calls not triggered properly with vLLM 0.8.5 and Qwen2.5-Coder-32B-Instruct-GPTQ-Int4 bug;stale;tool-calling ### Your current environment ### 🐛 Describe the bug Hi team, I am running `vllm` version 0.8.5 with the f...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
