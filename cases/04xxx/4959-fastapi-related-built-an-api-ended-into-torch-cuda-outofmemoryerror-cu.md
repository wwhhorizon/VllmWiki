# vllm-project/vllm#4959: [FastAPI related] Built an API, ended into torch.cuda.OutOfMemoryError: CUDA out of memory

| 字段 | 值 |
| --- | --- |
| Issue | [#4959](https://github.com/vllm-project/vllm/issues/4959) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;quantization;sampling |
| 症状 | build_error;crash;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [FastAPI related] Built an API, ended into torch.cuda.OutOfMemoryError: CUDA out of memory

### Issue 正文摘录

env: nvcc: NVIDIA (R) Cuda compiler driver Copyright (c) 2005-2023 NVIDIA Corporation Built on Mon_Apr__3_17:16:06_PDT_2023 Cuda compilation tools, release 12.1, V12.1.105 Build cuda_12.1.r12.1/compiler.32688072_0 +---------------------------------------------------------------------------------------+ | NVIDIA-SMI 535.86.10 Driver Version: 535.86.10 CUDA Version: 12.2 | |-----------------------------------------+----------------------+----------------------+ | GPU Name Persistence-M | Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap | Memory-Usage | GPU-Util Compute M. | | | | MIG M. | |=========================================+======================+======================| | 0 NVIDIA L4 Off | 00000000:00:03.0 Off | 0 | | N/A 62C P0 33W / 72W | 4MiB / 23034MiB | 0% Default | | | | N/A | +-----------------------------------------+----------------------+----------------------+ +---------------------------------------------------------------------------------------+ | Processes: | | GPU GI CI PID Type Process name GPU Memory | | ID ID Usage | |=======================================================================================| | No running processes found | +...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: da.OutOfMemoryError: CUDA out of memory usage env: nvcc: NVIDIA (R) Cuda compiler driver Copyright (c) 2005-2023 NVIDIA Corporation Built on Mon_Apr__3_17:16:06_PDT_2023 Cuda compilation tools, release 12.1, V12.1.105 B...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ameters self.llm = LLM( model=model_dir, quantization="gptq_marlin", dtype=torch.float16, # Use mixed precision enforce_eager=True, # Enforce eager mode to avoid CUDA graphs gpu_memory_utilization=0.8 # Adjusted number...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [FastAPI related] Built an API, ended into torch.cuda.OutOfMemoryError: CUDA out of memory usage env: nvcc: NVIDIA (R) Cuda compiler driver Copyright (c) 2005-2023 NVIDIA Corporation Built on Mon_Apr__3_17:16:06_PDT_202...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: PU GI CI PID Type Process name GPU Memory | | ID ID Usage | |=======================================================================================| | No running processes fou
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: graphs gpu_memory_utilization=0.8 # Adjusted number of CPU blocks ) # Initialize conversation history self.conversation_history = [] # Create a sampling params object for vLLM self.sampling_params = SamplingParams( temp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
