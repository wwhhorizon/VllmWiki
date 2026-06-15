# vllm-project/vllm#4741: [Bug]: squeezeLLM with sparse could not work.

| 字段 | 值 |
| --- | --- |
| Issue | [#4741](https://github.com/vllm-project/vllm/issues/4741) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: squeezeLLM with sparse could not work.

### Issue 正文摘录

### Your current environment python 3.11, vllm 0.4.2 ### 🐛 Describe the bug I used the squeezeLLM 4bit to quant my model. While it seems that there is a bug. I just follow the squeezeLLM steps: python chunk_models.py --model [MODEL_PATH] --output [MODEL_CHUNKS_PATH] --model_type llama python chunk_models.py --model [GRADIENT_PATH] --output [GRADIENT_CHUNKS_PATH] --model_type llama python generate_outlier_config.py --model [MODEL_CHUNKS_PATH] --range [RANGE] --output [OUTLIERS_CONFIG_PATH] python nuq.py --bit 4 --model_type llama --model [MODEL_CHUNKS_PATH] --gradient [GRADIENT_CHUNKS_PATH] --output [LUT_PATH] python pack.py --model [MODEL_PATH] --wbits 4 --folder [LUT_PATH] --save [PACKED_CKPT_PATH] --include_sparse --balance [rank0]: Traceback (most recent call last): [rank0]: File "/home/ryan/vllm/benchmarks/benchmark_latency.py", line 195, in [rank0]: main(args) [rank0]: File "/home/ryan/vllm/benchmarks/benchmark_latency.py", line 20, in main [rank0]: llm = LLM(model=args.model, [rank0]: ^^^^^^^^^^^^^^^^^^^^^ [rank0]: File "/home/ryan/vllm/vllm/entrypoints/llm.py", line 123, in init [rank0]: self.llm_engine = LLMEngine.from_engine_args( [rank0]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^ [ran...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: lm 0.4.2 ### 🐛 Describe the bug I used the squeezeLLM 4bit to quant my model. While it seems that there is a bug. I just follow the squeezeLLM steps: python chunk_models.py --model [MODEL_PATH] --output [MODEL_CHUNKS_PA...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ank0]: Traceback (most recent call last): [rank0]: File "/home/ryan/vllm/benchmarks/benchmark_latency.py", line 195, in [rank0]: main(args) [rank0]: File "/home/ryan/vllm/benchmarks/benchmark_latency.py", line 20, in ma...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: 3.11, vllm 0.4.2 ### 🐛 Describe the bug I used the squeezeLLM 4bit to quant my model. While it seems that there is a bug. I just follow the squeezeLLM steps: python chunk_models.py --model [MODEL_PATH] --output [MODEL_C...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: != "model.layers.0.self_attn.qkv_proj.rows": param = params_dict[name] else: param = params_dict["model.layers.0.self_attn.qkv_proj.qweight"] Still get a gut [rank0]: Traceback (most recent call last): [rank0]: File "/h...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: squeezeLLM with sparse could not work. bug;stale ### Your current environment python 3.11, vllm 0.4.2 ### 🐛 Describe the bug I used the squeezeLLM 4bit to quant my model. While it seems that there is a bug. I jus...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
