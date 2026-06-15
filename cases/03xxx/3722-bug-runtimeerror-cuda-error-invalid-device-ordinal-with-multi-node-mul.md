# vllm-project/vllm#3722: [Bug]: RuntimeError: CUDA error: invalid device ordinal  with multi node multi gpus 

| 字段 | 值 |
| --- | --- |
| Issue | [#3722](https://github.com/vllm-project/vllm/issues/3722) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;quantization;triton |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: CUDA error: invalid device ordinal  with multi node multi gpus 

### Issue 正文摘录

### Your current environment vllm(0.3.3) on ray(2.10.0) cluster deployed by docker on 2 nodes with 2 GPU(Tesla T4) each. ### 🐛 Describe the bug vllm works good with argument ```--tensor-parallel-size 2```, but sucks with ```--tensor-parallel-size 4```

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Your current environment vllm(0.3.3) on ray(2.10.0) cluster deployed by docker on 2 nodes with 2 GPU(Tesla T4) each. ### 🐛 Describe the bug vllm works good with argument ```--tensor-parallel-size 2```, but sucks with ``...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization attention;cuda;kernel;quantization;triton build_error;crash;mismatch dtype;env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: RuntimeError: CUDA error: invalid device ordinal with multi node multi gpus bug ### Your current environment vllm(0.3.3) on ray(2.10.0) cluster deployed by docker on 2 nodes with 2 GPU(Tesla T4) each. ### 🐛 Descr...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ontend_api;model_support;quantization attention;cuda;kernel;quantization;triton build_error;crash;mismatch dtype;env_dependency Your current environment
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: quantization attention;cuda;kernel;quantization;triton build_error;crash;mismatch dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
