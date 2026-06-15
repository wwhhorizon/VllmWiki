# vllm-project/vllm#3034: 部署qwen1.5-7B-Chat的时候遇到API接口返回缺10个字符的问题

| 字段 | 值 |
| --- | --- |
| Issue | [#3034](https://github.com/vllm-project/vllm/issues/3034) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> 部署qwen1.5-7B-Chat的时候遇到API接口返回缺10个字符的问题

### Issue 正文摘录

我在部署qwen1.5-7B-Chat的时候遇到调用API时最后有10个字符缺失的问题，长度正好是结束token 。 ``` nohup python -m vllm.entrypoints.openai.api_server \ --model /Qwen/Qwen1.5-7B-Chat --host 0.0.0.0 \ --port 80 \ --trust-remote-code \ ``` 临时的解决方案：_调用接口的时候传入：include_stop_str_in_output=True_ 可能是因为在调用api的时候include_stop_str_in_output默认是False，而在 [https://github.com/vllm-project/vllm/blob/main/vllm/engine/llm_engine.py#L966](https://github.com/vllm-project/vllm/blob/70f3e8e3a1ed081003c0a2b70de151bb144f98e0/vllm/engine/llm_engine.py#L966)中，最后的stop token会被截断掉，但是seq.output_text中并不包含 ，所以就截断错了。 ```python def _finalize_sequence(self, seq: Sequence, sampling_params: SamplingParams, stop_string: str) -> None: if not sampling_params.include_stop_str_in_output and stop_string: # Truncate the output text so that the stop string is # not included in the output. seq.output_text = seq.output_text[:-len(stop_string)] ``` 感觉是不是改成如下就OK了 ```python def _finalize_sequence(self, seq: Sequence, sampling_params: SamplingParams, stop_string: str) -> None: if not sampling_params.include_stop_str_in_output and stop_string: # Truncate the output text so that the stop string is # not included in the output. seq.output_text = seq.output_text.rstrip(sto...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 部署qwen1.5-7B-Chat的时候遇到API接口返回缺10个字符的问题 stale 我在部署qwen1.5-7B-Chat的时候遇到调用API时最后有10个字符缺失的问题，长度正好是结束token 。 ``` nohup python -m vllm.entrypoints.openai.api_server \ --model /Qwen/Qwen1.5-7B-Chat --host 0.0.0.0 \ --port 80 \
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: de_stop_str_in_output=True_ 可能是因为在调用api的时候include_stop_str_in_output默认是False，而在 [https://github.com/vllm-project/vllm/blob/main/vllm/engine/llm_engine.py#L966](https://github.com/vllm-project/vllm/blob/70f3e8e3a1ed08100...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: 部署qwen1.5-7B-Chat的时候遇到API接口返回缺10个字符的问题 stale 我在部署qwen1.5-7B-Chat的时候遇到调用API时最后有10个字符缺失的问题，长度正好是结束token 。 ``` nohup python -m vllm.entrypoints.openai.api_server \ --model /Qwen/Qwen1.5-7B-Chat --host 0.0.0.0 \ --port 80 \...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
