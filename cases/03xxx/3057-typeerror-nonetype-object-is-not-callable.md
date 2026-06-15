# vllm-project/vllm#3057: TypeError: 'NoneType' object is not callable

| 字段 | 值 |
| --- | --- |
| Issue | [#3057](https://github.com/vllm-project/vllm/issues/3057) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> TypeError: 'NoneType' object is not callable

### Issue 正文摘录

when I test for mutil-gpu with llama2-70b, run `vllm/examples/offline_inference.py` , use params `enforce_eager=False`, the result can output, but it occur some error ``` Prompt: 'Hello, my name is', Generated text: ' Dustin Nelson and I’m going to be posting articles and my thoughts' Prompt: 'The president of the United States is', Generated text: ' one of the most powerful people in the world, as the leader of the only' Prompt: 'The capital of France is', Generated text: ' one of the world’s leading cities in terms of art, fashion, food' Prompt: 'The future of AI is', Generated text: ' neither utopian nor apocalyptic—it’s both.\n' Exception ignored in: Traceback (most recent call last): File "/usr/local/lib/python3.10/dist-packages/cupyx/distributed/_store.py", line 59, in __del__ File "/usr/local/lib/python3.10/dist-packages/cupyx/distributed/_store.py", line 109, in stop File "/usr/local/lib/python3.10/dist-packages/cupyx/distributed/_store.py", line 39, in join File "/usr/lib/python3.10/multiprocessing/connection.py", line 257, in poll File "/usr/lib/python3.10/multiprocessing/connection.py", line 424, in _poll TypeError: 'NoneType' object is not callable ``` the error in the...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: : 'NoneType' object is not callable stale when I test for mutil-gpu with llama2-70b, run `vllm/examples/offline_inference.py` , use params `enforce_eager=False`, the result can output, but it occur some error ``` Prompt...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 'The capital of France is', Generated text: ' one of the world’s leading cities in terms of art, fashion, food' Prompt: 'The future of AI is', Generated text: ' neither utopian nor apocalyptic—it’s both.\n' Exception ig...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: , run `vllm/examples/offline_inference.py` , use params `enforce_eager=False`, the result can output, but it occur some error ``` Prompt: 'Hello, my name is', Generated text: ' Dustin Nelson and I’m going to be posting...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: TypeError: 'NoneType' object is not callable stale when I test for mutil-gpu with llama2-70b, run `vllm/examples/offline_inference.py` , use params `enforce_eager=False`, the result can output, but it occur some error `...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: TypeError: 'NoneType' object is not callable stale when I test for mutil-gpu with llama2-70b, run `vllm/examples/offline_inference.py` , use params `enforce_eager=False`, the result can output, but it occur some error `...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
