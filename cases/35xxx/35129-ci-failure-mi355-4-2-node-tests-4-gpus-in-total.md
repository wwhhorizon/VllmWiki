# vllm-project/vllm#35129: [CI Failure]:  mi355_4: 2 Node Tests (4 GPUs in total)

| 字段 | 值 |
| --- | --- |
| Issue | [#35129](https://github.com/vllm-project/vllm/issues/35129) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]:  mi355_4: 2 Node Tests (4 GPUs in total)

### Issue 正文摘录

### Name of failing test `["VLLM_TEST_SAME_HOST=0 torchrun --nnodes 2 --nproc-per-node=2 --rdzv_backend=c10d --rdzv_endpoint=192.168.10.10 distributed/test_same_node.py", "NUM_NODES=2 torchrun --nnodes 2 --nproc-per-node=2 --rdzv_backend=c10d --rdzv_endpoint=192.168.10.10 distributed/test_node_count.py", "python3 ../examples/offline_inference/data_parallel.py -dp=2 -tp=1 --dp-num-nodes=2 --dp-node-rank=0 --dp-master-addr=192.168.10.10 --dp-master-port=12345 --enforce-eager --trust-remote-code", "VLLM_MULTI_NODE=1 pytest -v -s distributed/test_multi_node_assignment.py", "VLLM_MULTI_NODE=1 pytest -v -s distributed/test_pipeline_parallel.py"] && ["VLLM_TEST_SAME_HOST=0 torchrun --nnodes 2 --nproc-per-node=2 --rdzv_backend=c10d --rdzv_endpoint=192.168.10.10 distributed/test_same_node.py", "NUM_NODES=2 torchrun --nnodes 2 --nproc-per-node=2 --rdzv_backend=c10d --rdzv_endpoint=192.168.10.10 distributed/test_node_count.py", "python3 ../examples/offline_inference/data_parallel.py -dp=2 -tp=1 --dp-num-nodes=2 --dp-node-rank=1 --dp-master-addr=192.168.10.10 --dp-master-port=12345 --enforce-eager --trust-remote-code"]` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ]...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi355_4: 2 Node Tests (4 GPUs in total) ci-failure ### Name of failing test `["VLLM_TEST_SAME_HOST=0 torchrun --nnodes 2 --nproc-per-node=2 --rdzv_backend=c10d --rdzv_endpoint=192.168.10.10 distributed/tes
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: `["VLLM_TEST_SAME_HOST=0 torchrun --nnodes 2 --nproc-per-node=2 --rdzv_backend=c10d --rdzv_endpoint=192.168.10.10 distributed/test_same_node.py", "NUM_NODES=2 torchrun --nnodes 2 --nproc-per-node=2 --rdzv_backend=c10d -...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: -trust-remote-code"]` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test There is possibly an infra-related...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: dp-master-port=12345 --enforce-eager --trust-remote-code"]` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: mi355_4: 2 Node Tests (4 GPUs in total) ci-failure ### Name of failing test `["VLLM_TEST_SAME_HOST=0 torchrun --nnodes 2 --nproc-per-node=2 --rdzv_backend=c10d --rdzv_endpoint=192.168.10.10 distributed/tes...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
