# vllm-project/vllm#1846: Model Loading Stuck (in ray ?)

| 字段 | 值 |
| --- | --- |
| Issue | [#1846](https://github.com/vllm-project/vllm/issues/1846) |
| 状态 | closed |
| 标签 |  |
| 评论 | 21; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Model Loading Stuck (in ray ?)

### Issue 正文摘录

python = 3.11.5 torch = 2.1.0 + cu121 vllm = 0.2.2 GPU: L40 * 4 I install vllm by "pip install vllm". It will STUCK when loading vicuna-7b-v1.5 model using the vllm framework, while the fastchat framework work well. When I arise a KeyboardInterrupt, it is stuck at the ./ray/_private/worker.py, line 769, in get_objects data_metadata_pairs = self.core_worker.get_objects( File "python/ray/_raylet.pyx" in line 3211, in ray._raylet.CoreWorker.get_objects File "python/ray/_raylet.pyx" in line 449, in ray._raylet.check_status KeyboardInterrupt

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ay ?) python = 3.11.5 torch = 2.1.0 + cu121 vllm = 0.2.2 GPU: L40 * 4 I install vllm by "pip install vllm". It will STUCK when loading vicuna-7b-v1.5 model using the vllm framework, while the fastchat framework work wel...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: s stuck at the ./ray/_private/worker.py, line 769, in get_objects data_metadata_pairs = self.core_worker.get_objects( File "python/ray/_raylet.pyx" in line 3211, in ray._raylet.CoreWorker.get_objects File "python/ray/_r...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Model Loading Stuck (in ray ?) python = 3.11.5 torch = 2.1.0 + cu121 vllm = 0.2.2 GPU: L40 * 4 I install vllm by "pip install vllm". It will STUCK when loading vicuna-7b-v1.5 model using the vllm framework, while the f

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
