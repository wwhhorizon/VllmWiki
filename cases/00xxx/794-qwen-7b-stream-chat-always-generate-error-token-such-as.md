# vllm-project/vllm#794: Qwen-7B, stream chat always generate error token, such as '�'

| 字段 | 值 |
| --- | --- |
| Issue | [#794](https://github.com/vllm-project/vllm/issues/794) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Qwen-7B, stream chat always generate error token, such as '�'

### Issue 正文摘录

when I use vllm.entrypoints.openai.api_server with model named Qwen-7B, and I send a ChatCompletion request with stream=True, ```response = openai.ChatCompletion.create( model=model, messages=[{"role": "user", "content": prompt}], temperature=0, max_tokens=1024, stop=[" ", " ", " "], stream=True # again, we set stream=True )``` I got error token with this '�', how I can avoid this? Which line code I can modify to fix this problem? Thanks in advance!!!

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Qwen-7B, stream chat always generate error token, such as '�' when I use vllm.entrypoints.openai.api_server with model named Qwen-7B, and I send a ChatCompletion request with stream=True, ```response = openai.ChatCo
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: enai.api_server with model named Qwen-7B, and I send a ChatCompletion request with stream=True, ```response = openai.ChatCompletion.create( model=model, messages=[{"role": "user", "content": prompt}], temperature=0, max...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
