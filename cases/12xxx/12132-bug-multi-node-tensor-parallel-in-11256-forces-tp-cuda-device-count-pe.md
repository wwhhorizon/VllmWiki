# vllm-project/vllm#12132: [Bug]: Multi-Node Tensor-Parallel in #11256 forces TP > cuda_device_count per node

| 字段 | 值 |
| --- | --- |
| Issue | [#12132](https://github.com/vllm-project/vllm/issues/12132) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Multi-Node Tensor-Parallel in #11256 forces TP > cuda_device_count per node

### Issue 正文摘录

### Your current environment Running in Docker container (Kubernetes) on (4) GH200 nodes. 1 GPU per node. ### Model Input Dumps python3 -m vllm.entrypoints.openai.api_server --model /models/my-model \ --tensor-parallel-size 4 \ --gpu-memory-utilization 0.95 \ --served-model-name my-model \ --trust-remote-code \ --api-key "NONE" \ --rope-scaling '{"rope_type":"dynamic","factor":4.0}' \ --enable-prefix-caching \ --max-model-len 131072 ### 🐛 Describe the bug @youkaichao, it looks like https://github.com/vllm-project/vllm/pull/11256 forces --tensor-parallel-size to be > per node GPU. https://github.com/vllm-project/vllm/blob/main/vllm/platforms/cuda.py#L156 ```python # Use confusing message for more common TP-only case. assert tensor_parallel_size ", line 19, in __init__ File "/usr/local/lib/python3.12/dist-packages/vllm/config.py", line 3204, in __post_init__ current_platform.check_and_update_config(self) File "/usr/local/lib/python3.12/dist-packages/vllm/platforms/cuda.py", line 156, in check_and_update_config assert tensor_parallel_size <= cuda_device_count, ( ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ AssertionError: please set tensor_parallel_size (4) to less than max local gpu co...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: cuda_device_count per node bug ### Your current environment Running in Docker container (Kubernetes) on (4) GH200 nodes. 1 GPU per node. ### Model Input Dumps python3 -m vllm.entrypoints.openai.api_server --model /model...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Multi-Node Tensor-Parallel in #11256 forces TP > cuda_device_count per node bug ### Your current environment Running in Docker container (Kubernetes) on (4) GH200 nodes. 1 GPU per node. ### Model Input Dumps pyth...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: n Docker container (Kubernetes) on (4) GH200 nodes. 1 GPU per node. ### Model Input Dumps python3 -m vllm.entrypoints.openai.api_server --model /models/my-model \ --tensor-parallel-size 4 \ --gpu-memory-utilization 0.95...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;frontend_api;model_support cuda crash env_d...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
