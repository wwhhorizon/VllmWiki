# vllm-project/vllm#44181: [Bug]: [Bug] Severe GPU Memory Leak and OOM with Native KV Offloading in Multi-Node PP=2 TP=8 Setup (v0.22.0)

| 字段 | 值 |
| --- | --- |
| Issue | [#44181](https://github.com/vllm-project/vllm/issues/44181) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | attention;cache;cuda;fp8;moe |
| 症状 | crash;oom;slowdown |
| 根因提示 | dtype;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [Bug] Severe GPU Memory Leak and OOM with Native KV Offloading in Multi-Node PP=2 TP=8 Setup (v0.22.0)

### Issue 正文摘录

### Your current environment ### ### 🐛 Describe the bug ### 🐛 Bug Description When deploying **DeepSeek-V4-Pro** in a multi-node distributed environment (2 nodes, 16x H100 GPUs) using **PP=2 and TP=8**, enabling native KV offloading (`--kv_offloading_backend native --kv_offloading_size 200`) along with `--enable-prefix-caching` causes a severe and continuous GPU memory leak. Over time, under a high-throughput workload , the GPU memory usage monotonically increases until the engine crashes with an Out-of-Memory (OOM) error. ### 🔍 Isolation & Observations 1. **Workaround:** If we completely remove `--kv_offloading_backend native` and `--kv_offloading_size 200` from the startup arguments, the memory leak **disappears completely**, and the cluster runs stably. 2. **Version History:** In `v0.21.0`, KV offloading was entirely unusable/broken in this topology. In `v0.22.0`, it starts successfully but suffers from this severe memory leak. 3. **Suspected Cause:** There appears to be a flaw in vLLM's KV cache block management or reference counting when swapping/offloading blocks to CPU memory, especially when interacting with `prefix_caching` and Pipeline Parallelism (PP). --- ### 💻 Environ...

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 6: [Bug]: [Bug] Severe GPU Memory Leak and OOM with Native KV Offloading in Multi-Node PP=2 TP=8 Setup (v0.22.0) bug ### Your current environment ### ### 🐛 Describe the bug ### 🐛 Bug Description When deploying **DeepSeek-V...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: memory leak **disappears completely**, and the cluster runs stably. 2. **Version History:** In `v0.21.0`, KV offloading was entirely unusable/broken in this topology. In `v0.22.0`, it starts successfully but suffers fro...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: *DeepSeek-V4-Pro** in a multi-node distributed environment (2 nodes, 16x H100 GPUs) using **PP=2 and TP=8**, enabling native KV offloading (`--kv_offloading_backend native --kv_offloading_size 200`) along with `--enable...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: --trust-remote-code \ --served-model-name deepseek_pro \ --kv-cache-dtype fp8 \ --block-size 256 \ --enable-expert-parallel \ -cc.pass_config.fuse_allreduce_rms=False \ --tensor-parallel-size 8 \ --pipeline-parallel-siz...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: k. 3. **Suspected Cause:** There appears to be a flaw in vLLM's KV cache block management or reference counting when swapping/offloading blocks to CPU memory, especially when interacting with `prefix_caching` and Pipeli...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
