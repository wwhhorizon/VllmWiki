# vllm-project/vllm#2104: argument 'tokens': 'NoneType' object cannot be converted to 'PyString'

| 字段 | 值 |
| --- | --- |
| Issue | [#2104](https://github.com/vllm-project/vllm/issues/2104) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> argument 'tokens': 'NoneType' object cannot be converted to 'PyString'

### Issue 正文摘录

sampling_params = SamplingParams(temperature=0.2) 正常运行 sampling_params = SamplingParams(temperature=0.2, frequency_penalty=1.2, presence_penalty=1.2, top_p=0.95, top_k=1, stop=[" ", ' ', ' '], max_tokens=4096) 报错信息： Traceback (most recent call last): File "/home/house365ai/xxm/new/vllm4/demo.py", line 33, in outputs = llm.generate(prompts, sampling_params) File "/home/house365ai/xxm/new/vllm4/vllm/entrypoints/llm.py", line 153, in generate return self._run_engine(use_tqdm) File "/home/house365ai/xxm/new/vllm4/vllm/entrypoints/llm.py", line 173, in _run_engine step_outputs = self.llm_engine.step() File "/home/house365ai/xxm/new/vllm4/vllm/engine/llm_engine.py", line 585, in step return self._process_model_outputs(output, scheduler_outputs) File "/home/house365ai/xxm/new/vllm4/vllm/engine/llm_engine.py", line 545, in _process_model_outputs self._process_sequence_group_outputs(seq_group, outputs) File "/home/house365ai/xxm/new/vllm4/vllm/engine/llm_engine.py", line 416, in _process_sequence_group_outputs self._decode_sequence(seq, seq_group.sampling_params) File "/home/house365ai/xxm/new/vllm4/vllm/engine/llm_engine.py", line 663, in _decode_sequence read_offset) = detokenize_increme...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: engine.py", line 585, in step return self._process_model_outputs(output, scheduler_outputs) File "/home/house365ai/xxm/new/vllm4/vllm/engine/llm_engine.py", line 545, in _process_model_outputs self._process_sequence_gro...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: zation_utils_fast.py", line 612, in convert_tokens_to_string return self.backend_tokenizer.decoder.decode(tokens) TypeError: argument 'tokens': 'NoneType' object cannot be converted to 'PyString'
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: vllm4/vllm/engine/llm_engine.py", line 585, in step return self._process_model_outputs(output, scheduler_outputs) File "/home/house365ai/xxm/new/vllm4/vllm/engine/llm_engine.py", line 545, in _process_model_outputs self...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
