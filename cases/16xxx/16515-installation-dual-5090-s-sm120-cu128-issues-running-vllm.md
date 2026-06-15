# vllm-project/vllm#16515: [Installation]: Dual 5090's (sm120, cu128) Issues Running vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#16515](https://github.com/vllm-project/vllm/issues/16515) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 21; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;fp8;moe;operator |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Dual 5090's (sm120, cu128) Issues Running vLLM

### Issue 正文摘录

### Your current environment (collect_env.py failed) ### How you are installing vllm For the last week, I have been scouring the VLLM issues, reading Nvidia libraries documentation, and attempting to get VLLM working across two 5090s, with minimal success. Success for me would be running an FP8 model leveraging the 5090's native support for this quantinisation. The Issue arrives after graph generation: `Compiling a graph for general shape takes 32.51 s` And appears to fail at: ```text torch.ops._C.cutlass_scaled_mm.default(buf10, buf0, arg4_1, buf5, arg5_1, arg6_1) File "/usr/local/lib/python3.10/dist-packages/torch/_ops.py", line 776, in __call__ return self._op(*args, **kwargs) ``` [2025-04-11_Debug.txt](https://github.com/user-attachments/files/19714180/2025-04-11_Debug.txt) I believe the main issue is that I am trying to use the newest versions of everything, such as sm120, Cuda 12.8, NCCL, and Cutlass, which is causing a large mess. If I was to pin it on one problem, it would be Cutlass, which I'm relying on VLLM to install with the VLLM_CUTLASS_SRC_DIR as per the documentation: [VLLM Installation Documentation](https://docs.vllm.ai/en/latest/getting_started/installation/gpu....

## 现有链接修复摘要

#17278 [NVIDIA] Support Cutlass w8a8 for Blackwell Geforce GPUs (sm120) | #17280 [NVIDIA] Support Cutlass w8a8 FP8 for Blackwell Geforce GPUs (sm120)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Installation]: Dual 5090's (sm120, cu128) Issues Running vLLM installation ### Your current environment (collect_env.py failed) ### How you are installing vllm For the last week, I have been scouring the VLLM issues
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ross two 5090s, with minimal success. Success for me would be running an FP8 model leveraging the 5090's native support for this quantinisation. The Issue arrives after graph generation: `Compiling a graph for general s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Installation]: Dual 5090's (sm120, cu128) Issues Running vLLM installation ### Your current environment (collect_env.py failed) ### How you are installing vllm For the last week, I have been scouring the VLLM issues, r...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: two 5090s, with minimal success. Success for me would be running an FP8 model leveraging the 5090's native support for this quantinisation. The Issue arrives after graph generation: `Compiling a graph for general shape...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: /en/latest/getting_started/installation/gpu.html) I would appreciate an expert eye on this, as I have run out of ideas and am willing to try anything. I hope this can help anyone in the future with a similar setup. ###...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#17278](https://github.com/vllm-project/vllm/pull/17278) | closes_keyword | 0.95 | [NVIDIA] Support Cutlass w8a8 for Blackwell Geforce GPUs (sm120) | FIX #16515 |
| [#17280](https://github.com/vllm-project/vllm/pull/17280) | closes_keyword | 0.95 | [NVIDIA] Support Cutlass w8a8 FP8 for Blackwell Geforce GPUs (sm120) | FIX #16515 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
