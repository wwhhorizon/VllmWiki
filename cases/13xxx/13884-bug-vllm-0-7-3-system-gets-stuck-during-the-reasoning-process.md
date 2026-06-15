# vllm-project/vllm#13884: [Bug]: vllm 0.7.3, system gets stuck during the reasoning process

| 字段 | 值 |
| --- | --- |
| Issue | [#13884](https://github.com/vllm-project/vllm/issues/13884) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cache;cuda;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm 0.7.3, system gets stuck during the reasoning process

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug use vllm 0.7.3 `export CUDA_VISIBLE_DEVICES=1,2` `export VLLM_USER_V1=1` `vllm serve '/data/1/models/deepseek/DeepSeek-R1-Distill-Qwen-32B' --served-model-name deepseek-32b --host 0.0.0.0 --port 9581 --max-model-len 81920 --gpu_memory_utilization 0.6 --tensor-parallel-size 2 --quantization awq_marlin --block-size 32 --max-num-batched-tokens 81920 --enable-prefix-caching --uvicorn-log-level debug` Currently, there is occasionally an issue where the system gets stuck during the reasoning process. Specifically, this manifests as repetitive output in the reasoning process, such as "**examples, examples, examples, examples, examples, examples, examples, examples...**," with the GPU KV cache usage gradually increasing. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: y an issue where the system gets stuck during the reasoning process. Specifically, this manifests as repetitive output in the reasoning process, such as "**examples, examples, examples, examples, examples, examples, exa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: r current environment ### 🐛 Describe the bug use vllm 0.7.3 `export CUDA_VISIBLE_DEVICES=1,2` `export VLLM_USER_V1=1` `vllm serve '/data/1/models/deepseek/DeepSeek-R1-Distill-Qwen-32B' --served-model-name deepseek-32b -...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ilization 0.6 --tensor-parallel-size 2 --quantization awq_marlin --block-size 32 --max-num-batched-tokens 81920 --enable-prefix-caching --uvicorn-log-level debug` Currently, there is occasionally an issue where the syst...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: t CUDA_VISIBLE_DEVICES=1,2` `export VLLM_USER_V1=1` `vllm serve '/data/1/models/deepseek/DeepSeek-R1-Distill-Qwen-32B' --served-model-name deepseek-32b --host 0.0.0.0 --port 9581 --max-model-len 81920 --gpu_memory_utili...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ware_porting;model_support;quantization cache;cuda;operator;quantization;triton build_error env_dependency;memory_layout Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
