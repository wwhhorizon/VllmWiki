# vllm-project/vllm#2540: ValueError: Port could not be cast to integer value as '<function get_open_port at 0x7fc97190a7a0>

| 字段 | 值 |
| --- | --- |
| Issue | [#2540](https://github.com/vllm-project/vllm/issues/2540) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> ValueError: Port could not be cast to integer value as '<function get_open_port at 0x7fc97190a7a0>

### Issue 正文摘录

` torch.distributed.init_process_group( File "/root/miniconda3/envs/vllm2/lib/python3.10/site-packages/torch/distributed/c10d_logger.py", line 74, in wrapper func_return = func(*args, **kwargs) File "/root/miniconda3/envs/vllm2/lib/python3.10/site-packages/torch/distributed/distributed_c10d.py", line 1141, in init_process_group store, rank, world_size = next(rendezvous_iterator) File "/root/miniconda3/envs/vllm2/lib/python3.10/site-packages/torch/distributed/rendezvous.py", line 184, in _tcp_rendezvous_handler if not result.port: File "/root/miniconda3/envs/vllm2/lib/python3.10/urllib/parse.py", line 185, in port raise ValueError(f"Port could not be cast to integer value as {port!r}") ValueError: Port could not be cast to integer value as ' ' `

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
