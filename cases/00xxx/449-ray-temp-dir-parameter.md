# vllm-project/vllm#449: Ray _temp_dir Parameter

| 字段 | 值 |
| --- | --- |
| Issue | [#449](https://github.com/vllm-project/vllm/issues/449) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Ray _temp_dir Parameter

### Issue 正文摘录

Hello, I had the following OS error when running VLLM in a shared Slurm cluster environment. It seems to be caused by using the default _temp_dir during the initialization of Ray cluster. I don't have write permissions to the default directory. Could you please add an option to set a custom `_temp_dir`? Thank you! ``` File "/usr/local/lib/python3.8/dist-packages/vllm/engine/llm_engine.py", line 152, in from_engine_args distributed_init_method, devices = initialize_cluster(parallel_config) File "/usr/local/lib/python3.8/dist-packages/vllm/engine/ray_utils.py", line 41, in initialize_cluster ray.init(address=ray_address) File "/usr/local/lib/python3.8/dist-packages/ray/_private/client_mode_hook.py", line 103, in wrapper return func(*args, **kwargs) File "/usr/local/lib/python3.8/dist-packages/ray/_private/worker.py", line 1534, in init _global_node = ray._private.node.Node( File "/usr/local/lib/python3.8/dist-packages/ray/_private/node.py", line 209, in __init__ self._init_temp() File "/usr/local/lib/python3.8/dist-packages/ray/_private/node.py", line 383, in _init_temp try_to_create_directory(self._temp_dir) File "/usr/local/lib/python3.8/dist-packages/ray/_private/utils.py", line...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: _args distributed_init_method, devices = initialize_cluster(parallel_config) File "/usr/local/lib/python3.8/dist-packages/vllm/engine/ray_utils.py", line 41, in initialize_cluster ray.init(address=ray_address) File "/us...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
