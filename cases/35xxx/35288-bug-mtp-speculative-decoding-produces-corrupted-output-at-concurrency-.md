# vllm-project/vllm#35288: [Bug]: MTP speculative decoding produces corrupted output at concurrency >= 4 (V1 engine)

| 字段 | 值 |
| --- | --- |
| Issue | [#35288](https://github.com/vllm-project/vllm/issues/35288) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: MTP speculative decoding produces corrupted output at concurrency >= 4 (V1 engine)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Model Large MoE model (80B total / 3B active params, Qwen3-based architecture) Qwen3 Next 80B instruct ## How would you like to use vllm Serving via the OpenAI-compatible API with MTP speculative decoding. ## Description When serving a model with MTP speculative decoding (`num_speculative_tokens=2`) and 4+ concurrent requests land in the decode batch simultaneously, a CUDA illegal memory access corrupts the model's internal state. This produces **completely garbage output** — not verbose-but-valid text, but corrupted token sequences that loop until `max_tokens` is hit. The configured stop token is never matched because the output is unintelligible noise. This is 100% reproducible. ## Speculative decoding config ```json {"method": "mtp", "num_speculative_tokens": 2} ``` ## Normal output (concurrency=1, MTP working correctly) ``` The model produces a coherent, well-structured ~93-token answer. finish_reason=stop, stop token matched correctly. ``` ## Corrupted output (concurrency=4, bug triggered) ### Example 1: Garbage then single-token repetition loop ``` suggested> (black/now.com **>! etc/ast Bill ** # 1997-1997-1996-1996-1996...

## 现有链接修复摘要

#1997 Replace head_mapping params with num_kv_heads to attention kernel.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: matched because the output is unintelligible noise. This is 100% reproducible. ## Speculative decoding config ```json {"method": "mtp", "num_speculative_tokens": 2} ``` ## Normal output (concurrency=1, MTP working corre...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: engine) bug ### Your current environment ### 🐛 Describe the bug ## Model Large MoE model (80B total / 3B active params, Qwen3-based architecture) Qwen3 Next 80B instruct ## How would you like to use vllm Serving via the...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: MTP speculative decoding produces corrupted output at concurrency >= 4 (V1 engine) bug ### Your current environment ### 🐛 Describe the bug ## Model Large MoE model (80B total / 3B active params, Qwen3-based archi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ug ## Model Large MoE model (80B total / 3B active params, Qwen3-based architecture) Qwen3 Next 80B instruct ## How would you like to use vllm Serving via the OpenAI-compatible API with MTP speculative decoding. ## Desc...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: s=2000, stop=[" "], extra_body={"skip_special_tokens": False}, ) print(f"tokens={response.usage.completion_tokens}, " f"finish={response.choices[0].finish_reason}") # At c>=4, expect finish_reason=length and ~2000 token...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#1997](https://github.com/vllm-project/vllm/pull/1997) | mentioned | 0.45 | Replace head_mapping params with num_kv_heads to attention kernel. | m **>!<this>etc/ast bill ** # 1997-1997-1996-1996-1996-1996-1996-1996-#1997-1996-1996-1996-1996-1996-1996- 1996-1996-1996-1996-1996-1996-1996-1996-1996-1996-1996-1996-1996-1996-19… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
