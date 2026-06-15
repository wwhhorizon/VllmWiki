# vllm-project/vllm#2938: `early_stopping` potentially not working via api request

| 字段 | 值 |
| --- | --- |
| Issue | [#2938](https://github.com/vllm-project/vllm/issues/2938) |
| 状态 | closed |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> `early_stopping` potentially not working via api request

### Issue 正文摘录

While using `v0.3.1`, `early_stopping` will not toggle to `True` due to an omission in the protocol definition (see below comments). I am prompting like this: ``` headers = { 'Content-Type': 'application/json', } json_data = { 'model': '/mnt/models/', 'prompt': ['Something', 'Something'], 'max_tokens': 128, 'use_beam_search': True, 'best_of': 4, 'temperature': 0, 'early_stopping': True, ###'min_tokens': 30 ###'stop_token_ids': [50256], } response = requests.post(f'{api_server}/v1/completions', headers=headers, json=json_data, verify=False) print(json.loads(response.text)) ``` and this is what I get on server side: ``` INFO 02-20 21:36:30 async_llm_engine.py:433] Received request cmpl-0a8493bd1a77481fb2396bb42c6bd9af-1: prompt: None, prefix_pos: None,sampling_params: SamplingParams(n=1, best_of=4, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.0, top_p=1.0, top_k=-1, min_p=0.0, use_beam_search=True, length_penalty=1.0, early_stopping=False, stop=[], stop_token_ids=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=128, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True), prompt_token_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: _eos=False, max_tokens=128, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True), prompt_token_ids: [5195, 407, 30], lora_request: None. ``` Everything else I set is there,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: mpt': ['Something', 'Something'], 'max_tokens': 128, 'use_beam_search': True, 'best_of': 4, 'temperature': 0, 'early_stopping': True, ###'min_tokens': 30 ###'stop_token_ids': [50256], } response = requests.post(f'{api_s...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: '{api_server}/v1/completions', headers=headers, json=json_data, verify=False) print(json.loads(response.text)) ``` and this is what I get on server side: ``` INFO 02-20 21:36:30 async_llm_engine.py:433] Received request...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: eaders = { 'Content-Type': 'application/json', } json_data = { 'model': '/mnt/models/', 'prompt': ['Something', 'Something'], 'max_tokens': 128, 'use_beam_search': True, 'best_of': 4, 'temperature': 0, 'early_stopping':...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: `early_stopping` potentially not working via api request While using `v0.3.1`, `early_stopping` will not toggle to `True` due to an omission in the protocol definition (see below comments). I am prompting like this: ```...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
