# vllm-project/vllm#5204: [Bug]: Different token return behaviors from vllm 0.3.0 → 0.4.3

| 字段 | 值 |
| --- | --- |
| Issue | [#5204](https://github.com/vllm-project/vllm/issues/5204) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Different token return behaviors from vllm 0.3.0 → 0.4.3

### Issue 正文摘录

### Your current environment ### vllm 0.3.0 Traceback (most recent call last): File "/usr/src/app/collect_env.py", line 721, in main() File "/usr/src/app/collect_env.py", line 700, in main output = get_pretty_env_info() File "/usr/src/app/collect_env.py", line 695, in get_pretty_env_info return pretty_str(get_env_info()) File "/usr/src/app/collect_env.py", line 532, in get_env_info vllm_version = get_vllm_version() File "/usr/src/app/collect_env.py", line 264, in get_vllm_version return vllm.__version__ AttributeError: module 'vllm' has no attribute '__version__' ### vllm 0.4.3 ```text The output of `python collect_env.py` Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.27.6 Libc version: glibc-2.35 Python version: 3.10.12 (main, Jun 11 2023, 05:26:28) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.15.0-1041-nvidia-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.2.140 CUDA_MODULE_LOADING set to: LAZY GPU mod...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: File "/usr/src/app/collect_env.py", line 532, in get_env_info vllm_version = get_vllm_version() File "/usr/src/app/collect_env.py", line 264, in get_vllm_version return vllm.__version__ AttributeError: module 'vllm' has...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: 3 ```text The output of `python collect_env.py` Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ==0.7.0a0 [pip3] torchtext==0.16.0a0 [pip3] torchvision==0.16.0a0 [pip3] triton==2.3.0 [conda] Could not collectROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.4.3 vLLM Build Flags: CUDA Archs: 5...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: _occup_llc cqm_mbm_total cqm_mbm_local split_lock_detect avx_vnni avx512_bf16 wbnoinvd dtherm ida arat pln pts hwp hwp_act_window hwp_epp hwp_pkg_req avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmulqdq a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
