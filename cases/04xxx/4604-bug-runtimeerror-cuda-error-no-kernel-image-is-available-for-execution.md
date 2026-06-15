# vllm-project/vllm#4604: [Bug]: RuntimeError: CUDA error: no kernel image is available for execution on the device

| 字段 | 值 |
| --- | --- |
| Issue | [#4604](https://github.com/vllm-project/vllm/issues/4604) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;triton |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: CUDA error: no kernel image is available for execution on the device

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Red Hat Enterprise Linux Server release 7.9 (Maipo) (x86_64) GCC version: (GCC) 10.2.0 Clang version: Could not collect CMake version: version 3.29.2 Libc version: glibc-2.17 Python version: 3.11.3 (main, Apr 28 2023, 13:12:35) [GCC 4.9.2] (64-bit runtime) Python platform: Linux-3.10.0-1160.53.1.el7.x86_64-x86_64-with-glibc2.17 Is CUDA available: True CUDA runtime version: 12.2.140 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: Tesla P100-PCIE-16GB Nvidia driver version: 535.54.03 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Byte Order: Little Endian CPU(s): 36 On-line CPU(s) list: 0-35 Thread(s) per core: 1 Core(s) per socket: 18 Socket(s): 2 NUMA node(s): 2 Vendor ID: GenuineIntel CPU family: 6 Model: 85 Model name: Intel(R) Xeon(R) Gold 6140 CPU @ 2.30GHz Stepping: 4 CPU MHz: 3098.345 CPU max MHz: 3700.0000 CPU min MHz: 1000.0000 BogoMIPS: 4600.00 Virtualization: VT-x L1d cache:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: xecution on the device bug ### Your current environment ```text PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Red Hat Enterprise Linux Server rel...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: True CUDA runtime version: 12.2.140 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: Tesla P100-PCIE-16GB Nvidia driver version: 535.54.03 cuDNN version: Could not collect HIP runtime version: N/A M...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: RuntimeError: CUDA error: no kernel image is available for execution on the device bug ### Your current environment ```text PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ints.openai.api_server --model $MODEL --trust-remote-code --port $PORT --dtype half --enforce-eager \ --max-model-len 5000 \ --gpu-memory-utilization 0.80 & ``` ``` INFO 05-05 10:54:15 api_server.py:151] vLLM API server...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: e, image_token_id=None, image_input_shape=None, image_feature_size=None, scheduler_delay_factor=0.0, enable_chunked_prefill=False, speculative_model=None, num_speculative_tokens=None, speculative_max_model_len=None, mod...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
