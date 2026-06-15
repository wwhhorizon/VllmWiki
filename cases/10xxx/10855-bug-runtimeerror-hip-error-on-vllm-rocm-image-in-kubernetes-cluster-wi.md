# vllm-project/vllm#10855: [Bug]: RuntimeError: HIP Error on vLLM ROCm Image in Kubernetes Cluster with AMD GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#10855](https://github.com/vllm-project/vllm/issues/10855) |
| 状态 | closed |
| 标签 | bug;rocm;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: HIP Error on vLLM ROCm Image in Kubernetes Cluster with AMD GPUs

### Issue 正文摘录

### Your current environment ### Logs Here are the relevant sections of the output: GPU Detection: ``` Name: AMD Instinct MI210 Node: 2 Compute Unit: 104 ROCm Runtime Version: 6.2 ``` Error Logs: ``` ERROR 11-29 09:36:15 engine.py:366] HIP error: invalid argument ERROR 11-29 09:36:15 engine.py:366] For debugging consider passing AMD_SERIALIZE_KERNEL=3 ERROR 11-29 09:36:15 engine.py:366] Compile with `TORCH_USE_HIP_DSA` to enable device-side assertions. ``` Debugging Attempts: Verified the GPU and ROCm setup using rocminfo and rocm-smi. Confirmed that the GPU operator is operational, and the gfx90a architecture is detected. Checked for potential resource or memory issues during the startup process. Additional Context: Image used: rocm/vllm-ci:382fc0be9e168fe8ae47176ba54fbdc126f36940 GPU: AMD Instinct MI210 (gfx90a) Kubernetes environment: AMD GPU Operator installed and configured. The issue seems related to torch.cuda.mem_get_info(). Questions: Is there a specific configuration required for this image to run in a Kubernetes environment with AMD GPUs? Could the issue be related to torch.cuda.mem_get_info() or a mismatch in runtime configurations? Are there any additional debugging s...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: on: ``` Name: AMD Instinct MI210 Node: 2 Compute Unit: 104 ROCm Runtime Version: 6.2 ``` Error Logs: ``` ERROR 11-29 09:36:15 engine.py:366] HIP error: invalid argument ERROR 11-29 09:36:15 engine.py:366] For debugging...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: IP Error on vLLM ROCm Image in Kubernetes Cluster with AMD GPUs bug;rocm;stale ### Your current environment ### Logs Here are the relevant sections of the output: GPU Detection: ``` Name: AMD Instinct MI210 Node: 2 Comp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: RuntimeError: HIP Error on vLLM ROCm Image in Kubernetes Cluster with AMD GPUs bug;rocm;stale ### Your current environment ### Logs Here are the relevant sections of the output: GPU Detection: ``` Name: AMD Insti...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: t MI210 Vendor Name: AMD Feature: KERNEL_DISPATCH Profile: BASE_PROFILE Float Round Mode: NEAR Max Queue Number: 128(0x80) Queue Min Size: 64(0x40) Queue Max Size: 131072(0x20000) Queue Type:
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: per Eng.: 1 WatchPts on Addr. Ranges:4 Coherent Host Access: FALSE Memory Properties: Features: KERNEL_DISPATCH Fast F16 Operation: TRUE Wavefront Size: 64(0x40) Workgroup Max Size: 1024(0x400) Workgroup Max Size per Di...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
