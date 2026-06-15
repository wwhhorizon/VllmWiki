# vllm-project/vllm#30741: [Performance]: Performance Drops by ~20% When Using LoRA Adapter

| 字段 | 值 |
| --- | --- |
| Issue | [#30741](https://github.com/vllm-project/vllm/issues/30741) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Performance Drops by ~20% When Using LoRA Adapter

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression When deploying Qwen3-Next-80B model, I observed a ~20% performance drop when LoRA adapter is enabled, and this degradation occurs even when I requested the base model. In my test, input length is 1024~4096 tokens, output length is 256 tokens. The performance when LoRA adapter is disabled is: ``` ┏━━━━━━┳━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━┓ ┃ ┃ ┃ Avg ┃ P99 ┃ Gen. ┃ Avg ┃ P99 ┃ Avg ┃ P99 ┃ Success┃ ┃Conc. ┃ RPS ┃ Lat.(s) ┃ Lat.(s) ┃ toks/s ┃ TTFT(s) ┃ TTFT(s) ┃ TPOT(s) ┃ TPOT(s) ┃ Rate┃ ┡━━━━━━╇━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━┩ │ 10 │ 3.78 │ 2.645 │ 2.878 │ 967.43 │ 0.321 │ 0.579 │ 0.009 │ 0.010 │ 100.0%│ │ 20 │ 6.09 │ 3.284 │ 3.818 │ 1558.27 │ 0.384 │ 0.845 │ 0.011 │ 0.013 │ 100.0%│ │ 30 │ 7.81 │ 3.839 │ 4.556 │ 1999.08 │ 0.432 │ 1.040 │ 0.013 │ 0.015 │ 100.0%│ │ 40 │ 7.61 │ 5.226 │ 7.724 │ 1947.16 │ 1.177 │ 4.010 │ 0.016 │ 0.017 │ 100.0%│ │ 50 │ 7.59 │ 6.510 │ 8.335 │ 1943.28 │ 2.453 │ 4.498 │ 0.016 │ 0.017 │ 100.0%│ └──────┴──────┴──────────┴──────────┴─────────┴──────────┴────────...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: difference between "linear_qkv" and "all-linear". Is it possible to explicitly control the target modules used by LoRA adapters in vLLM to reduce overhead? ### Misc discussion on performance _No response_ ### Your curre...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: roposal to improve performance _No response_ ### Report of performance regression When deploying Qwen3-Next-80B model, I observed a ~20% performance drop when LoRA adapter is enabled, and this degradation occurs even wh...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: nce _No response_ ### Report of performance regression When deploying Qwen3-Next-80B model, I observed a ~20% performance drop when LoRA adapter is enabled, and this degradation occurs even when I requested the base mod...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ar;hardware_porting;model_support;sampling_logits cuda;operator;sampling;triton build_error env_dependency Proposal to improve performance

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
