# vllm-project/vllm#3627: [Bug]: System error: Can't get attribute 'TokenizerGroup' on <module 'vllm.transformers_utils.tokenizer'

| 字段 | 值 |
| --- | --- |
| Issue | [#3627](https://github.com/vllm-project/vllm/issues/3627) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: System error: Can't get attribute 'TokenizerGroup' on <module 'vllm.transformers_utils.tokenizer'

### Issue 正文摘录

### Your current environment ```text cuda 12.1 simple pip install vllm ``` ### 🐛 Describe the bug `python benchmarks/benchmark_throughput.py --backend vllm --input-len 1024 --output-len 512 --model /share/datasets/public_models/Qwen_Qwen-72B-Chat --tensor-parallel-size 4 --trust-remote-code` This will result in the following errors: ![image](https://github.com/vllm-project/vllm/assets/79788571/f2bb89b0-bc19-4e3b-859f-0b63ffe76dd7)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: r' bug;stale ### Your current environment ```text cuda 12.1 simple pip install vllm ``` ### 🐛 Describe the bug `python benchmarks/benchmark_throughput.py --backend vllm --input-len 1024 --output-len 512 --model /share/d...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: nchmark_throughput.py --backend vllm --input-len 1024 --output-len 512 --model /share/datasets/public_models/Qwen_Qwen-72B-Chat --tensor-parallel-size 4 --trust-remote-code` This will result in the following errors: ![i...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: cuda 12.1 simple pip install vllm ``` ### 🐛 Describe the bug `python benchmarks/benchmark_throughput.py --backend vllm --input-len 1024 --output-len 512 --model /share/datasets/public_models/Qwen_Qwen-72B-Chat --tensor-...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: `` ### 🐛 Describe the bug `python benchmarks/benchmark_throughput.py --backend vllm --input-len 1024 --output-len 512 --model /share/datasets/public_models/Qwen_Qwen-72B-Chat --tensor-parallel-size 4 --trust-remote-code...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: formers_utils.tokenizer' bug;stale ### Your current environment ```text cuda 12.1 simple pip install vllm ``` ### 🐛 Describe the bug `python benchmarks/benchmark_throughput.py --backend vllm --input-len 1024 --output-le...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
