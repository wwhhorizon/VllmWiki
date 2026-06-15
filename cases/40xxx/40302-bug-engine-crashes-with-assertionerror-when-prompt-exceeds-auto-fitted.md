# vllm-project/vllm#40302: [Bug]: Engine crashes with AssertionError when prompt exceeds auto-fitted max_model_len (admission check missing)

| 字段 | 值 |
| --- | --- |
| Issue | [#40302](https://github.com/vllm-project/vllm/issues/40302) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Engine crashes with AssertionError when prompt exceeds auto-fitted max_model_len (admission check missing)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When `--max-model-len=-1` is used (the default auto-fit behavior), vLLM correctly reduces `max_model_len` from the model config value (262,144) to what fits in GPU memory (15,168 on 1× H100-80GB). However, the **admission layer still uses the original 262,144 value**, so prompts between 15,168 and 262,144 tokens are accepted into the engine pipeline and then crash it with a fatal `AssertionError` in `_bookkeeping_sync`. ### Expected behavior Prompts exceeding the auto-fitted `max_model_len` should be rejected at admission with **HTTP 400** ("prompt too long"). Thw engine should remain alive. ### Actual behavior 1. `/v1/models` advertises `"max_model_len": 262144` (the HF config value, not the auto-fitted 15,168) 2. A prompt with ~15,500 tokens passes admission 3. The engine crashes at `gpu_model_runner.py:3446` with `AssertionError` 4. `EngineDeadError` propagates → HTTP 500 → process exits → pod restarts (~2-3 min) 5. All other in-flight requests on that engine get 503 ### Two sub-issues 1. **`/v1/models` reports the wrong `max_model_len`** — it should report the auto-fitted value (15,168), not the model config value (262,144)....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: should be 15168 ``` Send prompts of increasing size: ```python import requests, json def test_prompt(n_tokens): prompt = "The quick brown fox jumps over the lazy dog. " * (n_tokens // 10) r = requests.post("http://local...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: : Engine crashes with AssertionError when prompt exceeds auto-fitted max_model_len (admission check missing) bug ### Your current environment ### 🐛 Describe the bug When `--max-model-len=-1` is used (the default auto-fi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: he model config value (262,144) to what fits in GPU memory (15,168 on 1× H100-80GB). However, the **admission layer still uses the original 262,144 value**, so prompts between 15,168 and 262,144 tokens are accepted into...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: P 500 → process exits → pod restarts (~2-3 min) 5. All other in-flight requests on that engine get 503 ### Two sub-issues 1. **`/v1/models` reports the wrong `max_model_len`** — it should report the auto-fitted value (1...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ar;hardware_porting;model_support;sampling_logits cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
