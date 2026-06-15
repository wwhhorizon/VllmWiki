# vllm-project/vllm#572: ModuleNotFoundError: No module named 'transformers_modules' with API serving using baichuan-7b

| 字段 | 值 |
| --- | --- |
| Issue | [#572](https://github.com/vllm-project/vllm/issues/572) |
| 状态 | closed |
| 标签 |  |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> ModuleNotFoundError: No module named 'transformers_modules' with API serving using baichuan-7b

### Issue 正文摘录

I tried to deploy an API serving using baichuan-7b, but there is an error: ``` NCCL_P2P_DISABLE=1 CUDA_VISIBLE_DEVICES=6,7 python -m vllm.entrypoints.openai.api_server --model /root/data/zyy/baichuan-7B --host 0.0.0.0 --port 11114 --tensor-parallel-size 2 --trust-remote-code ``` ``` (RayWorker pid=53626) No module named 'transformers_modules' (RayWorker pid=53626) Traceback (most recent call last): (RayWorker pid=53626) File "/root/miniconda3/envs/vllm/lib/python3.9/site-packages/ray/_private/serialization.py", line 387, in deserialize_objects (RayWorker pid=53626) obj = self._deserialize_object(data, metadata, object_ref) (RayWorker pid=53626) File "/root/miniconda3/envs/vllm/lib/python3.9/site-packages/ray/_private/serialization.py", line 268, in _deserialize_object (RayWorker pid=53626) return self._deserialize_msgpack_data(data, metadata_fields) (RayWorker pid=53626) File "/root/miniconda3/envs/vllm/lib/python3.9/site-packages/ray/_private/serialization.py", line 223, in _deserialize_msgpack_data (RayWorker pid=53626) python_objects = self._deserialize_pickle5_data(pickle5_data) (RayWorker pid=53626) File "/root/miniconda3/envs/vllm/lib/python3.9/site-packages/ray/_private/ser...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: serving using baichuan-7b, but there is an error: ``` NCCL_P2P_DISABLE=1 CUDA_VISIBLE_DEVICES=6,7 python -m vllm.entrypoints.openai.api_server --model /root/data/zyy/baichuan-7B --host 0.0.0.0 --port 11114 --tensor-para...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: e_objects (RayWorker pid=53626) obj = self._deserialize_object(data, metadata, object_ref) (RayWorker pid=53626) File "/root/miniconda3/envs/vllm/lib/python3.9/site-packages/ray/_private/serialization.py", line 268, in...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: CUDA_VISIBLE_DEVICES=6,7 python -m vllm.entrypoints.openai.api_server --model /root/data/zyy/baichuan-7B --host 0.0.0.0 --port 11114 --tensor-parallel-size 2 --trust-remote-code ``` ``` (RayWorker pid=53626) No module n...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
