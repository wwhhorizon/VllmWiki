# vllm-project/vllm#10185: [Bug]: 500 Internal Server Error when calling v1/completions and v1/chat/completions with vllm/vllm-openai:v0.6.3.post1 on OpenShift

| 字段 | 值 |
| --- | --- |
| Issue | [#10185](https://github.com/vllm-project/vllm/issues/10185) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: 500 Internal Server Error when calling v1/completions and v1/chat/completions with vllm/vllm-openai:v0.6.3.post1 on OpenShift

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm deploying the [latest docker container](https://hub.docker.com/r/vllm/vllm-openai/tags) (0.6.3.post1) on OpenShift. Regardless of model I'm getting "500 Internal Server Error" while calling v1/completions and v1/chat/completions endpoints when deployed on OpenShift. Remaining endpoints such as tokenize and v1/models are working as expected. Appears to be similar to #9193 but I don't see any of the permission issues mentioned by @apexx77 and hopefully resolved by @Cognitus-Stuti and @s-sajid-ali too. ``` DEBUG 11-09 10:30:11 client.py:170] Waiting for output from MQLLMEngine. INFO: 10.254.4.2:48216 - "GET /v1/models HTTP/1.1" 200 OK INFO 11-09 10:30:12 logger.py:37] Received request chat-288661688ea84b4dbd1e5b381e5ad4dc: prompt: ' system \n\nCutting Knowledge Date: December 2023\nToday Date: 26 Jul 2024\n\nYou are a helpful assistant. user \n\nWho won the world series in 2020? assistant \n\nThe Los Angeles Dodgers won the World Series in 2020. user \n\nWhere was it played? assistant \n\n', params: SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temper...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Dumps _No response_ ### 🐛 Describe the bug I'm deploying the [latest docker container](https://hub.docker.com/r/vllm/vllm-openai/tags) (0.6.3.post1) on OpenShift. Regardless of model I'm getting "500 Internal Server Err...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: us-Stuti and @s-sajid-ali too. ``` DEBUG 11-09 10:30:11 client.py:170] Waiting for output from MQLLMEngine. INFO: 10.254.4.2:48216 - "GET /v1/models HTTP/1.1" 200 OK INFO 11-09 10:30:12 logger.py:37] Received request ch...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: rams(json=None, regex=None, choice=None, grammar=None, json_object=None, backend=None, whitespace_pattern=None) INFO: 10.254.4.2:48216 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error DEBUG 11-09 10:30:1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: by. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 0.0, seed=None, stop=[], stop_token_ids=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=4017, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
