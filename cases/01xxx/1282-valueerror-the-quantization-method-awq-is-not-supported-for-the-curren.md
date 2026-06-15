# vllm-project/vllm#1282: `ValueError`: The quantization method awq is not supported for the current GPU. Minimum capability: 80. Current capability: 75.

| 字段 | 值 |
| --- | --- |
| Issue | [#1282](https://github.com/vllm-project/vllm/issues/1282) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> `ValueError`: The quantization method awq is not supported for the current GPU. Minimum capability: 80. Current capability: 75.

### Issue 正文摘录

[AutoAWQ states that in order to use AWQ, you need a GPU with](https://github.com/casper-hansen/AutoAWQ/blob/0baf5e1845f48c71991d74965cf9594b27940f10/README.md?plain=1#L30): > Compute Capability 7.5 (sm75). Turing and later architectures are supported. But when I try to use vLLM to serve my AWQ LLM: ``` + python app.py --host 0.0.0.0 --port 5085 --model wasertech/assistant-llama2-7b-chat-awq --tokenizer hf-internal-testing/llama-tokenizer --dtype half --tensor-parallel-size 1 --gpu-memory-utilization 0.65 --quantization awq Downloading (…)lve/main/config.json: 100%|███████| 677/677 [00:00 engine = AsyncLLMEngine.from_engine_args(engine_args) File "/usr/local/lib/python3.8/dist-packages/vllm/engine/async_llm_engine.py", line 486, in from_engine_args engine = cls(engine_args.worker_use_ray, File "/usr/local/lib/python3.8/dist-packages/vllm/engine/async_llm_engine.py", line 270, in __init__ self.engine = self._init_engine(*args, **kwargs) File "/usr/local/lib/python3.8/dist-packages/vllm/engine/async_llm_engine.py", line 306, in _init_engine return engine_class(*args, **kwargs) File "/usr/local/lib/python3.8/dist-packages/vllm/engine/llm_engine.py", line 108, in __init__ self._init_w...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: LM to serve my AWQ LLM: ``` + python app.py --host 0.0.0.0 --port 5085 --model wasertech/assistant-llama2-7b-chat-awq --tokenizer hf-internal-testing/llama-tokenizer --dtype half --tensor-parallel-size 1 --gpu-memory-ut...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: he quantization method awq is not supported for the current GPU. Minimum capability: 80. Current capability: 75. [AutoAWQ states that in order to use AWQ, you need a GPU with](https://github.com/casper-hansen/AutoAWQ/bl...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: `ValueError`: The quantization method awq is not supported for the current GPU. Minimum capability: 80. Current capability: 75. [AutoAWQ states that in order to use AWQ, you need a GPU with](https://github.com/casper-ha...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: 5 --model wasertech/assistant-llama2-7b-chat-awq --tokenizer hf-internal-testing/llama-tokenizer --dtype half --tensor-parallel-size 1 --gpu-memory-utilization 0.65 --quantization awq Downloading (…)lve/main/config.json...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
