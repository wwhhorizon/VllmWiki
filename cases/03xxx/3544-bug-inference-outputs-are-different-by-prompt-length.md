# vllm-project/vllm#3544: [Bug]: Inference outputs are different by prompt length

| 字段 | 值 |
| --- | --- |
| Issue | [#3544](https://github.com/vllm-project/vllm/issues/3544) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Inference outputs are different by prompt length

### Issue 正文摘录

### Your current environment ``` Collecting environment information... PyTorch version: 2.1.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.26.4 Libc version: glibc-2.35 Python version: 3.10.13 (main, Sep 11 2023, 13:44:35) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.4.0-169-generic-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 11.8.89 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB Nvidia driver version: 525.147.05 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.9.6 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.9.6 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.9.6 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.9.6 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_train.so.8.9.6 /usr/lib/x86_64-linux-gnu/libcudnn_ops_infer.so.8.9.6 /usr/lib/x86_64-linux-gnu/libcudnn_ops_train.so.8.9.6 HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: r current environment ``` Collecting environment information... PyTorch version: 2.1.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.1.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: gth bug;stale ### Your current environment ``` Collecting environment information... PyTorch version: 2.1.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: path = 'squarelike/Gugugo-koen-7B-V1.1' model = LLM( model_path, dtype=torch.float16, trust_remote_code=True, ) # Prompt def make_prompt(text): prompt_format = "### 영어: {} \n### 한국어:" return prompt_format.format(text) p...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Inference outputs are different by prompt length bug;stale ### Your current environment ``` Collecting environment information... PyTorch version: 2.1.1+cu121 Is debug build: False CUDA used to build PyTorch: 12....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
