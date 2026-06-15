# vllm-project/vllm#27007: [Bug] [ROCm] [Flex Attention]: Unable to run

| 字段 | 值 |
| --- | --- |
| Issue | [#27007](https://github.com/vllm-project/vllm/issues/27007) |
| 状态 | closed |
| 标签 | bug;rocm;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] [ROCm] [Flex Attention]: Unable to run

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Flex Attention is enabled in this PR [Hardware][AMD] Enable FlexAttention backend on ROCm https://github.com/vllm-project/vllm/pull/26439 Docker image: `rocm/vllm-dev:nightly` Reinstall with latest vLLM commit. Command: `VLLM_ATTENTION_BACKEND="FLEX_ATTENTION" vllm serve meta-llama/Llama-3.1-8B-Instruct` LM_eval command: ``` #!/bin/bash lm_eval \ --model local-completions \ --tasks gsm8k \ --model_args model=meta-llama/Llama-3.1-8B-Instruct,base_url=http://127.0.0.1:8000/v1/completions \ --batch_size 100 ``` Error log when I send lm_eval evaluation: ```log (EngineCore_DP0 pid=549800) File "/usr/local/lib/python3.12/dist-packages/torch/nn/modules/module.py", line 1773, in _wrapped_call_impl (EngineCore_DP0 pid=549800) return self._call_impl(*args, **kwargs) (EngineCore_DP0 pid=549800) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=549800) File "/usr/local/lib/python3.12/dist-packages/torch/nn/modules/module.py", line 1784, in _call_impl (EngineCore_DP0 pid=549800) return forward_call(*args, **kwargs) (EngineCore_DP0 pid=549800) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=549800) File " .2", line 5, in forward (EngineCo...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: tention backend on ROCm https://github.com/vllm-project/vllm/pull/26439 Docker image: `rocm/vllm-dev:nightly` Reinstall with latest vLLM commit. Command: `VLLM_ATTENTION_BACKEND="FLEX_ATTENTION" vllm serve meta-llama/Ll...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug] [ROCm] [Flex Attention]: Unable to run bug;rocm;stale ### Your current environment ### 🐛 Describe the bug Flex Attention is enabled in this PR [Hardware][AMD] Enable FlexAttention backend on ROCm https://github.co...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: mit. Command: `VLLM_ATTENTION_BACKEND="FLEX_ATTENTION" vllm serve meta-llama/Llama-3.1-8B-Instruct` LM_eval command: ``` #!/bin/bash lm_eval \ --model local-completions \ --tasks gsm8k \ --model_args model=meta-llama/Ll...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: lex Attention is enabled in this PR [Hardware][AMD] Enable FlexAttention backend on ROCm https://github.com/vllm-project/vllm/pull/26439 Docker image: `rocm/vllm-dev:nightly` Reinstall with latest vLLM commit. Command:...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug] [ROCm] [Flex Attention]: Unable to run bug;rocm;stale ### Your current environment ### 🐛 Describe the bug Flex Attention is enabled in this PR [Hardware][AMD] Enable FlexAttention backend on ROCm https://github.co...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
