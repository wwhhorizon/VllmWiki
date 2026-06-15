# vllm-project/vllm#340: Decode error while inferencing a batch of prompts

| 字段 | 值 |
| --- | --- |
| Issue | [#340](https://github.com/vllm-project/vllm/issues/340) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 22; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Decode error while inferencing a batch of prompts

### Issue 正文摘录

I'm trying to benchmark the performance of vLLM OPT. But I find that when I pass a relatively large batch of prompts to vLLM, it will raise decode error **when the sequence length meets a threshold** (which makes the problem look like an OOM). A minimal reproduction for this issue: ```python from vllm import LLM, SamplingParams def make_input(bs): return ["Hello!" for _ in range(bs)] bs = 128 generate_length = 200 # Create a sampling params object. sampling_params = SamplingParams( temperature=0.8, top_p=0.95, max_tokens=generate_length) # Create an LLM. llm = LLM( model="facebook/opt-125m", use_dummy_weights=True, ) input = make_input(bs) out = llm.generate(input, sampling_params) ``` When `bs=128`, the error happens in the 108-th token approximately. The error looks like ``` Traceback (most recent call last): File "vllm-none-problem-repro.py", line 21, in out = llm.generate(input, sampling_params) File "/llm-bench/vllm-src/vllm/entrypoints/llm.py", line 127, in generate return self._run_engine(use_tqdm) File "/llm-bench/vllm-src/vllm/entrypoints/llm.py", line 147, in _run_engine step_outputs = self.llm_engine.step() File "/llm-bench/vllm-src/vllm/engine/llm_engine.py", line 246,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: Decode error while inferencing a batch of prompts bug I'm trying to benchmark the performance of vLLM OPT. But I find that when I pass a relatively large batch of prompts to vLLM, it will raise decode error **when the s...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: on_utils_fast.py", line 533, in convert_tokens_to_string return self.backend_tokenizer.decoder.decode(tokens) TypeError: argument 'tokens': 'NoneType' object cannot be converted to 'PyString ``` If I use a smaller bs, t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: kens': 'NoneType' object cannot be converted to 'PyString ``` If I use a smaller bs, the "threshold" will also increase (>108). For example, it's around 210 when `bs=64`. Seems that there is a limit for `bs * length`.
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: equence length meets a threshold** (which makes the problem look like an OOM). A minimal reproduction for this issue: ```python from vllm import LLM, SamplingParams def make_input(bs): return ["Hello!" for _ in range(bs...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: =0.95, max_tokens=generate_length) # Create an LLM. llm = LLM( model="facebook/opt-125m", use_dummy_weights=True, ) input = make_input(bs) out = llm.generate(input, sampling_params) ``` When `bs=128`, the error happens...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
