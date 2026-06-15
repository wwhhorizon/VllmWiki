# vllm-project/vllm#44280: [Roadmap] Rust Frontend Feature Parity

| 字段 | 值 |
| --- | --- |
| Issue | [#44280](https://github.com/vllm-project/vllm/issues/44280) |
| 状态 | open |
| 标签 | rust |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Roadmap] Rust Frontend Feature Parity

### Issue 正文摘录

## Motivation The Rust frontend has landed in the vLLM repository as a drop-in alternative to the Python API server process. It is enabled through `VLLM_USE_RUST_FRONTEND=1` and uses the existing vLLM engine/core boundary. The Rust frontend is still experimental and not yet feature-complete relative to the Python frontend. This issue tracks the roadmap for the remaining gaps in feature parity and provides community contributors with a place to find scoped work. This roadmap prioritizes user value and the Rust frontend's architectural goals over blanket 1:1 parity with the Python frontend. In particular, we may skip: - Features / endpoints / options that are not commonly used in production - Options that mainly reflect Python frontend implementation details or Python-side workarounds - Features whose Python implementation has accumulated enough complexity that redesigning or removing them may be better than porting them directly **For items marked with 🧭:** Please start with a design discussion before implementation, covering the intended API/architecture, co-design with the engine if needed, and the testing plan. Related context: - Original RFC: https://github.com/vllm-project/vll...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: stered image processor/model specs - [x] Multi-engine internal load balancing with scheduler-stat-aware routing - [x] Admin and operational routes: health, load, version, metrics, reset-cache, sleep/wake - [x] Mock-engi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: reaming) - [x] Tool calling and reasoning output support for several key model families - [x] Commonly used OpenAI-compatible sampling options - [x] Image-only multimodal chat path for registered image processor/model s...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ge processor/model specs - [x] Multi-engine internal load balancing with scheduler-stat-aware routing - [x] Admin and operational routes: health, load, version, metrics, reset-cache, sleep/wake - [x] Mock-engine and HTT...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ecs - [x] Multi-engine internal load balancing with scheduler-stat-aware routing - [x] Admin and operational routes: health, load, version, metrics, reset-cache, sleep/wake - [x] Mock-engine and HTTP integration-test in...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: Rust frontend development ## Roadmap ### Distributed serving and large-scale control plane - [ ] External DP load-balancing mode: support the Python-style shape where each API server connects to one DP rank 🧭 - [ ] Hybr...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
