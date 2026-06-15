# vllm-project/vllm#3032: [BUG] Prompt logprobs causing tensor broadcast issue in `sampler.py`

| 字段 | 值 |
| --- | --- |
| Issue | [#3032](https://github.com/vllm-project/vllm/issues/3032) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [BUG] Prompt logprobs causing tensor broadcast issue in `sampler.py`

### Issue 正文摘录

Hi, I am trying to obtain the prompt logprobs of 'meta-llama/llama-2-13b-chat-hf' but run into a size mismatch error. Here are the sampling params: ``` SamplingParams(temperature=0, max_tokens=512, prompt_logprobs=1) ``` And here's the model: ``` self.llm = LLM('meta-llama/llama-2-13b-chat-hf', tensor_parallel_size=2) ``` I run into this issue if I pass in a large number or prompts (say 1k prompts) to the LLM. (For smaller sizes it appears to do fine): ``` File "/home/abhinavr/git_clones/rlkf/src/model/llama_model.py", line 90, in forward responses = self.llm.generate(prompts, sampling_params=sampling_params) File "/home/abhinavr/miniconda3/envs/culeval/lib/python3.9/site-packages/vllm/entrypoints/llm.py", line 182, in generate return self._run_engine(use_tqdm) File "/home/abhinavr/miniconda3/envs/culeval/lib/python3.9/site-packages/vllm/entrypoints/llm.py", line 208, in _run_engine step_outputs = self.llm_engine.step() File "/home/abhinavr/miniconda3/envs/culeval/lib/python3.9/site-packages/vllm/engine/llm_engine.py", line 817, in step all_outputs = self._run_workers( File "/home/abhinavr/miniconda3/envs/culeval/lib/python3.9/site-packages/vllm/engine/llm_engine.py", line 1014, i...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ler.py` bug;stale Hi, I am trying to obtain the prompt logprobs of 'meta-llama/llama-2-13b-chat-hf' but run into a size mismatch error. Here are the sampling params: ``` SamplingParams(temperature=0, max_tokens=512, pro...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: rompt logprobs of 'meta-llama/llama-2-13b-chat-hf' but run into a size mismatch error. Here are the sampling params: ``` SamplingParams(temperature=0, max_tokens=512, prompt_logprobs=1) ``` And here's the model: ``` sel...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: prompt logprobs of 'meta-llama/llama-2-13b-chat-hf' but run into a size mismatch error. Here are the sampling params: ``` SamplingParams(temperature=0, max_tokens=512, prompt_logprobs=1) ``` And here's the model: ``` se...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: in execute_model output = self.model_runner.execute_model(seq_group_metadata_list, File "/home/abhinavr/miniconda3/envs/culeval/lib/python3.9/site-packages/torch/utils/_contextlib.py", line 115, in decorate_context retu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [BUG] Prompt logprobs causing tensor broadcast issue in `sampler.py` bug;stale Hi, I am trying to obtain the prompt logprobs of 'meta-llama/llama-2-13b-chat-hf' but run into a size mismatch error. Here are the sampling...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
