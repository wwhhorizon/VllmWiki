# vllm-project/vllm#12234: [Usage]: how to input messages as multi-message (a batch) instead of just one

| 字段 | 值 |
| --- | --- |
| Issue | [#12234](https://github.com/vllm-project/vllm/issues/12234) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: how to input messages as multi-message (a batch) instead of just one

### Issue 正文摘录

### Your current environment currently i could input a message and call vllm api. the message could be like: messages = [ {"role": "system", "content": "In the following sentence, please give some suggestions to improve word usage. Please give the results with the JSON format of {“original word”: [“suggestion 1”, “suggestion 2”]}. The 'original word' should include all words that can be improved in the sentence, directly extracted from the sentence itself, and the suggestions should be ranked in order of the degree of improvement, from the most effective to the least."}, {"role": "user", "content": "In conclusion, the professor pointed out the inconsistencies between the reading and the listening passages and explained why the arguments in the speech are more reliable."}, ] but if i want to input a batch size > 1 messages, like: messages = [[ {"role": "system", "content": "In the following sentence, please give some suggestions to improve word usage. Please give the results with the JSON format of {“original word”: [“suggestion 1”, “suggestion 2”]}. The 'original word' should include all words that can be improved in the sentence, directly extracted from the sentence itself, and t...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: suggestions to improve word usage. Please give the results with the JSON format of {“original word”: [“suggestion 1”, “suggestion 2”]}. The 'original word' should include all words that can be improved in the sentence,...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: er", "content": "In conclusion, the professor pointed out the inconsistencies between the reading and the listening passages and explained why the arguments in the speech are more reliable."}, ] but if i want to input a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ]. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ou. ### How would you like to use vllm I want to run inference of a [unsloth/Llama-3.3-70B-Instruct-bnb-4bit]. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: self._make_status_error_from_response(err.response) from None openai.BadRequestError: Error code: 400 - {'object': 'error', 'message': '[{\'type\': \'dict_type\', \'loc\': (\'body\', \'messages\', 0, \'typed-dict\'), \'...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
