# vllm-project/vllm#7738: [Usage]: About bitsandbytes

| 字段 | 值 |
| --- | --- |
| Issue | [#7738](https://github.com/vllm-project/vllm/issues/7738) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: About bitsandbytes

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I just wanted to ask about which quantization am I using when I run the following command. It worked fine I didnt have trouble but I was unable to identify which quantization is it. python3 -m vllm.entrypoints.openai.api_server --host x.x.x.x --port xxxx --model xxxx/Llama3-8b --quatization bitsandbytes --enforce_eager --dtype half Are there any support for bnb 8bit quantization? Thnx lot.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: `` ### How would you like to use vllm I just wanted to ask about which quantization am I using when I run the following command. It worked fine I didnt have trouble but I was unable to identify which quantization is it....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: thon3 -m vllm.entrypoints.openai.api_server --host x.x.x.x --port xxxx --model xxxx/Llama3-8b --quatization bitsandbytes --enforce_eager --dtype half Are there any support for bnb 8bit quantization? Thnx lot.
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: About bitsandbytes usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I just wanted to ask about which quantization am I using when I r...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
