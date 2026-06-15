# vllm-project/vllm#2754: Possible sampling parameter bug in VLLM Server 

| 字段 | 值 |
| --- | --- |
| Issue | [#2754](https://github.com/vllm-project/vllm/issues/2754) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Possible sampling parameter bug in VLLM Server 

### Issue 正文摘录

I'm using VLLM 0.3.0 How I start an async server: `python -m vllm.entrypoints.openai.api_server --model mistralai/Mixtral-8x7B-Instruct-v0.1 --tensor-parallel-size 8` How I do my server call: ``` import json import requests headers = { "Content-Type": "application/json", } data = { "model": 'mistralai/Mixtral-8x7B-Instruct-v0.1', "prompt": "What's your name", "temperature": 0.000001, "max_tokens": 256, "top_k": 3, } print(data) response = requests.post( "http://localhost:8000/v1/completions", headers=headers, data=json.dumps(data) ) text = response.json()["choices"][0]["text"] print(text) ``` Server log output `INFO 02-05 06:07:10 async_llm_engine.py:431] Received request cmpl-138b6b226481411891d25fb8673422fb-0: prompt: None, prefix_pos: None,sampling params: SamplingParams(n=1, best_of=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=1e-06, top_p=1.0, top_k=-1, min_p=0.0, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[], stop_token_ids=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=256, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True), prompt token ids:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 7B-Instruct-v0.1 --tensor-parallel-size 8` How I do my server call: ``` import json import requests headers = { "Content-Type": "application/json", } data = { "model": 'mistralai/Mixtral-8x7B-Instruct-v0.1', "prompt": "...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: nalty=1.0, temperature=1e-06, top_p=1.0, top_k=-1, min_p=0.0, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[], stop_token_ids=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=2...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: .0, temperature=1e-06, top_p=1.0, top_k=-1, min_p=0.0, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[], stop_token_ids=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=256, log...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: start an async server: `python -m vllm.entrypoints.openai.api_server --model mistralai/Mixtral-8x7B-Instruct-v0.1 --tensor-parallel-size 8` How I do my server call: ``` import json import requests headers = { "Content-T...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ensor-parallel-size 8` How I do my server call: ``` import json import requests headers = { "Content-Type": "application/json", } data = { "model": 'mistralai/Mixtral-8x7B-Instruct-v0.1', "prompt": "What's your name", "...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
