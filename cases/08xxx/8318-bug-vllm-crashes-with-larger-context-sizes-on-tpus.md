# vllm-project/vllm#8318: [Bug]: vLLM crashes with larger context sizes on TPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#8318](https://github.com/vllm-project/vllm/issues/8318) |
| 状态 | closed |
| 标签 | bug;tpu |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM crashes with larger context sizes on TPUs

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am trying to deploy llama3.1 8B instruct on GKE 2x4 v5e TPUs. The vLLM server boots up normally and works properly if `max-model-len` is very low (ie 1024), but crashes with higher context sizes (tried 16k and above). I'm using the Dockerfile.tpu, and the command `python3.10 -u -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --model meta-llama/Meta-Llama-3.1-8B-Instruct --tensor-parallel-size 8 --swap-space 16 --disable-log-requests --max-model-len=32768` Here is my full log file: [vllm-llama31-tpu.log](https://github.com/user-attachments/files/16939650/vllm-llama31-tpu.log) Here is my full k8s manifest: ```yaml apiVersion: apps/v1 kind: Deployment metadata: name: llama3-8b-instruct-vllm-deployment namespace: default labels: app: llama3-8b-instruct-vllm spec: replicas: 1 selector: matchLabels: app: llama3-8b-instruct-vllm template: metadata: labels: app: llama3-8b-instruct-vllm spec: nodeSelector: cloud.google.com/gke-tpu-topology: 2x4 cloud.google.com/gke-tpu-accelerator: tpu-v5-lite-podslice hostIPC: true hostNetwork: true containers: - name: llama3-8b-instruct-vllm image: us-central1-docker.pkg.dev/project-lighthouse-40...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: t crashes with higher context sizes (tried 16k and above). I'm using the Dockerfile.tpu, and the command `python3.10 -u -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --model meta-llama/Meta-Llama-3.1-8B-Instruct...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ur current environment ### 🐛 Describe the bug I am trying to deploy llama3.1 8B instruct on GKE 2x4 v5e TPUs. The vLLM server boots up normally and works properly if `max-model-len` is very low (ie 1024), but crashes wi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: a-3.1-8B-Instruct --tensor-parallel-size 8 --swap-space 16 --disable-log-requests --max-model-len=32768` Here is my full log file: [vllm-llama31-tpu.log](https://github.com/user-attachments/files/16939650/vllm-llama31-t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
