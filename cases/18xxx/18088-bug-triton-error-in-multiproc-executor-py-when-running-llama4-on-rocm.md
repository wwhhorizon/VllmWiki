# vllm-project/vllm#18088: [Bug]: Triton Error in `multiproc_executor.py` when running llama4 on ROCm

| 字段 | 值 |
| --- | --- |
| Issue | [#18088](https://github.com/vllm-project/vllm/issues/18088) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cuda;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Triton Error in `multiproc_executor.py` when running llama4 on ROCm

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running the following script ```python # SPDX-License-Identifier: Apache-2.0 import argparse import dataclasses # from transformers import AutoTokenizer from vllm import LLM, SamplingParams from vllm.engine.arg_utils import EngineArgs from vllm.utils import FlexibleArgumentParser def main(args: argparse.Namespace): print(args) engine_args = EngineArgs.from_cli_args(args) # NOTE(woosuk): If the request cannot be processed in a single batch, # the engine will automatically process the request in multiple batches. llm = LLM(**dataclasses.asdict(engine_args)) sampling_params = SamplingParams( n=args.n, temperature=0, top_p=1.0, ignore_eos=True, max_tokens=args.output_len, ) print(sampling_params) # tokenizer = AutoTokenizer.from_pretrained(engine_args.model) # inputs = tokenizer('Hello, world!', return_tensors='pt').input_ids inputs = [ "Hello, my name is", "The president of the United States is", ("1 + " * 50) + " 1 = ", # Longer prompt. "The capital of France is", ] # Prompt 0: 'Hello, my name is', # Generated text: ' John and I am a 30-year-old man from the United States. I am a software engineer by profession and I have been...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ng the following script ```python # SPDX-License-Identifier: Apache-2.0 import argparse import dataclasses # from transformers import AutoTokenizer from vllm import LLM, SamplingParams from vllm.engine.arg_utils import...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: engine_args = EngineArgs.from_cli_args(args) # NOTE(woosuk): If the request cannot be processed in a single batch, # the engine will automatically process the request in multiple batches. llm = LLM(**dataclasses.asdict(...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 6: == '__main__': parser = FlexibleArgumentParser( description='Benchmark the latency of processing a single batch of ' 'requests till completion.') parser.add_argument('--input-len', type=int, default=32) parser.add_argum...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: [Bug]: Triton Error in `multiproc_executor.py` when running llama4 on ROCm bug;rocm ### Your current environment ### 🐛 Describe the bug When running the following script ```python # SPDX-License-Identifier: Apache-2.0 i...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ride_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=10000, download_dir=None, load_format=auto, tensor_parallel_size=2, pipeline_parallel_size=1, disable_custom_all...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
