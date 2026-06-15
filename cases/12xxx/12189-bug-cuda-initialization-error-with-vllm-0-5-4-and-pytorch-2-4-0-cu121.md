# vllm-project/vllm#12189: [Bug]: CUDA initialization error with vLLM 0.5.4 and PyTorch 2.4.0+cu121

| 字段 | 值 |
| --- | --- |
| Issue | [#12189](https://github.com/vllm-project/vllm/issues/12189) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA initialization error with vLLM 0.5.4 and PyTorch 2.4.0+cu121

### Issue 正文摘录

### Your current environment ``` PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.2 LTS (x86_64) GCC version: (Ubuntu 11.3.0-1ubuntu1~22.04) 11.3.0 Clang version: Could not collect CMake version: version 3.31.4 Libc version: glibc-2.35 Python version: 3.11.11 (main, Dec 11 2024, 16:28:39) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.10.134-008.7.kangaroo.al8.x86_64-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB GPU 1: NVIDIA A100-SXM4-80GB GPU 2: NVIDIA A100-SXM4-80GB GPU 3: NVIDIA A100-SXM4-80GB GPU 4: NVIDIA A100-SXM4-80GB GPU 5: NVIDIA A100-SXM4-80GB GPU 6: NVIDIA A100-SXM4-80GB GPU 7: NVIDIA A100-SXM4-80GB Nvidia driver version: 535.54.03 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.9.1 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.9.1 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.9.1 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.9.1 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_train.so.8.9.1 /usr/lib/x86_64-linux-gnu/...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: d PyTorch 2.4.0+cu121 bug;stale ### Your current environment ``` PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.2 LTS (x86_64) GCC ve...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: CUDA initialization error with vLLM 0.5.4 and PyTorch 2.4.0+cu121 bug;stale ### Your current environment ``` PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB GPU 1: NVIDIA A100-SXM4-80GB GPU 2: NVIDIA A100-SXM4-80GB GPU 3: NVIDIA A100-SXM4-80GB GPU...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: None, rope_theta=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=8192, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=8, pipeline_parallel_size=1, disable_...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ]: CUDA initialization error with vLLM 0.5.4 and PyTorch 2.4.0+cu121 bug;stale ### Your current environment ``` PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
