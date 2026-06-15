# vllm-project/vllm#1287: Feature request. Allow a few model instances in one GPU if they can feet in VRAM.

| 字段 | 值 |
| --- | --- |
| Issue | [#1287](https://github.com/vllm-project/vllm/issues/1287) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Feature request. Allow a few model instances in one GPU if they can feet in VRAM.

### Issue 正文摘录

The idea in having more instances of the model in VRAM of single GPU, for example two 7B models can fit 24Gb easily, so on 2 24Gb GPUs we can have 4 instances for concurrent requests and wuth Ray help it should be possible if vLLM will support such kind of spreading. Now when trying to run 4 instances on 2 GPUs I got: ``` 2023-10-07 16:28:06,308 INFO worker.py:1642 -- Started a local Ray instance. Traceback (most recent call last): File " ", line 198, in _run_module_as_main File " ", line 88, in _run_code File "/usr/local/lib/python3.11/site-packages/vllm/entrypoints/openai/api_server.py", line 616, in engine = AsyncLLMEngine.from_engine_args(engine_args) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.11/site-packages/vllm/engine/async_llm_engine.py", line 483, in from_engine_args distributed_init_method, placement_group = initialize_cluster( ^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.11/site-packages/vllm/engine/ray_utils.py", line 107, in initialize_cluster raise ValueError( ValueError: The number of required GPUs exceeds the total number of available GPUs in the cluster. ```

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Feature request. Allow a few model instances in one GPU if they can feet in VRAM. The idea in having more instances of the model in VRAM of single GPU, for example two 7B models can fit 24Gb easily, so on 2 24Gb GPUs we...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Feature request. Allow a few model instances in one GPU if they can feet in VRAM. The idea in having more instances of the model in VRAM of single GPU, for example two 7B models can fit 24Gb easily, so on 2 24Gb GPUs we...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
