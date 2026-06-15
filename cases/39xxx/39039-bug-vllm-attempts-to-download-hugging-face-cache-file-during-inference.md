# vllm-project/vllm#39039: [Bug]: vLLM attempts to download Hugging Face cache file during inference despite local model path (Gemma 4)

| 字段 | 值 |
| --- | --- |
| Issue | [#39039](https://github.com/vllm-project/vllm/issues/39039) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vLLM attempts to download Hugging Face cache file during inference despite local model path (Gemma 4)

### Issue 正文摘录

### Your current environment Environment: vLLM version: 19.0.0 Python: 3.12 Envoirement: Kube When I allow downloads, vLLm tries to trigger HuggingFace download, which is not desired here ### 🐛 Describe the bug I'm trying to run Gemma 4 (google/gemma-4-31B-it) with vLLM in a strictly air-gapped environment where downloads and inference must be completely separated. ### Expected behavior After downloading the model locally via hf, vLLM should load entirely from the local path without any network requests to Hugging Face. ### Actual behavior When starting inference with vLLM, it suddenly attempts to download a cache file from Hugging Face. This breaks my offline setup. I have never observed this behavior with other LLMs (Llama, Mistral, etc.) or previous Gemma versions. ### Steps to reproduce Download model (on machine with internet): ```bash hf download google/gemma-4-31B-it ``` Move to air-gapped environment and run ```bash vllm serve /mnt/models/google/gemma-4-26b-it ``` vLLM initialization triggers attempted download instead of using local files only (with export HF_HUB_OFFLINE=1 it simply crashes and says it could not find the files). ### Before submitting a new issue... - [x]...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: empts to download Hugging Face cache file during inference despite local model path (Gemma 4) bug ### Your current environment Environment: vLLM version: 19.0.0 Python: 3.12 Envoirement: Kube When I allow downloads, vLL...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: er LLMs (Llama, Mistral, etc.) or previous Gemma versions. ### Steps to reproduce Download model (on machine with internet): ```bash hf download google/gemma-4-31B-it ``` Move to air-gapped environment and run ```bash v...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: model path (Gemma 4) bug ### Your current environment Environment: vLLM version: 19.0.0 Python: 3.12 Envoirement: Kube When I allow downloads, vLLm tries to trigger HuggingFace download, which is not desired here ### 🐛...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: s). ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: nload Hugging Face cache file during inference despite local model path (Gemma 4) bug ### Your current environment Environment: vLLM version: 19.0.0 Python: 3.12 Envoirement: Kube When I allow downloads, vLLm tries to t...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
