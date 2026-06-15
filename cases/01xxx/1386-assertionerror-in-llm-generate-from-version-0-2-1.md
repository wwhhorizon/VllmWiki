# vllm-project/vllm#1386: AssertionError in LLM.generate from version 0.2.1

| 字段 | 值 |
| --- | --- |
| Issue | [#1386](https://github.com/vllm-project/vllm/issues/1386) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> AssertionError in LLM.generate from version 0.2.1

### Issue 正文摘录

I've only tested this using Zephyr (mistral-type model), but when calling LLM.generate in version 0.2.1, I receive an AssertionError in the worker runs. Code to reproduce: ```py from vllm import LLM, SamplingParams llm = LLM("HuggingFaceH4/zephyr-7b-alpha", tensor_parallel_size=4) sampling_params = SamplingParams( temperature=0.1, top_p=0.95, max_tokens=400 ) output = llm.generate(["Hello, how are you?", "Tell me a joke!"], sampling_params=sampling_params) ``` Same code block works fine in 0.2.0. Full traceback in version 0.2.1: ``` AssertionError Traceback (most recent call last) File , line 10 3 llm = LLM("HuggingFaceH4/zephyr-7b-alpha", tensor_parallel_size=4) 5 sampling_params = SamplingParams( 6 temperature=0.1, 7 top_p=0.95, 8 max_tokens=400 9 ) ---> 10 output = llm.generate(["Hello, how are you?", "Tell me a joke!"], sampling_params=sampling_params) File /local_disk0/.ephemeral_nfs/envs/pythonEnv-f955471c-8346-4f89-b3b6-d25bfb1d27ae/lib/python3.10/site-packages/vllm/entrypoints/llm.py:157, in LLM.generate(self, prompts, sampling_params, prompt_token_ids, use_tqdm) 155 token_ids = prompt_token_ids[i] 156 self._add_request(prompt, sampling_params, token_ids) --> 157 return se...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: AssertionError in LLM.generate from version 0.2.1 bug I've only tested this using Zephyr (mistral-type model), but when calling LLM.generate in version 0.2.1, I receive an AssertionError in the worker runs. Code to repr...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ou?", "Tell me a joke!"], sampling_params=sampling_params) ``` Same code block works fine in 0.2.0. Full traceback in version 0.2.1: ``` AssertionError Traceback (most recent call last) File , line 10 3 llm = LLM("Huggi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: from version 0.2.1 bug I've only tested this using Zephyr (mistral-type model), but when calling LLM.generate in version 0.2.1, I receive an AssertionError in the worker runs. Code to reproduce: ```py from vllm import L...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: m) 155 token_ids = prompt_token_ids[i] 156 self._add_request(prompt, sampling_params, token_ids) --> 157 return self._run_engine(use_tqdm) File /local_disk0/.ephemeral_nfs/envs/pythonEnv-f955471c-8346-4f89-b3b6-d25bfb1d...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: version 0.2.1, I receive an AssertionError in the worker runs. Code to reproduce: ```py from vllm import LLM, SamplingParams llm = LLM("HuggingFaceH4/zephyr-7b-alpha", tensor_parallel_size=4) sampling_params = SamplingP...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
