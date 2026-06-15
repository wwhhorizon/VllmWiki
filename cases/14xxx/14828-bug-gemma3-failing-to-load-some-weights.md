# vllm-project/vllm#14828: [Bug]: Gemma3 failing to load some weights

| 字段 | 值 |
| --- | --- |
| Issue | [#14828](https://github.com/vllm-project/vllm/issues/14828) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | activation;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma3 failing to load some weights

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When launching vllm server for gemma 3 27b it, vllm logs warn that some weights are not initialized from checkpoint. Software environment ``` pip install vllm --pre --extra-index-url https://wheels.vllm.ai/nightly pip install git+https://github.com/huggingface/transformers@v4.49.0-Gemma-3 ``` Hardware: A100 (40GB) vllm server launch command ``` python -m vllm.entrypoints.openai.api_server --tensor-parallel-size 4 --model google/gemma-3-27b-it --port 8000 ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: hts are not initialized from checkpoint. Software environment ``` pip install vllm --pre --extra-index-url https://wheels.vllm.ai/nightly pip install git+https://github.com/huggingface/transformers@v4.49.0-Gemma-3 ``` H...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: tps://github.com/huggingface/transformers@v4.49.0-Gemma-3 ``` Hardware: A100 (40GB) vllm server launch command ``` python -m vllm.entrypoints.openai.api_server --tensor-parallel-size 4 --model google/gemma-3-27b-it --po...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Gemma3 failing to load some weights bug ### Your current environment ### 🐛 Describe the bug When launching vllm server for gemma 3 27b it, vllm logs warn that some weights are not initialized from checkpoint. Soft
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: t;sampling_logits;speculative_decoding activation;cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: Gemma3 failing to load some weights bug ### Your current environment ### 🐛 Describe the bug When launching vllm server for gemma 3 27b it, vllm logs warn that some weights are not initialized from checkpoint. Soft

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
