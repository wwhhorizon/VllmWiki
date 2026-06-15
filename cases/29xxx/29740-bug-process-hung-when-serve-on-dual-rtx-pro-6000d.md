# vllm-project/vllm#29740: [Bug]: process hung when serve on dual RTX Pro 6000D

| 字段 | 值 |
| --- | --- |
| Issue | [#29740](https://github.com/vllm-project/vllm/issues/29740) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: process hung when serve on dual RTX Pro 6000D

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug NCCL_DEBUG=INFO CUDA_DEVICE_ORDER=PCI_BUS_ID CUDA_VISIBLE_DEVICES=0,1 vllm serve Qwen3-8B --tensor-parallel-size 2 --tool-call-parser hermes --enable-auto-tool-choice --max-num-seqs 130 --gpu-memory-utilization 0.9 --port 8000 (EngineCore_DP0 pid=23762) INFO 11-30 12:30:59 [shm_broadcast.py:466] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation). ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: vironment ### 🐛 Describe the bug NCCL_DEBUG=INFO CUDA_DEVICE_ORDER=PCI_BUS_ID CUDA_VISIBLE_DEVICES=0,1 vllm serve Qwen3-8B --tensor-parallel-size 2 --tool-call-parser hermes --enable-auto-tool-choice --max-num-seqs 130...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: process hung when serve on dual RTX Pro 6000D bug ### Your current environment ### 🐛 Describe the bug NCCL_DEBUG=INFO CUDA_DEVICE_ORDER=PCI_BUS_ID CUDA_VISIBLE_DEVICES=0,1 vllm serve Qwen3-8B --tensor-parallel-si...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: -30 12:30:59 [shm_broadcast.py:466] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation). ### Before...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: UG=INFO CUDA_DEVICE_ORDER=PCI_BUS_ID CUDA_VISIBLE_DEVICES=0,1 vllm serve Qwen3-8B --tensor-parallel-size 2 --tool-call-parser hermes --enable-auto-tool-choice --max-num-seqs 130 --gpu-memory-utilization 0.9 --port 8000...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency;memory_layout Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
