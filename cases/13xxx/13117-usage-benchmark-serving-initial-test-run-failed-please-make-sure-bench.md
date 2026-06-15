# vllm-project/vllm#13117: [Usage]: benchmark_serving: Initial test run failed - Please make sure benchmark arguments are correctly specified. Error: Not Found

| 字段 | 值 |
| --- | --- |
| Issue | [#13117](https://github.com/vllm-project/vllm/issues/13117) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: benchmark_serving: Initial test run failed - Please make sure benchmark arguments are correctly specified. Error: Not Found

### Issue 正文摘录

### Your current environment Output of collect_env ``` /usr/local/lib/python3.11/dist-packages/torchvision/io/image.py:14: UserWarning: Failed to load image Python extension: 'libpng16.so.16: cannot open shared object file: No such file or directory'If you don't plan on using image functionality from `torchvision.io`, you can ignore this warning. Otherwise, there might be something wrong with your environment. Did you have `libjpeg` or `libpng` installed before building `torchvision` from source? warn( Collecting environment information... PyTorch version: 2.5.1 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (aarch64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.35 Python version: 3.11.0rc1 (main, Aug 12 2022, 10:02:14) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-6.8.0-1021-nvidia-64k-aarch64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.4.131 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GH200 480GB Nvidia driver version: 550.120 cuDNN version: Probably one of the foll...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: test run failed - Please make sure benchmark arguments are correctly specified. Error: Not Found usage ### Your current environment Output of collect_env ``` /usr/local/lib/python3.11/dist-packages/torchvision/io/image....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: environment information... PyTorch version: 2.5.1 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (aarch64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ore building `torchvision` from source? warn( Collecting environment information... PyTorch version: 2.5.1 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ed Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Reg file data sampling: Not affected Vulnerability Retbleed: Not affected Vulnerability Spec rstack overflow: Not affecte...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: p sve2 sveaes svepmull svebitperm svesha3 svesm4 flagm2 frint svei8mm svebf16 i8mm bf16 dgh bti L1d cache: 4.5 MiB (72 instances) L1i cache: 4.5 MiB (72 instances) L2 cache: 72 MiB (72 instances) L3 cache:

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
