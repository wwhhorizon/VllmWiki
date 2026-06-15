# vllm-project/vllm#28635: [Bug]: Streaming=True causes missing or scrambled tokens with GPT-OSS 120B on vLLM v0.11.0

| 字段 | 值 |
| --- | --- |
| Issue | [#28635](https://github.com/vllm-project/vllm/issues/28635) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 26; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;moe;sampling_logits;scheduler_memory |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;moe |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Streaming=True causes missing or scrambled tokens with GPT-OSS 120B on vLLM v0.11.0

### Issue 正文摘录

### Your current environment | NVIDIA-SMI 550.127.05 Driver Version: 550.127.05 CUDA Version: 12.4 | * vLLM versions: v0.10.2 and v0.11.0 * Model: GPT-OSS 120B * Streaming: True * --enforce-eager: Tested ### 🐛 Describe the bug Issue: When using Streaming=True, some tokens are missing or arrive in scrambled order. * With Streaming=False, all tokens are generated correctly. * Using --enforce-eager produces the correct token sequence but significantly slows down generation. This issue occurs in both v0.10.2 and v0.11.0. Expected behavior: Streaming should produce all tokens in the correct order, similar to --enforce-eager, without the performance penalty. Steps to reproduce: 1. Run GPT-OSS 120B with vLLM v0.11.0 (or v0.10.2) 2. Enable streaming (Streaming=True) 3. Generate text and observe missing or scrambled tokens Additional notes: The problem appears to be specific to asynchronous streaming. Using eager execution ensures correct token order but reduces speed. Command Example ``` CUDA_VISIBLE_DEVICES=0,1,2,3 vllm serve openai/gpt-oss-120b \ --tensor-parallel-size 4 \ --enable-expert-parallel \ --tool-call-parser openai \ --reasoning-parser openai_gptoss \ --enable-auto-tool-choice...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ### Your current environment | NVIDIA-SMI 550.127.05 Driver Version: 550.127.05 CUDA Version: 12.4 | * vLLM versions: v0.10.2 and v0.11.0 * Model: GPT-OSS 120B * Streaming: True * --enforce-eager: Tested ### 🐛 Describe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: GPT-OSS 120B on vLLM v0.11.0 bug ### Your current environment | NVIDIA-SMI 550.127.05 Driver Version: 550.127.05 CUDA Version: 12.4 | * vLLM versions: v0.10.2 and v0.11.0 * Model: GPT-OSS 120B * Streaming: True * --enfo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Streaming=True causes missing or scrambled tokens with GPT-OSS 120B on vLLM v0.11.0 bug ### Your current environment | NVIDIA-SMI 550.127.05 Driver Version: 550.127.05 CUDA Version: 12.4 | * vLLM versions: v0.10....
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: lm serve openai/gpt-oss-120b \ --tensor-parallel-size 4 \ --enable-expert-parallel \ --tool-call-parser openai \ --reasoning-parser openai_gptoss \ --enable-auto-tool-choice \ --async-scheduling \ --max-model-len 131072...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: , similar to --enforce-eager, without the performance penalty. Steps to reproduce: 1. Run GPT-OSS 120B with vLLM v0.11.0 (or v0.10.2) 2. Enable streaming (Streaming=True) 3. Generate text and observe missing or scramble...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
