# vllm-project/vllm#2538: outputs includes eos token

| 字段 | 值 |
| --- | --- |
| Issue | [#2538](https://github.com/vllm-project/vllm/issues/2538) |
| 状态 | closed |
| 标签 | good first issue |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> outputs includes eos token

### Issue 正文摘录

### code ``` gen_kwargs = {"top_p": top_p, "temperature": temperature, "max_tokens": max_length, "include_stop_str_in_output": False} eos_token_id = [tokenizer.eos_token_id, tokenizer.get_command(" "), tokenizer.get_command(" ")] sampling_params = SamplingParams(stop_token_ids=eos_token_id, **gen_kwargs) outputs = self.model.generate(sampling_params=sampling_params, prompt_token_ids=inputs["input_ids"].tolist()) ``` ### outputs string ``` I need to use the insauto_quote_tool tool to get the user's car insurance quote. insauto_quote_tool ```python tool_call(type='object', properties={'quote_biz_id': '20220906000831000002005700226000'}) ``` ``` ### question lwhy is ' ' still at the end? ### environment Model：ChatGLM3-6b

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: : temperature, "max_tokens": max_length, "include_stop_str_in_output": False} eos_token_id = [tokenizer.eos_token_id, tokenizer.get_command(" "), tokenizer.get_command(" ")] sampling_params = SamplingParams(stop_token_i...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: SamplingParams(stop_token_ids=eos_token_id, **gen_kwargs) outputs = self.model.generate(sampling_params=sampling_params, prompt_token_ids=inputs["input_ids"].tolist()) ``` ### outputs string ``` I need to use the insaut...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
