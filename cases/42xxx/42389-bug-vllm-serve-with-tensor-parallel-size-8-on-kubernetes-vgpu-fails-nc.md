# vllm-project/vllm#42389: [Bug]: vLLM serve with tensor-parallel-size=8 on Kubernetes + vGPU fails: NCCL TCPStore broken pipe, EngineCore initialization failed

| 字段 | 值 |
| --- | --- |
| Issue | [#42389](https://github.com/vllm-project/vllm/issues/42389) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | cold_start |
| Operator 关键词 | fp8;operator |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM serve with tensor-parallel-size=8 on Kubernetes + vGPU fails: NCCL TCPStore broken pipe, EngineCore initialization failed

### Issue 正文摘录

### Your current environment 1 ### 🐛 Describe the bug **vLLM version**: FROM vllm/vllm-openai:deepseekv4-cu129 **Python version**: 3.12 **Hardware/Cluster**: Kubernetes cluster, nodes with H100 vGPUs (virtual GPUs), requesting 8 vGPUs via `nvidia.com/vgpu` resource **Operating System**: Container image based on Ubuntu (inferred) **Full launch command**: ```bash vllm serve /shared/models/huggingface/hub/models--deepseek-ai--DeepSeek-V4-Flash/snapshots/6976c7ff1b30a1b2cb7805021b8ba4684041f136 \ --host 0.0.0.0 \ --port 5180 \ --enable-prefix-caching \ --trust-remote-code \ --enable-auto-tool-choice \ --tensor-parallel-size 8 \ --max-model-len 8192 \ --tokenizer-mode deepseek_v4 \ --tool-call-parser deepseek_v4 \ --kv-cache-dtype fp8 ``` **Kubernetes resource configuration**: - Requests/limits: `nvidia.com/vgpu: 8`, CPU 32/16, memory 320Gi/160Gi - `hostIPC: true` and `/dev/shm` volume were **not set** initially (we later added them, but vLLM's compatibility with vGPUs still needs confirmation) ### Problem Description When starting the DeepSeek-V4-Flash model with `--tensor-parallel-size 8` to run inference across 8 vGPUs, the service fails during initialization with the following two...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: n Ubuntu (inferred) **Full launch command**: ```bash vllm serve /shared/models/huggingface/hub/models--deepseek-ai--DeepSeek-V4-Flash/snapshots/6976c7ff1b30a1b2cb7805021b8ba4684041f136 \ --host 0.0.0.0 \ --port 5180 \ -...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: iled bug ### Your current environment 1 ### 🐛 Describe the bug **vLLM version**: FROM vllm/vllm-openai:deepseekv4-cu129 **Python version**: 3.12 **Hardware/Cluster**: Kubernetes cluster, nodes with H100 vGPUs (virtual G...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: nizer-mode deepseek_v4 \ --tool-call-parser deepseek_v4 \ --kv-cache-dtype fp8 ``` **Kubernetes resource configuration**: - Requests/limits: `nvidia.com/vgpu: 8`, CPU 32/16, memory 320Gi/160Gi - `hostIPC: true` and `/de...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: on version**: 3.12 **Hardware/Cluster**: Kubernetes cluster, nodes with H100 vGPUs (virtual GPUs), requesting 8 vGPUs via `nvidia.com/vgpu` resource **Operating System**: Container image based on Ubuntu (inferred) **Ful...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: --tokenizer-mode deepseek_v4 \ --tool-call-parser deepseek_v4 \ --kv-cache-dtype fp8 ``` **Kubernetes resource configuration**: - Requests/limits: `nvidia.com/vgpu: 8`, CPU 32/16, memory 320Gi/160Gi - `hostIPC: true` an...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
