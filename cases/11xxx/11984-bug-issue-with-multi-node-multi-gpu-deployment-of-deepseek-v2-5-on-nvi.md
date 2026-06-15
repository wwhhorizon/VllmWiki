# vllm-project/vllm#11984: [Bug]: Issue with Multi-Node Multi-GPU Deployment of DeepSeek-v2.5 on NVIDIA 4090

| 字段 | 值 |
| --- | --- |
| Issue | [#11984](https://github.com/vllm-project/vllm/issues/11984) |
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

> [Bug]: Issue with Multi-Node Multi-GPU Deployment of DeepSeek-v2.5 on NVIDIA 4090

### Issue 正文摘录

### Your current environment ### Model Input Dumps https://gist.github.com/R-Tars/de721273ce29a369489b46fd76f56cab [err_execute_model_input_20250112-194758.zip](https://github.com/user-attachments/files/18392520/err_execute_model_input_20250112-194758.zip) ### 🐛 Describe the bug #### Description: Hello, I encountered an issue while trying to deploy **DeepSeek-V2.5** using **VLLM** across multiple nodes and multiple GPUs. The deployment was conducted on machines equipped with RTX 4090 GPUs, and I used the following command for setup: ```bash vllm serve /model/DeepSeek-V2.5-1210 \ --tensor-parallel-size 8 \ --pipeline-parallel-size 3 \ --trust_remote_code \ --enforce-eager ``` However, the deployment did not succeed as expected, and I received the following error message: ``` https://gist.github.com/R-Tars/de721273ce29a369489b46fd76f56cab ``` #### Environment: - **Model**: DeepSeek-V2.5-1210 - **Inference Framework**: VLLM - **Hardware**: RTX 4090 - **Deployment Configuration**: - Tensor parallel size: 8 - Pipeline parallel size: 3 #### Additional Notes: Could you please provide guidance on resolving this issue? Any help would be greatly appreciated! ### Before submitting a new issu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: provide guidance on resolving this issue? Any help would be greatly appreciated! ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: nd multiple GPUs. The deployment was conducted on machines equipped with RTX 4090 GPUs, and I used the following command for setup: ```bash vllm serve /model/DeepSeek-V2.5-1210 \ --tensor-parallel-size 8 \ --pipeline-pa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: pSeek-v2.5 on NVIDIA 4090 bug;stale ### Your current environment ### Model Input Dumps https://gist.github.com/R-Tars/de721273ce29a369489b46fd76f56cab [err_execute_model_input_20250112-194758.zip](https://github.com/use...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: with Multi-Node Multi-GPU Deployment of DeepSeek-v2.5 on NVIDIA 4090 bug;stale ### Your current environment ### Model Input Dumps https://gist.github.com/R-Tars/de721273ce29a369489b46fd76f56cab [err_execute_model_input_...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
