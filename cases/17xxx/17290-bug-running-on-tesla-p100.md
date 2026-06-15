# vllm-project/vllm#17290: [Bug]: Running on tesla P100

| 字段 | 值 |
| --- | --- |
| Issue | [#17290](https://github.com/vllm-project/vllm/issues/17290) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Running on tesla P100

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am trying to run vllm on the OS (pve VM) directly, without docker. here is what I did: - I changed (adding 6.0) CMakeLists.txt to "set(CUDA_SUPPORTED_ARCHS "6.0;7.0;7.2;7.5;8.0;8.6;8.7;8.9;9.0;10.0;10.1;12.0")." - created and activated a venv - pip install -r requirements/build.txt - CUDACXX=/usr/local/cuda/bin/nvcc pip install -e . it was building for quite some time and errored while "Building wheels for collected packages: vllm" with: ``` Requirement already satisfied: mdurl~=0.1 in ./venv/lib/python3.11/site-packages (from markdown-it-py>=2.2.0->rich>=13.7.1->rich-toolkit>=0.11.1->fastapi-cli[standard]>=0.0.5->fastapi[standard]>=0.115.0->vllm==0.8.5.dev72+g3408e4715.d20250428) (0.1.2) Building wheels for collected packages: vllm Building editable for vllm (pyproject.toml) ... error error: subprocess-exited-with-error × Building editable for vllm (pyproject.toml) did not run successfully. │ exit code: 1 ╰─> [562 lines of output] /tmp/pip-build-env-pqgbmbjy/overlay/lib/python3.11/site-packages/torch/_subclasses/functional_tensor.py:275: UserWarning: Failed to initialize NumPy: No module named 'numpy' (Triggered internally at...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 11: be the bug I am trying to run vllm on the OS (pve VM) directly, without docker. here is what I did: - I changed (adding 6.0) CMakeLists.txt to "set(CUDA_SUPPORTED_ARCHS "6.0;7.0;7.2;7.5;8.0;8.6;8.7;8.9;9.0;10.0;10.1;12....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 8: ompatible archs found in CUDA target architectures -- Not building scaled_mm_c3x_sm90 as no compatible archs found in CUDA target architectures -- Not building scaled_mm_c3x_100 as no compatible archs found in CUDA targ...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: abling cumem allocator extension. -- CMake Version: 4.0.0 -- CUTLASS 3.8.0 -- Found CUDAToolkit: /usr/local/cuda/targets/x86_64-linux/include (found version "12.5.82") -- CUDART: /usr/local/cuda/lib64/libcudart.so -- CU...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: er. here is what I did: - I changed (adding 6.0) CMakeLists.txt to "set(CUDA_SUPPORTED_ARCHS "6.0;7.0;7.2;7.5;8.0;8.6;8.7;8.9;9.0;10.0;10.1;12.0")." - created and activated a venv - pip install -r requirements/build.txt...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: rchitectures -- Enabling C extension. -- Not building Marlin MOE kernels as no compatible archs found in CUDA target architectures -- Enabling moe extension. CMake Warning (dev) at /tmp/pip-build-env-pqgbmbjy/overlay/li...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
