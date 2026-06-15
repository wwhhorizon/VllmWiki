# vllm-project/vllm#26431: [Bug]: KV Cache Quantization not working on v1 (rtx3090)  "type fp8e4nv not supported in this architecture"

| 字段 | 值 |
| --- | --- |
| Issue | [#26431](https://github.com/vllm-project/vllm/issues/26431) |
| 状态 | open |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: KV Cache Quantization not working on v1 (rtx3090)  "type fp8e4nv not supported in this architecture"

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug im using the vllm docker image vllm/vllm-openai:v0.11.0 (same configuration worked in v0.10.2 but it had fallback to V0 ) With this command: command: > --model jart25/Qwen3-Coder-30B-A3B-Instruct-Int4-gptq --uvicorn-log-level "info" --gpu-memory-utilization 0.70 --tensor-parallel-size 2 --enable-auto-tool-choice --tool-call-parser "hermes" --max-model-len 128000 --dtype "auto" --kv_cache_dtype fp8_e5m2 It says ValueError("type fp8e4nv not supported in this architecture. The supported fp8 dtypes are ('fp8e4b15', 'fp8e5')") But i never specified fp8e4nv anywhere. it works when i disable kv cache quantization This is the Error including the stacktrace (Had to remove a bit from the end, as im hitting a character limit ): ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: # Your current environment ### 🐛 Describe the bug im using the vllm docker image vllm/vllm-openai:v0.11.0 (same configuration worked in v0.10.2 but it had fallback to V0 ) With this command: command: > --model jart25/Qw...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: KV Cache Quantization not working on v1 (rtx3090) "type fp8e4nv not supported in this architecture" bug ### Your current environment ### 🐛 Describe the bug im using the vllm docker image vllm/vllm-openai:v0.11.0...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: KV Cache Quantization not working on v1 (rtx3090) "type fp8e4nv not supported in this architecture" bug ### Your current environment ### 🐛 Describe the bug im using the vllm docker image vllm/vllm-openai:v0.11.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: e the bug im using the vllm docker image vllm/vllm-openai:v0.11.0 (same configuration worked in v0.10.2 but it had fallback to V0 ) With this command: command: > --model jart25/Qwen3-Coder-30B-A3B-Instruct-Int4-gptq --u...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: llm/vllm-openai:v0.11.0 (same configuration worked in v0.10.2 but it had fallback to V0 ) With this command: command: > --model jart25/Qwen3-Coder-30B-A3B-Instruct-Int4-gptq --uvicorn-log-level "info" --gpu-memory-utili...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
