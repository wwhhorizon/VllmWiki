# vllm-project/vllm#29532: [CI Failure]: mi325_4: 2 Node Tests (4 GPUs in total)

| 字段 | 值 |
| --- | --- |
| Issue | [#29532](https://github.com/vllm-project/vllm/issues/29532) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel |
| 子分类 |  |
| Operator 关键词 | operator |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: mi325_4: 2 Node Tests (4 GPUs in total)

### Issue 正文摘录

### Name of failing test `["VLLM_TEST_SAME_HOST=0 torchrun --nnodes 2 --nproc-per-node=2 --rdzv_backend=c10d --rdzv_endpoint=192.168.10.10 distributed/test_same_node.py | grep 'Same node test passed'", "NUM_NODES=2 torchrun --nnodes 2 --nproc-per-node=2 --rdzv_backend=c10d --rdzv_endpoint=192.168.10.10 distributed/test_node_count.py | grep 'Node count test passed'", "python3 ../examples/offline_inference/data_parallel.py --dp-size=2 --tp-size=1 --node-size=2 --node-rank=0 --master-addr=192.168.10.10 --master-port=12345 --enforce-eager --trust-remote-code", "VLLM_MULTI_NODE=1 pytest -v -s distributed/test_multi_node_assignment.py", "VLLM_MULTI_NODE=1 pytest -v -s distributed/test_pipeline_parallel.py"] && ["VLLM_TEST_SAME_HOST=0 torchrun --nnodes 2 --nproc-per-node=2 --rdzv_backend=c10d --rdzv_endpoint=192.168.10.10 distributed/test_same_node.py | grep 'Same node test passed'", "NUM_NODES=2 torchrun --nnodes 2 --nproc-per-node=2 --rdzv_backend=c10d --rdzv_endpoint=192.168.10.10 distributed/test_node_count.py | grep 'Node count test passed'", "python3 ../examples/offline_inference/data_parallel.py --dp-size=2 --tp-size=1 --node-size=2 --node-rank=1 --master-addr=192.168.10.10 --mast...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi325_4: 2 Node Tests (4 GPUs in total) ci-failure ### Name of failing test `["VLLM_TEST_SAME_HOST=0 torchrun --nnodes 2 --nproc-per-node=2 --rdzv_backend=c10d --rdzv_endpoint=192.168.10.10 distributed/test
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: --master-port=12345 --enforce-eager --trust-remote-code"]` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: `["VLLM_TEST_SAME_HOST=0 torchrun --nnodes 2 --nproc-per-node=2 --rdzv_backend=c10d --rdzv_endpoint=192.168.10.10 distributed/test_same_node.py | grep 'Same node test passed'", "NUM_NODES=2 torchrun --nnodes 2 --nproc-p...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: -trust-remote-code"]` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **Failing Test:** Multi-node distr...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: mi325_4: 2 Node Tests (4 GPUs in total) ci-failure ### Name of failing test `["VLLM_TEST_SAME_HOST=0 torchrun --nnodes 2 --nproc-per-node=2 --rdzv_backend=c10d --rdzv_endpoint=192.168.10.10 distributed/tes...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
