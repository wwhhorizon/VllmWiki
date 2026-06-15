# vllm-project/vllm#23752: [Bug]: DeepSeek R1 with DP=8 on one 8xB200 node has 3x TPOT when concurrency < 8 than concurrency >= 8

| 字段 | 值 |
| --- | --- |
| Issue | [#23752](https://github.com/vllm-project/vllm/issues/23752) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DeepSeek R1 with DP=8 on one 8xB200 node has 3x TPOT when concurrency < 8 than concurrency >= 8

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running a 1p1d configuration across 2 nodes for DeepSeek R1 on 2x B200 nodes. P is configured high throughput and D is configured low latency. On the D node, running a 1:100 input/output token serving benchmark shows: * TPOT of ~120ms for concurrency 1 through 7 * TPOT of 41ms at concurrency 8 * TPOT of 45ms at concurrency 9 This also occurs with the same test on the P node. Command line flags and env described [here](https://github.com/smarterclayton/ig-load/blob/pd/config/deploy_base_deepseek_r1_ep_pd.yaml#L81) #### Concurrency=7 ``` Namespace(backend='vllm', base_url='http://vllm-deepseek-r1-ep-pd-0.vllm-deepseek-r1-ep-pd.default:8000', host='127.0.0.1', port=8000, endpoint='/v1/completions', dataset_name='random', dataset_path=None, no_stream=False, max_concurrency=7, model='deepseek-ai/DeepSeek-R1', tokenizer=None, use_beam_search=False, num_prompts=21, logprobs=None, request_rate=inf, burstiness=1.0, seed=12101231, trust_remote_code=False, disable_tqdm=False, profile=False, save_result=False, save_detailed=False, append_result=False, metadata=None, result_dir=None, result_filename=None, ignore_eos=True, percentile_metrics='...

## 现有链接修复摘要

#23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 6: [Bug]: DeepSeek R1 with DP=8 on one 8xB200 node has 3x TPOT when concurrency < 8 than concurrency >= 8 bug;stale ### Your current environment ### 🐛 Describe the bug Running a 1p1d configuration across 2 nodes for DeepSe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: DeepSeek R1 with DP=8 on one 8xB200 node has 3x TPOT when concurrency < 8 than concurrency >= 8 bug;stale ### Your current environment ### 🐛 Describe the bug Running a 1p1d configuration across 2 nodes for DeepSe...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ploy_base_deepseek_r1_ep_pd.yaml#L81) #### Concurrency=7 ``` Namespace(backend='vllm', base_url='http://vllm-deepseek-r1-ep-pd-0.vllm-deepseek-r1-ep-pd.default:8000', host='127.0.0.1', port=8000, endpoint='/v1/completio...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;sampling_logits;speculative_decoding cuda;operator;sampling;triton b...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ### Your current environment ### 🐛 Describe the bug Running a 1p1d configuration across 2 nodes for DeepSeek R1 on 2x B200 nodes. P is configured high throughput and D is configured low latency. On the D node, running a...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#23942](https://github.com/vllm-project/vllm/pull/23942) | mentioned | 0.6 | [CI]  Add `aiter` to matching list of issue auto labeller for `rocm` tag | el: NO (0 matches) #23754: Should have ROCm label: NO (0 matches) #23752: Should have ROCm label: NO (0 matches) #23744: Should have ROCm label: NO (0 matches) #23739: Should hav |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
