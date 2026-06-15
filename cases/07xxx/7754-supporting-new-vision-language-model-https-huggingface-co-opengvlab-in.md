# vllm-project/vllm#7754: Supporting new vision language model - https://huggingface.co/OpenGVLab/InternVL2-26B

| 字段 | 值 |
| --- | --- |
| Issue | [#7754](https://github.com/vllm-project/vllm/issues/7754) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Supporting new vision language model - https://huggingface.co/OpenGVLab/InternVL2-26B

### Issue 正文摘录

### The model to consider. Currently vLLM supports [OpenGVLab/InternVL2-4B, OpenGVLab/InternVL2-8B] models, so it would be really helpful to get support for 26B model Exceptions for 26B, File "/usr/local/lib/python3.10/dist-packages/transformers/models/auto/auto_factory.py", line 732, in __getitem__ model_type = self._reverse_config_mapping[key.__name__] KeyError: 'InternVLChatConfig' Traceback (most recent call last): File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/openai/api_server.py", line 150, in build_async_engine_client await async_engine_client.setup() File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/openai/rpc/client.py", line 35, in setup await self.wait_for_server() File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/openai/rpc/client.py", line 136, in wait_for_server await self._send_one_way_rpc_request( File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/openai/rpc/client.py", line 112, in _send_one_way_rpc_request raise TimeoutError(f"server didn't reply within {timeout} ms") TimeoutError: server didn't reply within 1000 ms ### The closest model vllm already supports. _No response_ ### What's your difficulty of suppo...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Supporting new vision language model - https://huggingface.co/OpenGVLab/InternVL2-26B new-model ### The model to consider. Currently vLLM supports [OpenGVLab/InternVL2-4B, OpenGVLab/InternVL2-8B] models, so it would be...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: n3.10/dist-packages/vllm/entrypoints/openai/api_server.py", line 150, in build_async_engine_client await async_engine_client.setup() File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/openai/rpc/client.py",...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: tory.py", line 732, in __getitem__ model_type = self._reverse_config_mapping[key.__name__] KeyError: 'InternVLChatConfig' Traceback (most recent call last): File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: lient.py", line 136, in wait_for_server await self._send_one_way_rpc_request( File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/openai/rpc/client.py", line 112, in _send_one_way_rpc_request raise TimeoutErr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
