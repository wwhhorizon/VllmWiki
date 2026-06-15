# vllm-project/vllm#3041: Issue Serving mistralai/Mixtral-8x7B-v0.1

| 字段 | 值 |
| --- | --- |
| Issue | [#3041](https://github.com/vllm-project/vllm/issues/3041) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Issue Serving mistralai/Mixtral-8x7B-v0.1

### Issue 正文摘录

I've been successfully serving mistralai/Mixtral-8x7B-Instruct-v0.1 on 2xA100 80GBs with the following command just fine: `python3 -m vllm.entrypoints.openai.api_server --model mistralai/Mixtral-8x7B-Instruct-v0.1 --tensor-parallel-size 2` However, i just tried switching to mistralai/Mixtral-8x7B-v0.1 and have been running into errors. I did the following: - i just replaced the model name and was giving the following warning: `WARNING 02-26 18:34:06 api_server.py:115] No chat template provided. Chat API will not work.` - So i pulled this chat_template down (https://github.com/vllm-project/vllm/blob/main/examples/template_chatml.jinja) and added it to my command: `python3 -m vllm.entrypoints.openai.api_server --model mistralai/Mixtral-8x7B-v0.1 --tensor-parallel-size 2 --chat-template ./template_chatml.jinja` After doing this, I'm now getting 404 errors from programs i was using to interface with Mixtral-Instruct. I successfully issued a curl request but it seemed to run indefinitely... I got one completion but it was a nonsense response... Am i using a bad chat_template for Mixtral or is there something else I'm doing wrong? Thank you!

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: I've been successfully serving mistralai/Mixtral-8x7B-Instruct-v0.1 on 2xA100 80GBs with the following command just fine: `python3 -m vllm.entrypoints.openai.api_server --model mistralai/Mixtral-8x7B-Instruct-v0.1 --ten...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: se... Am i using a bad chat_template for Mixtral or is there something else I'm doing wrong? Thank you!
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: wing command just fine: `python3 -m vllm.entrypoints.openai.api_server --model mistralai/Mixtral-8x7B-Instruct-v0.1 --tensor-parallel-size 2` However, i just tried switching to mistralai/Mixtral-8x7B-v0.1 and have been...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: s using to interface with Mixtral-Instruct. I successfully issued a curl request but it seemed to run indefinitely... I got one completion but it was a nonsense response... Am i using a bad chat_template for Mixtral or...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
