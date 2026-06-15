# vllm-project/vllm#43428: [Bug]: Endless '!' output when a long context request is sent on qwen3.5/3.6, B60 gpus

| 字段 | 值 |
| --- | --- |
| Issue | [#43428](https://github.com/vllm-project/vllm/issues/43428) |
| 状态 | open |
| 标签 | bug;intel-gpu |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Endless '!' output when a long context request is sent on qwen3.5/3.6, B60 gpus

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug All vllm serve cases are affected except parallelism(not including dp) is disabled. e.g ```bash vllm serve "/data/models/Qwen3.6-27B-GPTQ-Pro-4bit/" --dtype=bfloat16 --port 8000 --gpu-memory-util 0.9 --served-model-name qwen3.6-27b --enable-auto-tool-choice --reasoning-parser qwen3 --tool-call-parser qwen3_xml -cc.cudagraph_mode=full -tp=2 -dp=2 vllm serve "/data/models/Qwen3.6-27B" --dtype=bfloat16 --port 8000 --gpu-memory-util 0.9 --served-model-name qwen3.6-27b --enable-auto-tool-choice --reasoning-parser qwen3 --tool-call-parser qwen3_xml --enforce-eager -tp=4 ``` are affected. ```bash vllm serve "/data/models/Qwen3.5-9B/" --dtype=bfloat16 --port 8000 --gpu-memory-util 0.9 --served-model-name qwen3.6-27b --enable-auto-tool-choice --reasoning-parser qwen3 --tool-call-parser qwen3_xml -dp=4 ``` This won't cause the problem. When a small context request is sent, vllm works perfect. When a large context one is sent, it will cause ALL concurrent requests to generate infinite "!!!!!!!!!!!.....". ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: d. e.g ```bash vllm serve "/data/models/Qwen3.6-27B-GPTQ-Pro-4bit/" --dtype=bfloat16 --port 8000 --gpu-memory-util 0.9 --served-model-name qwen3.6-27b --enable-auto-tool-choice --reasoning-parser qwen3 --tool-call-parse...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;kernel;operator;q...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ## 🐛 Describe the bug All vllm serve cases are affected except parallelism(not including dp) is disabled. e.g ```bash vllm serve "/data/models/Qwen3.6-27B-GPTQ-Pro-4bit/" --dtype=bfloat16 --port 8000 --gpu-memory-util 0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Endless '!' output when a long context request is sent on qwen3.5/3.6, B60 gpus bug;intel-gpu ### Your current environment ### 🐛 Describe the bug All vllm serve cases are affected except parallelism(not including...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Endless '!' output when a long context request is sent on qwen3.5/3.6, B60 gpus bug;intel-gpu ### Your current environment ### 🐛 Describe the bug All vllm serve cases are affected except parallelism(not including...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
