# vllm-project/vllm#18946: [Bug]: Eagle3 in vLLM v0.9.0 has no acceleration effect.

| 字段 | 值 |
| --- | --- |
| Issue | [#18946](https://github.com/vllm-project/vllm/issues/18946) |
| 状态 | closed |
| 标签 | bug;speculative-decoding |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Eagle3 in vLLM v0.9.0 has no acceleration effect.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Test details: vLLM version: 0.9.0 Test dataset: MT-bench GPU: RTX 3090 Base model: Llama-3.1-8B-Instruct Eagle models: EAGLE-LLaMA3.1-Instruct-8B, EAGLE3-LLaMA3.1-Instruct-8B Execution commands: python examples/offline_inference/eagle.py --num_spec_tokens 2 --max_num_seqs 1 --num_prompts 80 --method 'eagle' python examples/offline_inference/eagle.py --num_spec_tokens 2 --max_num_seqs 1 --num_prompts 80 --method 'eagle3' Results: eagle: 75 tokens/s eagle3: 47 tokens/s baseline (no speculative decoding): 48 tokens/s When testing the same models in the original Eagle repository, both show acceleration effects: eagle achieves 2.4x speedup eagle3 achieves 3.7x speedup Question: Does this mean vLLM 0.9.0 has compatibility issues with Eagle3? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Your current environment ### 🐛 Describe the bug Test details: vLLM version: 0.9.0 Test dataset: MT-bench GPU: RTX 3090 Base model: Llama-3.1-8B-Instruct Eagle models: EAGLE-LLaMA3.1-Instruct-8B, EAGLE3-LLaMA3.1-Instruct...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: e the bug Test details: vLLM version: 0.9.0 Test dataset: MT-bench GPU: RTX 3090 Base model: Llama-3.1-8B-Instruct Eagle models: EAGLE-LLaMA3.1-Instruct-8B, EAGLE3-LLaMA3.1-Instruct-8B Execution commands: python example...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: t details: vLLM version: 0.9.0 Test dataset: MT-bench GPU: RTX 3090 Base model: Llama-3.1-8B-Instruct Eagle models: EAGLE-LLaMA3.1-Instruct-8B, EAGLE3-LLaMA3.1-Instruct-8B Execution commands: python examples/offline_inf...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Eagle3 in vLLM v0.9.0 has no acceleration effect. bug;speculative-decoding ### Your current environment ### 🐛 Describe the bug Test details: vLLM version: 0.9.0 Test dataset: MT-bench GPU: RTX 3090 Base model: Ll...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
