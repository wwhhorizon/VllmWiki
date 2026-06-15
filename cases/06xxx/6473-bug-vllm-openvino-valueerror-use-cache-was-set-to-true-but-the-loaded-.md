# vllm-project/vllm#6473: [Bug]: [vllm-openvino]: ValueError: `use_cache` was set to `True` but the loaded model only supports `use_cache=False`. 

| 字段 | 值 |
| --- | --- |
| Issue | [#6473](https://github.com/vllm-project/vllm/issues/6473) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 21; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;import_error;mismatch;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [vllm-openvino]: ValueError: `use_cache` was set to `True` but the loaded model only supports `use_cache=False`. 

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` (vllm-openvino) yongshuai_wang@cpu-10-48-1-249:~/models$ python collect_env.py Collecting environment information... WARNING 07-16 19:50:52 _custom_ops.py:14] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") /home/yongshuai_wang/miniconda3/envs/vllm-openvino/lib/python3.10/site-packages/vllm/usage/usage_lib.py:19: RuntimeWarning: Failed to read commit hash: No module named 'vllm.commit_id' from vllm.version import __version__ as VLLM_VERSION PyTorch version: 2.3.1+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.30.0 Libc version: glibc-2.35 Python version: 3.10.14 (main, May 6 2024, 19:42:50) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.0-94-generic-x86_64-with-glibc2.35 Is CUDA available: False CUDA runtime version: No CUDA CUDA_MODULE_LOADING set to: N/A GPU models and configuration: No CUDA Nvidia driver version: No CUDA cuDNN version: No CUDA HIP runtime version: N/A MIOpen r...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: cted Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Retbleed: Not affected Vulnerability Spec rstack overflow: Not affected Vulnerability Spec store bypass: Mitigation; Sp...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: nment information... WARNING 07-16 19:50:52 _custom_ops.py:14] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") /home/yongshuai_wang/miniconda3/envs/vllm-openvino/lib/python3.10/site-p...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: _occup_llc cqm_mbm_total cqm_mbm_local split_lock_detect avx_vnni avx512_bf16 wbnoinvd dtherm ida arat pln pts avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg tme avx512_vpo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: vllm-openvino]: ValueError: `use_cache` was set to `True` but the loaded model only supports `use_cache=False`. bug ### Your current environment ```text The output of `python collect_env.py` (vllm-openvino) yongshuai_wa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: rsion__ as VLLM_VERSION PyTorch version: 2.3.1+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
