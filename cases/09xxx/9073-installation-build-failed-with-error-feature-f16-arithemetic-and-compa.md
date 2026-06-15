# vllm-project/vllm#9073: [Installation]: Build failed with error   : Feature 'f16 arithemetic and compare instructions' requires .target sm_53 or higher

| 字段 | 值 |
| --- | --- |
| Issue | [#9073](https://github.com/vllm-project/vllm/issues/9073) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;fp8;operator;quantization;triton |
| 症状 | build_error;import_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Build failed with error   : Feature 'f16 arithemetic and compare instructions' requires .target sm_53 or higher

### Issue 正文摘录

### Your current environment ```text Collecting environment information... WARNING 10-04 20:22:40 _custom_ops.py:18] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.30.4 Libc version: glibc-2.35 Python version: 3.11.9 (main, Apr 19 2024, 16:48:06) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-4.19.91-014.15-kangaroo.alios7.x86_64-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.4.99 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA H800 GPU 1: NVIDIA H800 Nvidia driver version: 525.105.17 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.9.0.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv.so.9.0.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn.so.9.0.0 /usr/lib/x86_64-linux-gnu/libcudnn_engines_precompiled.so.9.0.0 /usr/lib/x86_64-linux-gnu/libcudnn_engines_runtime_compiled.so.9.0.0 /usr/lib/x86_64-linux-gnu/libcudnn_gr...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 11: [Installation]: Build failed with error : Feature 'f16 arithemetic and compare instructions' requires .target sm_53 or higher installation ### Your current environment ```text Collecting environment information... WARN
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: : Feature 'f16 arithemetic and compare instructions' requires .target sm_53 or higher installation ### Your current environment ```text Collecting environment information... WARNING 10-04 20:22:40 _custom_ops.py:18] Fai...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: avx512cd sha_ni avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves avx512_bf16 wbnoinvd avx512vbmi umip pku waitpkg avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg avx512_vpopcntdq rdpid cldemote movdiri movdi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: tallation ### Your current environment ```text Collecting environment information... WARNING 10-04 20:22:40 _custom_ops.py:18] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") PyTorch...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: module named 'vllm._C'") PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
