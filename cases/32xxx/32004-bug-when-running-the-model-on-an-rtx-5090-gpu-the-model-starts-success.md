# vllm-project/vllm#32004: [Bug]: When running the model on an RTX 5090 GPU, the model starts successfully, but the CPU usage remains at 100%.

| 字段 | 值 |
| --- | --- |
| Issue | [#32004](https://github.com/vllm-project/vllm/issues/32004) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: When running the model on an RTX 5090 GPU, the model starts successfully, but the CPU usage remains at 100%.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **Issue Description** When running the model on an RTX 5090 GPU, the model starts successfully, but the CPU usage remains at 100%. * After startup, **even without any incoming requests**, the CPU usage stays at 100%. * When requests are sent, the CPU usage is still 100%. * After all requests finish, the CPU usage **does not decrease** and remains at 100%. This behavior persists continuously and does not recover automatically. **Startup Command** ```bash CUDA_VISIBLE_DEVICES=0,1,2,3 nohup vllm serve /data/models/Qwen3-30B-A3B-Instruct-2507/ \ --tensor-parallel-size 4 \ --gpu-memory-utilization 0.85 \ --port 11434 \ --served-model-name Qwen3-30B-A3B-Instruct-2507 \ --enable-prefix-caching \ --enable-auto-tool-choice \ --tool-call-parser hermes \ 1>/data/lj/vllm_logs/vllm_30_a3b_i.log 2>&1 & ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: When running the model on an RTX 5090 GPU, the model starts successfully, but the CPU usage remains at 100%. bug ### Your current environment ### 🐛 Describe the bug **Issue Description** When running the model on...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: When running the model on an RTX 5090 GPU, the model starts successfully, but the CPU usage remains at 100%. bug ### Your current environment ### 🐛 Describe the bug **Issue Description** When running the model on...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: CPU usage remains at 100%. * After startup, **even without any incoming requests**, the CPU usage stays at 100%. * When requests are sent, the CPU usage is still 100%. * After all requests finish, the CPU usage **does n...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
