# vllm-project/vllm#41296: [RFC]: Custom graph dumping for vLLM-compile and depyf deprecation

| 字段 | 值 |
| --- | --- |
| Issue | [#41296](https://github.com/vllm-project/vllm/issues/41296) |
| 状态 | open |
| 标签 | RFC;torch.compile |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Custom graph dumping for vLLM-compile and depyf deprecation

### Issue 正文摘录

### Motivation. Currently, vLLM uses depyf for graph dumping and introspection. However: - depyf is becoming a maintenance burden - tlparse (an alternative) is clunky, time-consuming and designed for PyTorch, not vLLM use cases - We need an extremely lightweight (single <300LOC PR), vLLM-aware graph dumping system The goal is that any vLLM developer not even familiar with `torch.compile` can set `VLLM_DEBUG_DUMP_PATH` and easily navigate the produced graph dumps. ### Proposed Change. Implement a mini-system that: 1. Hooks into `lazy_format_graph_code` to capture graphs at every (relevant) stage - Not sure if we need something different for output code 2. Dumps to `VLLM_DEBUG_DUMP_PATH`/`CompilationConfig.debug_dump_path`, with easily navigable structure 3. Preserves vLLM compilation context, including: - pass_context properties (e.g., compile ranges, donated inputs) - vllm config and model name associated with the dump - Any relevant vllm_ir metadata (like what provider will be selected in pre-lowered graphs) - Captures function names for `torch.compile` on smaller functions 4. Exports both representations: - Structured traces nesting by layer: #39215 - Unstructured traces: raw fx...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ### Proposed Change. Implement a mini-system that: 1. Hooks into `lazy_format_graph_code` to capture graphs at every (relevant) stage - Not sure if we need something different for output code 2. Dumps to `VLLM_DEBUG_DUM...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [RFC]: Custom graph dumping for vLLM-compile and depyf deprecation RFC;torch.compile ### Motivation. Currently, vLLM uses depyf for graph dumping and introspection. However: - depyf is becoming a maintenance burden - tl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: pre-lowered graphs) - Captures function names for `torch.compile` on smaller functions 4. Exports both representations: - Structured traces nesting by layer: #39215 - Unstructured traces: raw fx.Graph dump We can finall...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: config and model name associated with the dump - Any relevant vllm_ir metadata (like what provider will be selected in pre-lowered graphs) - Captures function names for `torch.compile` on smaller functions 4. Exports bo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
