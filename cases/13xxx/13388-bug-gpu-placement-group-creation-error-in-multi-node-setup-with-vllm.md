# vllm-project/vllm#13388: [Bug]: GPU Placement Group Creation Error in Multi-Node Setup with vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#13388](https://github.com/vllm-project/vllm/issues/13388) |
| 状态 | closed |
| 标签 | bug;ray |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GPU Placement Group Creation Error in Multi-Node Setup with vLLM

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Issue Description We're running into an issue while trying to run vLLM with multiple GPUs (16) in a Kubernetes environment. Based on the Ray dashboard, all 16 GPUs are visible and ALIVE, but we're getting placement group creation errors. ## Environment - Running in Kubernetes - 16 GPUs across multiple nodes - Using Ray for distributed setup - DeepSeek model with tensor parallel size 16 ## Command Used ```bash # For head node ray start --head --port=6379 --block vllm serve /models/DeepSeek-R1 \ --tensor-parallel-size 16 \ --trust-remote-code # For worker nodes ray start --address=${DEEPSEEK_HEAD_HOST}:6379 --block ``` ## Error Message ``` Waiting for creating a placement group of specs for 70 seconds... Error: No available node types can fulfill resource request {'node:10.61.0.27': 0.001, 'GPU': 1.0} ``` ## What We've Checked 1. VLLM_HOST_IP is correctly set to respective node IPs 2. Ray status shows all nodes are active. Here's the full output: ``` ======== Autoscaler status: 2025-02-16 07:20:29.943586 ======== Node status --------------------------------------------------------------- Active: 1 node_5b4c1d6ab97c55faf64f3224ac...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: reation failure despite having all GPUs available? Are we missing any specific configuration for multi-node GPU setup? ## Additional Context We've verified that: - All nodes can see each other - The Ray cluster is prope...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ed. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ## Command Used ```bash # For head node ray start --head --port=6379 --block vllm serve /models/DeepSeek-R1 \ --tensor-parallel-size 16 \ --trust-remote-code # For worker nodes ray start --address=${DEEPSEEK_HEAD_HOST}:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: GPUs across multiple nodes - Using Ray for distributed setup - DeepSeek model with tensor parallel size 16 ## Command Used ```bash # For head node ray start --head --port=6379 --block vllm serve /models/DeepSeek-R1 \ --...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: t --address=${DEEPSEEK_HEAD_HOST}:6379 --block ``` ## Error Message ``` Waiting for creating a placement group of specs for 70 seconds... Error: No available node types can fulfill resource request {'node:10.61.0.27': 0...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
