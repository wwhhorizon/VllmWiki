# vllm-project/vllm#7169: [Bug]:  Multi Lora Bug with different LORAS

| 字段 | 值 |
| --- | --- |
| Issue | [#7169](https://github.com/vllm-project/vllm/issues/7169) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:  Multi Lora Bug with different LORAS

### Issue 正文摘录

### Your current environment ```text In this example https://github.com/vllm-project/vllm/blob/main/examples/multilora_inference.py if you gave two different loras instead of same loras with different name, the output is coming from the first lora initialized ``` ### 🐛 Describe the bug give two any two different loras and do inference, the model is pocking only the first lora in order , the second one inference also coming from the first lora( "[user] Write a SQL query to answer the question based on the table schema.\n\n context: CREATE TABLE table_name_74 (icao VARCHAR, airport VARCHAR)\n\n question: Name the ICAO for lilongwe international airport [/user] [assistant]", SamplingParams(temperature=0.0, logprobs=1, prompt_logprobs=1, max_tokens=128, stop_token_ids=[32003]), LoRARequest("sql-lora2", 2, lora_path)), ( "my nam is", SamplingParams(n=3, best_of=3, use_beam_search=True, temperature=0, max_tokens=128, stop_token_ids=[32003]), LoRARequest("sql-lora", 1, 'timdettmers/qlora-flan-7b')),

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Multi Lora Bug with different LORAS bug;stale ### Your current environment ```text In this example https://github.com/vllm-project/vllm/blob/main/examples/multilora_inference.py if you gave two different loras in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ased on the table schema.\n\n context: CREATE TABLE table_name_74 (icao VARCHAR, airport VARCHAR)\n\n question: Name the ICAO for lilongwe international airport [/user] [assistant]", SamplingParams(temperature=0.0, logp...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: escribe the bug give two any two different loras and do inference, the model is pocking only the first lora in order , the second one inference also coming from the first lora( "[user] Write a SQL query to answer the qu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
