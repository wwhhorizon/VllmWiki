# vllm-project/vllm#41960: [CI Failure]: PyTorch Fullgraph Smoke Test — counter assertions and AOT cache collision in tests/compile/fullgraph/

| 字段 | 值 |
| --- | --- |
| Issue | [#41960](https://github.com/vllm-project/vllm/issues/41960) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;hardware_porting;model_support |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: PyTorch Fullgraph Smoke Test — counter assertions and AOT cache collision in tests/compile/fullgraph/

### Issue 正文摘录

### Name of failing test ``` tests/compile/fullgraph/test_toy_llama.py::test_toy_llama[eager-False] tests/compile/fullgraph/test_toy_llama.py::test_toy_llama[inductor-False] tests/compile/fullgraph/test_toy_llama.py::test_toy_llama[inductor-True] tests/compile/fullgraph/test_multiple_graphs.py::test_multi_graph_piecewise_compile[True-False] tests/compile/fullgraph/test_multiple_graphs.py::test_multi_graph_piecewise_compile[True-True] tests/compile/fullgraph/test_multiple_graphs.py::test_multi_graph_piecewise_compile[False-False] tests/compile/fullgraph/test_multiple_graphs.py::test_multi_graph_piecewise_compile[False-True] tests/compile/fullgraph/test_simple.py::test_simple_piecewise_compile[False-inductor] ``` ### Basic information - [x] Can reproduce locally - [ ] Flaky test - [ ] Caused by external libraries ### 🧪 Describe the failing test The "PyTorch Fullgraph Smoke Test" Buildkite step fails with two distinct error patterns ([CI build #64888](https://buildkite.com/vllm/ci/builds/64888/canvas?sid=019e01bb-c842-47bf-857e-0fcc74925db6&tab=output)). **Pattern 1 — counter assertion (7 of 8):** ``` File "/usr/local/lib/python3.12/dist-packages/vllm/compilation/counter.py", line 51...

## 现有链接修复摘要

#41953 [CI][Bugfix] Fix failure CI step "PyTorch Fullgraph Smoke Test"

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [CI Failure]: PyTorch Fullgraph Smoke Test — counter assertions and AOT cache collision in tests/compile/fullgraph/ ### Name of failing test ``` tests/compile/fullgraph/test_toy_llama.py::test_toy_llama[eager-False] test
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [CI Failure]: PyTorch Fullgraph Smoke Test — counter assertions and AOT cache collision in tests/compile/fullgraph/ ### Name of failing test ``` tests/compile/fullgraph/test_toy_llama.py::test_toy_llama[eager-False] tes...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ullgraph/ ### Name of failing test ``` tests/compile/fullgraph/test_toy_llama.py::test_toy_llama[eager-False] tests/compile/fullgraph/test_toy_llama.py::test_toy_llama[inductor-False] tests/compile/fullgraph/test_toy_ll...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: se `num_graphs_seen` stays at 0 even after `torch.compile` runs and `VllmBackend.__call__` increments it. Root cause: `tests/utils.py:spawn_new_process_for_each_test` cloudpickles the inner test function `f` and runs it...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: t ``` tests/compile/fullgraph/test_toy_llama.py::test_toy_llama[eager-False] tests/compile/fullgraph/test_toy_llama.py::test_toy_llama[inductor-False] tests/compile/fullgraph/test_toy_llama.py::test_toy_llama[inductor-T...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41953](https://github.com/vllm-project/vllm/pull/41953) | closes_keyword | 0.95 | [CI][Bugfix] Fix failure CI step "PyTorch Fullgraph Smoke Test" | Fixes #41960 — 8 fullgraph failures introduced by #41423 ([CI build #64888](https://buildkite.com/vllm/ci/builds/64888/canvas?sid=019e01bb-c842-47bf-857e-0fcc74925db6&tab=output)): |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
