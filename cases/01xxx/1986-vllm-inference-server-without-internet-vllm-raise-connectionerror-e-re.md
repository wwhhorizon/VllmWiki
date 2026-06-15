# vllm-project/vllm#1986: vllm inference server without internet: vLLM: raise ConnectionError(e, request=request)

| 字段 | 值 |
| --- | --- |
| Issue | [#1986](https://github.com/vllm-project/vllm/issues/1986) |
| 状态 | closed |
| 标签 |  |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> vllm inference server without internet: vLLM: raise ConnectionError(e, request=request)

### Issue 正文摘录

When I ran vllm inference server without internet connection then it throws the following error `File "/home/miniconda3/envs/vllm/lib/python3.10/site-packages/requests/adapters.py", line 519, in send raise ConnectionError(e, request=request) requests.exceptions.ConnectionError: (MaxRetryError('HTTPSConnectionPool(host=\'huggingface.co\', port=443): Max retries exceeded with url: /api/models/meta-llama/Llama-2-13b-chat-hf/revision/main (Caused by NameResolutionError(" : Failed to resolve \'huggingface.co\' ([Errno -3] Temporary failure in name resolution)"))'), '(Request ID: 180aa8f1-bd8d-4f1e-bc19-2ba285227928)')` When i power on the server, it ask for internet connection to run vllm. However, I want to use h2ogpt with vllm inferencing on my private server without internet connection. Please help me regarding this! ****Command I hit: `python -m vllm.entrypoints.openai.api_server --port=5000 --host=0.0.0.0 --model meta-llam a/Llama-2-13b-chat-hf --tokenizer=hf-internal-testing/llama-tokenizer --tensor-parallel-size=1 --seed 1234 --max-num-batched-tokens=4096` `

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: s.exceptions.ConnectionError: (MaxRetryError('HTTPSConnectionPool(host=\'huggingface.co\', port=443): Max retries exceeded with url: /api/models/meta-llama/Llama-2-13b-chat-hf/revision/main (Caused by NameResolutionErro...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: t connection to run vllm. However, I want to use h2ogpt with vllm inferencing on my private server without internet connection. Please help me regarding this! ****Command I hit: `python -m vllm.entrypoints.openai.api_se...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: vllm inference server without internet: vLLM: raise ConnectionError(e, request=request) When I ran vllm inference server without internet connection then it throws the following error `File "/home/miniconda3/envs/vllm/l...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: =0.0.0.0 --model meta-llam a/Llama-2-13b-chat-hf --tokenizer=hf-internal-testing/llama-tokenizer --tensor-parallel-size=1 --seed 1234 --max-num-batched-tokens=4096` `

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
