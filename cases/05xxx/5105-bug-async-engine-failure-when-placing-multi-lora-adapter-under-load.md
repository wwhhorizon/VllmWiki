# vllm-project/vllm#5105: [Bug]: async engine failure when placing multi lora adapter under load

| 字段 | 值 |
| --- | --- |
| Issue | [#5105](https://github.com/vllm-project/vllm/issues/5105) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: async engine failure when placing multi lora adapter under load

### Issue 正文摘录

my current environment: ``` 0.4.2 ``` my bug: i deployed hermes-2-pro-mistral-7b model with multi lora adapters. after applying a large multi adapter load on it, i started receiving an error stating it couldnt find the location of the stored adapters. any idea why? important note - the interval in which this error occurs is inconsistent. meaning it sometimes occurs under load of 30RPS (requests per second) applied for 30 minutes, and sometimes can occur under load of 3RPS for 10 seconds ``` Vllm error code Error in create_completion traceback: Traceback (most recent call last): File "/usr/local/lib/python3.10/dist-packages/vllm/lora/worker_manager.py", line 174, in _load_lora lora = self._lora_model_cls.from_local_checkpoint( File "/usr/local/lib/python3.10/dist-packages/vllm/lora/models.py", line 303, in from_local_checkpoint with open(lora_config_path) as f: FileNotFoundError: [Errno 2] No such file or directory: '/data/adapters/2024-03-28-00-04-12--lgy/adapter_config.json' The above exception was the direct cause of the following exception: Traceback (most recent call last): File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/openai/api_server.py", line 155, in creat...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: async engine failure when placing multi lora adapter under load bug;stale my current environment: ``` 0.4.2 ``` my bug: i deployed hermes-2-pro-mistral-7b model with multi lora adapters. after applying a large mu...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: in execute_model output = self.model_runner.execute_model(seq_group_metadata_list, File "/usr/local/lib/python3.10/dist-packages/torch/utils/_contextlib.py", line 115, in decorate_context return func(*args, **kwargs) Fi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: environment: ``` 0.4.2 ``` my bug: i deployed hermes-2-pro-mistral-7b model with multi lora adapters. after applying a large multi adapter load on it, i started receiving an error stating it couldnt find the location of...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ug]: async engine failure when placing multi lora adapter under load bug;stale my current environment: ``` 0.4.2 ``` my bug: i deployed hermes-2-pro-mistral-7b model with multi lora adapters. after applying a large mult...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
