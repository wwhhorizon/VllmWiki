# vllm-project/vllm#21096: [Bug]: The same query yields different results across different vLLM versions under identical reasoning.

| 字段 | 值 |
| --- | --- |
| Issue | [#21096](https://github.com/vllm-project/vllm/issues/21096) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: The same query yields different results across different vLLM versions under identical reasoning.

### Issue 正文摘录

### Your current environment I've tried three different version of vllm: 0.6.5, 0.8.4, 0.9.2. For example, in the environment, I only ran `pip install vllm==0.6.5`. The output after running the `collect_env.py`: ``` Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.7.0+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.11 | packaged by Anaconda, Inc. | (main, Jun 5 2025, 13:09:17) [GCC 11.2.0] (64-bit runtime) Python platform : Linux-5.15.0-94-generic-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.4.99 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA A800-SXM4-40GB GPU 1: NV...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: [Bug]: The same query yields different results across different vLLM versions under identical reasoning. bug;stale ### Your current environment I've tried three different version of vllm: 0.6.5, 0.8.4, 0.9.2. For exampl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: version : 2.7.0+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.11 |...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: output after running the `collect_env.py`: ``` Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4....
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: re=0.0, max_tokens=1024) llm = LLM(model=model_path) SYS = "You are an expert in using tools to handle real-time queries from users.\nFirst I will give you the task description, and your task start.\nAt each step, your...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: nt results across different vLLM versions under identical reasoning. bug;stale ### Your current environment I've tried three different version of vllm: 0.6.5, 0.8.4, 0.9.2. For example, in the environment, I only ran `p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
