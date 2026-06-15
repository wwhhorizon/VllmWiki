# vllm-project/vllm#9330: QWEN2-VL Model Inference

| 字段 | 值 |
| --- | --- |
| Issue | [#9330](https://github.com/vllm-project/vllm/issues/9330) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> QWEN2-VL Model Inference

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The script to start the service ``` python -m vllm.entrypoints.openai.api_server \ --served-model-name Qwen2-VL-7B-Instruct \ --model /data/CodeSpace/models/Qwen2-VL-7B-Instruct \ --dtype float16 \ --port ${deploy_port} \ --gpu-memory-utilization 0.998 \ --enable-prefix-caching ``` v100 machine, qwen2-vl model, 7b model takes 2.47s per image, 2b model takes 2.3s per image. Is this as expected, why is 2b model only a little faster than 7b model ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;hardware_porting;model_support cuda;operator;triton build_error dtype;env_dependency Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: Instruct \ --model /data/CodeSpace/models/Qwen2-VL-7B-Instruct \ --dtype float16 \ --port ${deploy_port} \ --gpu-memory-utilization 0.998 \ --enable-prefix-caching ``` v100 machine, qwen2-vl model, 7b model takes 2.47s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: del ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: QWEN2-VL Model Inference bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The script to start the service ``` python -m vllm.entrypoints.openai.api_server \ --served-m
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: _build;distributed_parallel;hardware_porting;model_support cuda;operator;triton build_error dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
