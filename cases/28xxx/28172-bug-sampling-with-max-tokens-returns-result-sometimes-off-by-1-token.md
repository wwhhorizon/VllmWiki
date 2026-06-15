# vllm-project/vllm#28172: [Bug]: Sampling with max_tokens returns result sometimes off by 1 token

| 字段 | 值 |
| --- | --- |
| Issue | [#28172](https://github.com/vllm-project/vllm/issues/28172) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;sampling |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Sampling with max_tokens returns result sometimes off by 1 token

### Issue 正文摘录

### Your current environment ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.9 (main, Mar 17 2025, 21:01:58) [Clang 20.1.0 ] (64-bit runtime) Python platform : Linux-6.5.0-14-generic-x86_64-with-glibc2.35 ============================== vLLM Info ============================== ROCM Version : Could not collect vLLM Version : 0.11.0 vLLM Build Flags: CUDA Archs: Not Set; ROCm: Disabled GPU Topology: GPU0 GPU1 GPU2 GPU3 CPU Affinity NUMA Affinity GPU0 X NV4 NV4 NV4 0-31,64-95 0 GPU1 NV4 X NV4 NV4 0-31,64-95 0 GPU2 NV4 NV4 X NV4 32-63,96-127 1 GPU3 NV4 NV4 NV4 X 32-63,96-127 1 Legend: X = Self SYS = Connection traversing PCIe as well as the SMP interconnect between NUMA nodes (e.g., QPI/UPI...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.9 (m...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: g]: Sampling with max_tokens returns result sometimes off by 1 token bug;stale ### Your current environment ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: orch version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: tch while min_val {transition}: VLLM generates fewer tokens (hits model length limit)") # Verify the transition print(f"\n=== Verification ===") print(f"Testing max_tokens={transition} (should be exact):") req, act = te...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
