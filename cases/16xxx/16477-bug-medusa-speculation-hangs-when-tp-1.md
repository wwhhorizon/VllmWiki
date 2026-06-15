# vllm-project/vllm#16477: [Bug]: Medusa speculation hangs when tp > 1

| 字段 | 值 |
| --- | --- |
| Issue | [#16477](https://github.com/vllm-project/vllm/issues/16477) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Medusa speculation hangs when tp > 1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi team! Launching a model with Medusa heads as a drafter with TP > 1 causes hangs when collecting the unembedding layer. Code to reproduce: ```python from vllm.entrypoints.llm import LLM if __name__ == "__main__": MODEL_NAME = "JackFram/llama-68m" SPEC_MODEL = "abhigoyal/vllm-medusa-llama-68m-random" llm = LLM( model=MODEL_NAME, max_model_len=1024, speculative_config={ "model": SPEC_MODEL, "num_speculative_tokens": 5, }, tensor_parallel_size=2, seed=0, ) outputs = llm.generate(prompts=["Hi! How are you doing?"], use_tqdm=True) ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: embedding layer. Code to reproduce: ```python from vllm.entrypoints.llm import LLM if __name__ == "__main__": MODEL_NAME = "JackFram/llama-68m" SPEC_MODEL = "abhigoyal/vllm-medusa-llama-68m-random" llm = LLM( model=MODE...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: our current environment ### 🐛 Describe the bug Hi team! Launching a model with Medusa heads as a drafter with TP > 1 causes hangs when collecting the unembedding layer. Code to reproduce: ```python from vllm.entrypoints...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Medusa speculation hangs when tp > 1 bug;stale ### Your current environment ### 🐛 Describe the bug Hi team! Launching a model with Medusa heads as a drafter with TP > 1 causes hangs when collecting the unembeddin...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: pport;sampling_logits;speculative_decoding cuda;kernel;operator;sampling;triton build_error;nan_inf env_dependency #4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size Your cur...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | > + 0x94ac3 (0x7f80264d7ac3 in /lib/x86_64-linux-gnu/libc.so.6) frame #4: <unknown function> + 0x126850 (0x7f8026569850 in /lib/x86_64-linux-gnu/libc.so.6) /opt/conda/lib/python3.… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | > + 0x94ac3 (0x7f80264d7ac3 in /lib/x86_64-linux-gnu/libc.so.6) frame #6: <unknown function> + 0x126850 (0x7f8026569850 in /lib/x86_64-linux-gnu/libc.so.6) exception raised from n… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
