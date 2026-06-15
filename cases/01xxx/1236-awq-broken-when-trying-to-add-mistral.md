# vllm-project/vllm#1236: AWQ broken when trying to add Mistral

| 字段 | 值 |
| --- | --- |
| Issue | [#1236](https://github.com/vllm-project/vllm/issues/1236) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | cuda;quantization |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> AWQ broken when trying to add Mistral

### Issue 正文摘录

I am getting illegal memory access after building from `main`. I am not sure if this is because of the cast from torch.bfloat16 to torch.float16 or if it is something else. Llama models still work without any problem. I simply added `MistralForCausalLM` here since the model definition is exactly the same as Llama and just works: https://github.com/vllm-project/vllm/blob/0967102c6de874902d973f0bcb98d48149a8eb49/vllm/model_executor/model_loader.py#L36-L38 Testing with an example: ``` CUDA_LAUNCH_BLOCKING=1 python examples/llm_engine_example.py --model TheBloke/Mistral-7B-Instruct-v0.1-AWQ --quantization awq --dtype half ``` Traceback: ``` root@d185de394aeb:/workspace/vllm# CUDA_LAUNCH_BLOCKING=1 python examples/llm_engine_example.py --model TheBloke/Mistral-7B-Instruct-v0.1-AWQ --quantization awq --dtype half WARNING 09-30 19:56:00 config.py:341] Casting torch.bfloat16 to torch.float16. INFO 09-30 19:56:00 llm_engine.py:72] Initializing an LLM engine with config: model='TheBloke/Mistral-7B-Instruct-v0.1-AWQ', tokenizer='TheBloke/Mistral-7B-Instruct-v0.1-AWQ', tokenizer_mode=auto, revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=32768, download_dir=None, load_...

## 现有链接修复摘要

#1295 Fix overflow in awq kernel

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: ing from `main`. I am not sure if this is because of the cast from torch.bfloat16 to torch.float16 or if it is something else. Llama models still work without any problem. I simply added `MistralForCausalLM` here since...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: when trying to add Mistral bug I am getting illegal memory access after building from `main`. I am not sure if this is because of the cast from torch.bfloat16 to torch.float16 or if it is something else. Llama models st...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: he cast from torch.bfloat16 to torch.float16 or if it is something else. Llama models still work without any problem. I simply added `MistralForCausalLM` here since the model definition is exactly the same as Llama and...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: of the cast from torch.bfloat16 to torch.float16 or if it is something else. Llama models still work without any problem. I simply added `MistralForCausalLM` here since the model definition is exactly the same as Llama...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: 4902d973f0bcb98d48149a8eb49/vllm/model_executor/model_loader.py#L36-L38 Testing with an example: ``` CUDA_LAUNCH_BLOCKING=1 python examples/llm_engine_example.py --model TheBloke/Mistral-7B-Instruct-v0.1-AWQ --quantizat...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#1295](https://github.com/vllm-project/vllm/pull/1295) | closes_keyword | 0.95 | Fix overflow in awq kernel | Fix overflow problem in #1236. For Mistral model, the output dimension of gate_up_proj is `14336 * 2 = 28672` and maximum blockIdx_z is `7`, so when a length over `2147483647 / 7 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
