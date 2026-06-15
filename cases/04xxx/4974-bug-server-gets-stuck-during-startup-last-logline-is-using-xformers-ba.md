# vllm-project/vllm#4974: [Bug]: Server gets stuck during startup, last logline is 'Using XFormers backend'

| 字段 | 值 |
| --- | --- |
| Issue | [#4974](https://github.com/vllm-project/vllm/issues/4974) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cuda;operator;quantization;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Server gets stuck during startup, last logline is 'Using XFormers backend'

### Issue 正文摘录

### Your current environment ```text root@9206753dc19c:/# python3 collect_env.py Collecting environment information... PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 12 (bookworm) (x86_64) GCC version: Could not collect Clang version: 14.0.6 CMake version: version 3.29.3 Libc version: glibc-2.36 Python version: 3.11.9 (main, May 14 2024, 08:15:15) [GCC 12.2.0] (64-bit runtime) Python platform: Linux-4.4.0-x86_64-with-glibc2.36 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB GPU 1: NVIDIA A100-SXM4-80GB Nvidia driver version: 535.129.03 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 96 On-line CPU(s) list: 0-95 Vendor ID: GenuineIntel Model name: unknown CPU family: 6 Model: 85 Thread(s) per core: 0 Core(s) per socket: 0 Socket(s): 0 Stepping: unknown BogoMIPS: 2200.15 Flags: fpu vme d...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: :/# python3 collect_env.py Collecting environment information... PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 12 (bookworm) (x8...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 12 (bookworm) (x86_64) GCC version: Could not collect Clang...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: ext root@9206753dc19c:/# python3 collect_env.py Collecting environment information... PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Debian GNU/Li...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ='auto', trust_remote_code=False, download_dir=None, load_format='auto', dtype='auto', kv_cache_dtype='auto', quantization_param_path=None, max_model_len=None, guided_decoding_backend='outlines', worker_use_ray=False, p...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: e, image_token_id=None, image_input_shape=None, image_feature_size=None, scheduler_delay_factor=0.0, enable_chunked_prefill=False, speculative_model=None, num_speculative_tokens=None, speculative_max_model_len=None, mod...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
