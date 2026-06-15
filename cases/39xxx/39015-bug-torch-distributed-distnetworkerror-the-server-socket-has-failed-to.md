# vllm-project/vllm#39015: [Bug]: torch.distributed.DistNetworkError: The server socket has failed to listen on any local network address. port: 29500, useIpv6: false, code: -98, name: EADDRINUSE, message: address already in use

| 字段 | 值 |
| --- | --- |
| Issue | [#39015](https://github.com/vllm-project/vllm/issues/39015) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: torch.distributed.DistNetworkError: The server socket has failed to listen on any local network address. port: 29500, useIpv6: false, code: -98, name: EADDRINUSE, message: address already in use

### Issue 正文摘录

### Your current environment in _invoke_run self._initialize_workers(self._worker_group) File "/mnt/bn/zjw-2/anaconda3/envs/vlm/lib/python3.11/site-packages/torch/distributed/elastic/metrics/api.py", line 138, in wrapper result = f(*args, **kwargs) ^^^^^^^^^^^^^^^^^^ File "/mnt/bn/zjw-2/anaconda3/envs/vlm/lib/python3.11/site-packages/torch/distributed/elastic/agent/server/api.py", line 683, in _initialize_workers self._rendezvous(worker_group) File "/mnt/bn/zjw-2/anaconda3/envs/vlm/lib/python3.11/site-packages/torch/distributed/elastic/metrics/api.py", line 138, in wrapper result = f(*args, **kwargs) ^^^^^^^^^^^^^^^^^^ File "/mnt/bn/zjw-2/anaconda3/envs/vlm/lib/python3.11/site-packages/torch/distributed/elastic/agent/server/api.py", line 498, in _rendezvous rdzv_info = spec.rdzv_handler.next_rendezvous() ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/mnt/bn/zjw-2/anaconda3/envs/vlm/lib/python3.11/site-packages/torch/distributed/elastic/rendezvous/static_tcp_rendezvous.py", line 67, in next_rendezvous self._store = TCPStore( # type: ignore[call-arg] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ torch.distributed.DistNetworkError: The server socket has failed to listen on any local network addres...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: tialize_workers(self._worker_group) File "/mnt/bn/zjw-2/anaconda3/envs/vlm/lib/python3.11/site-packages/torch/distributed/elastic/metrics/api.py", line 138, in wrapper result = f(*args, **kwargs) ^^^^^^^^^^^^^^^^^^ File...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 常运行 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: s failed to listen on any local network address. port: 29500, useIpv6: false, code: -98, name: EADDRINUSE, message: address already in use bug ### Your current environment in _invoke_run self._initialize_workers(self._w...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: true --save_safetensors true --dataset /mnt/bn/zjw-2/MultiModal/LLM/sft_test.jsonl --train_iters 10 --tensor_model_parallel_size 2 --sequence_parallel true --micro_batch_size 16 --global_batch_size 16 --recompute_granul...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
