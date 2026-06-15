# vllm-project/vllm#9443: [Bug]: Could we provide an interface for setting the "dtype" when calling the example/benchmarks python?  

| 字段 | 值 |
| --- | --- |
| Issue | [#9443](https://github.com/vllm-project/vllm/issues/9443) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Could we provide an interface for setting the "dtype" when calling the example/benchmarks python?  

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug My GPU is "Nvidia Tesla T4", when I execute the examples in my env, like "offline_inference_vision_language_multi_image.py", it will report: "ValueError: Bfloat16 is only supported on GPUs with compute capability of at least 8.0. Your Tesla T4 GPU has compute capability 7.5. You can use float16 instead by explicitly setting the`dtype` flag in CLI, for example: --dtype=half." but the python main is not support dtype input, so I cannot run this example in my env. We can see similar issue in benchmarks/benchmark_prefix_caching.py, others benchmarks cases already support dtype setting. Fail log: ![image](https://github.com/user-attachments/assets/060ab236-bcc3-4804-9984-a6a10c1c59d2) And for examples/offline_inference_vision_language_multi_image.py, if I change the code like this, it can run in my env: ![image](https://github.com/user-attachments/assets/831d4808-12d6-4bfd-9eeb-5beb0d17d0e2) ![image](https://github.com/user-attachments/assets/7ab52f1e-c39c-42a2-a676-1d4a163005e0) ![image](https://github.com/user-attachments/assets/6287018b-ae5f-45d7-acbc-2acf08fa7d82) A successfully executed log. ![...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: a T4 GPU has compute capability 7.5. You can use float16 instead by explicitly setting the`dtype` flag in CLI, for example: --dtype=half." but the python main is not support dtype input, so I cannot run this example in...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Could we provide an interface for setting the "dtype" when calling the example/benchmarks python? bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug My GPU is "Nvidi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ill report: "ValueError: Bfloat16 is only supported on GPUs with compute capability of at least 8.0. Your Tesla T4 GPU has compute capability 7.5. You can use float16 instead by explicitly setting the`dtype` flag in CLI...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: we provide an interface for setting the "dtype" when calling the example/benchmarks python? bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug My GPU is "Nvidia Tesla T4",...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: _build;distributed_parallel;hardware_porting;model_support cuda;operator;triton build_error;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
