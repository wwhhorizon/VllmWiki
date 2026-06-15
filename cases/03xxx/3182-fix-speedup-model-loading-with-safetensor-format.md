# vllm-project/vllm#3182: [Fix] Speedup model loading with safetensor format

| 字段 | 值 |
| --- | --- |
| Issue | [#3182](https://github.com/vllm-project/vllm/issues/3182) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Fix] Speedup model loading with safetensor format

### Issue 正文摘录

In /vllm/model_executor/weight_utils.py ``` elif use_safetensors: for st_file in hf_weights_files: with safe_open(st_file, framework="pt") as f: for name in f.keys(): # noqa: SIM118 param = f.get_tensor(name) yield name, param ``` The default device for safe_open is 'cpu', which in some case severely slows down the weight loading speed. For example, in our case, it takes 194s to load a llama2-7b model. To fix this issue, we change the implementation a little bit: ``` elif use_safetensors: for st_file in hf_weights_files: with safe_open(st_file, framework="pt", **device=device**) as f: for name in f.keys(): # noqa: SIM118 param = f.get_tensor(name) yield name, param ``` which speed up the loading time from 194s to 6s, 32x faster.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Fix] Speedup model loading with safetensor format stale In /vllm/model_executor/weight_utils.py ``` elif use_safetensors: for st_file in hf_weights_files: with safe_open(st_file, framework="pt") as f: for name in f.key
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Fix] Speedup model loading with safetensor format stale In /vllm/model_executor/weight_utils.py ``` elif use_safetensors: for st_file in hf_weights_files: with safe_open(st_file, framework="pt") as f: for name in f.key...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
