# vllm-project/vllm#30126: [Bug]: microsoft/phi-2 fails on aarch64

| 字段 | 值 |
| --- | --- |
| Issue | [#30126](https://github.com/vllm-project/vllm/issues/30126) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: microsoft/phi-2 fails on aarch64

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `microsoft/phi-2` fails on aarch64 with `RuntimeError: Invalid CPU attention head_dim: 80` Reproducer: 1. Follow the build instructions for ARM64 from https://docs.vllm.ai/en/v0.12.0/getting_started/installation/cpu/#full-build 2. Run the script below ```python from vllm import LLM, SamplingParams def main(): sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="microsoft/phi-2") prompt = "The future of AI is" outputs = llm.generate(prompt, sampling_params) for output in outputs: prompt_text = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt_text!r}, Generated text: {generated_text!r}") if __name__ == "__main__": main() ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: imeError: Invalid CPU attention head_dim: 80` Reproducer: 1. Follow the build instructions for ARM64 from https://docs.vllm.ai/en/v0.12.0/getting_started/installation/cpu/#full-build 2. Run the script below ```python fr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: microsoft/phi-2 fails on aarch64 bug;stale ### Your current environment ### 🐛 Describe the bug `microsoft/phi-2` fails on aarch64 with `RuntimeError: Invalid CPU attention head_dim: 80` Reproducer: 1. Follow the...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: microsoft/phi-2 fails on aarch64 bug;stale ### Your current environment ### 🐛 Describe the bug `microsoft/phi-2` fails on aarch64 with `RuntimeError: Invalid CPU attention head_dim: 80` Reproducer: 1. Follow the...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ails on aarch64 with `RuntimeError: Invalid CPU attention head_dim: 80` Reproducer: 1. Follow the build instructions for ARM64 from https://docs.vllm.ai/en/v0.12.0/getting_started/installation/cpu/#full-build 2. Run the...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: peculative_decoding attention;cuda;operator;sampling build_error;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
