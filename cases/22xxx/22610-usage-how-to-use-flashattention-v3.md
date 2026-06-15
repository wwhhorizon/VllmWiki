# vllm-project/vllm#22610: [Usage]: How to use FlashAttention v3

| 字段 | 值 |
| --- | --- |
| Issue | [#22610](https://github.com/vllm-project/vllm/issues/22610) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | attention |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How to use FlashAttention v3

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm When I use the following commands： ’VLLM_FLASH_ATTN_VERSION=3 VLLM_USE_V1=1 python3 -m vllm.entrypoints.openai.api_server --model /workspace/Qwen3/model/Qwen3-32B --served-model-name qwen3-32b --gpu-memory-utilization=0.9 -tp 2 --enable-auto-tool-choice --tool-call-parser hermes --enable-reasoning --reasoning-parser qwen3‘ I didn't find any related fields for flashatten in the log, and there was no improvement in the test speed on the H100 either. Therefore, I believe it didn't take effect. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ou like to use vllm When I use the following commands： ’VLLM_FLASH_ATTN_VERSION=3 VLLM_USE_V1=1 python3 -m vllm.entrypoints.openai.api_server --model /workspace/Qwen3/model/Qwen3-32B --served-model-name qwen3-32b --gpu-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: hatten in the log, and there was no improvement in the test speed on the H100 either. Therefore, I believe it didn't take effect. ### Before submitting a new issue... - [x] Make sure you already searched for relevant is...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: RSION=3 VLLM_USE_V1=1 python3 -m vllm.entrypoints.openai.api_server --model /workspace/Qwen3/model/Qwen3-32B --served-model-name qwen3-32b --gpu-memory-utilization=0.9 -tp 2 --enable-auto-tool-choice --tool-call-parser...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Usage]: How to use FlashAttention v3 usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm When I use the following commands： ’VLLM_FLASH_ATTN_VERSION=3...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ed fields for flashatten in the log, and there was no improvement in the test speed on the H100 either. Therefore, I believe it didn't take effect. ### Before submitting a new issue... - [x] Make sure you already search...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
