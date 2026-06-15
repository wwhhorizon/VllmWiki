# vllm-project/vllm#6638: [Bug]: Qwen1.5( vllm>=0.4.2)  streaming generate token is abnormal.Using  engine.generate()

| 字段 | 值 |
| --- | --- |
| Issue | [#6638](https://github.com/vllm-project/vllm/issues/6638) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen1.5( vllm>=0.4.2)  streaming generate token is abnormal.Using  engine.generate()

### Issue 正文摘录

### Your current environment ```text A800*8 ，vllm==0.4.3 ``` ### 🐛 Describe the bug ``` results_generator = engine.generate(prompt_format, sampling_params, request_id) pre_index=0 async for request_output in results_generator: text_outputs = [output.text for output in request_output.outputs][0][pre_index:] pre_index+=len(text_outputs) res+=text_outputs ret = {'code': 1, 'answer':text_outputs,"request_id":request_id} yield (json.dumps(ret)).encode("utf-8") ``` The `text ` field is error in the streaming result, but `token_ids ` field is normal. ![1721636495461](https://github.com/user-attachments/assets/4b683555-a778-44ac-8c8b-e3f4d30848ba)

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen1.5( vllm>=0.4.2) streaming generate token is abnormal.Using engine.generate() bug;stale ### Your current environment ```text A800*8 ，vllm==0.4.3 ``` ### 🐛 Describe the bug ``` results_generator = engine.gene...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: .4.2) streaming generate token is abnormal.Using engine.generate() bug;stale ### Your current environment ```text A800*8 ，vllm==0.4.3 ``` ### 🐛 Describe the bug ``` results_generator = engine.generate(prompt_format, sam...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
