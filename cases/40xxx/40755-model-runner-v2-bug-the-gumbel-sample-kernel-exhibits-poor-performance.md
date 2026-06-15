# vllm-project/vllm#40755: [Model Runner V2][Bug]: The _gumbel_sample_kernel exhibits poor performance on H800.

| 字段 | 值 |
| --- | --- |
| Issue | [#40755](https://github.com/vllm-project/vllm/issues/40755) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Model Runner V2][Bug]: The _gumbel_sample_kernel exhibits poor performance on H800.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I have tested the performance of Model Runner V2 with Eagle3 enabled on H800. The result is inferior to that of Model Runner V1. Current analysis identifies that the excessive latency of the _gumbel_sample_kernel is the root cause, as shown in the figure below. I conducted the test with the following command and test script. command: > VLLM_USE_V2_MODEL_RUNNER=1 vllm serve /nas/disk1/Qwen3-8B --max-num-batched-tokens 32768 --no-enable-prefix-caching --host 0.0.0.0 --port 8898 test script > vllm bench serve --backend openai-chat --model /nas/disk1/Qwen3-8B --tokenizer /nas/disk1/Qwen3-8B --served-model-name /nas/disk1/Qwen3-8B --dataset-name custom --dataset-path /model/lyc/esData/esdata5daysago.jsonl --custom-output-len 100 --num-prompts 400 --max-concurrency 40 --endpoint /v1/chat/completions --ignore-eos --percentile-metrics ttft,tpot,itl,e2el --host 55.122.12.106 --port 30004 --seed 42 The _gumbel_sample_kernel needs to process logits with the shape of [num_tokens, vocab_size]. > def gumbel_sample( > logits: torch.Tensor, # [num_tokens, vocab_size] > ...... > ) -> torch.Tensor: > num_tokens, vocab_size = logits.shape > BLOCK_S...

## 现有链接修复摘要

#34854 [Model Runner V2] Use FP32 for Gumbel Noise

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: _sample_kernel[(num_tokens, num_blocks)]( When Eagle3 is disabled, each request generates one token. Under 40 concurrency, `num_tokens` equals 40, and the latency of this operator on the H800 is approximately 800 μs. Wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: 800. bug ### Your current environment ### 🐛 Describe the bug I have tested the performance of Model Runner V2 with Eagle3 enabled on H800. The result is inferior to that of Model Runner V1. Current analysis identifies t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ix-caching --host 0.0.0.0 --port 8898 test script > vllm bench serve --backend openai-chat --model /nas/disk1/Qwen3-8B --tokenizer /nas/disk1/Qwen3-8B --served-model-name /nas/disk1/Qwen3-8B --dataset-name custom --data...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ue? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#34854](https://github.com/vllm-project/vllm/pull/34854) | mentioned | 0.45 | [Model Runner V2] Use FP32 for Gumbel Noise | rrent performance data is shown below. 40 concurrency \| num_tokens \| #34854 pr \| #37798 pr \| \| ---------- \| --------- \| ------ \| \| 40(eagle3 disable) \| 81us \| 800us \| |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
