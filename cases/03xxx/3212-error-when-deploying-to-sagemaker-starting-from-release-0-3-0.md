# vllm-project/vllm#3212: Error when deploying to Sagemaker starting from release 0.3.0

| 字段 | 值 |
| --- | --- |
| Issue | [#3212](https://github.com/vllm-project/vllm/issues/3212) |
| 状态 | closed |
| 标签 |  |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Error when deploying to Sagemaker starting from release 0.3.0

### Issue 正文摘录

Since release 0.3.0 we have been unable to deploy vLLM containers to Sagemaker. It has to do with the `get_ip()` function call in `utils.py`. In release 0.3.0 we got an OS error, and with 0.3.3 we are getting the following: `socket.gaierror: [Errno -2] Name or service not known`, when making the following call: `s.connect(("dns.google", 80))`. Could you please add something to make the `get_ip()` function fall back to what was there in release `0.2.7` if all else fails? For reference, here is the function call in `0.2.7`: https://github.com/vllm-project/vllm/blob/v0.2.7/vllm/utils.py#L60 In `0.3.0` it was changed to the following, and stopped working on Sagemaker: https://github.com/vllm-project/vllm/blob/v0.3.0/vllm/utils.py#L164 It is now as follows: https://github.com/vllm-project/vllm/blob/v0.3.3/vllm/utils.py#L172

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: et_ip()` function fall back to what was there in release `0.2.7` if all else fails? For reference, here is the function call in `0.2.7`: https://github.com/vllm-project/vllm/blob/v0.2.7/vllm/utils.py#L60 In `0.3.0` it w...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
