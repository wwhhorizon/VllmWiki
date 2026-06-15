# vllm-project/vllm#26438: [Bug]: TypeError: argument 'id': StreamInput must be either an integer or a list of integers

| 字段 | 值 |
| --- | --- |
| Issue | [#26438](https://github.com/vllm-project/vllm/issues/26438) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: TypeError: argument 'id': StreamInput must be either an integer or a list of integers

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running inference with **Qwen3-Next-80B-A3B-Instruct** model using vLLM V1 engine, a `TypeError` occurs during token generation: ``` TypeError: argument 'id': StreamInput must be either an integer or a list of integers ``` **Critical constraint**: Qwen3-Next model **requires V1 engine** (has assertion `AssertionError: Qwen3Next requires VLLM_USE_V1`), so V0 engine cannot be used as a workaround. **Error Location**: `/vllm/v1/engine/detokenizer.py`, Line 237 **Full Stack Trace**: ```python Traceback (most recent call last): File "/vllm/v1/engine/output_processor.py", line 420, in process_outputs stop_string = req_state.detokenizer.update( File "/vllm/v1/engine/detokenizer.py", line 119, in update self.output_text += self.decode_next(new_token_id) File "/vllm/v1/engine/detokenizer.py", line 219, in decode_next token = self._protected_step(next_token_id) File "/vllm/v1/engine/detokenizer.py", line 237, in _protected_step token = self.stream.step(self.tokenizer, next_token_id) TypeError: argument 'id': StreamInput must be either an integer or a list of integers ``` ### Investigation & Debug Findings **Debug Output**: Added loggi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: it with the TypeError. **Attempted Fixes** (All Failed): 1. **Type conversion with `.item()`**: ```python if hasattr(next_token_id, 'item'): next_token_id = int(next_token_id.item()) ``` 2. **Explicit int() conversion**...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 821 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: nt environment ### 🐛 Describe the bug When running inference with **Qwen3-Next-80B-A3B-Instruct** model using vLLM V1 engine, a `TypeError` occurs during token generation: ``` TypeError: argument 'id': StreamInput must...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: pment ci_build;frontend_api;hardware_porting;model_support cuda;operator;triton build_error;crash env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: engine/detokenizer.py", line 119, in update self.output_text += self.decode_next(new_token_id) File "/vllm/v1/engine/detokenizer.py", line 219, in decode_next token = self._protected_step(next_token_id) File "/vllm/v1/e...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
