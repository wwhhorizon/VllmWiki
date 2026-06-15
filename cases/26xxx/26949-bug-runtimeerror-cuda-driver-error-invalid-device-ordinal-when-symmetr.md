# vllm-project/vllm#26949: [Bug]: RuntimeError: CUDA driver error: invalid device ordinal when symmetric memory (symm_mem) is enabled in multi-GPU vLLM setup with 4H100 PCIe

| 字段 | 值 |
| --- | --- |
| Issue | [#26949](https://github.com/vllm-project/vllm/issues/26949) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;model_support;quantization;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | cache;cuda;fp8 |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: CUDA driver error: invalid device ordinal when symmetric memory (symm_mem) is enabled in multi-GPU vLLM setup with 4H100 PCIe

### Issue 正文摘录

### My current environment Environment: Model: RedHatAI/Llama-4-Scout-17B-16E-Instruct-FP8-dynamic vLLM Version: latest main (installed via pip) Hardware: 4× NVIDIA H100 PCIe (80GB) Driver: 550.xx CUDA: 12.2 PyTorch: 2.4.0 OS: Ubuntu 22.04 Launch Command: python3 -m vllm.entrypoints.api_server \ --model /ephemeral/huggingface/models--RedHatAI--Llama-4-Scout-17B-16E-Instruct-FP8-dynamic/snapshots/... \ --tensor-parallel-size 4 \ --gpu-memory-utilization 0.85 \ --kv-cache-dtype fp8_e4m3 \ --max-model-len 4000000 \ --max-num-seqs 16 \ --enable-prefix-caching \ --kv-events-config '{"enable_kv_cache_events": true, "publisher": "zmq", "endpoint": "tcp://*:5557"}' ### bug RuntimeError: CUDA driver error: invalid device ordinal (EngineCore_DP0 pid=11546) ERROR [symm_mem.py:88] handle = torch_symm_mem.rendezvous(self.buffer, self.group.group_name) (EngineCore_DP0 pid=11546) ERROR WorkerProc failed to start RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {'EngineCore_DP0': 1} Behavior: When symm_mem is enabled (default) → fails with invalid device ordinal When symm_mem is disabled via --disable-symm-mem → ✅ vLLM engine starts ❌ No KV cache event l...

## 现有链接修复摘要

#33274 fix(symm_mem): add multicast support check to prevent crash on PCIe GPUs

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: mmetric memory (symm_mem) is enabled in multi-GPU vLLM setup with 4H100 PCIe bug;stale ### My current environment Environment: Model: RedHatAI/Llama-4-Scout-17B-16E-Instruct-FP8-dynamic vLLM Version: latest main (instal...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: setup with 4H100 PCIe bug;stale ### My current environment Environment: Model: RedHatAI/Llama-4-Scout-17B-16E-Instruct-FP8-dynamic vLLM Version: latest main (installed via pip) Hardware: 4× NVIDIA H100 PCIe (80GB) Drive...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: environment Environment: Model: RedHatAI/Llama-4-Scout-17B-16E-Instruct-FP8-dynamic vLLM Version: latest main (installed via pip) Hardware: 4× NVIDIA H100 PCIe (80GB) Driver: 550.xx CUDA: 12.2 PyTorch: 2.4.0 OS: Ubuntu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: RuntimeError: CUDA driver error: invalid device ordinal when symmetric memory (symm_mem) is enabled in multi-GPU vLLM setup with 4H100 PCIe bug;stale ### My current environment Environment: Model: RedHatAI/Llama-...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: --tensor-parallel-size 4 \ --gpu-memory-utilization 0.85 \ --kv-cache-dtype fp8_e4m3 \ --max-model-len 4000000 \ --max-num-seqs 16 \ --enable-prefix-caching \ --kv-events-config '{"enable_kv_cache_events": true, "publis...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#33274](https://github.com/vllm-project/vllm/pull/33274) | closes_keyword | 0.95 | fix(symm_mem): add multicast support check to prevent crash on PCIe GPUs | Fixes #26949: RuntimeError on H100 PCIe when symmetric memory is enabled. Symmetric memory requires CUDA multicast support, which is only available on NVLink-connected GPUs. Befor |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
