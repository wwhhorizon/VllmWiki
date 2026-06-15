# vllm-project/vllm#2115: pytest tests/models fail

| 字段 | 值 |
| --- | --- |
| Issue | [#2115](https://github.com/vllm-project/vllm/issues/2115) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> pytest tests/models fail

### Issue 正文摘录

Running the following command on an H100 computer ``` pytest tests/models/ ``` gave me the following errors: ``` FAILED tests/models/test_models.py::test_models[128-half-mistralai/Mistral-7B-v0.1] - AssertionError: tensor model parallel group is already initialized FAILED tests/models/test_models.py::test_models[128-half-tiiuae/falcon-7b] - AssertionError: tensor model parallel group is already initialized FAILED tests/models/test_models.py::test_models[128-half-gpt2] - AssertionError: tensor model parallel group is already initialized FAILED tests/models/test_models.py::test_models[128-half-bigcode/tiny_starcoder_py] - AssertionError: tensor model parallel group is already initialized FAILED tests/models/test_models.py::test_models[128-half-EleutherAI/gpt-j-6b] - AssertionError: tensor model parallel group is already initialized FAILED tests/models/test_models.py::test_models[128-half-EleutherAI/pythia-70m] - AssertionError: tensor model parallel group is already initialized FAILED tests/models/test_models.py::test_models[128-half-bigscience/bloom-560m] - AssertionError: tensor model parallel group is already initialized FAILED tests/models/test_models.py::test_models[128-half-mo...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: initialized FAILED tests/models/test_models.py::test_models[128-half-bigscience/bloom-560m] - AssertionError: tensor model parallel group is already initialized FAILED tests/models/test_models.py::test_models[128-half-m...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: pytest tests/models fail Running the following command on an H100 computer ``` pytest tests/models/ ``` gave me the following errors: ``` FAILED tests/models/test_models.py::test_models[128-half-mistralai/Mistral-7B-v0....
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ed FAILED tests/models/test_models.py::test_models[128-half-bigscience/bloom-560m] - AssertionError: tensor model parallel group is already initialized FAILED tests/models/test_models.py::test_models[128-half-mosaicml/m...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: pytest tests/models fail Running the following command on an H100 computer ``` pytest tests/models/ ``` gave me the following errors: ``` FAILED tests/models/test_models.py::test_models[128-half-mistralai/Mistral-7B-v0....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: pytest tests/models fail Running the following command on an H100 computer ``` pytest tests/models/ ``` gave me the following errors: ``` FAILED tests/models/test_models.py::test_models[128-half-mistralai/Mistral-7B-v0.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
