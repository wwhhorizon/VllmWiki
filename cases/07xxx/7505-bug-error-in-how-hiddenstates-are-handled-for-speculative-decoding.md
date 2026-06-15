# vllm-project/vllm#7505: [Bug]: Error in how HiddenStates are handled for speculative decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#7505](https://github.com/vllm-project/vllm/issues/7505) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Error in how HiddenStates are handled for speculative decoding

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug In draft models like Medusa, MLPSpeculator etc., when spec. decode is disabled (e.g. when the num_tokens + spec_tokens > max_len of the model) HiddenStates are not handled properly which causes an invalid shape error. How to reproduce? Code: ```python from vllm import LLM, SamplingParams llm = LLM( model="JackFram/llama-160m", speculative_model="ibm-fms/llama-160m-accelerator", num_speculative_tokens=3, use_v2_block_manager=True, enforce_eager=True, ) prompt = "The president of the United States is" output = llm.generate(prompt, SamplingParams(max_tokens=2048, ignore_eos=True)) ``` Output: ``` --------------------------------------------------------------------------- RuntimeError Traceback (most recent call last) [ ](https://localhost:8080/#) in () 10 prompt = "The president of the United States is" 11 ---> 12 output = llm.generate(prompt, SamplingParams(max_tokens=2048, ignore_eos=True)) 10 frames [/usr/local/lib/python3.10/dist-packages/vllm/spec_decode/spec_decode_worker.py](https://localhost:8080/#) in _verify_tokens(self, seq_group_metadata_list, proposal_scores, proposals, max_proposal_len) 645 # Contract hidden states bas...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Error in how HiddenStates are handled for speculative decoding bug ### Your current environment ### 🐛 Describe the bug In draft models like Medusa, MLPSpeculator etc., when spec. decode is disabled (e.g. when the...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: bm-fms/llama-160m-accelerator", num_speculative_tokens=3, use_v2_block_manager=True, enforce_eager=True, ) prompt = "The president of the United States is" output = llm.generate(prompt, SamplingParams(max_tokens=2048, i...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ng bug ### Your current environment ### 🐛 Describe the bug In draft models like Medusa, MLPSpeculator etc., when spec. decode is disabled (e.g. when the num_tokens + spec_tokens > max_len of the model) HiddenStates are...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: es are not handled properly which causes an invalid shape error. How to reproduce? Code: ```python from vllm import LLM, SamplingParams llm = LLM( model="JackFram/llama-160m", speculative_model="ibm-fms/llama-160m-accel...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: es an invalid shape error. How to reproduce? Code: ```python from vllm import LLM, SamplingParams llm = LLM( model="JackFram/llama-160m", speculative_model="ibm-fms/llama-160m-accelerator", num_speculative_tokens=3, use...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
