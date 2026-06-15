# vllm-project/vllm#24557: [Bug]: Intermittent Service Downtime Issue with Magistral-Small-2506 Model on GPU VM

| 字段 | 值 |
| --- | --- |
| Issue | [#24557](https://github.com/vllm-project/vllm/issues/24557) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Intermittent Service Downtime Issue with Magistral-Small-2506 Model on GPU VM

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug We have deployed the model “Magistral-Small-2506” on a virtual machine with a GPU card. Our environment details are as follows: OS version: Ubuntu 22.04.5 GPU card model: Nvidia A100 vllm version: 0.10 Recently, we noticed that the model service suddenly went down. We restarted the model, and it resumed normal operation. However, after running for a while, the problem occurred again. We tried to identify the root cause by examining the model logs but still have no idea what might be causing the issue. We start the model using the following command: CUDA_LAUNCH_BLOCKING=1 VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 CUDA_VISIBLE_DEVICES=0,1 vllm serve /models/Magistral-Small-2506 --served-model-name Magistral-Small-2506 --tokenizer_mode mistral --config_format mistral --load_format mistral --tool-call-parser mistral --enable-auto-tool-choice --tensor-parallel-size 2 --gpu-memory-utilization 0.9 --port 7999 --max-model-len 131072 >> /var/log/vllm/vllm-Magistral-Small-2506.log & Do you have any idea what might be causing this? Additionally, I have enclosed the error log for your reference. [error log.txt](https://github.com/user-attachments/file...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ual machine with a GPU card. Our environment details are as follows: OS version: Ubuntu 22.04.5 GPU card model: Nvidia A100 vllm version: 0.10 Recently, we noticed that the model service suddenly went down. We restarted...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Intermittent Service Downtime Issue with Magistral-Small-2506 Model on GPU VM bug;stale ### Your current environment ### 🐛 Describe the bug We have deployed the model “Magistral-Small-2506” on a virtual machine w...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Intermittent Service Downtime Issue with Magistral-Small-2506 Model on GPU VM bug;stale ### Your current environment ### 🐛 Describe the bug We have deployed the model “Magistral-Small-2506” on a virtual machine w...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ent Service Downtime Issue with Magistral-Small-2506 Model on GPU VM bug;stale ### Your current environment ### 🐛 Describe the bug We have deployed the model “Magistral-Small-2506” on a virtual machine with a GPU card....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
