# vllm-project/vllm#4258: [Bug]: TypeError when enable_lora=True on Python 3.8

| 字段 | 值 |
| --- | --- |
| Issue | [#4258](https://github.com/vllm-project/vllm/issues/4258) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: TypeError when enable_lora=True on Python 3.8

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: Could not collect CMake version: version 3.29.2 Libc version: glibc-2.31 Python version: 3.8.19 (default, Mar 20 2024, 19:58:24) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.4.0-126-generic-x86_64-with-glibc2.17 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 3090 GPU 1: NVIDIA GeForce RTX 3090 GPU 2: NVIDIA GeForce RTX 3090 GPU 3: NVIDIA GeForce RTX 3090 GPU 4: NVIDIA GeForce RTX 3090 GPU 5: NVIDIA GeForce RTX 3090 GPU 6: NVIDIA GeForce RTX 3090 GPU 7: NVIDIA GeForce RTX 3090 Nvidia driver version: 535.129.03 cuDNN version: Probably one of the following: /usr/local/cuda-11.8/targets/x86_64-linux/lib/libcudnn.so.8.9.6 /usr/local/cuda-11.8/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8.9.6 /usr/local/cuda-11.8/targets/x86_64-linux/lib/libcudnn_adv_train.so.8.9.6 /usr/local/cuda-11.8/ta...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: rrent environment ```text Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04 LTS (x86_64) GCC versi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: n 3.8 bug ### Your current environment ```text Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04 L...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ffected Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Mitigation; Clear CPU buffers; SMT vulnerable Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl and secc...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: a_name = "lora" prompt = "Hello, my name is" llm = LLM(model=model_name, dtype="float16", enable_lora=True) sampling_params = SamplingParams( temperature=0.8, top_p=0.95, max_tokens=75) preds = llm.generate(prompt, samp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
