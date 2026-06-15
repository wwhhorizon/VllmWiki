# vllm-project/vllm#39216: [Bug]: vLLM 0.19.0 on PyPI pins transformers<5, but Gemma 4 support requires transformers>=5.5.0

| 字段 | 值 |
| --- | --- |
| Issue | [#39216](https://github.com/vllm-project/vllm/issues/39216) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vLLM 0.19.0 on PyPI pins transformers<5, but Gemma 4 support requires transformers>=5.5.0

### Issue 正文摘录

### Current environment - OS: Ubuntu Server - Python version: 3.12 - Installation method: `venv` / pip - Deployment type: remote server - vLLM version: `0.19.0` - Transformers version installed with vLLM: `4.57.6` - Transformers version required to test Gemma 4: `5.5.0` - Accelerate version: `1.13.0` - huggingface-hub version: `1.9.1` - Additional conflicting packages observed: - `compressed-tensors==0.14.0.1` - `xformers==0.0.33.post1` - Target model: `google/gemma-4-31B-it` ### 🐛 Describe the bug When installing `vllm==0.19.0` from PyPI in a regular Python virtual environment, the package requires `transformers>=4.56.0, =4.56.0, but you have transformers 5.5.0 which is incompatible. ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: vLLM 0.19.0 on PyPI pins transformers<5, but Gemma 4 support requires transformers>=5.5.0 bug ### Current environment - OS: Ubuntu Server - Python version: 3.12 - Installation method: `venv` / pip - Deployment ty...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: formers>=5.5.0 bug ### Current environment - OS: Ubuntu Server - Python version: 3.12 - Installation method: `venv` / pip - Deployment type: remote server - vLLM version: `0.19.0` - Transformers version installed with v...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: vLLM 0.19.0 on PyPI pins transformers<5, but Gemma 4 support requires transformers>=5.5.0 bug ### Current environment - OS: Ubuntu Server - Python version: 3.12 - Installation method: `venv` / pip - Deployment ty...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: version installed with vLLM: `4.57.6` - Transformers version required to test Gemma 4: `5.5.0` - Accelerate version: `1.13.0` - huggingface-hub version: `1.9.1` - Additional conflicting packages observed: - `compressed-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
