# vllm-project/vllm#2061: error when loading CodeLlama-7b-Instruct

| 字段 | 值 |
| --- | --- |
| Issue | [#2061](https://github.com/vllm-project/vllm/issues/2061) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> error when loading CodeLlama-7b-Instruct

### Issue 正文摘录

vllm version: 0.2.3 ``` class Codellama(): @classmethod def init(cls, model_name="codellama/CodeLlama-34b-Python-hf", max_num_batched_tokens=8192): cls.llm = LLM( model=model_name, dtype="float16", # trust_remote_code=True, # tokenizer=model_name,#"hf-internal-testing/llama-tokenizer", max_num_batched_tokens=max_num_batched_tokens, tensor_parallel_size=1) @classmethod def generate(cls, prompt=None, prompt_token_ids=None, stop_token=None, temperature=0, top_p=1, max_new_tokens=160): #temperature= 0 means greedy sampling. stop_tokens = [' '] if stop_token: stop_tokens.append(stop_token) sampling_params = SamplingParams(temperature=temperature, top_p=top_p, max_tokens=max_new_tokens, stop=stop_tokens) completions = cls.llm.generate(prompt, prompt_token_ids = prompt_token_ids, sampling_params = sampling_params) return completions model_name = 'codellama/CodeLlama-7b-Instruct-hf' max_input_tokens = 20000 Codellama.init(model_name, max_input_tokens) ``` File "/gpfs/home3/llm.py", line 58, in init cls.llm = LLM( ^^^^ File "/home/.conda/envs/quest_gpu_snellius/lib/python3.11/site-packages/vllm/entrypoints/llm.py", line 93, in __init__ self.llm_engine = LLMEngine.from_engine_args(engine_ar...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: error when loading CodeLlama-7b-Instruct vllm version: 0.2.3 ``` class Codellama(): @classmethod def init(cls, model_name="codellama/CodeLlama-34b-Python-hf", max_num_batched_tokens=8192): cls.llm = LLM( model=mo
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: =8192): cls.llm = LLM( model=model_name, dtype="float16", # trust_remote_code=True, # tokenizer=model_name,#"hf-internal-testing/llama-tokenizer", max_num_batched_tokens=max_num_batched_tokens, tensor_parallel_size=1) @c
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: error when loading CodeLlama-7b-Instruct vllm version: 0.2.3 ``` class Codellama(): @classmethod def init(cls, model_name="codellama/CodeLlama-34b-Python-hf", max_num_batched_tokens=8192): cls.llm = LLM( model=model_nam...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Llama-7b-Instruct vllm version: 0.2.3 ``` class Codellama(): @classmethod def init(cls, model_name="codellama/CodeLlama-34b-Python-hf", max_num_batched_tokens=8192): cls.llm = LLM( model=model_name, dtype="float16", # t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: trust_remote_code=True, # tokenizer=model_name,#"hf-internal-testing/llama-tokenizer", max_num_batched_tokens=max_num_batched_tokens, tensor_parallel_size=1) @classmethod def generate(cls, prompt=None, prompt_token_ids=...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
