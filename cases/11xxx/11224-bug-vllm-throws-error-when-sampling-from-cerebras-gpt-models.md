# vllm-project/vllm#11224: [Bug]: vLLM throws error when sampling from Cerebras GPT Models

| 字段 | 值 |
| --- | --- |
| Issue | [#11224](https://github.com/vllm-project/vllm/issues/11224) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vLLM throws error when sampling from Cerebras GPT Models

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug vLLM throws an error when attempting to use Cerebras's models. Here is a minimal reproduction: ``` from vllm import LLM, SamplingParams from vllm.distributed.parallel_state import destroy_model_parallel model = LLM(model="cerebras/Cerebras-GPT-1.3B", dtype="bfloat16") model_sampling_params = SamplingParams( n=1, temperature=1.0, max_tokens=64, seed=0, ) output = model.generate( prompts=["Please continue the following sentence: The quick brown fox jumps "], sampling_params=model_sampling_params, ) ``` The error is: `TypeError: 'NoneType' object is not iterable` It arises here: ``` def _verify_embedding_mode(self) -> None: architectures = getattr(self.hf_config, "architectures", []) self.embedding_mode = any( ModelRegistry.is_embedding_model(arch) for arch in architectures) ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: destroy_model_parallel model = LLM(model="cerebras/Cerebras-GPT-1.3B", dtype="bfloat16") model_sampling_params = SamplingParams( n=1, temperature=1.0, max_tokens=64, seed=0, ) output = model.generate( prompts=["Please c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: vLLM throws error when sampling from Cerebras GPT Models bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug vLLM throws an error when attempting to use Cerebras's models....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: to use Cerebras's models. Here is a minimal reproduction: ``` from vllm import LLM, SamplingParams from vllm.distributed.parallel_state import destroy_model_parallel model = LLM(model="cerebras/Cerebras-GPT-1.3B", dtype...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: arises here: ``` def _verify_embedding_mode(self) -> None: architectures = getattr(self.hf_config, "architectures", []) self.embedding_mode = any( ModelRegistry.is_embedding_model(arch) for arch in architectures) ``` ##...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
