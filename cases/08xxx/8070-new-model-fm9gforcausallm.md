# vllm-project/vllm#8070: [New Model]: FM9GForCausalLM

| 字段 | 值 |
| --- | --- |
| Issue | [#8070](https://github.com/vllm-project/vllm/issues/8070) |
| 状态 | closed |
| 标签 | new-model;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: FM9GForCausalLM

### Issue 正文摘录

### Your current environment my vllm version is pip show vllm Name: vllm Version: 0.3.3+git3380931.abi0.dtk2404.torch2.1 Summary: A high-throughput and memory-efficient inference and serving engine for LLMs Home-page: https://github.com/vllm-project/vllm Author: vLLM Team Author-email: License: Apache 2.0 Location: /opt/conda/lib/python3.10/site-packages Requires: fastapi, ninja, numpy, prometheus-client, psutil, pydantic, ray, sentencepiece, starlette, tokenizers, transformers, typing-extensions, uvicorn Required-by: ### 🐛 Describe the bug [Bug]: ValueError: Model architectures ['FM9GForCausalLM'] are not supported for now. Supported architectures: ['AquilaModel', 'AquilaForCausalLM', 'BaiChuanForCausalLM', 'BaichuanForCausalLM', 'BloomForCausalLM', 'ChatGLMModel', 'ChatGLMForConditionalGeneration', 'DeciLMForCausalLM', 'DeepseekForCausalLM', 'FalconForCausalLM', 'GemmaForCausalLM', 'GPT2LMHeadModel', 'GPTBigCodeForCausalLM', 'GPTJForCausalLM', 'GPTNeoXForCausalLM', 'InternLMForCausalLM', 'InternLM2ForCausalLM', 'LlamaForCausalLM', 'LLaMAForCausalLM', 'MistralForCausalLM', 'MixtralForCausalLM', 'QuantMixtralForCausalLM', 'MptForCausalLM', 'MPTForCausalLM', 'OLMoForCausalLM', 'OPT...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [New Model]: FM9GForCausalLM new-model;stale ### Your current environment my vllm version is pip show vllm Name: vllm Version: 0.3.3+git3380931.abi0.dtk2404.torch2.1 Summary: A high-throughput and memory-efficient infer...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ]: FM9GForCausalLM new-model;stale ### Your current environment my vllm version is pip show vllm Name: vllm Version: 0.3.3+git3380931.abi0.dtk2404.torch2.1 Summary: A high-throughput and memory-efficient inference and s...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: me: vllm Version: 0.3.3+git3380931.abi0.dtk2404.torch2.1 Summary: A high-throughput and memory-efficient inference and serving engine for LLMs Home-page: https://github.com/vllm-project/vllm Author: vLLM Team Author-ema...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: salLM', 'LLaMAForCausalLM', 'MistralForCausalLM', 'MixtralForCausalLM', 'QuantMixtralForCausalLM', 'MptForCausalLM', 'MPTForCausalLM', 'OLMoForCausalLM', 'OPTForCausalLM', 'OrionForCausalLM', 'PhiForCausalLM', 'QWenLMHe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: , uvicorn Required-by: ### 🐛 Describe the bug [Bug]: ValueError: Model architectures ['FM9GForCausalLM'] are not supported for now. Supported architectures: ['AquilaModel', 'AquilaForCausalLM', 'BaiChuanForCausalLM', 'B...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
