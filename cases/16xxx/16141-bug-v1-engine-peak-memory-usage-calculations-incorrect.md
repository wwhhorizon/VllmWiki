# vllm-project/vllm#16141: [Bug]: V1 engine peak memory usage calculations incorrect

| 字段 | 值 |
| --- | --- |
| Issue | [#16141](https://github.com/vllm-project/vllm/issues/16141) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;kernel;quantization;sampling |
| 症状 | build_error;crash;mismatch;oom |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: V1 engine peak memory usage calculations incorrect

### Issue 正文摘录

### Your current environment The `collect_env.py` script doesn't work because I don't have vllm installed in my environment. This bug is reproducible using the docker image, so I don't think this matters. Affected VLLM version is `v0.8.3`. ### 🐛 Describe the bug The peak memory usage calculations for VLLM is buggy. It seems to think that the memory usage of the other processes on the GPU contribute to the minimum required. This happens with `v0.8.3`. This is a problem when running multiple instances of VLLM on the same GPU. ## Repro steps This is easy to reproduce with the docker image. Here is the `nvidia-smi` output before running VLLM. No memory usage. ```text +-----------------------------------------------------------------------------------------+ | NVIDIA-SMI 550.127.05 Driver Version: 550.127.05 CUDA Version: 12.4 | |-----------------------------------------+------------------------+----------------------+ | GPU Name Persistence-M | Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap | Memory-Usage | GPU-Util Compute M. | | | | MIG M. | |=========================================+========================+======================| | 0 NVIDIA RTX A6000 Off | 00...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ment The `collect_env.py` script doesn't work because I don't have vllm installed in my environment. This bug is reproducible using the docker image, so I don't think this matters. Affected VLLM version is `v0.8.3`. ###...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ps This is easy to reproduce with the docker image. Here is the `nvidia-smi` output before running VLLM. No memory usage. ```text +----------------------------------------------------------------------------------------...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: work because I don't have vllm installed in my environment. This bug is reproducible using the docker image, so I don't think this matters. Affected VLLM version is `v0.8.3`. ### 🐛 Describe the bug The peak memory usage...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: --max-model-len 512 ``` It starts successfully and consumes 10% of GPU memory. As expected. ```text +-----------------------------------------------------------------------------------------+ | NVIDIA-SMI 550.127.05 Dri...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits;scheduler_memory attention;cache;cuda;kernel;quantization;sampling build_error;crash;mismatch;oom dtype;env_dependenc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
