# vllm-project/vllm#19148: [Bug]: max-model-len + max-num-seqs is not reducing vram usage

| 字段 | 值 |
| --- | --- |
| Issue | [#19148](https://github.com/vllm-project/vllm/issues/19148) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: max-model-len + max-num-seqs is not reducing vram usage

### Issue 正文摘录

### Your current environment Hello ### 🐛 Describe the bug Runing the command`VLLM_ATTENTION_BACKEND=FLASHINFER CUDA_VISIBLE_DEVICES=1,2 VLLM_ATTENTION_BACKEND=DUAL_CHUNK_FLASH_ATTN vllm serve Qwen/Qwen2.5-7B-Instruct-1M --max-model-len 70000 --max-num-seqs 1 --port 2483 --enforce-eager` Should not eat more than what it takes for one concurrency, yet : `INFO 06-04 14:47:22 [executor_base.py:117] Maximum concurrency for 70000 tokens per request: 5.59x` Reduced the test case to : `vllm serve nvidia/Llama-3.1-Nemotron-8B-UltraLong-4M-Instruct --max-model-len 70000 --max-num-seqs 1 --port 2483` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ent Hello ### 🐛 Describe the bug Runing the command`VLLM_ATTENTION_BACKEND=FLASHINFER CUDA_VISIBLE_DEVICES=1,2 VLLM_ATTENTION_BACKEND=DUAL_CHUNK_FLASH_ATTN vllm serve Qwen/Qwen2.5-7B-Instruct-1M --max-model-len 70000 --...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: max-model-len + max-num-seqs is not reducing vram usage bug;stale ### Your current environment Hello ### 🐛 Describe the bug Runing the command`VLLM_ATTENTION_BACKEND=FLASHINFER CUDA_VISIBLE_DEVICES=1,2 VLLM_ATTEN...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: max-model-len + max-num-seqs is not reducing vram usage bug;stale ### Your current environment Hello ### 🐛 Describe the bug Runing the command`VLLM_ATTENTION_BACKEND=FLASHINFER CUDA_VISIBLE_DEVICES=1,2 VLLM_ATTEN...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: max-model-len + max-num-seqs is not reducing vram usage bug;stale ### Your current environment Hello ### 🐛 Describe the bug Runing the command`VLLM_ATTENTION_BACKEND=FLASHINFER CUDA_VISIBLE_DEVICES=1,2 VLLM_ATTEN...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 🐛 Describe the bug Runing the command`VLLM_ATTENTION_BACKEND=FLASHINFER CUDA_VISIBLE_DEVICES=1,2 VLLM_ATTENTION_BACKEND=DUAL_CHUNK_FLASH_ATTN vllm serve Qwen/Qwen2.5-7B-Instruct-1M --max-model-len 70000 --max-num-seqs 1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
