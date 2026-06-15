# vllm-project/vllm#37982: [Bug]: chart-helm does not support configuring shared memory (`/dev/shm`)

| 字段 | 值 |
| --- | --- |
| Issue | [#37982](https://github.com/vllm-project/vllm/issues/37982) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: chart-helm does not support configuring shared memory (`/dev/shm`)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug This issue concerns [chart-helm](https://github.com/vllm-project/vllm/tree/main/examples/online_serving/chart-helm). This Helm chart does not provide a way to configure shared memory (`/dev/shm`) for the vLLM container. This is a deployment gap because official vLLM docs explicitly show `/dev/shm` setup for Kubernetes and explain that it is needed for tensor parallel inference / IPC. ### Evidence from official docs #### 1. Kubernetes deployment docs include this comment and manifest pattern: >vLLM needs to access the host's shared memory for tensor parallel inference. and show: - `volumes[].emptyDir.medium: Memory` with `sizeLimit` - `volumeMounts[].mountPath: /dev/shm` Ref: - https://docs.vllm.ai/en/latest/deployment/k8s/#deployment-with-gpus #### 2. Parallelism/scaling docs also state Kubernetes pods should mount `/dev/shm` for IPC: >Shared memory with /dev/shm: mount /dev/shm in the pod spec to provide shared memory for interprocess communication (IPC). Ref: - https://docs.vllm.ai/en/stable/serving/parallelism_scaling/#enabling-gpudirect-rdma #### 3. Installation docs mention vLLM/PyTorch shared memory requirement >You can eit...

## 现有链接修复摘要

#37984 [Doc] Add configurable /dev/shm shared memory mount to helm chart

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: /dev/shm`) for the vLLM container. This is a deployment gap because official vLLM docs explicitly show `/dev/shm` setup for Kubernetes and explain that it is needed for tensor parallel inference / IPC. ### Evidence from...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: vllm.ai/en/latest/deployment/k8s/#deployment-with-gpus #### 2. Parallelism/scaling docs also state Kubernetes pods should mount `/dev/shm` for IPC: >Shared memory with /dev/shm: mount /dev/shm in the pod spec to provide...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: chart-helm does not support configuring shared memory (`/dev/shm`) bug ### Your current environment ### 🐛 Describe the bug This issue concerns [chart-helm](https://github.com/vllm-project/vllm/tree/main/examples/...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency #37984 [Doc] Add configurable /dev/shm shared memory mount to helm chart Your current environment
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency #3...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#37984](https://github.com/vllm-project/vllm/pull/37984) | closes_keyword | 0.95 | [Doc] Add configurable /dev/shm shared memory mount to helm chart | Fixes #37982 Fixes the configuration gap where `examples/online_serving/chart-helm` did not support configuring `/dev/shm` shared memory. This change adds configurable shared |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
