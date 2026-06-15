# vllm-project/vllm#31325: [Bug]: Qwen3-32B Quality Degeneration on Offline Generate

| 字段 | 值 |
| --- | --- |
| Issue | [#31325](https://github.com/vllm-project/vllm/issues/31325) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-32B Quality Degeneration on Offline Generate

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm getting a quality issue where lm eval harness is generating gibberish. The following prompt works with the openai api using `vllm complete --quick prompt`. ```python from vllm import LLM, SamplingParams llm = LLM(model="Qwen/Qwen3-32B",tensor_parallel_size=4,dtype="auto",gpu_memory_utilization=0.9,max_model_len=32768,max_num_batched_tokens=4096,max_num_seqs=128) sp = SamplingParams(**{"temperature": 0.6, "repetition_penalty": 1.2, "top_p": 0.95, "top_k": 20, "min_p": 0.0, "max_tokens": 16384}) prompts = [" system\nThe following are multiple choice questions (with answers) about biology. Think step by step and then finish your answer with \"the answer is (X)\" where X is the correct letter choice.\n \n user\nQuestion:\nWhich of the following would most likely provide examples of mitotic cell divisions?\nOptions:\nA. cross section of muscle tissue\nB. longitudinal section of a shoot tip\nC. longitudinal section of a leaf vein\nD. cross section of a fruit\nE. cross section of a leaf\nF. longitudinal section of a petal\nG. longitudinal section of a seed\nH. cross section of an anther (site of pollen production in a flower)\nAnswe...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: he openai api using `vllm complete --quick prompt`. ```python from vllm import LLM, SamplingParams llm = LLM(model="Qwen/Qwen3-32B",tensor_parallel_size=4,dtype="auto",gpu_memory_utilization=0.9,max_model_len=32768,max_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: }") ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen3-32B Quality Degeneration on Offline Generate bug ### Your current environment ### 🐛 Describe the bug I'm getting a quality issue where lm eval harness is generating gibberish. The following prompt works wit...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ronment ### 🐛 Describe the bug I'm getting a quality issue where lm eval harness is generating gibberish. The following prompt works with the openai api using `vllm complete --quick prompt`. ```python from vllm import L...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
