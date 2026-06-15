# vllm-project/vllm#19613: [Bug]: Get NCCL_ERROR_SYSTEM_ERROR with latest Docker vLLM image (v0.9.1)

| 字段 | 值 |
| --- | --- |
| Issue | [#19613](https://github.com/vllm-project/vllm/issues/19613) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;fp8;kernel;sampling |
| 症状 | crash |
| 根因提示 | dtype;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Get NCCL_ERROR_SYSTEM_ERROR with latest Docker vLLM image (v0.9.1)

### Issue 正文摘录

### Your current environment I am running distributed vLLM on a 4-node Ray cluster where each node has 8 GPUs (NVIDIA RTX 2000) and 8 NIC ports (CX-5). vLLM does start correctly at launch time. The crash happens when I start the HF Inference Benchmark. See details in the Describe the bug section below. Note that my test is working fine with vLLM v0.8.5.post1 (upgraded to Ray 2.4.6) Using the DeepSeek-R1-Distill-Llama-8B model but the issue also happens with other models, such as Llama-4-Maverick-17B-128E-Instruct-FP8 Current component version ``` root@echo:/vllm-workspace# pip show vllm Name: vllm Version: 0.9.1 root@echo:/vllm-workspace# pip show ray Name: ray Version: 2.46.0 NV_LIBNCCL_PACKAGE=libnccl2=2.25.1-1+cuda12.8 ``` ### 🐛 Describe the bug ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Get NCCL_ERROR_SYSTEM_ERROR with latest Docker vLLM image (v0.9.1) bug ### Your current environment I am running distributed vLLM on a 4-node Ray cluster where each node has 8 GPUs (NVIDIA RTX 2000) and 8 NIC por...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: so happens with other models, such as Llama-4-Maverick-17B-128E-Instruct-FP8 Current component version ``` root@echo:/vllm-workspace# pip show vllm Name: vllm Version: 0.9.1 root@echo:/vllm-workspace# pip show ray Name:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: tributed vLLM on a 4-node Ray cluster where each node has 8 GPUs (NVIDIA RTX 2000) and 8 NIC ports (CX-5). vLLM does start correctly at launch time. The crash happens when I start the HF Inference Benchmark. See details...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: oes start correctly at launch time. The crash happens when I start the HF Inference Benchmark. See details in the Describe the bug section below. Note that my test is working fine with vLLM v0.8.5.post1 (upgraded to Ray...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: Get NCCL_ERROR_SYSTEM_ERROR with latest Docker vLLM image (v0.9.1) bug ### Your current environment I am running distributed vLLM on a 4-node Ray cluster where each node has 8 GPUs (NVIDIA RTX 2000) and 8 NIC por...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
