# vllm-project/vllm#2628: HTTPError: 400 Client Error: Bad Request

| 字段 | 值 |
| --- | --- |
| Issue | [#2628](https://github.com/vllm-project/vllm/issues/2628) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> HTTPError: 400 Client Error: Bad Request

### Issue 正文摘录

I am trying to execute the Offline Batched Inference example shown in [Quickstart]. (https://docs.vllm.ai/en/latest/getting_started/quickstart.html) However, there is a 400 Client Error, which confused me. Do you have any suggestions to fix that and execute the example? ``` 2024-01-27 17:54:55,878 - modelscope - INFO - PyTorch version 2.1.2 Found. 2024-01-27 17:54:55,878 - modelscope - INFO - Loading ast index from /home/cc/.cache/modelscope/ast_indexer 2024-01-27 17:54:55,997 - modelscope - INFO - Loading done! Current index file version is 1.11.1, with md5 c9b988ee25325c806355d2d6d2c50417 and a total number of 956 components indexed Traceback (most recent call last): File "/home/cc/vllm/examples/./offline_inference.py", line 6, in api.login(YOUR_ACCESS_TOKEN) File "/home/cc/.local/lib/python3.9/site-packages/modelscope/hub/api.py", line 111, in login raise_for_http_status(r) File "/home/cc/.local/lib/python3.9/site-packages/modelscope/hub/errors.py", line 175, in raise_for_http_status raise HTTPError(http_error_msg, response=rsp) requests.exceptions.HTTPError: 400 Client Error: Bad Request, Request id: 138622c79212439ebdc255de54693400 for url: https://www.modelscope.cn/api/v1/lo...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: the example? ``` 2024-01-27 17:54:55,878 - modelscope - INFO - PyTorch version 2.1.2 Found. 2024-01-27 17:54:55,878 - modelscope - INFO - Loading ast index from /home/cc/.cache/modelscope/ast_indexer 2024-01-27 17:54:55...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ions to fix that and execute the example? ``` 2024-01-27 17:54:55,878 - modelscope - INFO - PyTorch version 2.1.2 Found. 2024-01-27 17:54:55,878 - modelscope - INFO - Loading ast index from /home/cc/.cache/modelscope/as...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: HTTPError: 400 Client Error: Bad Request I am trying to execute the Offline Batched Inference example shown in [Quickstart]. (https://docs.vllm.ai/en/latest/getting_started/quickstart.html) However, there is a 400 Clien...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ched Inference example shown in [Quickstart]. (https://docs.vllm.ai/en/latest/getting_started/quickstart.html) However, there is a 400 Client Error, which confused me. Do you have any suggestions to fix that and execute...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
