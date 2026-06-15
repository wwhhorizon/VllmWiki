# vllm-project/vllm#37140: [Usage]: CUDA error: the provided PTX was compiled with an unsupported toolchain.

| 字段 | 值 |
| --- | --- |
| Issue | [#37140](https://github.com/vllm-project/vllm/issues/37140) |
| 状态 | open |
| 标签 | usage |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;operator |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: CUDA error: the provided PTX was compiled with an unsupported toolchain.

### Issue 正文摘录

### Your current environment When I use deploy qwen3-vl local by vllm, I found the question below! ```text torch.AcceleratorError: CUDA error: the provided PTX was compiled with an unsupported toolchain. CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect. For debugging consider passing CUDA_LAUNCH_BLOCKING=1 Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. ``` While, when I deploy qwen3-8b, it worked. I don't know how to figure it. And my env is : ```text torch==2.8.0 vllm==0.11.0 flash-attn==2.8.3 ``` ```detail And, the detail of bug report is below Process EngineCore_DP0: Traceback (most recent call last): File "/mnt/bn/miniconda3/envs/swift_rlhf/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap self.run() File "/mnt/bn/miniconda3/envs/swift_rlhf/lib/python3.10/multiprocessing/process.py", line 108, in run self._target(*self._args, **self._kwargs) File "/mnt/bn/miniconda3/envs/swift_rlhf/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 712, in run_engine_core raise e File "/mnt/bn/miniconda3/envs/swift_rlhf/lib/python3.10/site-packages/vllm/v1/engine/core.py", line...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Usage]: CUDA error: the provided PTX was compiled with an unsupported toolchain. usage ### Your current environment When I use deploy qwen3-vl local by vllm, I found the question below! ```text torch.AcceleratorError:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: pported toolchain. usage ### Your current environment When I use deploy qwen3-vl local by vllm, I found the question below! ```text torch.AcceleratorError: CUDA error: the provided PTX was compiled with an unsupported t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Usage]: CUDA error: the provided PTX was compiled with an unsupported toolchain. usage ### Your current environment When I use deploy qwen3-vl local by vllm, I found the question below! ```text torch.AcceleratorError:...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ace below might be incorrect. For debugging consider passing CUDA_LAUNCH_BLOCKING=1 Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. ``` While, when I deploy qwen3-8b, it worked. I don't know how to f...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: orker.py", line 263, in determine_available_memory self.model_runner.profile_run() File "/mnt/bn/miniconda3/envs/swift_rlhf/lib/python3.10/site-packages/vllm/v1/worker/gpu_model_runner.py", line 3361, in profile_run sel...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
