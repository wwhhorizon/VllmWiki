# vllm-project/vllm#2629: 404 Client Error

| 字段 | 值 |
| --- | --- |
| Issue | [#2629](https://github.com/vllm-project/vllm/issues/2629) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> 404 Client Error

### Issue 正文摘录

I am trying to execute the Offline Batched Inference example shown in Quickstart. https://docs.vllm.ai/en/latest/getting_started/quickstart.html However, there is a 404 Client Error, which confused me. Do you have any suggestions to fix that and execute the example? ``` 2024-01-27 21:31:02,440 - modelscope - INFO - PyTorch version 2.1.2 Found. 2024-01-27 21:31:02,440 - modelscope - INFO - Loading ast index from /home/cc/.cache/modelscope/ast_indexer 2024-01-27 21:31:02,559 - modelscope - INFO - Loading done! Current index file version is 1.11.1, with md5 c9b988ee25325c806355d2d6d2c50417 and a total number of 956 components indexed Traceback (most recent call last): File "/home/cc/.local/lib/python3.9/site-packages/modelscope/hub/errors.py", line 91, in handle_http_response response.raise_for_status() File "/home/cc/.local/lib/python3.9/site-packages/requests/models.py", line 1021, in raise_for_status raise HTTPError(http_error_msg, response=self) requests.exceptions.HTTPError: 404 Client Error: Not Found for url: https://www.modelscope.cn/api/v1/models/gpt2/revisions?EndTime=1706391065 The above exception was the direct cause of the following exception: Traceback (most recent call...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ions to fix that and execute the example? ``` 2024-01-27 21:31:02,440 - modelscope - INFO - PyTorch version 2.1.2 Found. 2024-01-27 21:31:02,440 - modelscope - INFO - Loading ast index from /home/cc/.cache/modelscope/as...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: the example? ``` 2024-01-27 21:31:02,440 - modelscope - INFO - PyTorch version 2.1.2 Found. 2024-01-27 21:31:02,440 - modelscope - INFO - Loading ast index from /home/cc/.cache/modelscope/ast_indexer 2024-01-27 21:31:02...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ound', 'RequestId': 'b2f64e12-36da-46a8-af65-788cdab51810', 'Success': False}, Request id: 5a94bf1037c44b58b2b1ce1a76e791f9 ```
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: e.raise_for_status() File "/home/cc/.local/lib/python3.9/site-packages/requests/models.py", line 1021, in raise_for_status raise HTTPError(http_error_msg, response=self) requests.exceptions.HTTPError: 404 Client Error:...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: Batched Inference example shown in Quickstart. https://docs.vllm.ai/en/latest/getting_started/quickstart.html However, there is a 404 Client Error, which confused me. Do you have any suggestions to fix that and execute...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
