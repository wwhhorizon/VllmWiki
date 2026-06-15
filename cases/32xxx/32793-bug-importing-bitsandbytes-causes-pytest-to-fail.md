# vllm-project/vllm#32793: [Bug]: importing `bitsandbytes` causes pytest to fail

| 字段 | 值 |
| --- | --- |
| Issue | [#32793](https://github.com/vllm-project/vllm/issues/32793) |
| 状态 | open |
| 标签 | bug;unstale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: importing `bitsandbytes` causes pytest to fail

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm having a subtle issue when running tests with `pytest`. ```python from vllm import LLM import bitsandbytes def test(): LLM(model="Qwen/Qwen2.5-1.5B") if __name__ == "__main__": test() ``` The following error ```log FAILED tests/test_vllm_client_server.py::test - RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} ``` occurs when: - `bitsandbytes` is imported in the test file. (not even used!) - I run the test with `pytest mre.py` I insist on the fact that both of these conditions are required to reproduce the issue. | | `import bitsandbytes` | No `import bitsandbytes` | | --- | --- | --- | | `pytest mre.py` | ❌ | ✅ | | `python mre.py` | ✅ | ✅ | vLLM version: 0.11.2 bitsandbytes version: 0.49.1 pytest version: 8.4.2 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: importing `bitsandbytes` causes pytest to fail bug;unstale ### Your current environment ### 🐛 Describe the bug I'm having a subtle issue when running tests with `pytest`. ```python from vllm import LLM import bits
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 4.2 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ```python from vllm import LLM import bitsandbytes def test(): LLM(model="Qwen/Qwen2.5-1.5B") if __name__ == "__main__": test() ``` The following error ```log FAILED tests/test_vllm_client_server.py::test - RuntimeError...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: importing `bitsandbytes` causes pytest to fail bug;unstale ### Your current environment ### 🐛 Describe the bug I'm having a subtle issue when running tests with `pytest`. ```python from vllm import LLM import bit...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
