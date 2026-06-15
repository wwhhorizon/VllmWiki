# vllm-project/vllm#15420: [Bug]: logprobs/ranks not matching when comparing `vllm` with `transformers`

| 字段 | 值 |
| --- | --- |
| Issue | [#15420](https://github.com/vllm-project/vllm/issues/15420) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: logprobs/ranks not matching when comparing `vllm` with `transformers`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am RL'ing [mistralai/Mistral-Small-24B-Instruct-2501](https://huggingface.co/mistralai/Mistral-Small-24B-Instruct-2501) using `transformers`, and am moving RL sampling to use `vllm`. I am comparing the prompt logprobs to make sure the migration is the same. Here's the prompt logprobs and tokens coming from `transformers` (note the presence of the BOS token): ```none [('-1.76e+01', ' '), ('-1.49e+01', '[SYSTEM_PROMPT]'), ('-1.00e+01', 'You'), ('-6.53e+00', 'Ġare'), ('-8.25e+00', 'Ġa'), ('-1.41e+01', 'Ġscientific'), ...] ``` Here's the same set up with `vllm serve`: ``` [None, {'logprob': -1.71e+01, 'rank': 130797, 'decoded_token': '[SYSTEM_PROMPT]'}, {'logprob': -9.75e+00, 'rank': 979, 'decoded_token': 'You'}, {'logprob': -9.08e+00, 'rank': 177, 'decoded_token': 'Ġare'}, {'logprob': -6.81e+00, 'rank': 88, 'decoded_token': 'Ġa'}, {'logprob': -1.47e+01, 'rank': 6068, 'decoded_token': 'Ġscientific'}] ``` The primary differences are: - `logprob` values are different - BOS token is not present in the `vllm` output Both are using `flash_attention` 2 backend, `bfloat16`, and the same sampling configuration. --- Here is the full "stack"...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: the bug I am RL'ing [mistralai/Mistral-Small-24B-Instruct-2501](https://huggingface.co/mistralai/Mistral-Small-24B-Instruct-2501) using `transformers`, and am moving RL sampling to use `vllm`. I am comparing the prompt...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ogprobs/ranks not matching when comparing `vllm` with `transformers` bug;stale ### Your current environment ### 🐛 Describe the bug I am RL'ing [mistralai/Mistral-Small-24B-Instruct-2501](https://huggingface.co/mistralai...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: 'You'), ('-6.53e+00', 'Ġare'), ('-8.25e+00', 'Ġa'), ('-1.41e+01', 'Ġscientific'), ...] ``` Here's the same set up with `vllm serve`: ``` [None, {'logprob': -1.71e+01, 'rank': 130797, 'decoded_token': '[SYSTEM_PROMPT]'},...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: esent in the `vllm` output Both are using `flash_attention` 2 backend, `bfloat16`, and the same sampling configuration. --- Here is the full "stack" with `vllm serve`, running: ```bash VLLM_USE_V1=1 VLLM_ATTENTION_BACKE...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: t environment ### 🐛 Describe the bug I am RL'ing [mistralai/Mistral-Small-24B-Instruct-2501](https://huggingface.co/mistralai/Mistral-Small-24B-Instruct-2501) using `transformers`, and am moving RL sampling to use `vllm...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
