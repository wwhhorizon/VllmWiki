# vllm-project/vllm#21181: [Bug]: After outputting the normal content, keep outputting content= '', until finish_reason='length'.

| 字段 | 值 |
| --- | --- |
| Issue | [#21181](https://github.com/vllm-project/vllm/issues/21181) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: After outputting the normal content, keep outputting content= '', until finish_reason='length'.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Vllm commit commit https://github.com/vllm-project/vllm/commit/5f0af36af555a3813b9d30983bd29c384b84b647 (HEAD) Author: bigmoyan [moyan_work@foxmail.com](mailto:moyan_work@foxmail.com) Date: Sat Jul 12 04:16:14 2025 +0800 Update kimi-k2 tool calling docs, enable unit tests (https://github.com/vllm-project/vllm/pull/20821) I reproduced this problem on the latest code. GPU：8*H100 `vllm serve RedHatAI/Kimi-K2-Instruct-quantized.w4a16 --port 8000 --served-model-name kimi-k2-w4a16 --trust-remote-code --tensor-parallel-size 8 --enable-auto-tool-choice --tool-call-parser kimi_k2 --gpu-memory-utilization 0.95 --max-model-len 16384` After outputting the normal content, keep outputting content= '', until finish_reason='length'. I tested moonshotai/Kimi-K2-Instruct in the same environment, and the results were normal. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;operator;quantization;sampling...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ct/vllm/pull/20821) I reproduced this problem on the latest code. GPU：8*H100 `vllm serve RedHatAI/Kimi-K2-Instruct-quantized.w4a16 --port 8000 --served-model-name kimi-k2-w4a16 --trust-remote-code --tensor-parallel-size...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: , enable unit tests (https://github.com/vllm-project/vllm/pull/20821) I reproduced this problem on the latest code. GPU：8*H100 `vllm serve RedHatAI/Kimi-K2-Instruct-quantized.w4a16 --port 8000 --served-model-name kimi-k...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: lem on the latest code. GPU：8*H100 `vllm serve RedHatAI/Kimi-K2-Instruct-quantized.w4a16 --port 8000 --served-model-name kimi-k2-w4a16 --trust-remote-code --tensor-parallel-size 8 --enable-auto-tool-choice --tool-call-p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
