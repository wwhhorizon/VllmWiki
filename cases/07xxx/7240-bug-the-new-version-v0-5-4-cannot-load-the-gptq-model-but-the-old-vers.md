# vllm-project/vllm#7240: [Bug]: The new version (v0.5.4) cannot load the gptq model, but the old version (vllm=0.5.3.post1) can do it.

| 字段 | 值 |
| --- | --- |
| Issue | [#7240](https://github.com/vllm-project/vllm/issues/7240) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: The new version (v0.5.4) cannot load the gptq model, but the old version (vllm=0.5.3.post1) can do it.

### Issue 正文摘录

### Your current environment ```text --2024-08-07 03:22:15-- https://raw.githubusercontent.com/vllm-project/vllm/main/collect_env.py Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.111.133, 185.199.108.133, 185.199.110.133, ... Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.111.133|:443... connected. HTTP request sent, awaiting response... 200 OK Length: 25132 (25K) [text/plain] Saving to: ‘collect_env.py’ collect_env.py 100%[===================>] 24.54K --.-KB/s in 0.002s 2024-08-07 03:22:15 (13.9 MB/s) - ‘collect_env.py’ saved [25132/25132] Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: 14.0.0-1ubuntu1.1 CMake version: version 3.30.1 Libc version: glibc-2.35 Python version: 3.10.12 (main, Jul 29 2024, 16:56:48) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-6.1.85+-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.2.140 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: Tesla T...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Bug]: The new version (v0.5.4) cannot load the gptq model, but the old version (vllm=0.5.3.post1) can do it. bug ### Your current environment ```text --2024-08-07 03:22:15-- https://raw.githubusercontent.com/vllm-proje...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: The new version (v0.5.4) cannot load the gptq model, but the old version (vllm=0.5.3.post1) can do it. bug ### Your current environment ```text --2024-08-07 03:22:15-- https://raw.githubusercontent.com/vllm-proje...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: .com (raw.githubusercontent.com)|185.199.111.133|:443... connected. HTTP request sent, awaiting response... 200 OK Length: 25132 (25K) [text/plain] Saving to: ‘collect_env.py’ collect_env.py 100%[===================>] 2...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: h to your GPTQ model](https://huggingface.co/Qwen/Qwen2-7B-Instruct-GPTQ-Int4) model_path = '/content/Qwen2-7B-Instruct-GPTQ-Int4' # Initialize the LLM llm = LLM(model=model_path, max_model_len=4096) ValueError: Marlin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
