# vllm-project/vllm#5104: [Bug]: can not clean up the memory usage after instantiating the LLM class. 

| 字段 | 值 |
| --- | --- |
| Issue | [#5104](https://github.com/vllm-project/vllm/issues/5104) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: can not clean up the memory usage after instantiating the LLM class. 

### Issue 正文摘录

### Your current environment created a new conda environment and run `pip install vllm==0.4.2` ```python > python collect_env.py Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Fedora Linux 37 (Workstation Edition) (x86_64) GCC version: (GCC) 12.3.1 20230508 (Red Hat 12.3.1-1) Clang version: Could not collect CMake version: version 3.27.7 Libc version: glibc-2.36 Python version: 3.9.18 | packaged by conda-forge | (main, Aug 30 2023, 03:49:32) [GCC 12.3.0] (64-bit runtime) Python platform: Linux-6.5.12-100.fc37.x86_64-x86_64-with-glibc2.36 Is CUDA available: N/A CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: N/A GPU models and configuration: GPU 0: NVIDIA GeForce RTX 3050 Ti Laptop GPU Nvidia driver version: 545.29.06 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: N/A CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 39 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 20 On-line CPU(s) list: 0-19 Vendor ID: GenuineIntel Model name: 12th Gen Intel(R) Core(TM) i9-12900...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: # Your current environment created a new conda environment and run `pip install vllm==0.4.2` ```python > python collect_env.py Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: ting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Fedora Linux 37 (Workstation Edition) (x86_64) GCC version: (GCC) 12.3.1 20230...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: llm==0.4.2` ```python > python collect_env.py Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Fedora Linux 37 (Workstati...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: an not clean up the memory usage after instantiating the LLM class. bug;stale ### Your current environment created a new conda environment and run `pip install vllm==0.4.2` ```python > python collect_env.py Collecting e...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=2048, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, disable_custom_all_reduce=False, qu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
