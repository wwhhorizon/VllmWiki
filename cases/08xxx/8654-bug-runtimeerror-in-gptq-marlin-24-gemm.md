# vllm-project/vllm#8654: [Bug]: RuntimeError in gptq_marlin_24_gemm

| 字段 | 值 |
| --- | --- |
| Issue | [#8654](https://github.com/vllm-project/vllm/issues/8654) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: RuntimeError in gptq_marlin_24_gemm

### Issue 正文摘录

### Your current environment python 3.8 L20*4 vllm 0.5.4 ### Model Input Dumps _No response_ ### 🐛 Describe the bug $python -m vllm.entrypoints.api_server --model='/mntfn/yanyi/Qwen2-7B-Instruct_24_w4a16/stage_quantization' --max-model-len=16000 --tensor-parallel-size=4 --use-v2-block-manager --enable-prefix-caching [rank0]: File "/opt/conda/lib/python3.8/site-packages/vllm/engine/async_llm_engine.py", line 735, in from_engine_args [rank0]: engine = cls( [rank0]: File "/opt/conda/lib/python3.8/site-packages/vllm/engine/async_llm_engine.py", line 631, in __init__ [rank0]: self.engine = self._init_engine(*args, **kwargs) [rank0]: File "/opt/conda/lib/python3.8/site-packages/vllm/engine/async_llm_engine.py", line 830, in _init_engine [rank0]: return engine_class(*args, **kwargs) [rank0]: File "/opt/conda/lib/python3.8/site-packages/vllm/engine/async_llm_engine.py", line 267, in __init__ [rank0]: super().__init__(*args, **kwargs) [rank0]: File "/opt/conda/lib/python3.8/site-packages/vllm/engine/llm_engine.py", line 283, in __init__ [rank0]: self._initialize_kv_caches() [rank0]: File "/opt/conda/lib/python3.8/site-packages/vllm/engine/llm_engine.py", line 389, in _initialize_kv_caches...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: points.api_server --model='/mntfn/yanyi/Qwen2-7B-Instruct_24_w4a16/stage_quantization' --max-model-len=16000 --tensor-parallel-size=4 --use-v2-block-manager --enable-prefix-caching [rank0]: File "/opt/conda/lib/python3....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: bug;stale ### Your current environment python 3.8 L20*4 vllm 0.5.4 ### Model Input Dumps _No response_ ### 🐛 Describe the bug $python -m vllm.entrypoints.api_server --model='/mntfn/yanyi/Qwen2-7B-Instruct_24_w4a16/stage...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ne 195, in determine_num_available_blocks [rank0]: self.model_runner.profile_run() [rank0]: File "/opt/conda/lib/python3.8/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context [rank0]: return func(*a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 512 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ge_quantization' --max-model-len=16000 --tensor-parallel-size=4 --use-v2-block-manager --enable-prefix-caching [rank0]: File "/opt/conda/lib/python3.8/site-packages/vllm/engine/async_llm_engine.py", line 735, in from_en...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
