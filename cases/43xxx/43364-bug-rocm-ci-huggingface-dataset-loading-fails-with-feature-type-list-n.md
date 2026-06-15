# vllm-project/vllm#43364: [Bug]: [ROCm CI] HuggingFace dataset loading fails with "Feature type 'List' not found"

| 字段 | 值 |
| --- | --- |
| Issue | [#43364](https://github.com/vllm-project/vllm/issues/43364) |
| 状态 | open |
| 标签 | bug;rocm |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support |
| 子分类 | wrong_output |
| Operator 关键词 | cuda;kernel |
| 症状 | mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [ROCm CI] HuggingFace dataset loading fails with "Feature type 'List' not found"

### Issue 正文摘录

### Your current environment `collect_env.py` could not complete on the local machine due to a local CUDA driver/runtime mismatch during `torch.cuda.init()`. Relevant local test environment: * Ubuntu Linux * Python 3.12.3 * HuggingFace `datasets` successfully loads `philschmid/mt-bench` * `List` exists in `datasets.features._FEATURE_TYPES` ### 🐛 Describe the bug ## Summary Multiple ROCm CI suites are failing during HuggingFace dataset loading with: ```python id="j2sj4r" ValueError: Feature type 'List' not found ``` Affected suites observed: * `mi250_1: Multi-Modal Accuracy Eval (Small Models)` * `mi355_1: Examples` The failure occurs while loading: ```python id="agw81s" load_dataset("philschmid/mt-bench") ``` inside: ```python id="6qg0zm" vllm/benchmarks/datasets/datasets.py ``` ## Investigation The failure appears environment-specific rather than dataset-specific. I verified in a clean Linux environment that: ```python id="h1nhqz" from datasets import load_dataset ds = load_dataset("philschmid/mt-bench") ``` loads successfully using a modern HuggingFace `datasets` installation. Additionally: ```python id="cb7nh4" from datasets.features import features print("List" in features._FE...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: [ROCm CI] HuggingFace dataset loading fails with "Feature type 'List' not found" bug;rocm ### Your current environment `collect_env.py` could not complete on the local machine due to a local CUDA driver/runtime m...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: [ROCm CI] HuggingFace dataset loading fails with "Feature type 'List' not found" bug;rocm ### Your current environment `collect_env.py` could not complete on the local machine due to a local CUDA driver/runtime m...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: CUDA driver/runtime mismatch during `torch.cuda.init()`. Relevant local test environment: * Ubuntu Linux * Python 3.12.3 * HuggingFace `datasets` successfully loads `philschmid/mt-bench` * `List` exists in `datasets.fea...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: uld not complete on the local machine due to a local CUDA driver/runtime mismatch during `torch.cuda.init()`. Relevant local test environment: * Ubuntu Linux * Python 3.12.3 * HuggingFace `datasets` successfully loads `...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: [ROCm CI] HuggingFace dataset loading fails with "Feature type 'List' not found" bug;rocm ### Your current environment `collect_env.py` could not complete on the local machine due to a local CUDA driver/runtime m...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
