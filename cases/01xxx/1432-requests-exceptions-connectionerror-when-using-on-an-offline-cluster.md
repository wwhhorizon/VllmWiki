# vllm-project/vllm#1432: requests.exceptions.ConnectionError when using on an offline cluster 

| 字段 | 值 |
| --- | --- |
| Issue | [#1432](https://github.com/vllm-project/vllm/issues/1432) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> requests.exceptions.ConnectionError when using on an offline cluster 

### Issue 正文摘录

I try to use vllm to run llama-7b on my offline cluster. And I have set the environment variable `TRANSFORMERS_OFFLINE=1`. But I still got error as follows. `requests.exceptions.ConnectionError: (MaxRetryError("HTTPSConnectionPool(host='huggingface.co', port=443): Max retries exceeded with url: /api/models/huggyllama/llama-7b/revision/main (Caused by NewConnectionError(' : Failed to establish a new connection: [Errno -3] Temporary failure in name resolution'))"), '(Request ID: 3b8686a3-75ca-4258-bebc-83ef391708a8)')` ### Environment info ``` python==3.8.18 vllm ==0.1.7 transformers==4.33.0 ``` Is it possible for me to use Vllm on an offline cluster? And how to do so?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: nnectionError when using on an offline cluster I try to use vllm to run llama-7b on my offline cluster. And I have set the environment variable `TRANSFORMERS_OFFLINE=1`. But I still got error as follows. `requests.excep...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: requests.exceptions.ConnectionError when using on an offline cluster I try to use vllm to run llama-7b on my offline cluster. And I have set the environment variable `TRANSFORMERS_OFFLINE=1`. But I still got error as fo

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
