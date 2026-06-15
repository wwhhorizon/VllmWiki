# vllm-project/vllm#27684: [Bug]: FlashInfer MLA prefill correctness issues

| 字段 | 值 |
| --- | --- |
| Issue | [#27684](https://github.com/vllm-project/vllm/issues/27684) |
| 状态 | closed |
| 标签 | bug;nvidia |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache |
| 子分类 |  |
| Operator 关键词 | attention |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: FlashInfer MLA prefill correctness issues

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `pytest tests/v1/attention/test_mla_backends.py` on B200 shows correctness issues, e.g.: ``` E Failed: 3 backend(s) failed: _Backend.CUTLASS_MLA, _Backend.FLASHINFER_MLA, _Backend.TRITON_MLA E [_Backend.CUTLASS_MLA] output differs from SDPA baseline. Max diff: 7.500000, max rel diff: 136.000000) E assert False E [_Backend.FLASHINFER_MLA] output differs from SDPA baseline. Max diff: 7.500000, max rel diff: 136.000000) E assert False E [_Backend.TRITON_MLA] output differs from SDPA baseline. Max diff: 7.500000, max rel diff: 136.000000) E assert False ``` These arise from the FlashInfer prefill. Setting `VLLM_DISABLE_FLASHINFER_PREFILL=1` is a workaround. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: [Bug]: FlashInfer MLA prefill correctness issues bug;nvidia ### Your current environment ### 🐛 Describe the bug `pytest tests/v1/attention/test_mla_backends.py` on B200 shows correctness issues, e.g.: ``` E Fail
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 🐛 Describe the bug `pytest tests/v1/attention/test_mla_backends.py` on B200 shows correctness issues, e.g.: ``` E Failed: 3 backend(s) failed: _Backend.CUTLASS_MLA, _Backend.FLASHINFER_MLA, _Backend.TRITON_MLA E [_Backe...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: frequently asked questions. correctness attention_kv_cache attention env_dependency Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: line. Max diff: 7.500000, max rel diff: 136.000000) E assert False E [_Backend.FLASHINFER_MLA] output differs from SDPA baseline. Max diff: 7.500000, max rel diff: 136.000000) E assert False E [_Backend.TRITON_MLA] outp...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: FlashInfer MLA prefill correctness issues bug;nvidia ### Your current environment ### 🐛 Describe the bug `pytest tests/v1/attention/test_mla_backends.py` on B200 shows correctness issues, e.g.: ``` E Failed: 3 ba...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
