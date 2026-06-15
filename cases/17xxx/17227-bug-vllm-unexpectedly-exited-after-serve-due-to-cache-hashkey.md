# vllm-project/vllm#17227: [Bug]: VLLM unexpectedly exited after serve due to cache hashkey

| 字段 | 值 |
| --- | --- |
| Issue | [#17227](https://github.com/vllm-project/vllm/issues/17227) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: VLLM unexpectedly exited after serve due to cache hashkey

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug After running for a period of time, VLLM unexpectedly exited after the serve command. **The issue occurred after running for some time, with all previous requests working fine.** ``` format. \n assistant\n', params: SamplingParams(n=16, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.05, temperature=0.7, top_p=0.9, top_k=-1, min_p=0.0, seed=None, stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=127835, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None, extra_args=None), prompt_token_ids: None, lora_request: None, prompt_adapter_request: None. ERROR 04-26 11:29:08 [core.py:387] EngineCore hit an exception: Traceback (most recent call last): ERROR 04-26 11:29:08 [core.py:387] File "/home/zhiyuan/anaconda3/envs/n-vllm/lib/python3.12/site-packages/cachetools/__init__.py", line 68, in __getitem__ ERROR 04-26 11:29:08 [core.py:387] return self.__data[key] ERROR 04-26 11:29:08 [core.py:387] ~~~~~~~~~~~^^^^^ ERROR 04-26 11:29:08 [core.py:387] KeyError: '...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: okens=127835, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None, extra_args=None), prompt_token_ids: None,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: nd. **The issue occurred after running for some time, with all previous requests working fine.** ``` format. \n assistant\n', params: SamplingParams(n=16, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: r running for some time, with all previous requests working fine.** ``` format. \n assistant\n', params: SamplingParams(n=16, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.05, temperature=0.7, top_p=...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
