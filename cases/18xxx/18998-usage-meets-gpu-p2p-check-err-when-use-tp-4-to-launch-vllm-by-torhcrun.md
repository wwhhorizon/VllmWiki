# vllm-project/vllm#18998: [Usage]: meets gpu p2p check err when use tp=4 to launch vllm by torhcrun

| 字段 | 值 |
| --- | --- |
| Issue | [#18998](https://github.com/vllm-project/vllm/issues/18998) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: meets gpu p2p check err when use tp=4 to launch vllm by torhcrun

### Issue 正文摘录

### Your current environment **Background** > i have one pytorchjob with 4 pods, every pod has one gpu, there are in the same host, and can communicate with each other by nvlink. i can train with pytorch with tp=4, but when i launch vllm servering with torchrun, it meets err. the pytroch job has 1 master and 3 workers, i launch vllm servering by mpirun in the master pod. ```text mpirun -np 4 -map-by node bash torchrun.sh ``` torchrun.sh ```text torchrun --nproc_per_node 1 --nnodes 4 --node_rank $RANK --master_addr $MASTER_ADDR --master_port $MASTER_PORT example.py ``` example.py ```text # SPDX-License-Identifier: Apache-2.0 """ experimental support for tensor-parallel inference with torchrun, see https://github.com/vllm-project/vllm/issues/11400 for the motivation and use case for this example. run the script with `torchrun --nproc-per-node=2 torchrun_example.py`, the argument 2 should match the `tensor_parallel_size` below. see `tests/distributed/test_torchrun_example.py` for the unit test. """ import torch.distributed as dist from vllm import LLM, SamplingParams # Create prompts, the same across all ranks prompts = [ "Hello, my name is", "The president of the United States is",...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: u, there are in the same host, and can communicate with each other by nvlink. i can train with pytorch with tp=4, but when i launch vllm servering with torchrun, it meets err. the pytroch job has 1 master and 3 workers,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: local/lib/python3.10/dist-packages/vllm/distributed/device_communicators/cuda_communicator.py", line 47, in __init__ [rank3]: self.ca_comm = CustomAllreduce( [rank3]: File "/usr/local/lib/python3.10/dist-packages/vllm/d...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: re that # all ranks have the same random seed, so that sampling can be # deterministic across ranks. llm = LLM( model="facebook/opt-125m", tensor_parallel_size=4, #pipeline_parallel_size=2, distributed_executor_backend=...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ed, so that sampling can be # deterministic across ranks. llm = LLM( model="facebook/opt-125m", tensor_parallel_size=4, #pipeline_parallel_size=2, distributed_executor_backend="external_launcher", #max_model_len=32768,...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: .py`, the argument 2 should match the `tensor_parallel_size` below. see `tests/distributed/test_torchrun_example.py` for the unit test. """ import torch.distributed as dist from vllm import LLM, SamplingParams # Create...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
