# vllm-project/vllm#4103: [Bug]: AttributeError: 'NoneType' object has no attribute 'nvmlInit'

| 字段 | 值 |
| --- | --- |
| Issue | [#4103](https://github.com/vllm-project/vllm/issues/4103) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: AttributeError: 'NoneType' object has no attribute 'nvmlInit'

### Issue 正文摘录

### Your current environment ``` torch 2.1.2 torchaudio 2.1.2 torchvision 0.16.2 四卡4090 ### 🐛 Describe the bug 启动服务的时候：python -m vllm.entrypoints.openai.api_server --model /root/autodl-tmp/huggingface_model/Yi-34B --chat-template ./examples/template_chatml.jinja --tensor-parallel-size 2 --trust-remote-code 报错：AttributeError: 'NoneType' object has no attribute 'nvmlInit' AttributeError: 'NoneType' object has no attribute 'nvmlShutdown'

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: escribe the bug 启动服务的时候：python -m vllm.entrypoints.openai.api_server --model /root/autodl-tmp/huggingface_model/Yi-34B --chat-template ./examples/template_chatml.jinja --tensor-parallel-size 2 --trust-remote-code 报错：Att...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: AttributeError: 'NoneType' object has no attribute 'nvmlInit' bug;stale ### Your current environment ``` torch 2.1.2 torchaudio 2.1.2 torchvision 0.16.2 四卡4090 ### 🐛 Describe the bug 启动服务的时候：python -m vllm.entryp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
