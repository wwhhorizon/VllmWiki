# vllm-project/vllm#14518: [Usage]: Can't use the local model with LLM class.

| 字段 | 值 |
| --- | --- |
| Issue | [#14518](https://github.com/vllm-project/vllm/issues/14518) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Can't use the local model with LLM class.

### Issue 正文摘录

### Your current environment I'm on Kaggle and trying to use LLM with the local trained model but getting the error: Code: ```py from vllm import LLM, SamplingParams llm_model_pth = "/kaggle/input/deepseek-r1/transformers/deepseek-r1-distill-qwen-7b-awq-casperhansen/1" MAX_NUM_SEQS = 128 MAX_MODEL_LEN = 8192 * 3 // 2 llm = LLM( llm_model_pth, max_num_seqs=MAX_NUM_SEQS, max_model_len=MAX_MODEL_LEN, trust_remote_code=True, tensor_parallel_size=4, gpu_memory_utilization=0.95, seed=2024 ) ``` Error: ```text HFValidationError: Repo id must be in the form 'repo_name' or 'namespace/repo_name': '/kaggle/input/deepseek-r1/transformers/deepseek-r1-distill-qwen-7b-awq-casperhansen/1'. Use `repo_type` argument if needed. ``` ### How would you like to use vllm _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: Can't use the local model with LLM class. usage ### Your current environment I'm on Kaggle and trying to use LLM with the local trained model but getting the error: Code: ```py from vllm import LLM, SamplingPar...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: th the local trained model but getting the error: Code: ```py from vllm import LLM, SamplingParams llm_model_pth = "/kaggle/input/deepseek-r1/transformers/deepseek-r1-distill-qwen-7b-awq-casperhansen/1" MAX_NUM_SEQS = 1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
