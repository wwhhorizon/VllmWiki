# vllm-project/vllm#24558: [Bug]: Unexpected service down of Llama-4-Scout-17B-16E-Instruct model on GPU-enabled VM

| 字段 | 值 |
| --- | --- |
| Issue | [#24558](https://github.com/vllm-project/vllm/issues/24558) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unexpected service down of Llama-4-Scout-17B-16E-Instruct model on GPU-enabled VM

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug We have deployed the model “Llama-4-Scout-17B-16E-Instruct” on a virtual machine with a GPU card. Our environment details are as follows: OS version: Ubuntu 22.04.5 GPU model: Nvidia A100 vLLM version: 0.10 Recently, we noticed that the model’s service unexpectedly went down. We restarted the model, and it resumed normal operation. However, after running for a period of time, the problem occurred again. We have tried to identify the root cause from the model logs but have not found any clues yet. We start the model using the following command: python -m vllm.entrypoints.openai.api_server --served-model-name Llama-4-Scout-17B-16E-Instruct --model /models/Llama-4-Scout-17B-16E-Instruct --tensor-parallel-size 4 --gpu-memory-utilization 0.9 --max-model-len 131072 --limit-mm-per-prompt.image 10 >> /var/log/vllm/vllm-Llama-4-Scout-17B-16E-Instruct.log & Do you have any ideas on what might be causing this issue? Additionally, I have enclosed the error log for your reference. [error log.txt](https://github.com/user-attachments/files/22247054/error.log.txt) ### Before submitting a new issue... - [x] Make sure you already searched for rele...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ual machine with a GPU card. Our environment details are as follows: OS version: Ubuntu 22.04.5 GPU model: Nvidia A100 vLLM version: 0.10 Recently, we noticed that the model’s service unexpectedly went down. We restarte...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: t details are as follows: OS version: Ubuntu 22.04.5 GPU model: Nvidia A100 vLLM version: 0.10 Recently, we noticed that the model’s service unexpectedly went down. We restarted the model, and it resumed normal operatio...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Unexpected service down of Llama-4-Scout-17B-16E-Instruct model on GPU-enabled VM bug;stale ### Your current environment ### 🐛 Describe the bug We have deployed the model “Llama-4-Scout-17B-16E-Instruct” on a vir...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: rvice down of Llama-4-Scout-17B-16E-Instruct model on GPU-enabled VM bug;stale ### Your current environment ### 🐛 Describe the bug We have deployed the model “Llama-4-Scout-17B-16E-Instruct” on a virtual machine with a...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: support;sampling_logits;speculative_decoding cuda;gemm;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
